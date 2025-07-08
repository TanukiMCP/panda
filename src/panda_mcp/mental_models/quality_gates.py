"""
Quality Gates Mental Model
"""
from typing import Dict, Any, List

# Type definition for mental model structure
MentalModel = Dict[str, Any]

quality_gates: MentalModel = {
    "description": "Establish systematic quality checkpoints throughout workflows to ensure deliverables meet standards before proceeding to next phases",
    "questions": [
        "What quality standards must be met at each stage?",
        "What specific criteria define 'done' and 'acceptable quality'?",
        "Where in the process should we place quality checkpoints?",
        "What verification methods will we use at each gate?",
        "Who has authority to approve passage through each gate?",
        "What happens when deliverables fail to meet quality standards?",
        "How will we measure and track quality metrics over time?",
        "What feedback loops will drive continuous quality improvement?"
    ],
    "structure": {
        "standards_definition": "Establish clear quality criteria and metrics",
        "checkpoint_placement": "Position gates at critical decision points",
        "verification_methods": "Design testing and review procedures",
        "approval_authority": "Assign responsibility for gate decisions",
        "failure_protocols": "Define actions when standards aren't met",
        "metrics_tracking": "Monitor quality trends and performance",
        "feedback_integration": "Use gate data to improve processes",
        "continuous_improvement": "Evolve standards based on learnings"
    },
    "next_steps": "Implement quality gate framework, train stakeholders on procedures, and establish monitoring dashboards for quality metrics"
} 