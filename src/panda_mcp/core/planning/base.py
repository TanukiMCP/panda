"""
Base classes for PandA planning framework
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from uuid import uuid4

class PlanningSession:
    """Represents a planning session with state management."""
    
    def __init__(self, session_id: str):
        """Initialize a planning session."""
        self.session_id = session_id
        self.state: Dict[str, Any] = {
            "steps": [],
            "current_step": 0,
            "mental_models": [],
            "context": {},
            "status": "initialized"
        }
    
    def add_step(self, step: Dict[str, Any]) -> None:
        """Add a planning step."""
        self.state["steps"].append(step)
    
    def get_current_step(self) -> Optional[Dict[str, Any]]:
        """Get the current planning step."""
        if not self.state["steps"]:
            return None
        return self.state["steps"][self.state["current_step"]]
    
    def advance_step(self) -> bool:
        """Advance to the next planning step."""
        if self.state["current_step"] < len(self.state["steps"]) - 1:
            self.state["current_step"] += 1
            return True
        return False
    
    def add_mental_model(self, model: str) -> None:
        """Add a mental model to the session."""
        if model not in self.state["mental_models"]:
            self.state["mental_models"].append(model)
    
    def update_context(self, context: Dict[str, Any]) -> None:
        """Update the session context."""
        self.state["context"].update(context)

class PlanningFramework(ABC):
    """Base class for planning frameworks."""
    
    def __init__(self, name: str, description: str):
        """Initialize a planning framework."""
        self.name = name
        self.description = description
        self.sessions: Dict[str, PlanningSession] = {}
    
    def create_session(self) -> str:
        """Create a new planning session."""
        session_id = str(uuid4())
        self.sessions[session_id] = PlanningSession(session_id)
        return session_id
    
    def get_session(self, session_id: str) -> Optional[PlanningSession]:
        """Get an existing planning session."""
        return self.sessions.get(session_id)
    
    @abstractmethod
    async def plan(
        self,
        session_id: str,
        parameters: Dict[str, Any],
        context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Execute the planning framework."""
        pass
    
    @abstractmethod
    def validate_parameters(self, parameters: Dict[str, Any]) -> bool:
        """Validate planning parameters."""
        pass 