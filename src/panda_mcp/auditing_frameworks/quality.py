"""
Quality Auditing Framework
"""
from typing import Dict, Any, List, Tuple

# Type definition for auditing framework structure
AuditingFramework = Dict[str, Any]

quality_framework: AuditingFramework = {
    "patterns": [
        # Long lines
        (r'.{120,}', "Line too long (over 120 characters)"),
        
        # Complex expressions
        (r'\([^)]*\([^)]*\([^)]*\)', "Deeply nested expressions"),
        
        # Magic numbers
        (r'\b(?<![\w.])[0-9]{2,}\b(?![\w.])', "Magic number (consider using named constant)"),
        
        # Empty catch blocks
        (r'except.*:\s*pass', "Empty exception handler"),
        
        # TODO/FIXME comments
        (r'#.*(?:TODO|FIXME|XXX)', "TODO/FIXME comment found"),
        
        # Duplicate code patterns
        (r'(\w+.*){3,}', "Potential code duplication"),
        
        # Missing docstrings
        (r'def\s+\w+\([^)]*\):\s*\n\s*(?!""")', "Function missing docstring"),
        
        # Poor variable names
        (r'\b[a-z]\b(?!\s*[=+\-*/])', "Single letter variable name"),
    ]
} 