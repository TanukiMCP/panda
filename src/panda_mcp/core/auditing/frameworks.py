"""
Auditing frameworks implementation for PandA
"""

import os
from typing import Any, Dict, List, Optional, Set
from .base import AuditingFramework
from .checkers import get_checker

class CodebaseAuditor(AuditingFramework):
    """Codebase auditing framework."""
    
    def __init__(self):
        """Initialize the codebase auditor."""
        super().__init__(
            name="codebase",
            description="Audit codebase for issues and best practices"
        )
        # Register supported checkers
        self.register_checker("security")
        self.register_checker("quality")
        self.register_checker("consistency")
        self.register_checker("compliance")
    
    def validate_parameters(self, parameters: Dict[str, Any]) -> bool:
        """Validate auditing parameters."""
        required_fields = ["path", "checkers"]
        if not all(field in parameters for field in required_fields):
            return False
        
        # Validate checkers
        return all(
            self.supports_checker(checker)
            for checker in parameters["checkers"]
        )
    
    async def audit(
        self,
        session_id: str,
        parameters: Dict[str, Any],
        context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Execute the codebase audit."""
        if not self.validate_parameters(parameters):
            return {
                "status": "error",
                "message": "Invalid parameters. Required: path, checkers"
            }
        
        session = self.get_session(session_id)
        if not session:
            session_id = self.create_session()
            session = self.get_session(session_id)
        
        # Update session context
        if context:
            session.update_context(context)
        
        # Load checkers
        checkers = []
        for checker_name in parameters["checkers"]:
            checker = get_checker(checker_name)
            if checker:
                checkers.append(checker)
                session.add_checker(checker_name)
        
        # Audit files
        path = parameters["path"]
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith((".py", ".js", ".ts", ".java", ".cpp", ".h")):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "r") as f:
                            content = f.read()
                            
                            # Run checkers
                            for checker in checkers:
                                findings = await checker.check(
                                    content,
                                    {"location": file_path}
                                )
                                for finding in findings:
                                    session.add_finding(finding)
                    except Exception as e:
                        session.add_finding({
                            "type": "error",
                            "severity": "error",
                            "message": f"Failed to audit file: {str(e)}",
                            "location": file_path
                        })
        
        return {
            "status": "success",
            "session_id": session_id,
            "metrics": session.get_metrics(),
            "findings": session.get_findings()
        }

class TextAuditor(AuditingFramework):
    """Text content auditing framework."""
    
    def __init__(self):
        """Initialize the text auditor."""
        super().__init__(
            name="text",
            description="Audit text content for issues and best practices"
        )
        # Register supported checkers
        self.register_checker("quality")
        self.register_checker("consistency")
    
    def validate_parameters(self, parameters: Dict[str, Any]) -> bool:
        """Validate auditing parameters."""
        required_fields = ["content", "checkers"]
        if not all(field in parameters for field in required_fields):
            return False
        
        # Validate checkers
        return all(
            self.supports_checker(checker)
            for checker in parameters["checkers"]
        )
    
    async def audit(
        self,
        session_id: str,
        parameters: Dict[str, Any],
        context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Execute the text audit."""
        if not self.validate_parameters(parameters):
            return {
                "status": "error",
                "message": "Invalid parameters. Required: content, checkers"
            }
        
        session = self.get_session(session_id)
        if not session:
            session_id = self.create_session()
            session = self.get_session(session_id)
        
        # Update session context
        if context:
            session.update_context(context)
        
        # Load checkers
        checkers = []
        for checker_name in parameters["checkers"]:
            checker = get_checker(checker_name)
            if checker:
                checkers.append(checker)
                session.add_checker(checker_name)
        
        # Run checkers
        content = parameters["content"]
        for checker in checkers:
            findings = await checker.check(
                content,
                {"location": context.get("location", "unknown")}
            )
            for finding in findings:
                session.add_finding(finding)
        
        return {
            "status": "success",
            "session_id": session_id,
            "metrics": session.get_metrics(),
            "findings": session.get_findings()
        }

class GeneralAuditor(AuditingFramework):
    """General-purpose auditing framework."""
    
    def __init__(self):
        """Initialize the general auditor."""
        super().__init__(
            name="general",
            description="General-purpose auditing framework for any content"
        )
        # Register all checkers
        self.register_checker("security")
        self.register_checker("quality")
        self.register_checker("consistency")
        self.register_checker("compliance")
    
    def validate_parameters(self, parameters: Dict[str, Any]) -> bool:
        """Validate auditing parameters."""
        required_fields = ["content", "checkers", "content_type"]
        if not all(field in parameters for field in required_fields):
            return False
        
        # Validate checkers
        return all(
            self.supports_checker(checker)
            for checker in parameters["checkers"]
        )
    
    async def audit(
        self,
        session_id: str,
        parameters: Dict[str, Any],
        context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Execute the general audit."""
        if not self.validate_parameters(parameters):
            return {
                "status": "error",
                "message": "Invalid parameters. Required: content, checkers, content_type"
            }
        
        session = self.get_session(session_id)
        if not session:
            session_id = self.create_session()
            session = self.get_session(session_id)
        
        # Update session context
        if context:
            session.update_context(context)
        
        # Load checkers
        checkers = []
        for checker_name in parameters["checkers"]:
            checker = get_checker(checker_name)
            if checker:
                checkers.append(checker)
                session.add_checker(checker_name)
        
        # Run checkers with content type context
        content = parameters["content"]
        content_type = parameters["content_type"]
        for checker in checkers:
            findings = await checker.check(
                content,
                {
                    "location": context.get("location", "unknown"),
                    "content_type": content_type
                }
            )
            for finding in findings:
                session.add_finding(finding)
        
        return {
            "status": "success",
            "session_id": session_id,
            "metrics": session.get_metrics(),
            "findings": session.get_findings()
        } 