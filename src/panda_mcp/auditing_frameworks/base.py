"""
Base structures for Auditing Frameworks.
"""
from typing import TypedDict, List, Tuple

class AuditingFramework(TypedDict):
    """
    A TypedDict that defines the structure for an auditing framework.
    
    Each framework consists of a list of patterns, where each pattern is a
    tuple containing a regex string and a description.
    """
    patterns: List[Tuple[str, str]] 