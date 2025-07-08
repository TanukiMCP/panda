"""
Parallel Processing Mental Model
"""
from typing import Dict, Any, List

# Type definition for mental model structure
MentalModel = Dict[str, Any]

parallel_processing: MentalModel = {
    "description": "Maximize efficiency by identifying tasks that can be executed simultaneously, optimizing resource utilization and reducing total time",
    "questions": [
        "Which tasks can be executed independently and in parallel?",
        "What dependencies exist that prevent parallel execution?",
        "How can we break large sequential tasks into parallel components?",
        "What resources are needed for each parallel stream?",
        "How do we coordinate and synchronize parallel work streams?",
        "What are the risks of parallel execution and how do we mitigate them?",
        "Where do parallel streams need to reconverge and integrate?",
        "How can we optimize load balancing across parallel processes?"
    ],
    "structure": {
        "independence_analysis": "Identify tasks that can run concurrently",
        "dependency_mapping": "Chart prerequisites and interdependencies",
        "decomposition_strategy": "Break sequential work into parallel components",
        "resource_allocation": "Assign resources to parallel execution streams",
        "coordination_mechanisms": "Establish synchronization and communication",
        "risk_management": "Address parallel execution risks and conflicts",
        "integration_points": "Plan convergence and synthesis of parallel work",
        "load_optimization": "Balance workload across parallel processes"
    },
    "next_steps": "Implement parallel execution plan, establish coordination mechanisms, and monitor performance gains from parallelization"
} 