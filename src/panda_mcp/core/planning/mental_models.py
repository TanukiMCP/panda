"""
Mental models implementation for PandA planning
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Type
from enum import Enum

class MentalModelType(Enum):
    """Types of mental models available."""
    DEFAULT = "default"
    FIRST_PRINCIPLES = "first_principles"
    SYSTEMS_THINKING = "systems_thinking"
    CRITICAL_PATH = "critical_path"
    DECISION_TREE = "decision_tree"

class MentalModel(ABC):
    """Base class for mental models."""
    
    def __init__(self, name: str, description: str):
        """Initialize a mental model."""
        self.name = name
        self.description = description
    
    @abstractmethod
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using this mental model."""
        pass

class DefaultMentalModel(MentalModel):
    """Default mental model for general-purpose planning."""
    
    def __init__(self):
        """Initialize the default mental model."""
        super().__init__(
            name=MentalModelType.DEFAULT.value,
            description="General-purpose planning model for any knowledge domain"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using the default model."""
        return [
            {
                "type": "analysis",
                "name": "Analyze Requirements",
                "description": f"Analyze the requirements for: {task}",
                "expected_output": "List of requirements and constraints"
            },
            {
                "type": "planning",
                "name": "Create Action Plan",
                "description": "Create a detailed action plan based on the analysis",
                "expected_output": "Ordered list of actions"
            },
            {
                "type": "execution",
                "name": "Execute Plan",
                "description": "Execute the action plan step by step",
                "expected_output": "Execution results"
            },
            {
                "type": "validation",
                "name": "Validate Results",
                "description": "Validate that the results meet the requirements",
                "expected_output": "Validation report"
            }
        ]

class FirstPrinciplesMentalModel(MentalModel):
    """First principles thinking mental model."""
    
    def __init__(self):
        """Initialize the first principles model."""
        super().__init__(
            name=MentalModelType.FIRST_PRINCIPLES.value,
            description="Break down complex problems into fundamental elements"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using first principles thinking."""
        return [
            {
                "type": "decomposition",
                "name": "Break Down Problem",
                "description": f"Break down {task} into fundamental elements",
                "expected_output": "List of fundamental components"
            },
            {
                "type": "analysis",
                "name": "Analyze Components",
                "description": "Analyze each fundamental component",
                "expected_output": "Component analysis"
            },
            {
                "type": "synthesis",
                "name": "Synthesize Solution",
                "description": "Build solution from fundamental components",
                "expected_output": "Synthesized solution"
            }
        ]

class SystemsThinkingMentalModel(MentalModel):
    """Systems thinking mental model."""
    
    def __init__(self):
        """Initialize the systems thinking model."""
        super().__init__(
            name=MentalModelType.SYSTEMS_THINKING.value,
            description="Understand interconnections and relationships in complex systems"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using systems thinking."""
        return [
            {
                "type": "mapping",
                "name": "Map System Components",
                "description": f"Identify all components and stakeholders involved in {task}",
                "expected_output": "System component map"
            },
            {
                "type": "relationships",
                "name": "Analyze Relationships",
                "description": "Identify relationships, dependencies, and feedback loops",
                "expected_output": "Relationship analysis"
            },
            {
                "type": "leverage_points",
                "name": "Find Leverage Points",
                "description": "Identify high-impact intervention points in the system",
                "expected_output": "List of leverage points"
            },
            {
                "type": "intervention",
                "name": "Design Intervention",
                "description": "Design intervention strategy based on leverage points",
                "expected_output": "Intervention plan"
            },
            {
                "type": "feedback",
                "name": "Monitor Feedback",
                "description": "Monitor system response and adjust approach",
                "expected_output": "Feedback analysis and adjustments"
            }
        ]

class CriticalPathMentalModel(MentalModel):
    """Critical path method mental model."""
    
    def __init__(self):
        """Initialize the critical path model."""
        super().__init__(
            name=MentalModelType.CRITICAL_PATH.value,
            description="Identify the critical path and optimize project scheduling"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using critical path method."""
        return [
            {
                "type": "task_breakdown",
                "name": "Break Down Tasks",
                "description": f"Break down {task} into individual tasks and activities",
                "expected_output": "Detailed task list"
            },
            {
                "type": "dependencies",
                "name": "Map Dependencies",
                "description": "Identify dependencies and prerequisites between tasks",
                "expected_output": "Dependency map"
            },
            {
                "type": "estimation",
                "name": "Estimate Duration",
                "description": "Estimate time and resources required for each task",
                "expected_output": "Time and resource estimates"
            },
            {
                "type": "critical_path",
                "name": "Identify Critical Path",
                "description": "Calculate critical path and identify bottlenecks",
                "expected_output": "Critical path analysis"
            },
            {
                "type": "optimization",
                "name": "Optimize Schedule",
                "description": "Optimize schedule and resource allocation",
                "expected_output": "Optimized project schedule"
            },
            {
                "type": "monitoring",
                "name": "Monitor Progress",
                "description": "Track progress and adjust critical path as needed",
                "expected_output": "Progress tracking and adjustments"
            }
        ]

class DecisionTreeMentalModel(MentalModel):
    """Decision tree mental model."""
    
    def __init__(self):
        """Initialize the decision tree model."""
        super().__init__(
            name=MentalModelType.DECISION_TREE.value,
            description="Structure decisions using decision tree analysis"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using decision tree analysis."""
        return [
            {
                "type": "problem_definition",
                "name": "Define Decision Problem",
                "description": f"Clearly define the decision problem for {task}",
                "expected_output": "Problem definition"
            },
            {
                "type": "alternatives",
                "name": "Identify Alternatives",
                "description": "Identify all possible alternatives and options",
                "expected_output": "List of alternatives"
            },
            {
                "type": "criteria",
                "name": "Define Criteria",
                "description": "Define evaluation criteria and success metrics",
                "expected_output": "Evaluation criteria"
            },
            {
                "type": "outcomes",
                "name": "Map Outcomes",
                "description": "Map potential outcomes and consequences for each alternative",
                "expected_output": "Outcome analysis"
            },
            {
                "type": "probabilities",
                "name": "Assess Probabilities",
                "description": "Assess probabilities and risks for each outcome",
                "expected_output": "Risk and probability assessment"
            },
            {
                "type": "evaluation",
                "name": "Evaluate Options",
                "description": "Evaluate options using decision tree analysis",
                "expected_output": "Decision tree analysis"
            },
            {
                "type": "selection",
                "name": "Select Best Option",
                "description": "Select the optimal decision based on analysis",
                "expected_output": "Selected decision with rationale"
            }
        ]

# Registry of available mental models
_MENTAL_MODELS: Dict[str, Type[MentalModel]] = {
    MentalModelType.DEFAULT.value: DefaultMentalModel,
    MentalModelType.FIRST_PRINCIPLES.value: FirstPrinciplesMentalModel,
    MentalModelType.SYSTEMS_THINKING.value: SystemsThinkingMentalModel,
    MentalModelType.CRITICAL_PATH.value: CriticalPathMentalModel,
    MentalModelType.DECISION_TREE.value: DecisionTreeMentalModel
}

def get_mental_model(name: str) -> Optional[MentalModel]:
    """Get a mental model by name."""
    model_class = _MENTAL_MODELS.get(name)
    if model_class:
        return model_class()
    return None

def register_mental_model(name: str, model_class: Type[MentalModel]) -> None:
    """Register a new mental model."""
    _MENTAL_MODELS[name] = model_class 