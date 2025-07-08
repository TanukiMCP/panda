"""
Rapid Prototyping Mental Model
"""
from typing import Dict, Any, List

# Type definition for mental model structure
MentalModel = Dict[str, Any]

rapid_prototyping: MentalModel = {
    "description": "Accelerate learning and validation through quick, low-fidelity experiments that test core assumptions before full implementation",
    "questions": [
        "What core assumptions or hypotheses need testing?",
        "What is the fastest way to create a testable prototype?",
        "What level of fidelity is needed to get meaningful feedback?",
        "Who should interact with the prototype and provide feedback?",
        "What specific questions will the prototype help us answer?",
        "How can we build learning loops into the prototyping process?",
        "What resources and constraints limit our prototyping speed?",
        "When should we move from prototype to full implementation?"
    ],
    "structure": {
        "assumption_identification": "Define key hypotheses to test",
        "speed_optimization": "Minimize time from idea to testable prototype",
        "fidelity_balancing": "Match prototype detail level to learning needs",
        "user_engagement": "Identify appropriate testers and feedback providers",
        "learning_objectives": "Clarify what insights the prototype should generate",
        "iteration_cycles": "Build rapid feedback and improvement loops",
        "resource_constraints": "Work within available time, tools, and skills",
        "graduation_criteria": "Define when to move beyond prototyping"
    },
    "next_steps": "Build minimal testable prototype, gather user feedback, iterate based on learnings, and plan transition to full solution"
} 