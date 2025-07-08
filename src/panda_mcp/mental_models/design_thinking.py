"""
Design Thinking Mental Model
"""
from typing import Dict, Any, List

# Type definition for mental model structure
MentalModel = Dict[str, Any]

design_thinking: MentalModel = {
    "description": "Human-centered approach to innovation that integrates the needs of people, possibilities of technology, and requirements for business success",
    "questions": [
        "Who are the users and what do they really need?",
        "What problems are we trying to solve?",
        "How might we approach this differently?",
        "What would the ideal user experience look like?",
        "How can we test our assumptions quickly?"
    ],
    "structure": {
        "empathize": "Understand the user's needs and context",
        "define": "Frame the problem clearly",
        "ideate": "Generate multiple solution ideas",
        "prototype": "Build testable versions",
        "test": "Gather feedback and iterate"
    },
    "next_steps": "Start with user research and rapid prototyping to validate assumptions"
} 