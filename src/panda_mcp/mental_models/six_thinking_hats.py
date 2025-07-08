"""
Six Thinking Hats Mental Model
"""
from typing import Dict, Any, List

# Type definition for mental model structure
MentalModel = Dict[str, Any]

six_thinking_hats: MentalModel = {
    "description": "Explore problems from six distinct perspectives using parallel thinking to ensure comprehensive analysis and avoid conflicts in group discussions",
    "questions": [
        "White Hat: What facts, data, and information do we need?",
        "Red Hat: What emotions, feelings, and intuitions are involved?", 
        "Black Hat: What are the risks, problems, and potential difficulties?",
        "Yellow Hat: What are the benefits, optimism, and positive outcomes?",
        "Green Hat: What creative alternatives and new ideas can we generate?",
        "Blue Hat: How should we manage this thinking process and next steps?"
    ],
    "structure": {
        "white_facts": "Gather objective information and data",
        "red_emotions": "Acknowledge feelings, hunches, and emotional responses",
        "black_caution": "Identify risks, problems, and critical concerns",
        "yellow_optimism": "Explore benefits, opportunities, and positive aspects",
        "green_creativity": "Generate new ideas, alternatives, and innovations",
        "blue_process": "Manage thinking process, set agenda, and control flow"
    },
    "next_steps": "Synthesize insights from all six perspectives to create a balanced, well-rounded understanding and action plan"
} 