"""
Systems Thinking Mental Model
"""
from typing import Dict, Any, List

# Type definition for mental model structure
MentalModel = Dict[str, Any]

systems_thinking: MentalModel = {
    "description": "Understand complex problems by examining the relationships and interactions between different parts of a system",
    "questions": [
        "What are the key components or stakeholders in this system?",
        "How do these components interact with each other?",
        "What feedback loops exist in the system?",
        "What are the unintended consequences of potential changes?",
        "How does this system connect to larger systems?"
    ],
    "structure": {
        "components": "Identify all key elements and stakeholders",
        "relationships": "Map connections and dependencies",
        "feedback_loops": "Find reinforcing and balancing loops",
        "leverage_points": "Identify where small changes create big impact"
    },
    "next_steps": "Look for high-leverage intervention points and consider system-wide effects"
} 