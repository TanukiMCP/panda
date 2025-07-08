"""
First Principles Mental Model
"""
from typing import Dict, Any, List

# Type definition for mental model structure
MentalModel = Dict[str, Any]

first_principles: MentalModel = {
    "description": "Break complex problems down into fundamental elements and build solutions from the ground up",
    "questions": [
        "What are the most basic, undeniable facts about this problem?",
        "What assumptions am I making that might not be true?",
        "If I had to explain this to someone with no background knowledge, what would I say?",
        "What are the core components that cannot be reduced further?",
        "How can I combine these fundamentals in new ways?"
    ],
    "structure": {
        "fundamentals": "List the basic, irreducible elements",
        "assumptions": "Identify and challenge assumptions",
        "synthesis": "Combine fundamentals into solutions"
    },
    "next_steps": "Consider how the fundamental elements can be combined or approached differently"
} 