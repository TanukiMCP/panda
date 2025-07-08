"""
Security Auditing Framework
"""
from typing import Dict, Any, List, Tuple

# Type definition for auditing framework structure
AuditingFramework = Dict[str, Any]

security_framework: AuditingFramework = {
    "patterns": [
        # API Keys and secrets
        (r'(?i)(api[_-]?key|apikey)\s*[=:]\s*[\'"][^\'"]{20,}[\'"]', "Potential API key exposure"),
        (r'(?i)(secret|token)\s*[=:]\s*[\'"][^\'"]{20,}[\'"]', "Potential secret/token exposure"),
        (r'(?i)(password|passwd|pwd)\s*[=:]\s*[\'"][^\'"]+[\'"]', "Potential password in code"),
        
        # SQL Injection patterns
        (r'(?i)execute\s*\(\s*[\'"].*%s.*[\'"]', "Potential SQL injection vulnerability"),
        (r'(?i)query\s*\(\s*[\'"].*\+.*[\'"]', "Potential SQL injection via string concatenation"),
        
        # Command injection
        (r'(?i)(os\.system|subprocess\.call|exec|eval)\s*\(.*input', "Potential command injection"),
        
        # Hardcoded URLs and IPs
        (r'https?://[^\s\'"]+', "Hardcoded URL"),
        (r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', "Hardcoded IP address"),
        
        # Weak crypto
        (r'(?i)(md5|sha1)\s*\(', "Weak cryptographic hash function"),
        (r'(?i)random\.random\(\)', "Weak random number generation for security"),
    ]
} 