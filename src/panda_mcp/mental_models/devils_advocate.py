"""
Devils Advocate Mental Model
"""
from typing import Dict, Any, List

# Type definition for mental model structure
MentalModel = Dict[str, Any]

devils_advocate: MentalModel = {
    "description": "Systematically challenge assumptions, identify potential flaws, and stress-test plans by arguing against proposed solutions to strengthen decision-making",
    "questions": [
        "What assumptions are we making that could be wrong?",
        "What are the strongest arguments against this approach?",
        "What could go catastrophically wrong with this plan?",
        "Who would disagree with this decision and why?",
        "What evidence contradicts our current thinking?",
        "What are we not considering or overlooking?",
        "How might our biases be influencing this decision?",
        "What would failure look like and how likely is it?"
    ],
    "structure": {
        "assumption_challenges": "Question fundamental assumptions behind the plan",
        "failure_scenarios": "Identify ways the plan could fail spectacularly",
        "opposing_perspectives": "Consider viewpoints of critics and skeptics",
        "evidence_gaps": "Find missing information or contradictory data",
        "bias_detection": "Uncover cognitive biases affecting judgment",
        "risk_amplification": "Explore worst-case scenarios and their likelihood"
    },
    "next_steps": "Use identified weaknesses to strengthen the plan, gather missing evidence, and develop contingency strategies for identified risks"
} 