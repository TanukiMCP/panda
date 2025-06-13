"""
PandA Plan - Planning tool implementation
"""

from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field

from ..core.planning import (
    PlanningFramework,
    SequentialPlanner,
    MentalModelType
)

class PlanParameters(BaseModel):
    """Parameters for the planning tool."""
    
    task: str = Field(..., description="The task to plan")
    framework: str = Field("sequential", description="The planning framework to use")
    mental_models: List[str] = Field(
        default=["default"],
        description="Mental models to apply in planning"
    )
    context: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Additional context for planning"
    )

class PandaPlan:
    """Planning tool for PandA MCP Server."""
    
    def __init__(self):
        """Initialize the planning tool."""
        self._frameworks = {
            "sequential": SequentialPlanner()
        }
        self._sessions = {}
    
    def get_available_frameworks(self) -> List[str]:
        """Get list of available planning frameworks."""
        return list(self._frameworks.keys())
    
    def get_available_mental_models(self) -> List[str]:
        """Get list of available mental models."""
        return [model.value for model in MentalModelType]
    
    async def execute(
        self,
        action: str,
        session_id: Optional[str] = None,
        parameters: Optional[Dict[str, Any]] = None,
        context: Optional[Dict[str, Any]] = None,
        result: Optional[Dict[str, Any]] = None,
        step_action: Optional[str] = None
    ) -> Dict[str, Any]:
        """Execute the planning tool with action-based interface.
        
        Args:
            action: The action to perform ('create_session', 'plan', 'advance_step', 'step_action', 'get_status')
            session_id: The session ID (optional for create_session)
            parameters: Action-specific parameters
            context: Optional additional context from the MCP server
            **kwargs: Additional action-specific arguments
            
        Returns:
            Dictionary containing the action result
        """
        try:
            if action == "create_session":
                return self._create_session(parameters or {})
            
            elif action == "plan":
                if not session_id:
                    return {"status": "error", "message": "session_id required for plan action"}
                return await self._plan(session_id, parameters or {}, context)
            
            elif action == "advance_step":
                if not session_id:
                    return {"status": "error", "message": "session_id required for advance_step action"}
                return await self._advance_step(session_id, result or {})
            
            elif action == "step_action":
                if not session_id:
                    return {"status": "error", "message": "session_id required for step_action action"}
                return await self._step_action(session_id, step_action or "status", result)
            
            elif action == "get_status":
                if not session_id:
                    return {"status": "error", "message": "session_id required for get_status action"}
                return self._get_status(session_id)
            
            else:
                return {
                    "status": "error",
                    "message": f"Unknown action: {action}",
                    "available_actions": ["create_session", "plan", "advance_step", "step_action", "get_status"]
                }
                
        except Exception as e:
            return {
                "status": "error",
                "message": f"Planning action failed: {str(e)}"
            }
    
    def _create_session(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new planning session."""
        import uuid
        session_id = str(uuid.uuid4())
        session_name = parameters.get("session_name", f"planning_session_{session_id[:8]}")
        
        self._sessions[session_id] = {
            "session_id": session_id,
            "session_name": session_name,
            "framework": None,
            "task": None,
            "status": "created"
        }
        
        return {
            "status": "success",
            "session_id": session_id,
            "session_name": session_name,
            "message": "Planning session created successfully"
        }
    
    async def _plan(self, session_id: str, parameters: Dict[str, Any], context: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        """Execute planning for a session."""
        # Validate parameters
        params = PlanParameters(**parameters)
        
        # Get planning framework
        framework = self._frameworks.get(params.framework)
        if not framework:
            return {
                "status": "error",
                "message": f"Unknown planning framework: {params.framework}",
                "available_frameworks": self.get_available_frameworks()
            }
        
        # Validate mental models
        available_models = self.get_available_mental_models()
        invalid_models = [
            model for model in params.mental_models
            if model not in available_models
        ]
        if invalid_models:
            return {
                "status": "error",
                "message": f"Unknown mental models: {invalid_models}",
                "available_models": available_models
            }
        
        # Execute planning framework
        result = await framework.plan(
            session_id,
            {
                "task": params.task,
                "mental_models": params.mental_models,
                **(params.context or {})
            },
            context
        )
        
        # Update session info
        if result["status"] == "success":
            session = self._sessions.get(session_id, {})
            session.update({
                "framework": params.framework,
                "task": params.task,
                "status": "planning_active"
            })
            self._sessions[session_id] = session
        
        return result
    
    async def _advance_step(self, session_id: str, result: Dict[str, Any]) -> Dict[str, Any]:
        """Advance to the next step in the plan."""
        return await self.advance_plan(session_id, result)
    
    async def _step_action(self, session_id: str, step_action: str, result: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        """Execute a specific action for the current step."""
        return await self.step_action(session_id, step_action, result=result)
    
    def _get_status(self, session_id: str) -> Dict[str, Any]:
        """Get execution status for a session."""
        return self.get_execution_status(session_id)
    
    async def advance_plan(self, session_id: str, result: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Advance to the next step in the plan."""
        session = self._sessions.get(session_id)
        if not session:
            return {
                "status": "error",
                "message": "Invalid session ID"
            }
        
        framework = self._frameworks.get(session["framework"])
        if not framework:
            return {
                "status": "error",
                "message": f"Unknown planning framework: {session['framework']}"
            }
        
        return await framework.advance(session_id, result)
    
    async def step_action(self, session_id: str, action: str, result: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Execute a specific action for the current step."""
        session = self._sessions.get(session_id)
        if not session:
            return {
                "status": "error",
                "message": "Invalid session ID"
            }
        
        framework = self._frameworks.get(session["framework"])
        if not framework:
            return {
                "status": "error",
                "message": f"Unknown planning framework: {session['framework']}"
            }
        
        if hasattr(framework, 'step_action'):
            return await framework.step_action(session_id, action, result=result)
        else:
            return {
                "status": "error",
                "message": "Framework does not support step actions"
            }
    
    def get_execution_status(self, session_id: str) -> Dict[str, Any]:
        """Get execution status for a session."""
        session = self._sessions.get(session_id)
        if not session:
            return {
                "status": "error",
                "message": "Invalid session ID"
            }
        
        framework = self._frameworks.get(session["framework"])
        if not framework:
            return {
                "status": "error",
                "message": f"Unknown planning framework: {session['framework']}"
            }
        
        if hasattr(framework, 'get_execution_status'):
            return framework.get_execution_status(session_id)
        else:
            return {
                "status": "error",
                "message": "Framework does not support execution status"
            } 