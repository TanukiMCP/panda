"""
Base classes for PandA auditing framework
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Set
from uuid import uuid4

class AuditSession:
    """Represents an auditing session with state management."""
    
    def __init__(self, session_id: str):
        """Initialize an audit session."""
        self.session_id = session_id
        self.state: Dict[str, Any] = {
            "findings": [],
            "checkers": set(),
            "context": {},
            "status": "initialized",
            "metrics": {
                "total_checks": 0,
                "passed_checks": 0,
                "failed_checks": 0,
                "warnings": 0
            }
        }
    
    def add_finding(self, finding: Dict[str, Any]) -> None:
        """Add an audit finding."""
        self.state["findings"].append(finding)
        
        # Update metrics
        severity = finding.get("severity", "info").lower()
        if severity == "error":
            self.state["metrics"]["failed_checks"] += 1
        elif severity == "warning":
            self.state["metrics"]["warnings"] += 1
        self.state["metrics"]["total_checks"] += 1
    
    def add_checker(self, checker: str) -> None:
        """Add an audit checker."""
        self.state["checkers"].add(checker)
    
    def update_context(self, context: Dict[str, Any]) -> None:
        """Update the session context."""
        self.state["context"].update(context)
    
    def get_findings(self, severity: Optional[str] = None) -> List[Dict[str, Any]]:
        """Get audit findings, optionally filtered by severity."""
        if not severity:
            return self.state["findings"]
        return [
            f for f in self.state["findings"]
            if f.get("severity", "").lower() == severity.lower()
        ]
    
    def get_metrics(self) -> Dict[str, int]:
        """Get audit metrics."""
        return self.state["metrics"]

class AuditingFramework(ABC):
    """Base class for auditing frameworks."""
    
    def __init__(self, name: str, description: str):
        """Initialize an auditing framework."""
        self.name = name
        self.description = description
        self.sessions: Dict[str, AuditSession] = {}
        self.supported_checkers: Set[str] = set()
    
    def create_session(self) -> str:
        """Create a new audit session."""
        session_id = str(uuid4())
        self.sessions[session_id] = AuditSession(session_id)
        return session_id
    
    def get_session(self, session_id: str) -> Optional[AuditSession]:
        """Get an existing audit session."""
        return self.sessions.get(session_id)
    
    def register_checker(self, checker: str) -> None:
        """Register a supported audit checker."""
        self.supported_checkers.add(checker)
    
    def supports_checker(self, checker: str) -> bool:
        """Check if a checker is supported."""
        return checker in self.supported_checkers
    
    @abstractmethod
    async def audit(
        self,
        session_id: str,
        parameters: Dict[str, Any],
        context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Execute the auditing framework."""
        pass
    
    @abstractmethod
    def validate_parameters(self, parameters: Dict[str, Any]) -> bool:
        """Validate auditing parameters."""
        pass 