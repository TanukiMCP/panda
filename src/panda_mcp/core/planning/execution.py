"""
Task execution engine for PandA planning framework.
This engine provides state management and step tracking for LLM-driven task execution.
The LLM is the brain - this is just the execution infrastructure.
"""

from typing import Any, Dict, List, Optional, Callable
from enum import Enum
from datetime import datetime
import uuid

class StepStatus(Enum):
    """Status of individual execution steps."""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"

class ExecutionStep:
    """Represents a single execution step."""
    
    def __init__(
        self,
        step_id: str,
        name: str,
        description: str,
        step_type: str = "action",
        expected_output: Optional[str] = None,
        dependencies: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None
    ):
        self.step_id = step_id
        self.name = name
        self.description = description
        self.step_type = step_type
        self.expected_output = expected_output
        self.dependencies = dependencies or []
        self.metadata = metadata or {}
        self.status = StepStatus.PENDING
        self.result: Optional[Dict[str, Any]] = None
        self.error: Optional[str] = None
        self.started_at: Optional[datetime] = None
        self.completed_at: Optional[datetime] = None
        self.execution_log: List[Dict[str, Any]] = []
    
    def start(self) -> None:
        """Mark step as started."""
        self.status = StepStatus.IN_PROGRESS
        self.started_at = datetime.now()
        self.log_event("step_started", {"timestamp": self.started_at.isoformat()})
    
    def complete(self, result: Dict[str, Any]) -> None:
        """Mark step as completed with result."""
        self.status = StepStatus.COMPLETED
        self.result = result
        self.completed_at = datetime.now()
        self.log_event("step_completed", {
            "result": result,
            "timestamp": self.completed_at.isoformat()
        })
    
    def fail(self, error: str) -> None:
        """Mark step as failed with error."""
        self.status = StepStatus.FAILED
        self.error = error
        self.completed_at = datetime.now()
        self.log_event("step_failed", {
            "error": error,
            "timestamp": self.completed_at.isoformat()
        })
    
    def skip(self, reason: str) -> None:
        """Mark step as skipped."""
        self.status = StepStatus.SKIPPED
        self.error = reason
        self.completed_at = datetime.now()
        self.log_event("step_skipped", {
            "reason": reason,
            "timestamp": self.completed_at.isoformat()
        })
    
    def log_event(self, event_type: str, data: Dict[str, Any]) -> None:
        """Log an execution event."""
        self.execution_log.append({
            "event_type": event_type,
            "timestamp": datetime.now().isoformat(),
            "data": data
        })
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert step to dictionary representation."""
        return {
            "step_id": self.step_id,
            "name": self.name,
            "description": self.description,
            "step_type": self.step_type,
            "expected_output": self.expected_output,
            "dependencies": self.dependencies,
            "metadata": self.metadata,
            "status": self.status.value,
            "result": self.result,
            "error": self.error,
            "started_at": self.started_at.isoformat() if self.started_at else None,
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
            "execution_log": self.execution_log
        }

class TaskExecutionEngine:
    """
    Task execution engine that provides step management for LLM-driven execution.
    The LLM orchestrates the execution - this engine just tracks state and progress.
    """
    
    def __init__(self, session_id: str):
        self.session_id = session_id
        self.steps: Dict[str, ExecutionStep] = {}
        self.step_order: List[str] = []
        self.current_step_index = 0
        self.execution_started = False
        self.execution_completed = False
        self.execution_metadata: Dict[str, Any] = {}
    
    def add_step(self, step: ExecutionStep) -> None:
        """Add a step to the execution plan."""
        self.steps[step.step_id] = step
        self.step_order.append(step.step_id)
    
    def add_steps(self, steps: List[ExecutionStep]) -> None:
        """Add multiple steps to the execution plan."""
        for step in steps:
            self.add_step(step)
    
    def get_current_step(self) -> Optional[ExecutionStep]:
        """Get the current step to execute."""
        if self.current_step_index >= len(self.step_order):
            return None
        step_id = self.step_order[self.current_step_index]
        return self.steps.get(step_id)
    
    def get_next_step(self) -> Optional[ExecutionStep]:
        """Get the next step without advancing."""
        if self.current_step_index + 1 >= len(self.step_order):
            return None
        step_id = self.step_order[self.current_step_index + 1]
        return self.steps.get(step_id)
    
    def advance_step(self) -> bool:
        """Advance to the next step. Returns True if advanced, False if at end."""
        if self.current_step_index < len(self.step_order) - 1:
            self.current_step_index += 1
            return True
        return False
    
    def start_execution(self) -> Dict[str, Any]:
        """Start the execution process."""
        self.execution_started = True
        current_step = self.get_current_step()
        
        if current_step:
            current_step.start()
            return {
                "status": "started",
                "current_step": current_step.to_dict(),
                "total_steps": len(self.step_order),
                "current_step_index": self.current_step_index
            }
        else:
            return {
                "status": "error",
                "message": "No steps to execute"
            }
    
    def complete_current_step(self, result: Dict[str, Any]) -> Dict[str, Any]:
        """Complete the current step and advance."""
        current_step = self.get_current_step()
        if not current_step:
            return {
                "status": "error",
                "message": "No current step to complete"
            }
        
        current_step.complete(result)
        
        # Check if this was the last step
        if not self.advance_step():
            self.execution_completed = True
            return {
                "status": "execution_completed",
                "completed_step": current_step.to_dict(),
                "total_steps": len(self.step_order),
                "summary": self.get_execution_summary()
            }
        
        # Get next step
        next_step = self.get_current_step()
        if next_step:
            next_step.start()
            return {
                "status": "step_completed",
                "completed_step": current_step.to_dict(),
                "next_step": next_step.to_dict(),
                "current_step_index": self.current_step_index,
                "total_steps": len(self.step_order)
            }
        
        return {
            "status": "error",
            "message": "Failed to advance to next step"
        }
    
    def fail_current_step(self, error: str) -> Dict[str, Any]:
        """Fail the current step."""
        current_step = self.get_current_step()
        if not current_step:
            return {
                "status": "error",
                "message": "No current step to fail"
            }
        
        current_step.fail(error)
        return {
            "status": "step_failed",
            "failed_step": current_step.to_dict(),
            "current_step_index": self.current_step_index,
            "total_steps": len(self.step_order),
            "can_retry": True,
            "can_skip": True
        }
    
    def skip_current_step(self, reason: str) -> Dict[str, Any]:
        """Skip the current step and advance."""
        current_step = self.get_current_step()
        if not current_step:
            return {
                "status": "error",
                "message": "No current step to skip"
            }
        
        current_step.skip(reason)
        
        # Advance to next step
        if not self.advance_step():
            self.execution_completed = True
            return {
                "status": "execution_completed",
                "skipped_step": current_step.to_dict(),
                "total_steps": len(self.step_order),
                "summary": self.get_execution_summary()
            }
        
        next_step = self.get_current_step()
        if next_step:
            next_step.start()
            return {
                "status": "step_skipped",
                "skipped_step": current_step.to_dict(),
                "next_step": next_step.to_dict(),
                "current_step_index": self.current_step_index,
                "total_steps": len(self.step_order)
            }
        
        return {
            "status": "error",
            "message": "Failed to advance after skipping step"
        }
    
    def retry_current_step(self) -> Dict[str, Any]:
        """Retry the current failed step."""
        current_step = self.get_current_step()
        if not current_step:
            return {
                "status": "error",
                "message": "No current step to retry"
            }
        
        if current_step.status != StepStatus.FAILED:
            return {
                "status": "error",
                "message": "Current step is not in failed state"
            }
        
        # Reset step state for retry
        current_step.status = StepStatus.PENDING
        current_step.error = None
        current_step.result = None
        current_step.start()
        
        return {
            "status": "step_retrying",
            "current_step": current_step.to_dict(),
            "current_step_index": self.current_step_index,
            "total_steps": len(self.step_order)
        }
    
    def get_execution_status(self) -> Dict[str, Any]:
        """Get current execution status."""
        current_step = self.get_current_step()
        
        return {
            "session_id": self.session_id,
            "execution_started": self.execution_started,
            "execution_completed": self.execution_completed,
            "current_step_index": self.current_step_index,
            "total_steps": len(self.step_order),
            "current_step": current_step.to_dict() if current_step else None,
            "progress_percentage": (self.current_step_index / len(self.step_order)) * 100 if self.step_order else 0
        }
    
    def get_execution_summary(self) -> Dict[str, Any]:
        """Get execution summary with all steps and their status."""
        step_summaries = []
        for step_id in self.step_order:
            step = self.steps[step_id]
            step_summaries.append({
                "step_id": step_id,
                "name": step.name,
                "status": step.status.value,
                "result": step.result,
                "error": step.error
            })
        
        status_counts = {}
        for step in self.steps.values():
            status = step.status.value
            status_counts[status] = status_counts.get(status, 0) + 1
        
        return {
            "session_id": self.session_id,
            "total_steps": len(self.step_order),
            "status_counts": status_counts,
            "steps": step_summaries,
            "execution_completed": self.execution_completed
        }
    
    def get_step_by_id(self, step_id: str) -> Optional[ExecutionStep]:
        """Get a specific step by ID."""
        return self.steps.get(step_id)
    
    def update_step_metadata(self, step_id: str, metadata: Dict[str, Any]) -> bool:
        """Update metadata for a specific step."""
        step = self.steps.get(step_id)
        if step:
            step.metadata.update(metadata)
            return True
        return False 