"""
Sequential planner implementation for PandA
"""

from typing import Any, Dict, List, Optional
from .base import PlanningFramework, PlanningSession
from .mental_models import MentalModel, get_mental_model
from .execution import TaskExecutionEngine, ExecutionStep
import uuid

class SequentialPlanner(PlanningFramework):
    """Sequential planning framework implementation."""
    
    def __init__(self):
        """Initialize the sequential planner."""
        super().__init__(
            name="sequential_planner",
            description="Sequential planning framework with step-by-step execution"
        )
        self.execution_engines: Dict[str, TaskExecutionEngine] = {}
    
    def validate_parameters(self, parameters: Dict[str, Any]) -> bool:
        """Validate planning parameters."""
        required_fields = ["task", "mental_models"]
        return all(field in parameters for field in required_fields)
    
    async def plan(
        self,
        session_id: str,
        parameters: Dict[str, Any],
        context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Execute the sequential planning framework."""
        if not self.validate_parameters(parameters):
            return {
                "status": "error",
                "message": "Invalid parameters. Required: task, mental_models"
            }
        
        session = self.get_session(session_id)
        if not session:
            session_id = self.create_session()
            session = self.get_session(session_id)
        
        # Update session context
        if context:
            session.update_context(context)
        
        # Load mental models
        models: List[MentalModel] = []
        for model_name in parameters["mental_models"]:
            model = get_mental_model(model_name)
            if model:
                models.append(model)
                session.add_mental_model(model_name)
        
        # Generate plan steps using mental models
        steps = []
        for model in models:
            model_steps = await model.generate_steps(
                parameters["task"],
                session.state["context"]
            )
            steps.extend(model_steps)
        
        # Create execution engine for this session
        execution_engine = TaskExecutionEngine(session_id)
        
        # Convert steps to execution steps and add to both session and engine
        execution_steps = []
        for i, step in enumerate(steps):
            execution_step = ExecutionStep(
                step_id=f"step_{i}_{uuid.uuid4().hex[:8]}",
                name=step.get("name", f"Step {i+1}"),
                description=step.get("description", ""),
                step_type=step.get("type", "action"),
                expected_output=step.get("expected_output"),
                metadata=step
            )
            execution_steps.append(execution_step)
            session.add_step(step)  # Keep original format for compatibility
        
        execution_engine.add_steps(execution_steps)
        self.execution_engines[session_id] = execution_engine
        
        # Start execution automatically
        execution_status = execution_engine.start_execution()
        
        # Return current plan state with execution info
        return {
            "status": "success",
            "session_id": session_id,
            "current_step": session.get_current_step(),
            "total_steps": len(session.state["steps"]),
            "mental_models": session.state["mental_models"],
            "execution": execution_status,
            "instructions": "Use advance_step to complete current step and move to next, or use step_action to execute specific actions"
        }
    
    async def advance(self, session_id: str, result: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Advance to the next planning step."""
        session = self.get_session(session_id)
        if not session:
            return {
                "status": "error",
                "message": "Invalid session ID"
            }
        
        execution_engine = self.execution_engines.get(session_id)
        if not execution_engine:
            return {
                "status": "error",
                "message": "No execution engine found for session"
            }
        
        # Complete current step in execution engine
        if result:
            execution_result = execution_engine.complete_current_step(result)
        else:
            execution_result = execution_engine.complete_current_step({"status": "completed"})
        
        # Also advance the session for compatibility
        session.advance_step()
        
        return {
            "status": execution_result["status"],
            "session_id": session_id,
            "execution": execution_result,
            "current_step": session.get_current_step(),
            "total_steps": len(session.state["steps"]),
            "is_final": execution_result.get("status") == "execution_completed"
        }
    
    async def step_action(self, session_id: str, action: str, result: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Execute a specific action for the current step."""
        execution_engine = self.execution_engines.get(session_id)
        if not execution_engine:
            return {
                "status": "error",
                "message": "No execution engine found for session"
            }
        
        current_step = execution_engine.get_current_step()
        if not current_step:
            return {
                "status": "error",
                "message": "No current step to execute action on"
            }
        
        if action == "complete":
            return execution_engine.complete_current_step(result or {"status": "completed"})
        elif action == "fail":
            error = result.get("error", "Step failed") if result else "Step failed"
            return execution_engine.fail_current_step(error)
        elif action == "skip":
            reason = result.get("reason", "Step skipped") if result else "Step skipped"
            return execution_engine.skip_current_step(reason)
        elif action == "retry":
            return execution_engine.retry_current_step()
        elif action == "status":
            return execution_engine.get_execution_status()
        else:
            return {
                "status": "error",
                "message": f"Unknown action: {action}",
                "available_actions": ["complete", "fail", "skip", "retry", "status"]
            }
    
    def get_execution_status(self, session_id: str) -> Dict[str, Any]:
        """Get execution status for a session."""
        execution_engine = self.execution_engines.get(session_id)
        if not execution_engine:
            return {
                "status": "error",
                "message": "No execution engine found for session"
            }
        
        return execution_engine.get_execution_status() 