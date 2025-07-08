"""
Decision Trees Mental Model
"""
from typing import Dict, Any, List

# Type definition for mental model structure
MentalModel = Dict[str, Any]

decision_trees: MentalModel = {
    "description": "Structure complex decisions by mapping out options, probabilities, and outcomes to identify optimal paths forward",
    "questions": [
        "What is the main decision we need to make?",
        "What are all the possible options or alternatives available?",
        "What key factors or criteria should influence this decision?",
        "What are the potential outcomes for each option?",
        "What is the probability of each outcome occurring?",
        "What are the costs, benefits, and risks of each path?",
        "How do different decision sequences affect final outcomes?",
        "What additional information would improve our decision quality?"
    ],
    "structure": {
        "decision_framing": "Clearly define the decision to be made",
        "option_enumeration": "List all viable alternatives and choices",
        "criteria_definition": "Establish evaluation factors and priorities",
        "outcome_mapping": "Identify possible results for each option",
        "probability_assessment": "Estimate likelihood of different outcomes",
        "value_analysis": "Quantify costs, benefits, and utility",
        "path_optimization": "Find optimal decision sequences",
        "sensitivity_testing": "Evaluate how assumptions affect conclusions"
    },
    "next_steps": "Select optimal decision path based on analysis, plan implementation steps, and establish monitoring for key assumptions"
} 