"""
Audit checkers implementation for PandA
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from enum import Enum

class AuditSeverity(Enum):
    """Audit finding severity levels."""
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"

class AuditChecker(ABC):
    """Base class for audit checkers."""
    
    def __init__(self, name: str, description: str):
        """Initialize an audit checker."""
        self.name = name
        self.description = description
    
    @abstractmethod
    async def check(
        self,
        content: Any,
        context: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """Execute the audit check."""
        pass

class SecurityChecker(AuditChecker):
    """Security audit checker."""
    
    def __init__(self):
        """Initialize the security checker."""
        super().__init__(
            name="security",
            description="Check for security issues and vulnerabilities"
        )
    
    async def check(
        self,
        content: Any,
        context: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """Execute security checks."""
        findings = []
        
        if isinstance(content, str):
            lines = content.split("\n")
            
            # Security patterns to check
            security_patterns = [
                (r"(?i)(api[_-]?key|apikey)\s*[=:]\s*['\"][^'\"]+['\"]", "Potential hardcoded API key"),
                (r"(?i)(password|passwd|pwd)\s*[=:]\s*['\"][^'\"]+['\"]", "Potential hardcoded password"),
                (r"(?i)(secret|token)\s*[=:]\s*['\"][^'\"]+['\"]", "Potential hardcoded secret"),
                (r"eval\s*\(", "Unsafe eval() usage"),
                (r"exec\s*\(", "Unsafe exec() usage"),
                (r"(?i)sql.*['\"].*\+.*['\"]", "Potential SQL injection vulnerability"),
                (r"(?i)select.*from.*where.*['\"].*\+", "Potential SQL injection in SELECT"),
                (r"(?i)insert.*into.*values.*['\"].*\+", "Potential SQL injection in INSERT"),
                (r"(?i)update.*set.*where.*['\"].*\+", "Potential SQL injection in UPDATE"),
                (r"(?i)delete.*from.*where.*['\"].*\+", "Potential SQL injection in DELETE"),
                (r"subprocess\.call\(.*shell=True", "Unsafe subprocess call with shell=True"),
                (r"os\.system\(", "Unsafe os.system() usage"),
                (r"(?i)md5\(", "Weak MD5 hash usage"),
                (r"(?i)sha1\(", "Weak SHA1 hash usage"),
                (r"random\.random\(\)", "Weak random number generation for security"),
                (r"(?i)http://", "Insecure HTTP protocol usage"),
                (r"ssl_verify\s*=\s*False", "SSL verification disabled"),
                (r"verify\s*=\s*False", "Certificate verification disabled")
            ]
            
            import re
            for i, line in enumerate(lines, 1):
                for pattern, message in security_patterns:
                    if re.search(pattern, line):
                        findings.append({
                            "type": "security",
                            "severity": AuditSeverity.ERROR.value,
                            "message": message,
                            "location": context.get("location", "unknown"),
                            "line": i,
                            "code": line.strip()
                        })
            
            # Check for sensitive file patterns
            location = context.get("location", "")
            sensitive_files = [".env", "config", "secret", "key", "password", "credential"]
            if any(pattern in location.lower() for pattern in sensitive_files):
                findings.append({
                    "type": "security",
                    "severity": AuditSeverity.WARNING.value,
                    "message": "File may contain sensitive information",
                    "location": location
                })
        
        return findings

class QualityChecker(AuditChecker):
    """Code/content quality checker."""
    
    def __init__(self):
        """Initialize the quality checker."""
        super().__init__(
            name="quality",
            description="Check for quality issues and best practices"
        )
    
    async def check(
        self,
        content: Any,
        context: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """Execute quality checks."""
        findings = []
        
        if isinstance(content, str):
            lines = content.split("\n")
            location = context.get("location", "unknown")
            
            # Quality patterns and checks
            import re
            
            # Line length check
            max_line_length = 88  # PEP 8 recommendation
            for i, line in enumerate(lines, 1):
                if len(line) > max_line_length:
                    findings.append({
                        "type": "quality",
                        "severity": AuditSeverity.WARNING.value,
                        "message": f"Line exceeds {max_line_length} characters ({len(line)} chars)",
                        "location": location,
                        "line": i,
                        "code": line[:50] + "..." if len(line) > 50 else line
                    })
            
            # Comment and documentation checks
            for i, line in enumerate(lines, 1):
                stripped = line.strip()
                
                # TODO/FIXME/HACK comments
                if re.search(r"(?i)(TODO|FIXME|HACK|XXX)", stripped):
                    findings.append({
                        "type": "quality",
                        "severity": AuditSeverity.INFO.value,
                        "message": "Technical debt comment found",
                        "location": location,
                        "line": i,
                        "code": stripped
                    })
                
                # Empty catch blocks
                if re.search(r"except.*:\s*pass\s*$", stripped):
                    findings.append({
                        "type": "quality",
                        "severity": AuditSeverity.WARNING.value,
                        "message": "Empty exception handler - consider logging or specific handling",
                        "location": location,
                        "line": i
                    })
                
                # Magic numbers (excluding common ones)
                if re.search(r"\b(?!0|1|2|10|100|1000)\d{2,}\b", stripped) and not re.search(r"#.*\d", stripped):
                    findings.append({
                        "type": "quality",
                        "severity": AuditSeverity.INFO.value,
                        "message": "Consider extracting magic number to named constant",
                        "location": location,
                        "line": i,
                        "code": stripped
                    })
            
            # Function and class complexity
            function_lines = 0
            in_function = False
            function_start = 0
            
            for i, line in enumerate(lines, 1):
                stripped = line.strip()
                
                # Function definition
                if re.match(r"^\s*def\s+", line):
                    if in_function and function_lines > 50:
                        findings.append({
                            "type": "quality",
                            "severity": AuditSeverity.WARNING.value,
                            "message": f"Function is too long ({function_lines} lines) - consider breaking it down",
                            "location": location,
                            "line": function_start
                        })
                    in_function = True
                    function_start = i
                    function_lines = 0
                
                # Class definition
                elif re.match(r"^\s*class\s+", line):
                    in_function = False
                
                # Count lines in function
                if in_function:
                    function_lines += 1
            
            # Check final function
            if in_function and function_lines > 50:
                findings.append({
                    "type": "quality",
                    "severity": AuditSeverity.WARNING.value,
                    "message": f"Function is too long ({function_lines} lines) - consider breaking it down",
                    "location": location,
                    "line": function_start
                })
            
            # Complexity indicators
            complexity_patterns = [
                (r"if.*and.*and", "Complex conditional - consider extracting to function"),
                (r"if.*or.*or", "Complex conditional - consider extracting to function"),
                (r"for.*for.*for", "Deeply nested loops - consider refactoring"),
                (r"try:.*except.*except.*except", "Multiple exception handlers - consider specific handling")
            ]
            
            for i, line in enumerate(lines, 1):
                for pattern, message in complexity_patterns:
                    if re.search(pattern, line):
                        findings.append({
                            "type": "quality",
                            "severity": AuditSeverity.INFO.value,
                            "message": message,
                            "location": location,
                            "line": i,
                            "code": line.strip()
                        })
        
        return findings

class ConsistencyChecker(AuditChecker):
    """Consistency and style checker."""
    
    def __init__(self):
        """Initialize the consistency checker."""
        super().__init__(
            name="consistency",
            description="Check for consistency and style issues"
        )
    
    async def check(
        self,
        content: Any,
        context: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """Execute consistency checks."""
        findings = []
        
        if isinstance(content, str):
            # Check indentation consistency
            lines = content.split("\n")
            prev_indent = 0
            for i, line in enumerate(lines, 1):
                if line.strip():
                    indent = len(line) - len(line.lstrip())
                    if indent > prev_indent + 4:
                        findings.append({
                            "type": "consistency",
                            "severity": AuditSeverity.WARNING.value,
                            "message": f"Inconsistent indentation at line {i}",
                            "location": context.get("location", "unknown"),
                            "line": i
                        })
                    prev_indent = indent
        
        return findings

class ComplianceChecker(AuditChecker):
    """Compliance and standards checker."""
    
    def __init__(self):
        """Initialize the compliance checker."""
        super().__init__(
            name="compliance",
            description="Check for compliance with standards and regulations"
        )
    
    async def check(
        self,
        content: Any,
        context: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """Execute compliance checks."""
        findings = []
        
        if isinstance(content, str):
            # Check for license headers
            if not any("license" in line.lower() for line in content.split("\n")[:10]):
                findings.append({
                    "type": "compliance",
                    "severity": AuditSeverity.WARNING.value,
                    "message": "Missing license header",
                    "location": context.get("location", "unknown")
                })
            
            # Check for copyright notices
            if not any("copyright" in line.lower() for line in content.split("\n")[:10]):
                findings.append({
                    "type": "compliance",
                    "severity": AuditSeverity.INFO.value,
                    "message": "Missing copyright notice",
                    "location": context.get("location", "unknown")
                })
        
        return findings

# Registry of available checkers
_CHECKERS: Dict[str, AuditChecker] = {
    "security": SecurityChecker(),
    "quality": QualityChecker(),
    "consistency": ConsistencyChecker(),
    "compliance": ComplianceChecker()
}

def get_checker(name: str) -> Optional[AuditChecker]:
    """Get an audit checker by name."""
    return _CHECKERS.get(name)

def register_checker(name: str, checker: AuditChecker) -> None:
    """Register a new audit checker."""
    _CHECKERS[name] = checker 