# src/panda_mcp/mental_models/__init__.py

from typing import Dict, Any
from .base import MentalModel

# Import existing mental models
from .first_principles import first_principles
from .systems_thinking import systems_thinking
from .design_thinking import design_thinking
from .critical_path import critical_path
from .swot_analysis import swot_analysis

# Import new mental models - Devils Advocate + 4 Fun Extensions
from .devils_advocate import devils_advocate
from .scamper import scamper
from .six_thinking_hats import six_thinking_hats
from .scenario_planning import scenario_planning
from .threat_modeling import threat_modeling

# Import new cutting-edge mental models for LLM planning + Taskmaster synergy
from .task_decomposition import task_decomposition
from .evidence_synthesis import evidence_synthesis
from .resource_optimization import resource_optimization
from .quality_gates import quality_gates
from .stakeholder_alignment import stakeholder_alignment
from .feedback_loops import feedback_loops
from .decision_trees import decision_trees
from .performance_optimization import performance_optimization
from .knowledge_integration import knowledge_integration
from .adaptive_planning import adaptive_planning
from .minimum_viable_plan import minimum_viable_plan
from .constraint_optimization import constraint_optimization
from .value_stream_mapping import value_stream_mapping
from .parallel_processing import parallel_processing
from .outcome_prediction import outcome_prediction
from .rapid_prototyping import rapid_prototyping
from .systems_integration import systems_integration

# Registry of all mental models
MENTAL_MODELS = {
    # Existing models
    "first_principles": first_principles,
    "systems_thinking": systems_thinking,
    "design_thinking": design_thinking,
    "critical_path": critical_path,
    "swot_analysis": swot_analysis,
    
    # New models - Devils Advocate + 4 Fun Extensions
    "devils_advocate": devils_advocate,
    "scamper": scamper,
    "six_thinking_hats": six_thinking_hats,
    "scenario_planning": scenario_planning,
    "threat_modeling": threat_modeling,
    
    # New cutting-edge models for LLM planning + Taskmaster workflows
    "task_decomposition": task_decomposition,
    "evidence_synthesis": evidence_synthesis,
    "resource_optimization": resource_optimization,
    "quality_gates": quality_gates,
    "stakeholder_alignment": stakeholder_alignment,
    "feedback_loops": feedback_loops,
    "decision_trees": decision_trees,
    "performance_optimization": performance_optimization,
    "knowledge_integration": knowledge_integration,
    "adaptive_planning": adaptive_planning,
    "minimum_viable_plan": minimum_viable_plan,
    "constraint_optimization": constraint_optimization,
    "value_stream_mapping": value_stream_mapping,
    "parallel_processing": parallel_processing,
    "outcome_prediction": outcome_prediction,
    "rapid_prototyping": rapid_prototyping,
    "systems_integration": systems_integration,
}

def get_mental_model(name: str) -> Dict[str, Any]:
    """Get a mental model by name."""
    if name not in MENTAL_MODELS:
        raise ValueError(f"Mental model '{name}' not found. Available models: {list(MENTAL_MODELS.keys())}")
    return MENTAL_MODELS[name]

def list_mental_models() -> list:
    """List all available mental model names."""
    return list(MENTAL_MODELS.keys())

__all__ = [
    "MentalModel",
    "MENTAL_MODELS", 
    "get_mental_model",
    "list_mental_models",
    # Export all individual models
    "first_principles", "systems_thinking", "design_thinking", "critical_path", "swot_analysis",
    "devils_advocate", "scamper", "six_thinking_hats", "scenario_planning", "threat_modeling",
    "task_decomposition", "evidence_synthesis", "resource_optimization", "quality_gates",
    "stakeholder_alignment", "feedback_loops", "decision_trees", "performance_optimization",
    "knowledge_integration", "adaptive_planning", "minimum_viable_plan", "constraint_optimization",
    "value_stream_mapping", "parallel_processing", "outcome_prediction", "rapid_prototyping", 
    "systems_integration"
] 