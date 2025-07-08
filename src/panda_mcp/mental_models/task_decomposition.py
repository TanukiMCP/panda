"""
Task Decomposition Mental Model
"""
from typing import Dict, Any, List

# Type definition for mental model structure
MentalModel = Dict[str, Any]

task_decomposition: MentalModel = {
    "description": "Break down complex objectives into manageable, executable tasks with clear dependencies, resources, and success criteria for optimal workflow execution",
    "questions": [
        "What is the ultimate objective we're trying to achieve?",
        "What are the major phases or milestones needed to reach this objective?",
        "What specific tasks are required within each phase?",
        "Which tasks depend on others being completed first?",
        "What resources, skills, and tools are needed for each task?",
        "How can we measure progress and success for each task?",
        "Which tasks can be executed in parallel vs sequentially?",
        "What are the potential bottlenecks and how can we address them?"
    ],
    "structure": {
        "objective_clarity": "Define clear, measurable end goals",
        "phase_breakdown": "Identify major phases and milestones",
        "task_identification": "List specific, actionable tasks",
        "dependency_mapping": "Chart task relationships and prerequisites",
        "resource_allocation": "Assign required resources to each task",
        "success_criteria": "Define completion and quality metrics",
        "parallelization": "Identify opportunities for concurrent execution",
        "bottleneck_analysis": "Find and mitigate potential delays"
    },
    "next_steps": "Create detailed task execution plan with timeline, assign responsibilities, and establish monitoring checkpoints"
} 