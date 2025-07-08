"""
Critical Path Mental Model
"""
from typing import Dict, Any, List

# Type definition for mental model structure
MentalModel = Dict[str, Any]

critical_path: MentalModel = {
    "description": "Identify the sequence of dependent tasks that determines the minimum time needed to complete a project",
    "questions": [
        "What are all the tasks required to complete this project?",
        "Which tasks depend on others being completed first?",
        "What is the longest sequence of dependent tasks?",
        "Where are the bottlenecks and constraints?",
        "What tasks can be done in parallel?"
    ],
    "structure": {
        "tasks": "List all required tasks with time estimates",
        "dependencies": "Map which tasks depend on others",
        "critical_path": "Identify the longest sequence of dependencies",
        "parallel_work": "Find tasks that can be done simultaneously"
    },
    "next_steps": "Focus resources on critical path tasks and optimize parallel work streams"
} 