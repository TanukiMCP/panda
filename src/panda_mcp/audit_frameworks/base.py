"""
Base structures for Cognitive Audit Frameworks.
"""
from typing import TypedDict, List, Dict, Any

class AuditFramework(TypedDict):
    """
    A TypedDict that defines the structure for a cognitive audit framework.
    
    This replaces the old pattern-based approach with systematic investigation
    methodologies that guide LLMs through professional audit processes.
    """
    description: str
    investigation_questions: List[str]
    methodology: Dict[str, List[str]]  # phase_name: [steps]
    evidence_requirements: List[str]
    evaluation_criteria: List[str]
    reporting_structure: Dict[str, str]
    risk_assessment_approach: str 