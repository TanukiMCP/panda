"""
SCAMPER Creative Problem-Solving Mental Model
"""
from typing import Dict, Any, List

# Type definition for mental model structure
MentalModel = Dict[str, Any]

scamper: MentalModel = {
    "description": "Generate creative solutions and innovations by systematically applying seven modification techniques to existing ideas, processes, or problems",
    "questions": [
        "What can we Substitute - replace parts, materials, people, or processes?",
        "What can we Combine - merge ideas, purposes, functions, or appeals?",
        "What can we Adapt - alter, change function, or use part of another element?",
        "What can we Modify or Magnify - emphasize, exaggerate, or add value?",
        "What can we Put to other uses - how else can this be used?",
        "What can we Eliminate - remove elements, simplify, reduce to core?",
        "What can we Reverse or Rearrange - transpose elements, change order or layout?"
    ],
    "structure": {
        "substitute": "Replace components with alternatives for improvement",
        "combine": "Merge different elements to create new solutions", 
        "adapt": "Modify existing solutions for new contexts",
        "modify_magnify": "Enhance or amplify specific aspects",
        "put_to_other_uses": "Find alternative applications or purposes",
        "eliminate": "Remove unnecessary elements to simplify",
        "reverse_rearrange": "Change sequence, order, or perspective"
    },
    "next_steps": "Evaluate the most promising creative variations and develop them into actionable solutions with implementation plans"
} 