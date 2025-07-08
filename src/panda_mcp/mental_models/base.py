"""
Base structures for Mental Models.
"""
from typing import TypedDict, List, Dict, Any

class MentalModel(TypedDict):
    """
    A TypedDict that defines the structure for a mental model.
    """
    description: str
    questions: List[str]
    structure: Dict[str, Any]
    next_steps: str 