"""
Resource Optimization Mental Model
"""
from typing import Dict, Any, List

# Type definition for mental model structure
MentalModel = Dict[str, Any]

resource_optimization: MentalModel = {
    "description": "Maximize value and efficiency by strategically allocating limited resources across competing priorities and constraints",
    "questions": [
        "What resources do we have available (time, people, budget, tools)?",
        "What are the competing demands for these resources?",
        "Which activities provide the highest return on investment?",
        "What are the minimum resource requirements for each priority?",
        "Where can we achieve economies of scale or synergies?",
        "What trade-offs must we make between different objectives?",
        "How can we eliminate waste and inefficiencies?",
        "What contingency reserves should we maintain?"
    ],
    "structure": {
        "resource_inventory": "Catalog all available resources and constraints",
        "demand_analysis": "Map resource requirements across all priorities",
        "value_assessment": "Calculate ROI and impact for each allocation option",
        "constraint_optimization": "Balance competing demands within limits",
        "synergy_identification": "Find opportunities for shared benefits",
        "trade_off_evaluation": "Assess costs and benefits of different choices",
        "efficiency_analysis": "Eliminate waste and optimize processes",
        "risk_buffering": "Allocate reserves for uncertainty management"
    },
    "next_steps": "Implement optimal resource allocation plan, establish monitoring systems, and create reallocation triggers for changing conditions"
} 