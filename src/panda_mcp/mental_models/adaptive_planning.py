"""
Adaptive Planning Mental Model
"""
from typing import Dict, Any, List

# Type definition for mental model structure
MentalModel = Dict[str, Any]

adaptive_planning: MentalModel = {
    "description": "Design flexible plans that can evolve and adapt to changing conditions while maintaining strategic direction and core objectives",
    "questions": [
        "What core objectives must remain stable regardless of changes?",
        "What aspects of our plan should be flexible and adaptable?",
        "What signals will indicate when plan adjustments are needed?",
        "How quickly can we detect and respond to changing conditions?",
        "What decision frameworks will guide adaptation choices?",
        "How do we balance stability with agility in our planning?",
        "What scenarios require minor adjustments vs major pivots?",
        "How do we maintain team alignment during plan changes?"
    ],
    "structure": {
        "core_stability": "Identify unchanging objectives and principles",
        "flexibility_zones": "Define adaptable elements and boundaries",
        "signal_monitoring": "Establish early warning systems for change",
        "response_speed": "Optimize detection and adaptation capabilities",
        "decision_frameworks": "Create guidelines for adaptation choices",
        "agility_balance": "Manage tension between stability and change",
        "adaptation_triggers": "Set thresholds for different response levels",
        "alignment_maintenance": "Keep teams coordinated during transitions"
    },
    "next_steps": "Implement adaptive planning framework, establish monitoring systems, and train teams on dynamic adjustment processes"
} 