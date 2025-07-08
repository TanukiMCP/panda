"""
Feedback Loops Mental Model
"""
from typing import Dict, Any, List

# Type definition for mental model structure
MentalModel = Dict[str, Any]

feedback_loops: MentalModel = {
    "description": "Design systematic feedback mechanisms to enable continuous learning, adaptation, and improvement throughout project execution",
    "questions": [
        "What key metrics and signals should we monitor continuously?",
        "How frequently should we collect and review feedback?",
        "Who should provide feedback and who should receive it?",
        "What feedback collection methods will give us the best insights?",
        "How will we distinguish between noise and meaningful signals?",
        "What triggers should prompt immediate course corrections?",
        "How will we integrate feedback into planning and decision processes?",
        "What feedback loops exist in our current processes and are they effective?"
    ],
    "structure": {
        "signal_identification": "Define key metrics and indicators to track",
        "collection_mechanisms": "Establish systematic feedback gathering methods",
        "stakeholder_engagement": "Identify feedback providers and recipients",
        "frequency_optimization": "Balance timeliness with signal quality",
        "noise_filtering": "Distinguish actionable insights from irrelevant data",
        "trigger_systems": "Set thresholds for automated responses",
        "integration_processes": "Embed feedback into decision workflows",
        "loop_effectiveness": "Monitor and improve feedback system performance"
    },
    "next_steps": "Implement feedback collection systems, establish review cadences, and create response protocols for different types of feedback"
} 