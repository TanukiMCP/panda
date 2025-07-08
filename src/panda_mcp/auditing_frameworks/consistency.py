"""
Consistency Auditing Framework
"""
from typing import Dict, Any, List, Tuple

# Type definition for auditing framework structure
AuditingFramework = Dict[str, Any]

consistency_framework: AuditingFramework = {
    "patterns": [
        # Indentation inconsistencies
        (r'^(\s*)\S.*\n\1\s+\S', "Inconsistent indentation detected"),
        
        # Mixed quote styles
        (r'["\'].*["\'].*["\']', "Mixed quote styles in same context"),
        
        # Inconsistent naming conventions
        (r'\b[a-z]+_[a-z]+.*\b[A-Z][a-z]+', "Mixed naming conventions (snake_case and camelCase)"),
        
        # Trailing whitespace
        (r'\s+$', "Trailing whitespace"),
        
        # Mixed line endings (simplified pattern)
        (r'\r\n.*\n', "Mixed line endings detected"),
    ]
} 