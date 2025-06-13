"""
PandA Audit - Auditing tool implementation
"""

from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field

from ..core.auditing import (
    AuditingFramework,
    CodebaseAuditor,
    TextAuditor,
    GeneralAuditor
)

class AuditParameters(BaseModel):
    """Parameters for the auditing tool."""
    
    framework: str = Field(..., description="The auditing framework to use")
    checkers: List[str] = Field(..., description="Audit checkers to apply")
    content: Optional[str] = Field(None, description="Content to audit")
    path: Optional[str] = Field(None, description="Path to audit")
    content_type: Optional[str] = Field(None, description="Type of content being audited")
    context: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Additional context for auditing"
    )

class PandaAudit:
    """Auditing tool for PandA MCP Server."""
    
    def __init__(self):
        """Initialize the auditing tool."""
        self._frameworks = {
            "codebase": CodebaseAuditor(),
            "text": TextAuditor(),
            "general": GeneralAuditor()
        }
        self._sessions = {}
    
    def get_available_frameworks(self) -> List[str]:
        """Get list of available auditing frameworks."""
        return list(self._frameworks.keys())
    
    def get_available_checkers(self, framework: str) -> List[str]:
        """Get list of available checkers for a framework."""
        fw = self._frameworks.get(framework)
        if fw:
            return list(fw.supported_checkers)
        return []
    
    async def execute(
        self,
        action: str,
        session_id: Optional[str] = None,
        parameters: Optional[Dict[str, Any]] = None,
        context: Optional[Dict[str, Any]] = None,
        result: Optional[Dict[str, Any]] = None,
        step_action: Optional[str] = None
    ) -> Dict[str, Any]:
        """Execute the auditing tool with action-based interface.
        
        Args:
            action: The action to perform ('create_session', 'audit', 'advance_step', 'step_action', 'get_status')
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
            
            elif action == "audit":
                if not session_id:
                    return {"status": "error", "message": "session_id required for audit action"}
                return await self._audit(session_id, parameters or {}, context)
            
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
                    "available_actions": ["create_session", "audit", "advance_step", "step_action", "get_status"]
                }
                
        except Exception as e:
            return {
                "status": "error",
                "message": f"Auditing action failed: {str(e)}"
            }
    
    def _create_session(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new auditing session."""
        import uuid
        session_id = str(uuid.uuid4())
        session_name = parameters.get("session_name", f"audit_session_{session_id[:8]}")
        
        self._sessions[session_id] = {
            "session_id": session_id,
            "session_name": session_name,
            "framework": None,
            "checkers": [],
            "status": "created",
            "findings": [],
            "current_step": 0,
            "total_steps": 0
        }
        
        return {
            "status": "success",
            "session_id": session_id,
            "session_name": session_name,
            "message": "Auditing session created successfully"
        }
    
    async def _audit(self, session_id: str, parameters: Dict[str, Any], context: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        """Execute auditing for a session."""
        # Validate parameters
        params = AuditParameters(**parameters)
        
        # Get auditing framework
        framework = self._frameworks.get(params.framework)
        if not framework:
            return {
                "status": "error",
                "message": f"Unknown auditing framework: {params.framework}",
                "available_frameworks": self.get_available_frameworks()
            }
        
        # Validate checkers
        available_checkers = self.get_available_checkers(params.framework)
        invalid_checkers = [
            checker for checker in params.checkers
            if checker not in available_checkers
        ]
        if invalid_checkers:
            return {
                "status": "error",
                "message": f"Unknown checkers for {params.framework}: {invalid_checkers}",
                "available_checkers": available_checkers
            }
        
        # Prepare audit parameters
        audit_params = {
            "checkers": params.checkers
        }
        
        # Add framework-specific parameters
        if params.framework == "codebase":
            if not params.path:
                return {
                    "status": "error",
                    "message": "Path is required for codebase auditing"
                }
            audit_params["path"] = params.path
        
        elif params.framework in ["text", "general"]:
            if not params.content:
                return {
                    "status": "error",
                    "message": "Content is required for text/general auditing"
                }
            audit_params["content"] = params.content
            
            if params.framework == "general":
                if not params.content_type:
                    return {
                        "status": "error",
                        "message": "Content type is required for general auditing"
                    }
                audit_params["content_type"] = params.content_type
        
        # Add context if provided
        if params.context:
            audit_params.update(params.context)
        
        # Execute audit
        result = await framework.audit(
            session_id,
            audit_params,
            context
        )
        
        # Update session info
        if result["status"] == "success":
            session = self._sessions.get(session_id, {})
            session.update({
                "framework": params.framework,
                "checkers": params.checkers,
                "status": "audit_active",
                "findings": result.get("findings", []),
                "metrics": result.get("metrics", {})
            })
            self._sessions[session_id] = session
        
        return result
    
    async def _advance_step(self, session_id: str, result: Dict[str, Any]) -> Dict[str, Any]:
        """Advance to the next step in the audit."""
        session = self._sessions.get(session_id)
        if not session:
            return {"status": "error", "message": "Invalid session ID"}
        
        # For auditing, steps are typically the different checkers
        session["current_step"] = session.get("current_step", 0) + 1
        
        return {
            "status": "step_completed" if session["current_step"] < session.get("total_steps", 1) else "audit_completed",
            "session_id": session_id,
            "current_step": session["current_step"],
            "total_steps": session.get("total_steps", 1),
            "result": result
        }
    
    async def _step_action(self, session_id: str, step_action: str, result: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        """Execute a specific action for the current audit step."""
        session = self._sessions.get(session_id)
        if not session:
            return {"status": "error", "message": "Invalid session ID"}
        
        if step_action == "complete":
            return await self._advance_step(session_id, result or {"status": "completed"})
        elif step_action == "status":
            return self._get_status(session_id)
        elif step_action == "get_findings":
            return {
                "status": "success",
                "findings": session.get("findings", []),
                "metrics": session.get("metrics", {})
            }
        else:
            return {
                "status": "error",
                "message": f"Unknown step action: {step_action}",
                "available_actions": ["complete", "status", "get_findings"]
            }
    
    def _get_status(self, session_id: str) -> Dict[str, Any]:
        """Get audit status for a session."""
        session = self._sessions.get(session_id)
        if not session:
            return {"status": "error", "message": "Invalid session ID"}
        
        return {
            "status": "success",
            "session_id": session_id,
            "session_name": session.get("session_name", ""),
            "audit_status": session.get("status", "unknown"),
            "framework": session.get("framework"),
            "checkers": session.get("checkers", []),
            "current_step": session.get("current_step", 0),
            "total_steps": session.get("total_steps", 0),
            "findings_count": len(session.get("findings", [])),
            "metrics": session.get("metrics", {})
        } 