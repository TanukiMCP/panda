"""
Performance Optimization Mental Model
"""
from typing import Dict, Any, List

# Type definition for mental model structure
MentalModel = Dict[str, Any]

performance_optimization: MentalModel = {
    "description": "Systematically identify bottlenecks, inefficiencies, and improvement opportunities to maximize system and process performance",
    "questions": [
        "What are the key performance metrics we want to optimize?",
        "Where are the current bottlenecks and constraints limiting performance?",
        "What processes or components consume the most resources?",
        "Which optimization efforts would yield the highest impact?",
        "What trade-offs exist between different performance dimensions?",
        "How can we measure and validate performance improvements?",
        "What are the root causes of performance issues?",
        "What optimization techniques are available for each bottleneck?"
    ],
    "structure": {
        "metrics_definition": "Establish clear performance indicators and targets",
        "bottleneck_identification": "Find constraints limiting overall performance",
        "resource_analysis": "Identify highest consumption areas",
        "impact_prioritization": "Rank optimization opportunities by value",
        "trade_off_evaluation": "Balance competing performance objectives",
        "measurement_systems": "Implement tracking and validation mechanisms",
        "root_cause_analysis": "Understand underlying causes of inefficiencies",
        "optimization_techniques": "Apply appropriate improvement methods"
    },
    "next_steps": "Implement highest-impact optimizations, establish performance monitoring, and create continuous improvement processes"
} 