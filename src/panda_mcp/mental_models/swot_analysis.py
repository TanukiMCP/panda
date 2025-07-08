"""
SWOT Analysis Mental Model
"""
from typing import Dict, Any, List

# Type definition for mental model structure
MentalModel = Dict[str, Any]

swot_analysis: MentalModel = {
    "description": "Analyze internal strengths and weaknesses alongside external opportunities and threats to inform strategic decisions",
    "questions": [
        "What are our key strengths and advantages?",
        "What are our main weaknesses or limitations?",
        "What opportunities exist in the environment?",
        "What threats or risks do we need to consider?",
        "How can we leverage strengths to capitalize on opportunities?"
    ],
    "structure": {
        "strengths": "Internal positive factors and advantages",
        "weaknesses": "Internal limitations and areas for improvement",
        "opportunities": "External positive factors and potential gains",
        "threats": "External risks and potential challenges"
    },
    "next_steps": "Develop strategies that leverage strengths and opportunities while addressing weaknesses and threats"
} 