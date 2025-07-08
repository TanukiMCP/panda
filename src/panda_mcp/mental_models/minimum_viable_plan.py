"""
Minimum Viable Plan Mental Model
"""
from typing import Dict, Any, List

# Type definition for mental model structure
MentalModel = Dict[str, Any]

minimum_viable_plan: MentalModel = {
    "description": "Create the simplest plan that delivers core value while minimizing risk and effort, enabling rapid learning and iteration",
    "questions": [
        "What is the absolute minimum we need to achieve our core objective?",
        "Which features or components are essential vs nice-to-have?",
        "What is the smallest experiment that validates our key assumptions?",
        "How can we deliver value quickly while reducing complexity?",
        "What risks can we eliminate by starting small and simple?",
        "What feedback will tell us if we're on the right track?",
        "How can we build learning loops into our minimal approach?",
        "What is our strategy for scaling from MVP to full vision?"
    ],
    "structure": {
        "core_identification": "Define absolute essential requirements",
        "feature_prioritization": "Separate must-haves from nice-to-haves",
        "assumption_testing": "Design minimal experiments for validation",
        "value_optimization": "Maximize impact with minimal resources",
        "risk_reduction": "Eliminate unnecessary complexity and uncertainty",
        "feedback_mechanisms": "Build in rapid learning and validation loops",
        "iteration_planning": "Design for continuous improvement cycles",
        "scaling_strategy": "Plan evolution from MVP to full solution"
    },
    "next_steps": "Implement MVP approach, establish rapid feedback cycles, and plan iterative enhancement based on learnings"
} 