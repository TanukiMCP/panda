"""
Scenario Planning Mental Model
"""
from typing import Dict, Any, List

# Type definition for mental model structure
MentalModel = Dict[str, Any]

scenario_planning: MentalModel = {
    "description": "Explore multiple plausible future scenarios to test strategy robustness, identify risks and opportunities, and prepare for uncertainty",
    "questions": [
        "What are the key driving forces and uncertainties affecting our situation?",
        "What are 3-4 distinctly different scenarios that could unfold?",
        "How would our current strategy perform in each scenario?",
        "What early warning signals should we monitor for each scenario?",
        "What adaptations would we need to make in each scenario?",
        "Which scenarios are most likely and which would have highest impact?",
        "What robust strategies work well across multiple scenarios?",
        "What contingency plans should we prepare for each scenario?"
    ],
    "structure": {
        "driving_forces": "Identify key variables that will shape the future",
        "scenario_development": "Create distinct, plausible future narratives",
        "strategy_testing": "Evaluate current plans against each scenario",
        "signal_monitoring": "Define indicators to track scenario emergence",
        "adaptation_planning": "Prepare responses for different futures",
        "robustness_analysis": "Find strategies that work across scenarios"
    },
    "next_steps": "Develop adaptive strategies, establish monitoring systems for early signals, and create contingency plans for high-impact scenarios"
} 