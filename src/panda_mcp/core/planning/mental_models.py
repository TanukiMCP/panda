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
    OCCAMS_RAZOR = "occams_razor"
    SWOT_ANALYSIS = "swot_analysis"
    PARETO_PRINCIPLE = "pareto_principle"
    ROOT_CAUSE_ANALYSIS = "root_cause_analysis"
    OPPORTUNITY_COST = "opportunity_cost"
    FIVE_WHYS = "five_whys"
    DESIGN_THINKING = "design_thinking"
    LEAN_STARTUP = "lean_startup"
    FEEDBACK_LOOPS = "feedback_loops"
    LOSS_AVERSION = "loss_aversion"
    HANLONS_RAZOR = "hanlons_razor"
    CONFIRMATION_BIAS_AWARENESS = "confirmation_bias_awareness"
    ANCHORING_BIAS = "anchoring_bias"
    AVAILABILITY_HEURISTIC = "availability_heuristic"
    PORTERS_FIVE_FORCES = "porters_five_forces"
    BLUE_OCEAN_STRATEGY = "blue_ocean_strategy"
    JOBS_TO_BE_DONE = "jobs_to_be_done"
    EXPECTED_VALUE_CALCULATION = "expected_value_calculation"
    MONTE_CARLO_SIMULATION = "monte_carlo_simulation"
    REGRESSION_TO_MEAN = "regression_to_mean"
    COMPOUND_INTEREST = "compound_interest"
    NETWORK_EFFECTS = "network_effects"
    ECONOMIES_OF_SCALE = "economies_of_scale"
    BOTTLENECK_THEORY = "bottleneck_theory"
    MINIMUM_VIABLE_PRODUCT = "minimum_viable_product"
    SOCIAL_PROOF = "social_proof"
    RECIPROCITY_PRINCIPLE = "reciprocity_principle"
    COMMITMENT_CONSISTENCY = "commitment_consistency"
    SCARCITY_PRINCIPLE = "scarcity_principle"
    FISHBONE_DIAGRAM = "fishbone_diagram"
    LATERAL_THINKING = "lateral_thinking"
    SUNK_COST_FALLACY = "sunk_cost_fallacy"
    TIME_VALUE_OF_MONEY = "time_value_of_money"
    RISK_RETURN_TRADEOFF = "risk_return_tradeoff"
    DIVERSIFICATION = "diversification"
    PYRAMID_PRINCIPLE = "pyramid_principle"
    STORYTELLING_FRAMEWORK = "storytelling_framework"
    ACTIVE_LISTENING = "active_listening"
    NONVIOLENT_COMMUNICATION = "nonviolent_communication"
    INFLUENCE_MAPPING = "influence_mapping"
    GROWTH_MINDSET = "growth_mindset"
    DELIBERATE_PRACTICE = "deliberate_practice"
    DOUBLE_LOOP_LEARNING = "double_loop_learning"
    ANTIFRAGILITY = "antifragility"
    BLACK_SWAN_EVENTS = "black_swan_events"
    METACOGNITION = "metacognition"
    DUNNING_KRUGER_EFFECT = "dunning_kruger_effect"
    IMPOSTOR_SYNDROME = "impostor_syndrome"
    BEGINNERS_MIND = "beginners_mind"

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

class OccamsRazorMentalModel(MentalModel):
    """Occam's Razor mental model - the simplest explanation is usually correct."""
    
    def __init__(self):
        """Initialize the Occam's Razor model."""
        super().__init__(
            name=MentalModelType.OCCAMS_RAZOR.value,
            description="Apply Occam's Razor principle - prefer simpler explanations and solutions"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Occam's Razor principle."""
        return [
            {
                "type": "problem_identification",
                "name": "Identify Core Problem",
                "description": f"Identify the core problem in {task}, stripping away complexity",
                "expected_output": "Clear, simple problem statement"
            },
            {
                "type": "solution_brainstorm",
                "name": "Generate Simple Solutions",
                "description": "Brainstorm multiple solutions, prioritizing simplicity",
                "expected_output": "List of potential solutions ranked by simplicity"
            },
            {
                "type": "assumption_check",
                "name": "Challenge Assumptions",
                "description": "Identify and challenge unnecessary assumptions",
                "expected_output": "List of validated assumptions vs. eliminated complexity"
            },
            {
                "type": "simplicity_evaluation",
                "name": "Evaluate for Simplicity",
                "description": "Evaluate solutions based on simplicity and effectiveness",
                "expected_output": "Simplicity-effectiveness analysis"
            },
            {
                "type": "implementation",
                "name": "Implement Simplest Solution",
                "description": "Implement the simplest solution that addresses the core problem",
                "expected_output": "Simple, effective solution implementation"
            },
            {
                "type": "validation",
                "name": "Validate Effectiveness",
                "description": "Validate that the simple solution effectively solves the problem",
                "expected_output": "Validation results and refinements"
            }
        ]

class SWOTAnalysisMentalModel(MentalModel):
    """SWOT Analysis mental model - analyze Strengths, Weaknesses, Opportunities, and Threats."""
    
    def __init__(self):
        """Initialize the SWOT Analysis model."""
        super().__init__(
            name=MentalModelType.SWOT_ANALYSIS.value,
            description="Systematic analysis of Strengths, Weaknesses, Opportunities, and Threats"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using SWOT Analysis framework."""
        return [
            {
                "type": "context_analysis",
                "name": "Define Analysis Context",
                "description": f"Define the context and scope for SWOT analysis of {task}",
                "expected_output": "Clear context definition and analysis boundaries"
            },
            {
                "type": "strengths_analysis",
                "name": "Identify Strengths",
                "description": "Identify internal strengths and advantages",
                "expected_output": "Comprehensive list of strengths and capabilities"
            },
            {
                "type": "weaknesses_analysis",
                "name": "Identify Weaknesses",
                "description": "Identify internal weaknesses and limitations",
                "expected_output": "Honest assessment of weaknesses and gaps"
            },
            {
                "type": "opportunities_analysis",
                "name": "Identify Opportunities",
                "description": "Identify external opportunities and favorable conditions",
                "expected_output": "List of external opportunities to leverage"
            },
            {
                "type": "threats_analysis",
                "name": "Identify Threats",
                "description": "Identify external threats and challenges",
                "expected_output": "Assessment of external threats and risks"
            },
            {
                "type": "strategic_matching",
                "name": "Strategic Matching",
                "description": "Match strengths with opportunities and address weaknesses/threats",
                "expected_output": "Strategic options and recommendations"
            },
            {
                "type": "action_planning",
                "name": "Develop Action Plan",
                "description": "Create action plan based on SWOT analysis insights",
                "expected_output": "Prioritized action plan with specific initiatives"
            }
        ]

class ParetoPrincipleMentalModel(MentalModel):
    """Pareto Principle mental model - 80% of effects come from 20% of causes (80/20 rule)."""
    
    def __init__(self):
        """Initialize the Pareto Principle model."""
        super().__init__(
            name=MentalModelType.PARETO_PRINCIPLE.value,
            description="Apply the 80/20 rule to identify high-impact activities and optimize resource allocation"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Pareto Principle (80/20 rule)."""
        return [
            {
                "type": "activity_identification",
                "name": "Identify All Activities",
                "description": f"List all activities, tasks, or factors involved in {task}",
                "expected_output": "Comprehensive list of activities and factors"
            },
            {
                "type": "impact_assessment",
                "name": "Assess Impact",
                "description": "Evaluate the potential impact or value of each activity",
                "expected_output": "Impact assessment for each activity"
            },
            {
                "type": "effort_assessment",
                "name": "Assess Effort Required",
                "description": "Evaluate the effort, time, or resources required for each activity",
                "expected_output": "Effort assessment for each activity"
            },
            {
                "type": "impact_effort_analysis",
                "name": "Impact-Effort Analysis",
                "description": "Create impact vs. effort matrix to identify high-value activities",
                "expected_output": "Impact-effort matrix with activity categorization"
            },
            {
                "type": "vital_few_identification",
                "name": "Identify Vital Few",
                "description": "Identify the 20% of activities that will produce 80% of results",
                "expected_output": "List of high-impact, vital few activities"
            },
            {
                "type": "resource_allocation",
                "name": "Optimize Resource Allocation",
                "description": "Allocate resources to focus on the vital few activities",
                "expected_output": "Optimized resource allocation plan"
            },
            {
                "type": "implementation_prioritization",
                "name": "Prioritize Implementation",
                "description": "Create implementation plan prioritizing high-impact activities",
                "expected_output": "Prioritized implementation roadmap"
            },
            {
                "type": "monitoring",
                "name": "Monitor and Adjust",
                "description": "Monitor results and adjust focus based on actual impact",
                "expected_output": "Performance monitoring and adjustment plan"
            }
        ]

class RootCauseAnalysisMentalModel(MentalModel):
    """Root Cause Analysis mental model - systematic method for identifying root causes of problems."""
    
    def __init__(self):
        """Initialize the Root Cause Analysis model."""
        super().__init__(
            name=MentalModelType.ROOT_CAUSE_ANALYSIS.value,
            description="Systematic investigation to identify and address root causes of problems"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Root Cause Analysis methodology."""
        return [
            {
                "type": "problem_definition",
                "name": "Define the Problem",
                "description": f"Clearly define and document the problem in {task}",
                "expected_output": "Clear, specific problem statement with measurable impact"
            },
            {
                "type": "data_collection",
                "name": "Collect Data",
                "description": "Gather relevant data, evidence, and information about the problem",
                "expected_output": "Comprehensive data collection including timeline and context"
            },
            {
                "type": "symptom_identification",
                "name": "Identify Symptoms",
                "description": "Distinguish between symptoms and potential root causes",
                "expected_output": "Clear separation of symptoms from underlying causes"
            },
            {
                "type": "five_whys",
                "name": "Apply Five Whys Technique",
                "description": "Ask 'why' repeatedly to drill down to root causes",
                "expected_output": "Five Whys analysis revealing deeper causation layers"
            },
            {
                "type": "cause_categorization",
                "name": "Categorize Potential Causes",
                "description": "Use fishbone diagram or similar to categorize potential causes",
                "expected_output": "Organized categorization of potential causes (people, process, technology, environment)"
            },
            {
                "type": "root_cause_validation",
                "name": "Validate Root Causes",
                "description": "Test and validate identified root causes with evidence",
                "expected_output": "Validated root causes with supporting evidence"
            },
            {
                "type": "solution_development",
                "name": "Develop Solutions",
                "description": "Develop targeted solutions that address validated root causes",
                "expected_output": "Solution plan targeting root causes, not just symptoms"
            },
            {
                "type": "prevention_planning",
                "name": "Plan Prevention Measures",
                "description": "Design measures to prevent recurrence of the problem",
                "expected_output": "Prevention strategy and monitoring plan"
            },
            {
                "type": "implementation_monitoring",
                "name": "Implement and Monitor",
                "description": "Implement solutions and monitor effectiveness",
                "expected_output": "Implementation results and effectiveness monitoring"
            }
        ]

class OpportunityCostMentalModel(MentalModel):
    """Opportunity Cost mental model - the value of the best alternative foregone when making a choice."""
    
    def __init__(self):
        """Initialize the Opportunity Cost model."""
        super().__init__(
            name=MentalModelType.OPPORTUNITY_COST.value,
            description="Analyze the value of alternatives foregone to make better resource allocation decisions"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Opportunity Cost analysis."""
        return [
            {
                "type": "decision_identification",
                "name": "Identify Decision Context",
                "description": f"Clearly identify the decision to be made in {task} and available resources",
                "expected_output": "Clear decision context with resource constraints"
            },
            {
                "type": "alternative_identification",
                "name": "Identify All Alternatives",
                "description": "Identify all possible alternatives and options available",
                "expected_output": "Comprehensive list of viable alternatives"
            },
            {
                "type": "resource_analysis",
                "name": "Analyze Resource Requirements",
                "description": "Analyze time, money, effort, and other resources required for each alternative",
                "expected_output": "Resource requirement analysis for each option"
            },
            {
                "type": "value_assessment",
                "name": "Assess Value of Each Alternative",
                "description": "Evaluate the potential value, benefits, and returns of each alternative",
                "expected_output": "Value assessment for each alternative"
            },
            {
                "type": "opportunity_cost_calculation",
                "name": "Calculate Opportunity Costs",
                "description": "Calculate the opportunity cost of each choice (value of best alternative foregone)",
                "expected_output": "Opportunity cost analysis for each decision option"
            },
            {
                "type": "trade_off_analysis",
                "name": "Analyze Trade-offs",
                "description": "Analyze trade-offs between alternatives considering opportunity costs",
                "expected_output": "Trade-off analysis with opportunity cost considerations"
            },
            {
                "type": "decision_optimization",
                "name": "Optimize Decision",
                "description": "Select the option that maximizes value while minimizing opportunity cost",
                "expected_output": "Optimized decision with opportunity cost justification"
            },
            {
                "type": "monitoring_adjustment",
                "name": "Monitor and Adjust",
                "description": "Monitor outcomes and adjust future decisions based on actual opportunity costs",
                "expected_output": "Monitoring plan and decision adjustment framework"
            }
        ]

class FiveWhysMentalModel(MentalModel):
    """Five Whys mental model - asking 'why' five times to get to the root of a problem."""
    
    def __init__(self):
        """Initialize the Five Whys model."""
        super().__init__(
            name=MentalModelType.FIVE_WHYS.value,
            description="Iterative questioning technique to drill down to root causes by asking 'why' repeatedly"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Five Whys technique."""
        return [
            {
                "type": "problem_statement",
                "name": "State the Problem",
                "description": f"Clearly state the problem you want to solve in {task}",
                "expected_output": "Clear, specific problem statement"
            },
            {
                "type": "first_why",
                "name": "First Why - Initial Cause",
                "description": "Ask 'Why does this problem occur?' and identify the immediate cause",
                "expected_output": "First level cause identification"
            },
            {
                "type": "second_why",
                "name": "Second Why - Deeper Cause",
                "description": "Ask 'Why does the first cause occur?' to go deeper",
                "expected_output": "Second level cause identification"
            },
            {
                "type": "third_why",
                "name": "Third Why - Underlying Cause",
                "description": "Ask 'Why does the second cause occur?' to find underlying issues",
                "expected_output": "Third level cause identification"
            },
            {
                "type": "fourth_why",
                "name": "Fourth Why - Systemic Cause",
                "description": "Ask 'Why does the third cause occur?' to identify systemic issues",
                "expected_output": "Fourth level cause identification"
            },
            {
                "type": "fifth_why",
                "name": "Fifth Why - Root Cause",
                "description": "Ask 'Why does the fourth cause occur?' to reach the root cause",
                "expected_output": "Root cause identification"
            },
            {
                "type": "validation",
                "name": "Validate Root Cause",
                "description": "Verify that addressing the root cause would prevent the original problem",
                "expected_output": "Root cause validation and confirmation"
            },
            {
                "type": "solution_development",
                "name": "Develop Solution",
                "description": "Develop targeted solution that addresses the validated root cause",
                "expected_output": "Root cause solution plan"
            }
        ]

class DesignThinkingMentalModel(MentalModel):
    """Design Thinking mental model - human-centered approach to innovation and problem-solving."""
    
    def __init__(self):
        """Initialize the Design Thinking model."""
        super().__init__(
            name=MentalModelType.DESIGN_THINKING.value,
            description="Human-centered approach to innovation using empathy, ideation, and experimentation"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Design Thinking methodology."""
        return [
            {
                "type": "empathize",
                "name": "Empathize with Users",
                "description": f"Understand the human needs and context related to {task}",
                "expected_output": "User research insights, personas, and empathy maps"
            },
            {
                "type": "define",
                "name": "Define the Problem",
                "description": "Synthesize observations into a clear problem statement from user perspective",
                "expected_output": "Human-centered problem definition and point of view statement"
            },
            {
                "type": "ideate",
                "name": "Ideate Solutions",
                "description": "Generate a wide range of creative solution ideas through brainstorming",
                "expected_output": "Diverse set of potential solution concepts"
            },
            {
                "type": "prototype",
                "name": "Build Prototypes",
                "description": "Create simple, testable representations of the best ideas",
                "expected_output": "Low-fidelity prototypes for testing key assumptions"
            },
            {
                "type": "test",
                "name": "Test with Users",
                "description": "Test prototypes with real users to gather feedback and insights",
                "expected_output": "User feedback, validation results, and iteration insights"
            },
            {
                "type": "iterate",
                "name": "Iterate Based on Learning",
                "description": "Refine solutions based on user feedback and testing results",
                "expected_output": "Improved solution based on user insights"
            },
            {
                "type": "implement",
                "name": "Implement Solution",
                "description": "Develop and deploy the validated, user-centered solution",
                "expected_output": "Implemented solution with user adoption plan"
            }
        ]

class LeanStartupMentalModel(MentalModel):
    """Lean Startup mental model - Build-Measure-Learn cycle for rapid iteration and validation."""
    
    def __init__(self):
        """Initialize the Lean Startup model."""
        super().__init__(
            name=MentalModelType.LEAN_STARTUP.value,
            description="Rapid experimentation methodology using Build-Measure-Learn cycles to validate assumptions"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Lean Startup methodology."""
        return [
            {
                "type": "hypothesis_formation",
                "name": "Form Hypotheses",
                "description": f"Identify key assumptions and hypotheses about {task} that need validation",
                "expected_output": "List of testable hypotheses and assumptions"
            },
            {
                "type": "mvp_design",
                "name": "Design Minimum Viable Product",
                "description": "Design the simplest version that can test your key hypotheses",
                "expected_output": "MVP specification with core features only"
            },
            {
                "type": "build",
                "name": "Build MVP",
                "description": "Build the minimum viable product quickly and efficiently",
                "expected_output": "Functional MVP ready for testing"
            },
            {
                "type": "measure",
                "name": "Measure Results",
                "description": "Deploy MVP and collect data on key metrics and user behavior",
                "expected_output": "Quantitative and qualitative data from real users"
            },
            {
                "type": "learn",
                "name": "Learn from Data",
                "description": "Analyze results to validate or invalidate hypotheses",
                "expected_output": "Validated learning about what works and what doesn't"
            },
            {
                "type": "pivot_or_persevere",
                "name": "Pivot or Persevere Decision",
                "description": "Decide whether to pivot (change direction) or persevere based on learning",
                "expected_output": "Clear decision on next direction with rationale"
            },
            {
                "type": "iteration_planning",
                "name": "Plan Next Iteration",
                "description": "Plan the next Build-Measure-Learn cycle based on insights",
                "expected_output": "Next iteration plan with updated hypotheses"
            },
            {
                "type": "scale_preparation",
                "name": "Prepare for Scale",
                "description": "Once validated, prepare for scaling the successful solution",
                "expected_output": "Scaling strategy and implementation plan"
            }
        ]

class FeedbackLoopsMentalModel(MentalModel):
    """Feedback Loops mental model - understanding how outputs become inputs in systems."""
    
    def __init__(self):
        """Initialize the Feedback Loops model."""
        super().__init__(
            name=MentalModelType.FEEDBACK_LOOPS.value,
            description="Identify and leverage feedback mechanisms where system outputs influence future inputs"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Feedback Loops analysis."""
        return [
            {
                "type": "system_mapping",
                "name": "Map the System",
                "description": f"Map the key components and processes involved in {task}",
                "expected_output": "System diagram showing components, inputs, and outputs"
            },
            {
                "type": "feedback_identification",
                "name": "Identify Feedback Loops",
                "description": "Identify where outputs from one part become inputs to another",
                "expected_output": "List of existing feedback loops in the system"
            },
            {
                "type": "loop_classification",
                "name": "Classify Loop Types",
                "description": "Classify feedback loops as reinforcing (positive) or balancing (negative)",
                "expected_output": "Categorized feedback loops with their effects"
            },
            {
                "type": "delay_analysis",
                "name": "Analyze Delays",
                "description": "Identify time delays between actions and feedback in each loop",
                "expected_output": "Delay analysis for each feedback loop"
            },
            {
                "type": "leverage_points",
                "name": "Find Leverage Points",
                "description": "Identify points where small changes can create big impacts through feedback",
                "expected_output": "High-leverage intervention points in feedback loops"
            },
            {
                "type": "loop_design",
                "name": "Design New Feedback Loops",
                "description": "Design new feedback loops to improve system performance",
                "expected_output": "New feedback mechanisms to enhance system behavior"
            },
            {
                "type": "monitoring_system",
                "name": "Create Monitoring System",
                "description": "Set up monitoring to track feedback loop effectiveness",
                "expected_output": "Monitoring dashboard for feedback loop performance"
            },
            {
                "type": "optimization",
                "name": "Optimize Feedback Loops",
                "description": "Continuously optimize feedback loops based on monitoring data",
                "expected_output": "Optimized feedback system with improved performance"
            }
        ]

class LossAversionMentalModel(MentalModel):
    """Loss Aversion mental model - people prefer avoiding losses over acquiring equivalent gains."""
    
    def __init__(self):
        """Initialize the Loss Aversion model."""
        super().__init__(
            name=MentalModelType.LOSS_AVERSION.value,
            description="Account for loss aversion bias in decision making and change management"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Loss Aversion principles."""
        return [
            {
                "type": "stakeholder_analysis",
                "name": "Identify Stakeholders",
                "description": f"Identify all stakeholders who might experience gains or losses from {task}",
                "expected_output": "Comprehensive stakeholder map with interests"
            },
            {
                "type": "loss_identification",
                "name": "Identify Potential Losses",
                "description": "Identify what stakeholders might perceive as losses or risks",
                "expected_output": "List of perceived losses and risks for each stakeholder"
            },
            {
                "type": "gain_identification",
                "name": "Identify Potential Gains",
                "description": "Identify the benefits and gains that stakeholders will receive",
                "expected_output": "List of benefits and gains for each stakeholder"
            },
            {
                "type": "loss_mitigation",
                "name": "Mitigate Perceived Losses",
                "description": "Develop strategies to minimize or eliminate perceived losses",
                "expected_output": "Loss mitigation strategies and safety nets"
            },
            {
                "type": "gain_framing",
                "name": "Frame Gains Effectively",
                "description": "Frame benefits in ways that overcome loss aversion (e.g., as avoiding future losses)",
                "expected_output": "Compelling gain framing that addresses loss aversion"
            },
            {
                "type": "gradual_implementation",
                "name": "Plan Gradual Implementation",
                "description": "Design gradual implementation to reduce perceived risk and loss",
                "expected_output": "Phased implementation plan with low-risk steps"
            },
            {
                "type": "safety_nets",
                "name": "Create Safety Nets",
                "description": "Establish reversibility and safety mechanisms to reduce fear of loss",
                "expected_output": "Safety mechanisms and reversibility options"
            },
            {
                "type": "communication_strategy",
                "name": "Develop Communication Strategy",
                "description": "Create communication that addresses loss aversion concerns",
                "expected_output": "Communication plan that acknowledges and addresses loss concerns"
            }
        ]

class HanlonsRazorMentalModel(MentalModel):
    """Hanlon's Razor mental model - never attribute to malice that which can be adequately explained by stupidity."""
    
    def __init__(self):
        """Initialize the Hanlon's Razor model."""
        super().__init__(
            name=MentalModelType.HANLONS_RAZOR.value,
            description="Assume incompetence before malice when analyzing problems and conflicts"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Hanlon's Razor principles."""
        return [
            {
                "type": "situation_analysis",
                "name": "Analyze the Situation",
                "description": f"Objectively analyze the situation or problem in {task}",
                "expected_output": "Clear description of what happened and the negative outcomes"
            },
            {
                "type": "assumption_identification",
                "name": "Identify Initial Assumptions",
                "description": "Identify your initial assumptions about intent and motivations",
                "expected_output": "List of assumptions about why the problem occurred"
            },
            {
                "type": "incompetence_analysis",
                "name": "Consider Incompetence Explanations",
                "description": "Explore explanations based on lack of knowledge, skills, or understanding",
                "expected_output": "List of possible incompetence-based explanations"
            },
            {
                "type": "systemic_factors",
                "name": "Examine Systemic Factors",
                "description": "Look for systemic issues like poor processes, lack of resources, or communication failures",
                "expected_output": "Analysis of systemic factors that could explain the problem"
            },
            {
                "type": "evidence_evaluation",
                "name": "Evaluate Evidence for Malice",
                "description": "Only after ruling out incompetence, look for concrete evidence of malicious intent",
                "expected_output": "Evidence-based assessment of whether malice is actually involved"
            },
            {
                "type": "solution_design",
                "name": "Design Appropriate Solution",
                "description": "Design solutions based on the most likely explanation (usually incompetence or systemic issues)",
                "expected_output": "Solution focused on education, process improvement, or system fixes"
            },
            {
                "type": "prevention_strategy",
                "name": "Create Prevention Strategy",
                "description": "Develop strategies to prevent similar issues through better systems and training",
                "expected_output": "Prevention plan addressing root causes rather than assumed malice"
            }
        ]

class ConfirmationBiasAwarenessMentalModel(MentalModel):
    """Confirmation Bias Awareness mental model - recognizing the tendency to search for information that confirms existing beliefs."""
    
    def __init__(self):
        """Initialize the Confirmation Bias Awareness model."""
        super().__init__(
            name=MentalModelType.CONFIRMATION_BIAS_AWARENESS.value,
            description="Actively counteract confirmation bias by seeking disconfirming evidence and diverse perspectives"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Confirmation Bias Awareness principles."""
        return [
            {
                "type": "belief_identification",
                "name": "Identify Current Beliefs",
                "description": f"Identify your current beliefs, assumptions, and hypotheses about {task}",
                "expected_output": "List of current beliefs and assumptions"
            },
            {
                "type": "bias_recognition",
                "name": "Recognize Potential Bias",
                "description": "Acknowledge where confirmation bias might influence your analysis",
                "expected_output": "Assessment of where bias might affect judgment"
            },
            {
                "type": "disconfirming_evidence",
                "name": "Actively Seek Disconfirming Evidence",
                "description": "Deliberately search for evidence that contradicts your beliefs",
                "expected_output": "List of evidence that challenges initial assumptions"
            },
            {
                "type": "diverse_perspectives",
                "name": "Gather Diverse Perspectives",
                "description": "Seek input from people with different backgrounds, experiences, and viewpoints",
                "expected_output": "Collection of diverse viewpoints and opinions"
            },
            {
                "type": "devil_advocate",
                "name": "Play Devil's Advocate",
                "description": "Systematically argue against your own position to test its strength",
                "expected_output": "Strong counterarguments to your initial position"
            },
            {
                "type": "evidence_evaluation",
                "name": "Evaluate All Evidence Objectively",
                "description": "Weigh both confirming and disconfirming evidence fairly",
                "expected_output": "Balanced evaluation of all available evidence"
            },
            {
                "type": "belief_updating",
                "name": "Update Beliefs Based on Evidence",
                "description": "Modify your beliefs and assumptions based on the complete evidence",
                "expected_output": "Updated beliefs that reflect all available evidence"
            },
            {
                "type": "decision_framework",
                "name": "Create Bias-Resistant Decision Framework",
                "description": "Establish processes to minimize confirmation bias in future decisions",
                "expected_output": "Framework for making more objective decisions"
            }
        ]

class AnchoringBiasMentalModel(MentalModel):
    """Anchoring Bias mental model - over-relying on the first piece of information encountered."""
    
    def __init__(self):
        """Initialize the Anchoring Bias model."""
        super().__init__(
            name=MentalModelType.ANCHORING_BIAS.value,
            description="Generate multiple reference points to avoid over-relying on initial information"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Anchoring Bias awareness principles."""
        return [
            {
                "type": "anchor_identification",
                "name": "Identify Potential Anchors",
                "description": f"Identify the first pieces of information or initial estimates related to {task}",
                "expected_output": "List of initial information that might serve as anchors"
            },
            {
                "type": "bias_awareness",
                "name": "Acknowledge Anchoring Risk",
                "description": "Recognize how these initial pieces of information might bias your judgment",
                "expected_output": "Assessment of potential anchoring effects"
            },
            {
                "type": "multiple_references",
                "name": "Generate Multiple Reference Points",
                "description": "Deliberately seek out diverse reference points and starting assumptions",
                "expected_output": "Collection of alternative reference points and baselines"
            },
            {
                "type": "independent_estimation",
                "name": "Make Independent Estimates",
                "description": "Create estimates or judgments without referring to initial anchors",
                "expected_output": "Independent estimates made without anchor influence"
            },
            {
                "type": "range_thinking",
                "name": "Think in Ranges",
                "description": "Consider ranges of possibilities rather than single point estimates",
                "expected_output": "Range-based estimates with minimum and maximum values"
            },
            {
                "type": "outside_view",
                "name": "Take the Outside View",
                "description": "Look at similar situations or base rates to calibrate estimates",
                "expected_output": "External benchmarks and comparison data"
            },
            {
                "type": "deliberate_adjustment",
                "name": "Deliberately Adjust from Anchors",
                "description": "If using anchors, make conscious and sufficient adjustments",
                "expected_output": "Adjusted estimates with explicit reasoning for changes"
            },
            {
                "type": "validation_process",
                "name": "Validate Against Multiple Sources",
                "description": "Cross-check final estimates against multiple independent sources",
                "expected_output": "Validated estimates supported by diverse sources"
            }
        ]

class AvailabilityHeuristicMentalModel(MentalModel):
    """Availability Heuristic mental model - judging probability by how easily examples come to mind."""
    
    def __init__(self):
        """Initialize the Availability Heuristic model."""
        super().__init__(
            name=MentalModelType.AVAILABILITY_HEURISTIC.value,
            description="Counteract availability bias by systematically gathering data rather than relying on memorable examples"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Availability Heuristic awareness principles."""
        return [
            {
                "type": "initial_assessment",
                "name": "Capture Initial Impressions",
                "description": f"Document your initial impressions and easily recalled examples related to {task}",
                "expected_output": "List of memorable examples and initial probability assessments"
            },
            {
                "type": "bias_recognition",
                "name": "Recognize Availability Bias",
                "description": "Identify where memorable or recent events might be skewing your judgment",
                "expected_output": "Assessment of potential availability bias in initial impressions"
            },
            {
                "type": "systematic_data_gathering",
                "name": "Gather Systematic Data",
                "description": "Collect comprehensive data rather than relying on memorable examples",
                "expected_output": "Systematic dataset covering the full scope of relevant information"
            },
            {
                "type": "base_rate_analysis",
                "name": "Analyze Base Rates",
                "description": "Look up actual frequencies and base rates for similar situations",
                "expected_output": "Statistical base rates and frequency data"
            },
            {
                "type": "recency_check",
                "name": "Check for Recency Bias",
                "description": "Examine whether recent events are disproportionately influencing your assessment",
                "expected_output": "Analysis of temporal patterns in your examples and data"
            },
            {
                "type": "media_influence_analysis",
                "name": "Analyze Media Influence",
                "description": "Consider how media coverage might make certain events more memorable",
                "expected_output": "Assessment of media influence on perception of frequency"
            },
            {
                "type": "comprehensive_probability",
                "name": "Calculate Comprehensive Probabilities",
                "description": "Use systematic data to calculate more accurate probability estimates",
                "expected_output": "Data-driven probability estimates with confidence intervals"
            },
            {
                "type": "decision_framework",
                "name": "Create Data-Driven Decision Framework",
                "description": "Establish processes for making decisions based on systematic data rather than availability",
                "expected_output": "Framework for systematic data collection and analysis"
            }
        ]

class PortersFiveForcesModel(MentalModel):
    """Porter's Five Forces mental model - framework for analyzing competitive forces in an industry."""
    
    def __init__(self):
        """Initialize the Porter's Five Forces model."""
        super().__init__(
            name=MentalModelType.PORTERS_FIVE_FORCES.value,
            description="Analyze competitive dynamics through five key forces: competitive rivalry, supplier power, buyer power, threat of substitutes, and barriers to entry"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Porter's Five Forces analysis."""
        return [
            {
                "type": "industry_definition",
                "name": "Define Industry Boundaries",
                "description": f"Clearly define the industry and market scope for {task}",
                "expected_output": "Clear definition of industry boundaries and market scope"
            },
            {
                "type": "competitive_rivalry",
                "name": "Analyze Competitive Rivalry",
                "description": "Assess the intensity of competition among existing competitors",
                "expected_output": "Analysis of competitive intensity, number of competitors, market share distribution, and competitive strategies"
            },
            {
                "type": "supplier_power",
                "name": "Evaluate Supplier Power",
                "description": "Analyze the bargaining power of suppliers in the industry",
                "expected_output": "Assessment of supplier concentration, switching costs, supplier differentiation, and forward integration threats"
            },
            {
                "type": "buyer_power",
                "name": "Assess Buyer Power",
                "description": "Evaluate the bargaining power of customers and buyers",
                "expected_output": "Analysis of buyer concentration, price sensitivity, switching costs, and backward integration potential"
            },
            {
                "type": "substitutes_threat",
                "name": "Analyze Threat of Substitutes",
                "description": "Identify and assess the threat from substitute products or services",
                "expected_output": "List of substitute products/services and their threat level based on price-performance trade-offs"
            },
            {
                "type": "entry_barriers",
                "name": "Evaluate Barriers to Entry",
                "description": "Assess barriers that prevent new competitors from entering the market",
                "expected_output": "Analysis of capital requirements, economies of scale, brand loyalty, regulatory barriers, and access to distribution"
            },
            {
                "type": "force_interaction",
                "name": "Analyze Force Interactions",
                "description": "Examine how the five forces interact and influence each other",
                "expected_output": "Analysis of force interdependencies and combined effects"
            },
            {
                "type": "industry_attractiveness",
                "name": "Assess Industry Attractiveness",
                "description": "Evaluate overall industry attractiveness based on the five forces analysis",
                "expected_output": "Overall industry attractiveness rating with supporting rationale"
            },
            {
                "type": "strategic_implications",
                "name": "Derive Strategic Implications",
                "description": "Identify strategic opportunities and threats based on the five forces analysis",
                "expected_output": "Strategic recommendations for positioning and competitive advantage"
            },
            {
                "type": "monitoring_framework",
                "name": "Create Monitoring Framework",
                "description": "Establish ongoing monitoring of the five forces for strategic planning",
                "expected_output": "Framework for tracking changes in competitive forces over time"
            }
        ]

class BlueOceanStrategyMentalModel(MentalModel):
    """Blue Ocean Strategy mental model - creating uncontested market space rather than competing in existing markets."""
    
    def __init__(self):
        """Initialize the Blue Ocean Strategy model."""
        super().__init__(
            name=MentalModelType.BLUE_OCEAN_STRATEGY.value,
            description="Create new market space by making competition irrelevant through value innovation"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Blue Ocean Strategy principles."""
        return [
            {
                "type": "current_state_analysis",
                "name": "Map Current Competitive Landscape",
                "description": f"Analyze the current competitive landscape and red ocean conditions for {task}",
                "expected_output": "Competitive landscape map showing key players and competition factors"
            },
            {
                "type": "value_curve_analysis",
                "name": "Create Strategy Canvas",
                "description": "Map the current value curve showing how competitors compete on key factors",
                "expected_output": "Strategy canvas showing competitive factors and value curves"
            },
            {
                "type": "four_actions_framework",
                "name": "Apply Four Actions Framework",
                "description": "Identify factors to eliminate, reduce, raise, and create to break the value-cost trade-off",
                "expected_output": "Four actions grid with specific factors for eliminate/reduce/raise/create"
            },
            {
                "type": "non_customer_analysis",
                "name": "Analyze Non-Customers",
                "description": "Identify and analyze the three tiers of non-customers to expand market boundaries",
                "expected_output": "Analysis of soon-to-be, refusing, and unexplored non-customers"
            },
            {
                "type": "alternative_industries",
                "name": "Look Across Alternative Industries",
                "description": "Examine alternative industries that serve similar functions or forms",
                "expected_output": "List of alternative industries and their approaches to similar customer needs"
            },
            {
                "type": "strategic_groups",
                "name": "Look Across Strategic Groups",
                "description": "Analyze different strategic groups within the industry for blue ocean opportunities",
                "expected_output": "Strategic group analysis with opportunities for value innovation"
            },
            {
                "type": "buyer_chain_analysis",
                "name": "Redefine Buyer Chain",
                "description": "Look across the chain of buyers to find new value propositions",
                "expected_output": "Buyer chain analysis with new target buyer identification"
            },
            {
                "type": "blue_ocean_strategy",
                "name": "Formulate Blue Ocean Strategy",
                "description": "Create a new value proposition that makes competition irrelevant",
                "expected_output": "Blue ocean strategy with unique value proposition and positioning"
            },
            {
                "type": "implementation_roadmap",
                "name": "Create Implementation Roadmap",
                "description": "Develop a roadmap for implementing the blue ocean strategy",
                "expected_output": "Implementation plan with milestones, resources, and success metrics"
            }
        ]

class JobsToBeDoneMentalModel(MentalModel):
    """Jobs-to-be-Done Framework mental model - understanding what customers are trying to accomplish."""
    
    def __init__(self):
        """Initialize the Jobs-to-be-Done model."""
        super().__init__(
            name=MentalModelType.JOBS_TO_BE_DONE.value,
            description="Focus on the functional, emotional, and social jobs customers hire products to do"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Jobs-to-be-Done Framework principles."""
        return [
            {
                "type": "job_identification",
                "name": "Identify Core Jobs",
                "description": f"Identify the main jobs customers are trying to get done related to {task}",
                "expected_output": "List of core functional jobs customers need to accomplish"
            },
            {
                "type": "job_mapping",
                "name": "Map Job Steps",
                "description": "Break down each job into detailed steps and sub-jobs",
                "expected_output": "Detailed job map showing all steps in the customer's process"
            },
            {
                "type": "emotional_jobs",
                "name": "Identify Emotional Jobs",
                "description": "Understand the emotional outcomes customers seek when doing the job",
                "expected_output": "List of emotional jobs and desired feelings"
            },
            {
                "type": "social_jobs",
                "name": "Identify Social Jobs",
                "description": "Understand how customers want to be perceived by others when doing the job",
                "expected_output": "List of social jobs and desired perceptions"
            },
            {
                "type": "outcome_expectations",
                "name": "Define Desired Outcomes",
                "description": "Identify the specific outcomes customers use to measure job success",
                "expected_output": "List of outcome statements with importance and satisfaction metrics"
            },
            {
                "type": "constraints_analysis",
                "name": "Analyze Job Constraints",
                "description": "Identify constraints and pain points in the current job execution",
                "expected_output": "Analysis of constraints, barriers, and frustrations"
            },
            {
                "type": "competitive_analysis",
                "name": "Analyze Current Solutions",
                "description": "Evaluate how customers currently get the job done and competing solutions",
                "expected_output": "Analysis of current solutions and their job performance"
            },
            {
                "type": "opportunity_identification",
                "name": "Identify Innovation Opportunities",
                "description": "Find opportunities to help customers get the job done better",
                "expected_output": "Prioritized list of innovation opportunities based on job outcomes"
            },
            {
                "type": "solution_design",
                "name": "Design Job-Focused Solution",
                "description": "Create solutions that help customers get their jobs done better",
                "expected_output": "Solution design focused on job performance rather than product features"
            }
        ]

class ExpectedValueCalculationMentalModel(MentalModel):
    """Expected Value Calculation mental model - calculating the average outcome when the future includes scenarios with different probabilities."""
    
    def __init__(self):
        """Initialize the Expected Value Calculation model."""
        super().__init__(
            name=MentalModelType.EXPECTED_VALUE_CALCULATION.value,
            description="Make decisions by calculating probability-weighted outcomes across different scenarios"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Expected Value Calculation principles."""
        return [
            {
                "type": "scenario_identification",
                "name": "Identify Possible Scenarios",
                "description": f"Identify all possible outcomes and scenarios for {task}",
                "expected_output": "Comprehensive list of possible scenarios and outcomes"
            },
            {
                "type": "probability_estimation",
                "name": "Estimate Probabilities",
                "description": "Assign probability estimates to each scenario based on available data",
                "expected_output": "Probability estimates for each scenario (must sum to 100%)"
            },
            {
                "type": "outcome_quantification",
                "name": "Quantify Outcomes",
                "description": "Assign numerical values to the outcomes of each scenario",
                "expected_output": "Quantified outcomes for each scenario in consistent units"
            },
            {
                "type": "expected_value_calculation",
                "name": "Calculate Expected Values",
                "description": "Calculate expected value by multiplying probabilities by outcomes",
                "expected_output": "Expected value calculation: Σ(Probability × Outcome)"
            },
            {
                "type": "sensitivity_analysis",
                "name": "Perform Sensitivity Analysis",
                "description": "Test how changes in probabilities or outcomes affect the expected value",
                "expected_output": "Sensitivity analysis showing impact of key assumption changes"
            },
            {
                "type": "risk_assessment",
                "name": "Assess Risk and Variance",
                "description": "Calculate variance and standard deviation to understand risk",
                "expected_output": "Risk metrics including variance, standard deviation, and confidence intervals"
            },
            {
                "type": "alternative_comparison",
                "name": "Compare Alternatives",
                "description": "Compare expected values of different alternatives or strategies",
                "expected_output": "Comparative analysis of alternatives with expected values and risk profiles"
            },
            {
                "type": "decision_framework",
                "name": "Create Decision Framework",
                "description": "Establish framework for making decisions based on expected value analysis",
                "expected_output": "Decision criteria incorporating expected value, risk tolerance, and other factors"
            },
            {
                "type": "monitoring_plan",
                "name": "Plan Outcome Monitoring",
                "description": "Create plan to track actual outcomes vs. expected values for learning",
                "expected_output": "Monitoring plan to validate probability estimates and improve future calculations"
            }
        ]

class MonteCarloSimulationMentalModel(MentalModel):
    """Monte Carlo Simulation mental model - using random sampling to understand the impact of risk and uncertainty."""
    
    def __init__(self):
        """Initialize the Monte Carlo Simulation model."""
        super().__init__(
            name=MentalModelType.MONTE_CARLO_SIMULATION.value,
            description="Model uncertainty and risk by running thousands of scenarios with random inputs"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Monte Carlo Simulation principles."""
        return [
            {
                "type": "model_definition",
                "name": "Define the Model",
                "description": f"Define the mathematical model and key variables for {task}",
                "expected_output": "Mathematical model with input variables, relationships, and output metrics"
            },
            {
                "type": "uncertainty_identification",
                "name": "Identify Uncertain Variables",
                "description": "Identify which variables have uncertainty and could vary",
                "expected_output": "List of uncertain input variables with their potential ranges"
            },
            {
                "type": "distribution_modeling",
                "name": "Model Probability Distributions",
                "description": "Define probability distributions for each uncertain variable",
                "expected_output": "Probability distributions (normal, uniform, triangular, etc.) for each variable"
            },
            {
                "type": "correlation_analysis",
                "name": "Analyze Variable Correlations",
                "description": "Identify correlations between variables that should be modeled",
                "expected_output": "Correlation matrix and dependencies between variables"
            },
            {
                "type": "simulation_design",
                "name": "Design Simulation Parameters",
                "description": "Set simulation parameters including number of iterations and random seed",
                "expected_output": "Simulation configuration with iteration count and sampling methodology"
            },
            {
                "type": "simulation_execution",
                "name": "Run Monte Carlo Simulation",
                "description": "Execute the simulation with random sampling from input distributions",
                "expected_output": "Simulation results with thousands of scenario outcomes"
            },
            {
                "type": "results_analysis",
                "name": "Analyze Simulation Results",
                "description": "Analyze the distribution of outcomes and key statistics",
                "expected_output": "Statistical analysis including mean, median, percentiles, and confidence intervals"
            },
            {
                "type": "sensitivity_analysis",
                "name": "Perform Sensitivity Analysis",
                "description": "Identify which input variables have the most impact on outcomes",
                "expected_output": "Sensitivity analysis showing which variables drive the most uncertainty"
            },
            {
                "type": "scenario_planning",
                "name": "Develop Scenario Plans",
                "description": "Create plans for different probability ranges of outcomes",
                "expected_output": "Contingency plans for different outcome scenarios (best case, worst case, most likely)"
            },
            {
                "type": "risk_management",
                "name": "Create Risk Management Strategy",
                "description": "Develop strategies to manage identified risks and uncertainties",
                "expected_output": "Risk management plan with mitigation strategies for key uncertainties"
            }
        ]

class RegressionToMeanMentalModel(MentalModel):
    """Regression to the Mean mental model - extreme measurements tend to be closer to the average on subsequent measurements."""
    
    def __init__(self):
        """Initialize the Regression to the Mean model."""
        super().__init__(
            name=MentalModelType.REGRESSION_TO_MEAN.value,
            description="Account for natural tendency of extreme values to move toward the average over time"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Regression to the Mean principles."""
        return [
            {
                "type": "baseline_establishment",
                "name": "Establish Historical Baseline",
                "description": f"Establish the historical average and normal range for metrics related to {task}",
                "expected_output": "Historical baseline with mean, standard deviation, and normal ranges"
            },
            {
                "type": "extreme_identification",
                "name": "Identify Extreme Values",
                "description": "Identify current measurements that are significantly above or below average",
                "expected_output": "List of extreme values and their deviation from the mean"
            },
            {
                "type": "causation_analysis",
                "name": "Analyze Causes of Extremes",
                "description": "Distinguish between random variation and genuine systematic changes",
                "expected_output": "Analysis separating random fluctuation from real underlying changes"
            },
            {
                "type": "regression_prediction",
                "name": "Predict Regression Effects",
                "description": "Predict how extreme values are likely to move toward the mean",
                "expected_output": "Predictions of future values accounting for regression to mean"
            },
            {
                "type": "intervention_assessment",
                "name": "Assess Intervention Necessity",
                "description": "Determine if interventions are needed or if natural regression will occur",
                "expected_output": "Assessment of whether active intervention is required"
            },
            {
                "type": "measurement_strategy",
                "name": "Design Measurement Strategy",
                "description": "Create measurement approach that accounts for regression effects",
                "expected_output": "Measurement plan with multiple time points and control groups"
            },
            {
                "type": "performance_evaluation",
                "name": "Evaluate Performance Changes",
                "description": "Evaluate performance changes while accounting for regression effects",
                "expected_output": "Performance evaluation methodology that separates real improvement from regression"
            },
            {
                "type": "expectation_management",
                "name": "Manage Expectations",
                "description": "Set realistic expectations about future performance based on regression principles",
                "expected_output": "Realistic performance expectations and communication strategy"
            },
            {
                "type": "monitoring_framework",
                "name": "Create Long-term Monitoring",
                "description": "Establish long-term monitoring to distinguish trends from regression",
                "expected_output": "Monitoring framework to track true performance changes over time"
            }
        ]

class CompoundInterestMentalModel(MentalModel):
    """Compound Interest mental model - interest calculated on initial principal and accumulated interest."""
    
    def __init__(self):
        """Initialize the Compound Interest model."""
        super().__init__(
            name=MentalModelType.COMPOUND_INTEREST.value,
            description="Leverage exponential growth through compounding effects in various domains"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Compound Interest principles."""
        return [
            {
                "type": "baseline_establishment",
                "name": "Establish Starting Point",
                "description": f"Define the initial value, investment, or baseline for {task}",
                "expected_output": "Clear baseline measurement with units and timeframe"
            },
            {
                "type": "growth_rate_analysis",
                "name": "Identify Growth Rate",
                "description": "Determine the rate of growth or improvement that can be sustained",
                "expected_output": "Realistic growth rate with supporting evidence and benchmarks"
            },
            {
                "type": "compounding_frequency",
                "name": "Define Compounding Frequency",
                "description": "Determine how often the growth compounds (daily, monthly, annually)",
                "expected_output": "Compounding schedule with rationale for frequency choice"
            },
            {
                "type": "time_horizon_planning",
                "name": "Set Time Horizon",
                "description": "Define the time period over which compounding will occur",
                "expected_output": "Time horizon with milestones and review periods"
            },
            {
                "type": "exponential_projection",
                "name": "Calculate Exponential Projections",
                "description": "Project future values using compound growth formula",
                "expected_output": "Exponential growth projections with confidence intervals"
            },
            {
                "type": "reinvestment_strategy",
                "name": "Design Reinvestment Strategy",
                "description": "Plan how to reinvest gains to maximize compounding effects",
                "expected_output": "Reinvestment strategy that maximizes compound growth"
            },
            {
                "type": "risk_management",
                "name": "Manage Compounding Risks",
                "description": "Identify and mitigate risks that could interrupt compounding",
                "expected_output": "Risk management plan to protect compound growth"
            },
            {
                "type": "optimization_opportunities",
                "name": "Identify Optimization Opportunities",
                "description": "Find ways to increase growth rate or compounding frequency",
                "expected_output": "Optimization strategies to enhance compounding effects"
            },
            {
                "type": "monitoring_framework",
                "name": "Create Monitoring Framework",
                "description": "Establish tracking system to monitor compound growth progress",
                "expected_output": "Monitoring system with key metrics and review cycles"
            }
        ]

class NetworkEffectsMentalModel(MentalModel):
    """Network Effects mental model - value of a product/service increases as more people use it."""
    
    def __init__(self):
        """Initialize the Network Effects model."""
        super().__init__(
            name=MentalModelType.NETWORK_EFFECTS.value,
            description="Design systems where value increases exponentially with user adoption"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Network Effects principles."""
        return [
            {
                "type": "network_mapping",
                "name": "Map Network Structure",
                "description": f"Map the potential network structure and connections for {task}",
                "expected_output": "Network diagram showing nodes, connections, and value flows"
            },
            {
                "type": "value_proposition_analysis",
                "name": "Analyze Value Proposition",
                "description": "Identify how value increases with each additional user or participant",
                "expected_output": "Value proposition that scales with network size"
            },
            {
                "type": "network_type_identification",
                "name": "Identify Network Type",
                "description": "Determine the type of network effects (direct, indirect, data, social)",
                "expected_output": "Classification of network effects with characteristics"
            },
            {
                "type": "critical_mass_analysis",
                "name": "Define Critical Mass",
                "description": "Identify the minimum number of users needed for network effects to take hold",
                "expected_output": "Critical mass threshold with supporting analysis"
            },
            {
                "type": "chicken_egg_strategy",
                "name": "Solve Chicken-and-Egg Problem",
                "description": "Develop strategy to bootstrap initial user base before network effects kick in",
                "expected_output": "Bootstrap strategy to overcome initial adoption barriers"
            },
            {
                "type": "platform_design",
                "name": "Design Platform for Network Growth",
                "description": "Design platform features that encourage network growth and engagement",
                "expected_output": "Platform design that facilitates and incentivizes network expansion"
            },
            {
                "type": "viral_mechanisms",
                "name": "Create Viral Growth Mechanisms",
                "description": "Build features that encourage users to invite others and expand the network",
                "expected_output": "Viral growth features and referral mechanisms"
            },
            {
                "type": "network_defense",
                "name": "Build Network Defensibility",
                "description": "Create switching costs and lock-in effects to protect the network",
                "expected_output": "Defensibility strategy to maintain network advantages"
            },
            {
                "type": "scaling_strategy",
                "name": "Plan Network Scaling",
                "description": "Develop strategy for scaling the network while maintaining value",
                "expected_output": "Scaling plan that preserves network effects at larger sizes"
            }
        ]

class EconomiesOfScaleMentalModel(MentalModel):
    """Economies of Scale mental model - cost advantages obtained due to size, output, or scale of operation."""
    
    def __init__(self):
        """Initialize the Economies of Scale model."""
        super().__init__(
            name=MentalModelType.ECONOMIES_OF_SCALE.value,
            description="Achieve cost advantages and efficiency improvements through increased scale of operations"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Economies of Scale principles."""
        return [
            {
                "type": "current_scale_analysis",
                "name": "Analyze Current Scale",
                "description": f"Assess the current scale of operations and cost structure for {task}",
                "expected_output": "Current scale metrics with cost breakdown and efficiency measures"
            },
            {
                "type": "scale_opportunities",
                "name": "Identify Scale Opportunities",
                "description": "Identify areas where increased scale could reduce per-unit costs",
                "expected_output": "List of scale opportunities with potential cost savings"
            },
            {
                "type": "fixed_cost_analysis",
                "name": "Analyze Fixed Cost Distribution",
                "description": "Identify fixed costs that can be spread over larger volumes",
                "expected_output": "Fixed cost analysis showing scale leverage opportunities"
            },
            {
                "type": "volume_projections",
                "name": "Project Volume Requirements",
                "description": "Determine volume levels needed to achieve meaningful scale economies",
                "expected_output": "Volume projections with break-even analysis for scale benefits"
            },
            {
                "type": "operational_efficiency",
                "name": "Design Operational Efficiency",
                "description": "Design operations to maximize efficiency gains from increased scale",
                "expected_output": "Operational design optimized for scale efficiency"
            },
            {
                "type": "supply_chain_optimization",
                "name": "Optimize Supply Chain for Scale",
                "description": "Leverage scale to negotiate better supplier terms and reduce procurement costs",
                "expected_output": "Supply chain strategy that leverages scale for cost reduction"
            },
            {
                "type": "technology_leverage",
                "name": "Leverage Technology for Scale",
                "description": "Use technology and automation to achieve scale efficiencies",
                "expected_output": "Technology strategy that enables cost-effective scaling"
            },
            {
                "type": "scale_risks_management",
                "name": "Manage Scale Risks",
                "description": "Identify and mitigate risks associated with scaling operations",
                "expected_output": "Risk management plan for scaling challenges"
            },
            {
                "type": "competitive_advantage",
                "name": "Build Scale-Based Competitive Advantage",
                "description": "Use scale economies to create sustainable competitive advantages",
                "expected_output": "Competitive strategy leveraging scale advantages"
            }
        ]

class BottleneckTheoryMentalModel(MentalModel):
    """Bottleneck Theory (Theory of Constraints) mental model - system performance is limited by its weakest component."""
    
    def __init__(self):
        """Initialize the Bottleneck Theory model."""
        super().__init__(
            name=MentalModelType.BOTTLENECK_THEORY.value,
            description="Optimize system performance by identifying and managing constraints that limit overall throughput"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Bottleneck Theory principles."""
        return [
            {
                "type": "system_mapping",
                "name": "Map the System",
                "description": f"Map the entire system and process flow for {task}",
                "expected_output": "Complete system map showing all processes, dependencies, and flow paths"
            },
            {
                "type": "constraint_identification",
                "name": "Identify System Constraints",
                "description": "Identify the bottlenecks and constraints that limit system performance",
                "expected_output": "List of constraints ranked by their impact on system throughput"
            },
            {
                "type": "throughput_analysis",
                "name": "Analyze Current Throughput",
                "description": "Measure current system throughput and capacity at each stage",
                "expected_output": "Throughput analysis showing capacity and utilization at each stage"
            },
            {
                "type": "constraint_exploitation",
                "name": "Exploit the Constraint",
                "description": "Maximize the output of the identified constraint without additional investment",
                "expected_output": "Optimization plan to fully utilize constraint capacity"
            },
            {
                "type": "system_subordination",
                "name": "Subordinate Everything to the Constraint",
                "description": "Align all other processes to support the constraint's optimal performance",
                "expected_output": "System alignment plan that optimizes constraint utilization"
            },
            {
                "type": "constraint_elevation",
                "name": "Elevate the Constraint",
                "description": "Increase the capacity of the constraint through investment or process improvement",
                "expected_output": "Investment plan to increase constraint capacity"
            },
            {
                "type": "new_constraint_identification",
                "name": "Identify New Constraints",
                "description": "After elevating the constraint, identify the new system bottleneck",
                "expected_output": "Analysis of new constraints that emerge after improvement"
            },
            {
                "type": "continuous_improvement",
                "name": "Implement Continuous Improvement",
                "description": "Establish ongoing process to identify and manage evolving constraints",
                "expected_output": "Continuous improvement framework for constraint management"
            },
            {
                "type": "performance_monitoring",
                "name": "Monitor System Performance",
                "description": "Track system throughput and constraint performance over time",
                "expected_output": "Monitoring system for constraint performance and system throughput"
            }
        ]

class MinimumViableProductMentalModel(MentalModel):
    """Minimum Viable Product (MVP) mental model - product with minimum features to satisfy early customers and provide feedback."""
    
    def __init__(self):
        """Initialize the Minimum Viable Product model."""
        super().__init__(
            name=MentalModelType.MINIMUM_VIABLE_PRODUCT.value,
            description="Build and validate products with minimum features to maximize learning while minimizing development time and cost"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Minimum Viable Product principles."""
        return [
            {
                "type": "problem_validation",
                "name": "Validate Problem Worth Solving",
                "description": f"Validate that the problem addressed by {task} is worth solving",
                "expected_output": "Problem validation with evidence of customer pain points"
            },
            {
                "type": "core_value_identification",
                "name": "Identify Core Value Proposition",
                "description": "Identify the minimum core value that must be delivered to customers",
                "expected_output": "Clear core value proposition that addresses the main customer need"
            },
            {
                "type": "feature_prioritization",
                "name": "Prioritize Essential Features",
                "description": "Identify the minimum set of features needed to deliver core value",
                "expected_output": "Prioritized feature list with only essential MVP features"
            },
            {
                "type": "success_metrics",
                "name": "Define Success Metrics",
                "description": "Define measurable criteria for MVP success and learning objectives",
                "expected_output": "Success metrics and key learning questions to be answered"
            },
            {
                "type": "mvp_design",
                "name": "Design MVP Solution",
                "description": "Design the simplest solution that delivers core value and enables learning",
                "expected_output": "MVP design specification with minimal feature set"
            },
            {
                "type": "rapid_development",
                "name": "Build MVP Rapidly",
                "description": "Develop the MVP quickly using the most efficient methods available",
                "expected_output": "Functional MVP ready for customer testing"
            },
            {
                "type": "customer_testing",
                "name": "Test with Real Customers",
                "description": "Deploy MVP to real customers and gather usage data and feedback",
                "expected_output": "Customer feedback and usage data from MVP deployment"
            },
            {
                "type": "learning_analysis",
                "name": "Analyze Learning and Feedback",
                "description": "Analyze customer feedback and data to validate or invalidate assumptions",
                "expected_output": "Learning analysis with validated/invalidated assumptions"
            },
            {
                "type": "iteration_planning",
                "name": "Plan Next Iteration",
                "description": "Based on learning, plan the next iteration or pivot decision",
                "expected_output": "Next iteration plan or pivot strategy based on MVP learnings"
            }
        ]

class SocialProofMentalModel(MentalModel):
    """Social Proof mental model - people follow the actions of others in uncertain situations."""
    
    def __init__(self):
        """Initialize the Social Proof model."""
        super().__init__(
            name=MentalModelType.SOCIAL_PROOF.value,
            description="Leverage social validation and peer influence to guide behavior and decision-making"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Social Proof principles."""
        return [
            {
                "type": "target_audience_analysis",
                "name": "Analyze Target Audience",
                "description": f"Identify the target audience and their social reference groups for {task}",
                "expected_output": "Target audience profile with key social reference groups and influencers"
            },
            {
                "type": "social_proof_types",
                "name": "Identify Relevant Social Proof Types",
                "description": "Determine which types of social proof are most relevant (expert, user, wisdom of crowds, etc.)",
                "expected_output": "Prioritized list of social proof types with rationale for each"
            },
            {
                "type": "evidence_gathering",
                "name": "Gather Social Proof Evidence",
                "description": "Collect testimonials, reviews, case studies, and usage statistics",
                "expected_output": "Comprehensive collection of social proof evidence and validation"
            },
            {
                "type": "credibility_assessment",
                "name": "Assess Credibility and Authenticity",
                "description": "Ensure social proof evidence is credible, authentic, and verifiable",
                "expected_output": "Verified social proof evidence with credibility assessment"
            },
            {
                "type": "presentation_strategy",
                "name": "Design Presentation Strategy",
                "description": "Plan how to present social proof evidence effectively to the target audience",
                "expected_output": "Social proof presentation strategy with timing and placement"
            },
            {
                "type": "peer_influence_mapping",
                "name": "Map Peer Influence Networks",
                "description": "Identify key influencers and opinion leaders within the target community",
                "expected_output": "Influence network map with key stakeholders and communication channels"
            },
            {
                "type": "social_validation_mechanisms",
                "name": "Create Social Validation Mechanisms",
                "description": "Design systems that make social proof visible and accessible",
                "expected_output": "Social validation systems and feedback mechanisms"
            },
            {
                "type": "behavioral_nudges",
                "name": "Design Behavioral Nudges",
                "description": "Create subtle cues that leverage social proof to guide desired behaviors",
                "expected_output": "Behavioral nudge design using social proof principles"
            },
            {
                "type": "measurement_framework",
                "name": "Establish Measurement Framework",
                "description": "Create metrics to track the effectiveness of social proof strategies",
                "expected_output": "Measurement framework for social proof impact and effectiveness"
            }
        ]

class ReciprocityPrincipleMentalModel(MentalModel):
    """Reciprocity Principle mental model - people feel obligated to return favors."""
    
    def __init__(self):
        """Initialize the Reciprocity Principle model."""
        super().__init__(
            name=MentalModelType.RECIPROCITY_PRINCIPLE.value,
            description="Build relationships and influence through strategic giving and mutual benefit creation"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Reciprocity Principle."""
        return [
            {
                "type": "stakeholder_mapping",
                "name": "Map Key Stakeholders",
                "description": f"Identify key stakeholders and their needs/interests for {task}",
                "expected_output": "Stakeholder map with needs, interests, and influence levels"
            },
            {
                "type": "value_identification",
                "name": "Identify Value to Offer",
                "description": "Determine what value, help, or benefits you can provide to stakeholders",
                "expected_output": "Value proposition for each stakeholder with specific offerings"
            },
            {
                "type": "reciprocity_opportunities",
                "name": "Identify Reciprocity Opportunities",
                "description": "Find opportunities to give first and create reciprocal obligations",
                "expected_output": "List of reciprocity opportunities with timing and approach"
            },
            {
                "type": "giving_strategy",
                "name": "Design Strategic Giving Strategy",
                "description": "Plan how to give value in ways that create positive reciprocal relationships",
                "expected_output": "Strategic giving plan with specific actions and timing"
            },
            {
                "type": "relationship_building",
                "name": "Build Reciprocal Relationships",
                "description": "Execute giving strategy to build trust and reciprocal obligations",
                "expected_output": "Relationship building actions with follow-up plans"
            },
            {
                "type": "reciprocal_requests",
                "name": "Plan Reciprocal Requests",
                "description": "Strategically plan when and how to make requests based on reciprocal relationships",
                "expected_output": "Request strategy with timing and approach for each stakeholder"
            },
            {
                "type": "mutual_benefit_design",
                "name": "Design Mutual Benefit Scenarios",
                "description": "Create win-win scenarios that benefit all parties involved",
                "expected_output": "Mutual benefit scenarios with clear value for all parties"
            },
            {
                "type": "relationship_maintenance",
                "name": "Maintain Reciprocal Relationships",
                "description": "Plan ongoing relationship maintenance and continued value exchange",
                "expected_output": "Relationship maintenance plan with regular touchpoints"
            },
            {
                "type": "reciprocity_tracking",
                "name": "Track Reciprocity Balance",
                "description": "Monitor the balance of giving and receiving in relationships",
                "expected_output": "Reciprocity tracking system with relationship health metrics"
            }
        ]

class CommitmentConsistencyMentalModel(MentalModel):
    """Commitment and Consistency mental model - people want to be consistent with previous commitments."""
    
    def __init__(self):
        """Initialize the Commitment and Consistency model."""
        super().__init__(
            name=MentalModelType.COMMITMENT_CONSISTENCY.value,
            description="Leverage commitment psychology to drive consistent behavior and goal achievement"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Commitment and Consistency principles."""
        return [
            {
                "type": "goal_clarification",
                "name": "Clarify Goals and Objectives",
                "description": f"Define clear, specific goals and objectives for {task}",
                "expected_output": "Clear, measurable goals with specific success criteria"
            },
            {
                "type": "commitment_design",
                "name": "Design Commitment Mechanisms",
                "description": "Create formal and informal commitment mechanisms to increase follow-through",
                "expected_output": "Commitment mechanisms including public declarations and accountability"
            },
            {
                "type": "small_commitments",
                "name": "Start with Small Commitments",
                "description": "Begin with small, achievable commitments to build consistency momentum",
                "expected_output": "Series of small, progressive commitments leading to larger goals"
            },
            {
                "type": "public_accountability",
                "name": "Create Public Accountability",
                "description": "Make commitments public to leverage social pressure for consistency",
                "expected_output": "Public accountability system with stakeholder involvement"
            },
            {
                "type": "written_commitments",
                "name": "Document Written Commitments",
                "description": "Create written records of commitments to increase psychological ownership",
                "expected_output": "Written commitment documents with signatures and dates"
            },
            {
                "type": "consistency_tracking",
                "name": "Track Consistency Metrics",
                "description": "Monitor adherence to commitments and consistency over time",
                "expected_output": "Consistency tracking system with regular progress reviews"
            },
            {
                "type": "identity_alignment",
                "name": "Align with Personal Identity",
                "description": "Connect commitments to personal identity and values for stronger consistency",
                "expected_output": "Identity-based commitment framework linking actions to self-concept"
            },
            {
                "type": "escalation_ladder",
                "name": "Create Commitment Escalation Ladder",
                "description": "Design progressive commitment levels that build on previous consistency",
                "expected_output": "Escalation ladder with increasing commitment levels and rewards"
            },
            {
                "type": "consistency_reinforcement",
                "name": "Reinforce Consistent Behavior",
                "description": "Create systems to recognize and reinforce consistent behavior patterns",
                "expected_output": "Reinforcement system with recognition and reward mechanisms"
            }
        ]

class ScarcityPrincipleMentalModel(MentalModel):
    """Scarcity Principle mental model - people value things more when they are rare or limited."""
    
    def __init__(self):
        """Initialize the Scarcity Principle model."""
        super().__init__(
            name=MentalModelType.SCARCITY_PRINCIPLE.value,
            description="Leverage scarcity psychology to increase perceived value and drive action"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Scarcity Principle."""
        return [
            {
                "type": "scarcity_analysis",
                "name": "Analyze Natural Scarcity",
                "description": f"Identify naturally scarce resources, opportunities, or constraints in {task}",
                "expected_output": "Analysis of natural scarcity factors and their impact"
            },
            {
                "type": "artificial_scarcity_design",
                "name": "Design Artificial Scarcity",
                "description": "Create legitimate scarcity through limited availability, time constraints, or exclusive access",
                "expected_output": "Artificial scarcity mechanisms with ethical boundaries"
            },
            {
                "type": "urgency_creation",
                "name": "Create Sense of Urgency",
                "description": "Develop time-based scarcity to motivate immediate action",
                "expected_output": "Urgency framework with deadlines and time-sensitive opportunities"
            },
            {
                "type": "exclusivity_positioning",
                "name": "Position for Exclusivity",
                "description": "Create exclusive access or membership to increase perceived value",
                "expected_output": "Exclusivity strategy with clear membership criteria and benefits"
            },
            {
                "type": "limited_availability",
                "name": "Implement Limited Availability",
                "description": "Use quantity limits to create scarcity and increase demand",
                "expected_output": "Limited availability strategy with clear quantity constraints"
            },
            {
                "type": "loss_framing",
                "name": "Frame Potential Losses",
                "description": "Emphasize what people might lose by not acting rather than what they might gain",
                "expected_output": "Loss-framed messaging that highlights missed opportunities"
            },
            {
                "type": "social_scarcity",
                "name": "Leverage Social Scarcity",
                "description": "Use competition and social dynamics to create scarcity pressure",
                "expected_output": "Social scarcity mechanisms using competition and peer pressure"
            },
            {
                "type": "scarcity_communication",
                "name": "Communicate Scarcity Effectively",
                "description": "Develop clear, honest communication about scarcity without manipulation",
                "expected_output": "Scarcity communication strategy with ethical messaging"
            },
            {
                "type": "value_amplification",
                "name": "Amplify Value Through Scarcity",
                "description": "Use scarcity to highlight and amplify the true value of offerings",
                "expected_output": "Value amplification strategy that leverages scarcity psychology"
            }
        ]

class FishboneDiagramMentalModel(MentalModel):
    """Fishbone Diagram (Ishikawa) mental model - visual tool to systematically identify potential causes of a problem."""
    
    def __init__(self):
        """Initialize the Fishbone Diagram model."""
        super().__init__(
            name=MentalModelType.FISHBONE_DIAGRAM.value,
            description="Systematically identify and categorize potential causes of problems using structured cause-and-effect analysis"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Fishbone Diagram principles."""
        return [
            {
                "type": "problem_definition",
                "name": "Define the Problem Clearly",
                "description": f"Clearly define the specific problem or effect to be analyzed in {task}",
                "expected_output": "Clear, specific problem statement with measurable impact"
            },
            {
                "type": "category_identification",
                "name": "Identify Cause Categories",
                "description": "Determine the main categories of potential causes (6Ms: Man, Machine, Method, Material, Measurement, Environment)",
                "expected_output": "List of relevant cause categories appropriate for the problem domain"
            },
            {
                "type": "team_assembly",
                "name": "Assemble Cross-Functional Team",
                "description": "Gather team members with diverse perspectives and expertise relevant to the problem",
                "expected_output": "Cross-functional team with representatives from all relevant areas"
            },
            {
                "type": "brainstorming_session",
                "name": "Conduct Structured Brainstorming",
                "description": "Systematically brainstorm potential causes within each category",
                "expected_output": "Comprehensive list of potential causes organized by category"
            },
            {
                "type": "cause_drilling",
                "name": "Drill Down into Root Causes",
                "description": "For each potential cause, ask 'why' to identify deeper root causes",
                "expected_output": "Detailed cause hierarchy showing relationships between causes"
            },
            {
                "type": "evidence_gathering",
                "name": "Gather Supporting Evidence",
                "description": "Collect data and evidence to validate or eliminate potential causes",
                "expected_output": "Evidence-based validation of potential causes with supporting data"
            },
            {
                "type": "cause_prioritization",
                "name": "Prioritize Most Likely Causes",
                "description": "Rank causes by likelihood, impact, and ability to address them",
                "expected_output": "Prioritized list of causes with impact and feasibility assessment"
            },
            {
                "type": "action_planning",
                "name": "Develop Action Plans",
                "description": "Create specific action plans to address the highest priority root causes",
                "expected_output": "Action plans with specific steps, owners, and timelines for each priority cause"
            },
            {
                "type": "monitoring_framework",
                "name": "Create Monitoring Framework",
                "description": "Establish metrics and monitoring to track the effectiveness of corrective actions",
                "expected_output": "Monitoring framework with metrics to track problem resolution progress"
            }
        ]

class LateralThinkingMentalModel(MentalModel):
    """Lateral Thinking mental model - solving problems through indirect and creative approaches."""
    
    def __init__(self):
        """Initialize the Lateral Thinking model."""
        super().__init__(
            name=MentalModelType.LATERAL_THINKING.value,
            description="Generate creative solutions through indirect approaches, challenging assumptions, and exploring unconventional perspectives"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Lateral Thinking principles."""
        return [
            {
                "type": "assumption_identification",
                "name": "Identify Current Assumptions",
                "description": f"List all assumptions being made about {task} and the problem space",
                "expected_output": "Comprehensive list of assumptions with their underlying beliefs"
            },
            {
                "type": "assumption_challenging",
                "name": "Challenge Core Assumptions",
                "description": "Systematically question and challenge each assumption to open new possibilities",
                "expected_output": "Analysis of challenged assumptions with alternative perspectives"
            },
            {
                "type": "random_stimulation",
                "name": "Apply Random Stimulation",
                "description": "Use random words, images, or concepts to trigger new ideas and connections",
                "expected_output": "List of random stimuli and the creative connections they generate"
            },
            {
                "type": "perspective_shifting",
                "name": "Shift Perspectives",
                "description": "View the problem from different roles, industries, cultures, or time periods",
                "expected_output": "Multiple perspective analyses with unique insights from each viewpoint"
            },
            {
                "type": "reversal_technique",
                "name": "Apply Reversal Techniques",
                "description": "Consider the opposite of the problem or reverse the desired outcome",
                "expected_output": "Reversal analysis with insights from opposite scenarios"
            },
            {
                "type": "metaphor_exploration",
                "name": "Explore Metaphors and Analogies",
                "description": "Use metaphors from nature, other industries, or unrelated domains",
                "expected_output": "Metaphorical analysis with creative solution possibilities"
            },
            {
                "type": "constraint_removal",
                "name": "Remove Artificial Constraints",
                "description": "Identify and temporarily remove constraints that may not be necessary",
                "expected_output": "Constraint analysis with unconstrained solution possibilities"
            },
            {
                "type": "idea_combination",
                "name": "Combine Unrelated Ideas",
                "description": "Force connections between unrelated concepts to generate novel solutions",
                "expected_output": "Creative combinations with potential breakthrough solutions"
            },
            {
                "type": "solution_refinement",
                "name": "Refine and Develop Solutions",
                "description": "Take the most promising lateral ideas and develop them into practical solutions",
                "expected_output": "Refined creative solutions with implementation feasibility assessment"
            }
        ]

class SunkCostFallacyMentalModel(MentalModel):
    """Sunk Cost Fallacy mental model - continuing investment based on previously invested resources rather than future value."""
    
    def __init__(self):
        """Initialize the Sunk Cost Fallacy model."""
        super().__init__(
            name=MentalModelType.SUNK_COST_FALLACY.value,
            description="Make rational decisions by focusing on future value rather than past investments"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Sunk Cost Fallacy awareness."""
        return [
            {
                "type": "sunk_cost_identification",
                "name": "Identify Sunk Costs",
                "description": f"Identify all resources already invested in {task} that cannot be recovered",
                "expected_output": "Comprehensive inventory of sunk costs including time, money, and effort"
            },
            {
                "type": "future_value_analysis",
                "name": "Analyze Future Value Potential",
                "description": "Assess the potential future value and returns independent of past investments",
                "expected_output": "Future value analysis based solely on forward-looking potential"
            },
            {
                "type": "decision_reframing",
                "name": "Reframe Decision Context",
                "description": "Reframe the decision as if starting fresh, ignoring past investments",
                "expected_output": "Fresh decision framework that excludes sunk cost considerations"
            },
            {
                "type": "opportunity_cost_assessment",
                "name": "Assess Opportunity Costs",
                "description": "Evaluate alternative uses of future resources and their potential returns",
                "expected_output": "Opportunity cost analysis comparing alternative resource allocations"
            },
            {
                "type": "exit_criteria_definition",
                "name": "Define Clear Exit Criteria",
                "description": "Establish objective criteria for when to discontinue the investment",
                "expected_output": "Clear, measurable exit criteria independent of past investments"
            },
            {
                "type": "emotional_attachment_recognition",
                "name": "Recognize Emotional Attachments",
                "description": "Identify emotional attachments to past investments that may cloud judgment",
                "expected_output": "Analysis of emotional factors and their impact on decision-making"
            },
            {
                "type": "independent_evaluation",
                "name": "Conduct Independent Evaluation",
                "description": "Get external perspective from someone not invested in past decisions",
                "expected_output": "Independent evaluation and recommendations from unbiased perspective"
            },
            {
                "type": "incremental_decision_making",
                "name": "Make Incremental Decisions",
                "description": "Break large decisions into smaller increments to reduce sunk cost pressure",
                "expected_output": "Incremental decision framework with regular review points"
            },
            {
                "type": "learning_extraction",
                "name": "Extract Learning Value",
                "description": "Identify lessons learned from past investments regardless of continuation decision",
                "expected_output": "Learning summary that preserves value from past investments"
            }
        ]

class TimeValueOfMoneyMentalModel(MentalModel):
    """Time Value of Money mental model - money available now is worth more than the same amount in the future."""
    
    def __init__(self):
        """Initialize the Time Value of Money model."""
        super().__init__(
            name=MentalModelType.TIME_VALUE_OF_MONEY.value,
            description="Make financial decisions by accounting for the time value of money and opportunity costs"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Time Value of Money principles."""
        return [
            {
                "type": "cash_flow_mapping",
                "name": "Map Cash Flow Timeline",
                "description": f"Map all cash inflows and outflows over time for {task}",
                "expected_output": "Detailed cash flow timeline with amounts and timing"
            },
            {
                "type": "discount_rate_determination",
                "name": "Determine Appropriate Discount Rate",
                "description": "Establish the discount rate based on risk, opportunity cost, and market conditions",
                "expected_output": "Justified discount rate with supporting analysis"
            },
            {
                "type": "present_value_calculation",
                "name": "Calculate Present Values",
                "description": "Convert all future cash flows to present value using the discount rate",
                "expected_output": "Present value calculations for all cash flows"
            },
            {
                "type": "net_present_value_analysis",
                "name": "Analyze Net Present Value",
                "description": "Calculate the net present value to assess overall project value",
                "expected_output": "Net present value analysis with profitability assessment"
            },
            {
                "type": "sensitivity_analysis",
                "name": "Conduct Sensitivity Analysis",
                "description": "Test how changes in discount rate and timing affect present values",
                "expected_output": "Sensitivity analysis showing impact of key variable changes"
            },
            {
                "type": "alternative_comparison",
                "name": "Compare Alternative Investments",
                "description": "Compare the present values of different investment alternatives",
                "expected_output": "Comparative analysis of alternative investments using present value"
            },
            {
                "type": "inflation_adjustment",
                "name": "Adjust for Inflation",
                "description": "Account for inflation effects on future cash flows and purchasing power",
                "expected_output": "Inflation-adjusted cash flow analysis with real vs nominal values"
            },
            {
                "type": "payback_period_analysis",
                "name": "Analyze Payback Periods",
                "description": "Calculate both simple and discounted payback periods",
                "expected_output": "Payback period analysis with time-adjusted calculations"
            },
            {
                "type": "decision_framework",
                "name": "Create Decision Framework",
                "description": "Establish decision criteria based on time value analysis",
                "expected_output": "Decision framework incorporating time value considerations"
            }
        ]

class RiskReturnTradeoffMentalModel(MentalModel):
    """Risk-Return Tradeoff mental model - higher potential returns come with higher risk."""
    
    def __init__(self):
        """Initialize the Risk-Return Tradeoff model."""
        super().__init__(
            name=MentalModelType.RISK_RETURN_TRADEOFF.value,
            description="Balance risk and return to make optimal investment and strategic decisions"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Risk-Return Tradeoff principles."""
        return [
            {
                "type": "return_potential_analysis",
                "name": "Analyze Return Potential",
                "description": f"Assess the potential returns and upside scenarios for {task}",
                "expected_output": "Return analysis with best-case, expected, and conservative scenarios"
            },
            {
                "type": "risk_identification",
                "name": "Identify Risk Factors",
                "description": "Systematically identify all risk factors that could impact returns",
                "expected_output": "Comprehensive risk inventory with impact and probability assessments"
            },
            {
                "type": "risk_quantification",
                "name": "Quantify Risk Levels",
                "description": "Measure and quantify the identified risks using appropriate metrics",
                "expected_output": "Risk quantification with volatility measures and downside scenarios"
            },
            {
                "type": "risk_return_mapping",
                "name": "Map Risk-Return Relationships",
                "description": "Create visual mapping of risk levels against potential returns",
                "expected_output": "Risk-return matrix showing relationship between risk and reward"
            },
            {
                "type": "risk_tolerance_assessment",
                "name": "Assess Risk Tolerance",
                "description": "Determine the appropriate risk tolerance based on objectives and constraints",
                "expected_output": "Risk tolerance profile with acceptable risk levels"
            },
            {
                "type": "efficient_frontier_analysis",
                "name": "Analyze Efficient Frontier",
                "description": "Identify optimal risk-return combinations for different scenarios",
                "expected_output": "Efficient frontier analysis showing optimal risk-return combinations"
            },
            {
                "type": "risk_mitigation_strategies",
                "name": "Develop Risk Mitigation Strategies",
                "description": "Create strategies to reduce risk while preserving return potential",
                "expected_output": "Risk mitigation strategies with cost-benefit analysis"
            },
            {
                "type": "scenario_planning",
                "name": "Conduct Scenario Planning",
                "description": "Plan for different risk-return scenarios and their implications",
                "expected_output": "Scenario plans with risk-adjusted return expectations"
            },
            {
                "type": "monitoring_framework",
                "name": "Create Risk-Return Monitoring",
                "description": "Establish ongoing monitoring of risk-return performance",
                "expected_output": "Monitoring framework with risk-adjusted performance metrics"
            }
        ]

class DiversificationMentalModel(MentalModel):
    """Diversification mental model - spreading investments or efforts to reduce risk."""
    
    def __init__(self):
        """Initialize the Diversification model."""
        super().__init__(
            name=MentalModelType.DIVERSIFICATION.value,
            description="Reduce risk and improve outcomes by spreading investments, efforts, or strategies across multiple areas"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Diversification principles."""
        return [
            {
                "type": "concentration_risk_analysis",
                "name": "Analyze Concentration Risks",
                "description": f"Identify areas where {task} has excessive concentration and vulnerability",
                "expected_output": "Concentration risk analysis with vulnerability assessment"
            },
            {
                "type": "diversification_opportunities",
                "name": "Identify Diversification Opportunities",
                "description": "Find opportunities to spread risk across different areas, markets, or strategies",
                "expected_output": "List of diversification opportunities with risk reduction potential"
            },
            {
                "type": "correlation_analysis",
                "name": "Analyze Correlations",
                "description": "Assess correlations between different options to ensure true diversification",
                "expected_output": "Correlation analysis showing independence of diversification options"
            },
            {
                "type": "diversification_strategy",
                "name": "Design Diversification Strategy",
                "description": "Create a balanced approach that spreads risk while maintaining focus",
                "expected_output": "Diversification strategy with optimal allocation across options"
            },
            {
                "type": "resource_allocation",
                "name": "Allocate Resources Across Options",
                "description": "Determine optimal resource allocation across diversified options",
                "expected_output": "Resource allocation plan with diversification rationale"
            },
            {
                "type": "performance_tracking",
                "name": "Track Diversified Performance",
                "description": "Monitor performance across all diversified areas to assess effectiveness",
                "expected_output": "Performance tracking system for diversified portfolio"
            },
            {
                "type": "rebalancing_framework",
                "name": "Create Rebalancing Framework",
                "description": "Establish criteria and process for rebalancing diversified allocations",
                "expected_output": "Rebalancing framework with triggers and procedures"
            },
            {
                "type": "over_diversification_prevention",
                "name": "Prevent Over-Diversification",
                "description": "Ensure diversification doesn't dilute focus or create management complexity",
                "expected_output": "Guidelines to prevent over-diversification while maintaining benefits"
            },
            {
                "type": "diversification_review",
                "name": "Regular Diversification Review",
                "description": "Establish regular review process to assess and adjust diversification strategy",
                "expected_output": "Review framework for ongoing diversification optimization"
            }
        ]

class PyramidPrincipleMentalModel(MentalModel):
    """Pyramid Principle mental model - structuring communication with conclusion first, then supporting arguments."""
    
    def __init__(self):
        """Initialize the Pyramid Principle model."""
        super().__init__(
            name=MentalModelType.PYRAMID_PRINCIPLE.value,
            description="Structure communication effectively by leading with conclusions and supporting with logical arguments"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Pyramid Principle."""
        return [
            {
                "type": "main_message_identification",
                "name": "Identify Main Message",
                "description": f"Define the single, clear main message or conclusion for {task}",
                "expected_output": "Clear, concise main message that captures the core conclusion"
            },
            {
                "type": "audience_analysis",
                "name": "Analyze Target Audience",
                "description": "Understand the audience's knowledge level, interests, and decision-making needs",
                "expected_output": "Audience profile with communication preferences and requirements"
            },
            {
                "type": "supporting_arguments",
                "name": "Develop Supporting Arguments",
                "description": "Create 3-5 key supporting arguments that logically support the main message",
                "expected_output": "Logical supporting arguments with clear connection to main message"
            },
            {
                "type": "evidence_gathering",
                "name": "Gather Supporting Evidence",
                "description": "Collect data, examples, and evidence to support each argument",
                "expected_output": "Comprehensive evidence base for each supporting argument"
            },
            {
                "type": "logical_grouping",
                "name": "Group Information Logically",
                "description": "Organize supporting information into logical groups and hierarchies",
                "expected_output": "Logical information hierarchy with clear groupings"
            },
            {
                "type": "structure_design",
                "name": "Design Pyramid Structure",
                "description": "Create the pyramid structure with conclusion at top and supporting layers below",
                "expected_output": "Visual pyramid structure showing information hierarchy"
            },
            {
                "type": "flow_optimization",
                "name": "Optimize Information Flow",
                "description": "Ensure smooth logical flow from conclusion through supporting arguments",
                "expected_output": "Optimized information flow with clear transitions"
            },
            {
                "type": "clarity_testing",
                "name": "Test for Clarity",
                "description": "Review structure for clarity, completeness, and logical consistency",
                "expected_output": "Clarity assessment with recommendations for improvement"
            },
            {
                "type": "presentation_preparation",
                "name": "Prepare Final Presentation",
                "description": "Format the pyramid structure for effective delivery to the audience",
                "expected_output": "Final presentation structure optimized for audience and medium"
            }
        ]

class StorytellingFrameworkMentalModel(MentalModel):
    """Storytelling Framework mental model - using narrative structure to communicate ideas effectively."""
    
    def __init__(self):
        """Initialize the Storytelling Framework model."""
        super().__init__(
            name=MentalModelType.STORYTELLING_FRAMEWORK.value,
            description="Communicate ideas effectively through compelling narrative structures and emotional engagement"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Storytelling Framework."""
        return [
            {
                "type": "core_message_identification",
                "name": "Identify Core Message",
                "description": f"Define the key message or lesson to be conveyed through the story for {task}",
                "expected_output": "Clear core message that the story will communicate"
            },
            {
                "type": "audience_connection",
                "name": "Understand Audience Connection",
                "description": "Identify what will resonate emotionally and intellectually with the target audience",
                "expected_output": "Audience connection analysis with emotional and rational triggers"
            },
            {
                "type": "story_structure_selection",
                "name": "Select Story Structure",
                "description": "Choose appropriate narrative structure (hero's journey, problem-solution, before-after, etc.)",
                "expected_output": "Selected story structure with rationale for choice"
            },
            {
                "type": "character_development",
                "name": "Develop Characters",
                "description": "Create relatable characters that the audience can connect with",
                "expected_output": "Character profiles with motivations, challenges, and relatability factors"
            },
            {
                "type": "conflict_tension_creation",
                "name": "Create Conflict and Tension",
                "description": "Develop compelling conflict or challenge that drives the narrative forward",
                "expected_output": "Conflict structure that creates engagement and drives toward resolution"
            },
            {
                "type": "emotional_arc_design",
                "name": "Design Emotional Arc",
                "description": "Plan the emotional journey that will take the audience from beginning to end",
                "expected_output": "Emotional arc mapping with key emotional beats and transitions"
            },
            {
                "type": "sensory_details",
                "name": "Add Sensory Details",
                "description": "Include vivid, sensory details that make the story memorable and engaging",
                "expected_output": "Sensory detail inventory that brings the story to life"
            },
            {
                "type": "resolution_alignment",
                "name": "Align Resolution with Message",
                "description": "Ensure the story resolution clearly reinforces the core message",
                "expected_output": "Story resolution that powerfully delivers the intended message"
            },
            {
                "type": "delivery_optimization",
                "name": "Optimize Story Delivery",
                "description": "Adapt the story for the specific medium and context of delivery",
                "expected_output": "Delivery-optimized story format with timing and presentation notes"
            }
        ]

class ActiveListeningMentalModel(MentalModel):
    """Active Listening mental model - fully concentrating on, understanding, and responding to the speaker."""
    
    def __init__(self):
        """Initialize the Active Listening model."""
        super().__init__(
            name=MentalModelType.ACTIVE_LISTENING.value,
            description="Improve communication and relationships through focused, empathetic listening practices"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Active Listening principles."""
        return [
            {
                "type": "listening_environment",
                "name": "Create Optimal Listening Environment",
                "description": f"Establish an environment conducive to focused listening for {task}",
                "expected_output": "Optimized listening environment with minimal distractions"
            },
            {
                "type": "mental_preparation",
                "name": "Prepare Mental State",
                "description": "Clear mental distractions and prepare to focus fully on the speaker",
                "expected_output": "Mental preparation routine for focused listening"
            },
            {
                "type": "nonverbal_attention",
                "name": "Demonstrate Nonverbal Attention",
                "description": "Use body language and eye contact to show engagement and attention",
                "expected_output": "Nonverbal communication strategy that demonstrates active engagement"
            },
            {
                "type": "content_listening",
                "name": "Listen for Content",
                "description": "Focus on understanding the factual information and key points being shared",
                "expected_output": "Content comprehension with key points and factual information"
            },
            {
                "type": "emotional_listening",
                "name": "Listen for Emotions",
                "description": "Pay attention to emotional undertones, feelings, and unspoken concerns",
                "expected_output": "Emotional understanding with recognition of feelings and concerns"
            },
            {
                "type": "clarifying_questions",
                "name": "Ask Clarifying Questions",
                "description": "Use open-ended questions to deepen understanding and show engagement",
                "expected_output": "Clarifying question strategy that enhances understanding"
            },
            {
                "type": "paraphrasing_reflection",
                "name": "Paraphrase and Reflect",
                "description": "Reflect back what you've heard to confirm understanding",
                "expected_output": "Paraphrasing technique that validates understanding"
            },
            {
                "type": "empathetic_response",
                "name": "Respond Empathetically",
                "description": "Acknowledge emotions and demonstrate understanding of the speaker's perspective",
                "expected_output": "Empathetic response framework that validates the speaker's experience"
            },
            {
                "type": "action_planning",
                "name": "Plan Follow-up Actions",
                "description": "Identify and commit to specific actions based on what was heard",
                "expected_output": "Action plan that demonstrates the value of the listening session"
            }
        ]

class NonviolentCommunicationMentalModel(MentalModel):
    """Nonviolent Communication mental model - communication approach based on empathy and honest expression."""
    
    def __init__(self):
        """Initialize the Nonviolent Communication model."""
        super().__init__(
            name=MentalModelType.NONVIOLENT_COMMUNICATION.value,
            description="Communicate with empathy and honesty to resolve conflicts and build understanding"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Nonviolent Communication principles."""
        return [
            {
                "type": "observation_without_evaluation",
                "name": "Make Observations Without Evaluation",
                "description": f"Describe the specific, observable facts about {task} without judgment or interpretation",
                "expected_output": "Factual observations free from evaluation, judgment, or interpretation"
            },
            {
                "type": "feelings_identification",
                "name": "Identify and Express Feelings",
                "description": "Recognize and articulate your genuine feelings about the situation",
                "expected_output": "Clear expression of feelings using emotion words rather than thoughts"
            },
            {
                "type": "needs_recognition",
                "name": "Recognize Underlying Needs",
                "description": "Identify the universal human needs that are or aren't being met",
                "expected_output": "Identification of underlying needs that drive the feelings"
            },
            {
                "type": "specific_requests",
                "name": "Make Specific Requests",
                "description": "Formulate clear, specific, doable requests that could meet the identified needs",
                "expected_output": "Specific, actionable requests that address the underlying needs"
            },
            {
                "type": "empathetic_listening",
                "name": "Listen Empathetically",
                "description": "Listen for the observations, feelings, needs, and requests of others",
                "expected_output": "Empathetic understanding of others' observations, feelings, needs, and requests"
            },
            {
                "type": "self_empathy",
                "name": "Practice Self-Empathy",
                "description": "Apply the same compassionate understanding to your own experience",
                "expected_output": "Self-empathy practice that maintains emotional balance"
            },
            {
                "type": "conflict_transformation",
                "name": "Transform Conflict",
                "description": "Use NVC principles to transform conflict into opportunities for connection",
                "expected_output": "Conflict transformation strategy using NVC framework"
            },
            {
                "type": "boundary_setting",
                "name": "Set Protective Boundaries",
                "description": "Establish boundaries that protect needs while maintaining connection",
                "expected_output": "Boundary-setting approach that protects needs compassionately"
            },
            {
                "type": "connection_building",
                "name": "Build Authentic Connection",
                "description": "Foster genuine human connection through vulnerable, honest communication",
                "expected_output": "Connection-building strategy that promotes mutual understanding"
            }
        ]

class InfluenceMappingMentalModel(MentalModel):
    """Influence Mapping mental model - identifying and understanding stakeholder influence relationships."""
    
    def __init__(self):
        """Initialize the Influence Mapping model."""
        super().__init__(
            name=MentalModelType.INFLUENCE_MAPPING.value,
            description="Navigate complex stakeholder relationships by mapping influence networks and power dynamics"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Influence Mapping principles."""
        return [
            {
                "type": "stakeholder_identification",
                "name": "Identify All Stakeholders",
                "description": f"Map all individuals and groups who have interest or influence in {task}",
                "expected_output": "Comprehensive stakeholder list with roles and interests"
            },
            {
                "type": "influence_assessment",
                "name": "Assess Influence Levels",
                "description": "Evaluate the level of influence each stakeholder has on the outcome",
                "expected_output": "Influence assessment with high/medium/low classifications"
            },
            {
                "type": "interest_analysis",
                "name": "Analyze Stakeholder Interests",
                "description": "Understand what each stakeholder cares about and their motivations",
                "expected_output": "Interest analysis with motivations and priorities for each stakeholder"
            },
            {
                "type": "relationship_mapping",
                "name": "Map Stakeholder Relationships",
                "description": "Identify relationships, alliances, and conflicts between stakeholders",
                "expected_output": "Relationship map showing connections and dynamics between stakeholders"
            },
            {
                "type": "power_source_analysis",
                "name": "Analyze Sources of Power",
                "description": "Identify where each stakeholder's influence comes from (position, expertise, resources, etc.)",
                "expected_output": "Power source analysis showing basis of each stakeholder's influence"
            },
            {
                "type": "influence_strategy",
                "name": "Develop Influence Strategy",
                "description": "Create targeted approaches for engaging with different stakeholder groups",
                "expected_output": "Influence strategy with specific approaches for each stakeholder type"
            },
            {
                "type": "coalition_building",
                "name": "Build Strategic Coalitions",
                "description": "Identify opportunities to build alliances and coalitions among stakeholders",
                "expected_output": "Coalition-building strategy with potential alliances and partnerships"
            },
            {
                "type": "communication_planning",
                "name": "Plan Stakeholder Communication",
                "description": "Design communication strategies tailored to each stakeholder's influence and interests",
                "expected_output": "Communication plan with tailored messages and channels for each stakeholder"
            },
            {
                "type": "influence_monitoring",
                "name": "Monitor Influence Changes",
                "description": "Establish ongoing monitoring of stakeholder influence and relationship dynamics",
                "expected_output": "Monitoring system for tracking changes in stakeholder influence and relationships"
            }
        ]

class GrowthMindsetMentalModel(MentalModel):
    """Growth Mindset mental model - belief that abilities can be developed through dedication and hard work."""
    
    def __init__(self):
        """Initialize the Growth Mindset model."""
        super().__init__(
            name=MentalModelType.GROWTH_MINDSET.value,
            description="Foster continuous learning and development through belief in ability to grow and improve"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Growth Mindset principles."""
        return [
            {
                "type": "mindset_assessment",
                "name": "Assess Current Mindset",
                "description": f"Evaluate current beliefs about ability and intelligence related to {task}",
                "expected_output": "Mindset assessment identifying fixed vs growth mindset patterns"
            },
            {
                "type": "challenge_reframing",
                "name": "Reframe Challenges as Opportunities",
                "description": "View obstacles and setbacks as opportunities for learning and growth",
                "expected_output": "Reframed perspective that sees challenges as growth opportunities"
            },
            {
                "type": "effort_valuation",
                "name": "Value Effort and Process",
                "description": "Focus on effort, strategy, and process rather than just outcomes",
                "expected_output": "Process-focused approach that values learning over performance"
            },
            {
                "type": "feedback_embracing",
                "name": "Embrace Constructive Feedback",
                "description": "Actively seek and use feedback as a tool for improvement",
                "expected_output": "Feedback-seeking strategy that promotes continuous improvement"
            },
            {
                "type": "failure_learning",
                "name": "Learn from Failures",
                "description": "Extract valuable lessons from failures and setbacks",
                "expected_output": "Learning framework that transforms failures into growth opportunities"
            },
            {
                "type": "skill_development",
                "name": "Focus on Skill Development",
                "description": "Prioritize developing skills and capabilities over proving existing abilities",
                "expected_output": "Skill development plan focused on continuous improvement"
            },
            {
                "type": "inspiration_from_others",
                "name": "Find Inspiration in Others' Success",
                "description": "Use others' success as inspiration and learning opportunities",
                "expected_output": "Strategy for learning from and being inspired by others' achievements"
            },
            {
                "type": "persistence_cultivation",
                "name": "Cultivate Persistence",
                "description": "Develop resilience and persistence in the face of obstacles",
                "expected_output": "Persistence strategy that maintains motivation through challenges"
            },
            {
                "type": "growth_celebration",
                "name": "Celebrate Growth and Progress",
                "description": "Recognize and celebrate learning, improvement, and progress",
                "expected_output": "Recognition system that celebrates growth and learning achievements"
            }
        ]

class DeliberatePracticeMentalModel(MentalModel):
    """Deliberate Practice mental model - purposeful practice with immediate feedback and repetition."""
    
    def __init__(self):
        """Initialize the Deliberate Practice model."""
        super().__init__(
            name=MentalModelType.DELIBERATE_PRACTICE.value,
            description="Achieve expertise through focused, purposeful practice with immediate feedback"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Deliberate Practice principles."""
        return [
            {
                "type": "skill_assessment",
                "name": "Assess Current Skill Level",
                "description": f"Evaluate current skill level and identify specific areas for improvement in {task}",
                "expected_output": "Detailed skill assessment with specific improvement areas identified"
            },
            {
                "type": "specific_goals",
                "name": "Set Specific Practice Goals",
                "description": "Define clear, specific, and challenging goals for each practice session",
                "expected_output": "Specific, measurable practice goals with clear success criteria"
            },
            {
                "type": "focused_practice",
                "name": "Engage in Focused Practice",
                "description": "Practice with full concentration on specific skills that need improvement",
                "expected_output": "Structured practice sessions with focused attention on target skills"
            },
            {
                "type": "immediate_feedback",
                "name": "Seek Immediate Feedback",
                "description": "Get immediate feedback on performance to identify errors and corrections",
                "expected_output": "Feedback system that provides immediate performance insights"
            },
            {
                "type": "error_analysis",
                "name": "Analyze Errors and Mistakes",
                "description": "Systematically analyze errors to understand root causes and prevention",
                "expected_output": "Error analysis framework with corrective action plans"
            },
            {
                "type": "progressive_difficulty",
                "name": "Increase Difficulty Progressively",
                "description": "Gradually increase the difficulty of practice tasks as skills improve",
                "expected_output": "Progressive difficulty framework that challenges current skill level"
            },
            {
                "type": "repetition_refinement",
                "name": "Repeat and Refine",
                "description": "Repeat practice with continuous refinement based on feedback",
                "expected_output": "Repetition schedule with refinement strategies"
            },
            {
                "type": "mental_models",
                "name": "Develop Mental Models",
                "description": "Build mental models and frameworks that support skill development",
                "expected_output": "Mental models that enhance understanding and performance"
            },
            {
                "type": "performance_tracking",
                "type": "goal_setting",
                "name": "Set Specific Goals",
                "description": "Set clear, specific, and challenging goals for skill improvement",
                "expected_output": "Specific, measurable, achievable, relevant, and time-bound goals"
            },
            {
                "type": "deliberate_practice",
                "name": "Engage in Deliberate Practice",
                "description": "Practice skills in a focused, deliberate manner",
                "expected_output": "Regular, structured practice sessions with specific focus"
            },
            {
                "type": "feedback_seeking",
                "name": "Seek Constructive Feedback",
                "description": "Seek feedback from peers or mentors to improve performance",
                "expected_output": "Regular feedback sessions with actionable insights"
            },
            {
                "type": "skill_analysis",
                "name": "Analyze Skill Gaps",
                "description": "Identify specific areas for improvement and develop targeted practice plans",
                "expected_output": "Detailed analysis of skill gaps and development strategies"
            },
            {
                "type": "mindset_reinforcement",
                "name": "Develop Growth Mindset",
                "description": "Cultivate a growth mindset that views challenges as opportunities",
                "expected_output": "Strategies for maintaining a growth mindset during practice"
            },
            {
                "type": "progress_tracking",
                "name": "Track Progress",
                "description": "Monitor progress and adjust practice based on feedback",
                "expected_output": "Regular progress tracking and self-assessment"
            },
            {
                "type": "peer_feedback",
                "name": "Receive Peer Feedback",
                "description": "Seek feedback from peers to improve performance",
                "expected_output": "Constructive feedback sessions with actionable insights"
            },
            {
                "type": "skill_review",
                "name": "Review Skills",
                "description": "Regularly review and reflect on progress and areas for improvement",
                "expected_output": "Self-assessment of skill level and development plan review"
            },
            {
                "type": "continuous_learning",
                "name": "Engage in Continuous Learning",
                "description": "Stay updated with new knowledge and skills through reading, courses, or workshops",
                "expected_output": "Regular learning activities that enhance skill set"
            }
        ]

class DoubleLoopLearningMentalModel(MentalModel):
    """Double-Loop Learning mental model - questioning underlying assumptions and mental models, not just actions."""
    
    def __init__(self):
        """Initialize the Double-Loop Learning model."""
        super().__init__(
            name=MentalModelType.DOUBLE_LOOP_LEARNING.value,
            description="Learn by questioning underlying assumptions and mental models, not just correcting actions"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Double-Loop Learning principles."""
        return [
            {
                "type": "assumption_identification",
                "name": "Identify Underlying Assumptions",
                "description": f"Identify the underlying assumptions and beliefs that guide actions in {task}",
                "expected_output": "Comprehensive list of underlying assumptions and beliefs"
            },
            {
                "type": "assumption_questioning",
                "name": "Question Core Assumptions",
                "description": "Systematically question and challenge fundamental assumptions",
                "expected_output": "Critical analysis of core assumptions with alternative perspectives"
            },
            {
                "type": "mental_model_examination",
                "name": "Examine Mental Models",
                "description": "Analyze the mental models and frameworks that shape thinking and decision-making",
                "expected_output": "Analysis of current mental models and their limitations"
            },
            {
                "type": "feedback_loop_analysis",
                "name": "Analyze Feedback Loops",
                "description": "Examine how current mental models create feedback loops that reinforce existing patterns",
                "expected_output": "Feedback loop analysis showing reinforcement patterns"
            },
            {
                "type": "alternative_frameworks",
                "name": "Explore Alternative Frameworks",
                "description": "Consider alternative mental models and frameworks for understanding the situation",
                "expected_output": "Alternative frameworks and mental models for consideration"
            },
            {
                "type": "assumption_testing",
                "name": "Test New Assumptions",
                "description": "Design experiments to test new assumptions and mental models",
                "expected_output": "Experimental design to validate new assumptions and approaches"
            },
            {
                "type": "learning_integration",
                "name": "Integrate New Learning",
                "description": "Integrate insights from assumption questioning into new mental models",
                "expected_output": "Updated mental models incorporating new insights and learning"
            },
            {
                "type": "behavioral_change",
                "name": "Implement Behavioral Changes",
                "description": "Translate new mental models into concrete behavioral and strategic changes",
                "expected_output": "Action plan implementing changes based on new mental models"
            },
            {
                "type": "continuous_reflection",
                "name": "Establish Continuous Reflection",
                "description": "Create ongoing processes for questioning assumptions and updating mental models",
                "expected_output": "Reflection framework for continuous assumption questioning and learning"
            }
        ]

class AntifragilityMentalModel(MentalModel):
    """Antifragility mental model - systems that gain from disorder and stress."""
    
    def __init__(self):
        """Initialize the Antifragility model."""
        super().__init__(
            name=MentalModelType.ANTIFRAGILITY.value,
            description="Build systems and strategies that gain strength from volatility, stress, and disorder"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Antifragility principles."""
        return [
            {
                "type": "fragility_assessment",
                "name": "Assess Current Fragility",
                "description": f"Evaluate how {task} responds to stress, volatility, and unexpected events",
                "expected_output": "Fragility assessment identifying vulnerable areas and stress responses"
            },
            {
                "type": "stressor_identification",
                "name": "Identify Potential Stressors",
                "description": "Map potential sources of stress, volatility, and disorder",
                "expected_output": "Comprehensive stressor inventory with impact and probability analysis"
            },
            {
                "type": "antifragile_design",
                "name": "Design Antifragile Systems",
                "description": "Create systems that benefit from stress and volatility rather than just surviving them",
                "expected_output": "System design that gains strength from disorder and stress"
            },
            {
                "type": "optionality_creation",
                "name": "Create Optionality",
                "description": "Build in options and flexibility that provide upside from uncertainty",
                "expected_output": "Optionality framework that benefits from uncertainty and change"
            },
            {
                "type": "redundancy_planning",
                "name": "Plan Strategic Redundancy",
                "description": "Implement redundancy that strengthens rather than just protects the system",
                "expected_output": "Redundancy strategy that adds strength and capability"
            },
            {
                "type": "small_failures",
                "name": "Encourage Small Failures",
                "description": "Design for small, frequent failures that prevent large catastrophic ones",
                "expected_output": "Failure strategy that builds immunity through small stresses"
            },
            {
                "type": "learning_mechanisms",
                "name": "Build Learning Mechanisms",
                "description": "Create systems that learn and adapt from each stressor encountered",
                "expected_output": "Learning framework that converts stress into capability"
            },
            {
                "type": "asymmetric_payoffs",
                "name": "Seek Asymmetric Payoffs",
                "description": "Pursue opportunities with limited downside but unlimited upside potential",
                "expected_output": "Strategy for asymmetric risk-reward opportunities"
            },
            {
                "type": "antifragile_monitoring",
                "name": "Monitor Antifragile Progress",
                "description": "Track how well the system gains from disorder and stress over time",
                "expected_output": "Monitoring system for antifragile characteristics and improvements"
            }
        ]

class BlackSwanEventsMentalModel(MentalModel):
    """Black Swan Events mental model - rare, unpredictable events with major impact."""
    
    def __init__(self):
        """Initialize the Black Swan Events model."""
        super().__init__(
            name=MentalModelType.BLACK_SWAN_EVENTS.value,
            description="Prepare for and benefit from rare, unpredictable events with major impact"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Black Swan Events principles."""
        return [
            {
                "type": "black_swan_awareness",
                "name": "Develop Black Swan Awareness",
                "description": f"Recognize the potential for rare, high-impact events in {task}",
                "expected_output": "Awareness framework for identifying potential black swan scenarios"
            },
            {
                "type": "historical_analysis",
                "name": "Analyze Historical Black Swans",
                "description": "Study past black swan events in similar contexts to understand patterns",
                "expected_output": "Historical analysis of black swan events with pattern identification"
            },
            {
                "type": "scenario_imagination",
                "name": "Imagine Extreme Scenarios",
                "description": "Brainstorm extreme, low-probability but high-impact scenarios",
                "expected_output": "Extreme scenario inventory with impact and response considerations"
            },
            {
                "type": "robustness_building",
                "name": "Build Robustness",
                "description": "Create systems that can survive extreme, unexpected events",
                "expected_output": "Robustness strategy that withstands extreme scenarios"
            },
            {
                "type": "positive_black_swans",
                "name": "Position for Positive Black Swans",
                "description": "Create conditions to benefit from positive unexpected events",
                "expected_output": "Strategy to capture upside from positive black swan events"
            },
            {
                "type": "early_warning_systems",
                "name": "Develop Early Warning Systems",
                "description": "Create systems to detect early signals of potential black swan events",
                "expected_output": "Early warning framework for black swan event detection"
            },
            {
                "type": "rapid_response_capability",
                "name": "Build Rapid Response Capability",
                "description": "Develop ability to respond quickly when black swan events occur",
                "expected_output": "Rapid response framework for black swan event management"
            },
            {
                "type": "narrative_fallacy_avoidance",
                "name": "Avoid Narrative Fallacy",
                "description": "Resist the tendency to create neat explanations for random events",
                "expected_output": "Framework for avoiding post-hoc rationalization of random events"
            },
            {
                "type": "uncertainty_embrace",
                "name": "Embrace Uncertainty",
                "description": "Accept and work with fundamental uncertainty rather than trying to predict it",
                "expected_output": "Uncertainty management approach that works with unpredictability"
            }
        ]

class MetacognitionMentalModel(MentalModel):
    """Metacognition mental model - thinking about thinking; awareness of one's own thought processes."""
    
    def __init__(self):
        """Initialize the Metacognition model."""
        super().__init__(
            name=MentalModelType.METACOGNITION.value,
            description="Improve thinking and decision-making through awareness and regulation of thought processes"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Metacognition principles."""
        return [
            {
                "type": "thinking_awareness",
                "name": "Develop Thinking Awareness",
                "description": f"Become aware of your thinking patterns and processes while working on {task}",
                "expected_output": "Self-awareness of thinking patterns, biases, and cognitive processes"
            },
            {
                "type": "cognitive_monitoring",
                "name": "Monitor Cognitive Processes",
                "description": "Actively monitor your understanding, reasoning, and problem-solving approaches",
                "expected_output": "Cognitive monitoring system for tracking thinking effectiveness"
            },
            {
                "type": "strategy_evaluation",
                "name": "Evaluate Thinking Strategies",
                "description": "Assess the effectiveness of different thinking strategies and approaches",
                "expected_output": "Strategy evaluation framework for optimizing thinking approaches"
            },
            {
                "type": "bias_recognition",
                "name": "Recognize Cognitive Biases",
                "description": "Identify when cognitive biases might be influencing thinking and decisions",
                "expected_output": "Bias recognition system with corrective strategies"
            },
            {
                "type": "thinking_regulation",
                "name": "Regulate Thinking Processes",
                "description": "Actively control and adjust thinking strategies based on effectiveness",
                "expected_output": "Thinking regulation framework for optimizing cognitive performance"
            },
            {
                "type": "reflection_practice",
                "name": "Practice Regular Reflection",
                "description": "Engage in regular reflection on thinking processes and outcomes",
                "expected_output": "Reflection practice that improves metacognitive awareness"
            },
            {
                "type": "learning_optimization",
                "name": "Optimize Learning Strategies",
                "description": "Use metacognitive awareness to improve learning and knowledge acquisition",
                "expected_output": "Learning optimization strategy based on metacognitive insights"
            },
            {
                "type": "decision_quality",
                "name": "Improve Decision Quality",
                "description": "Apply metacognitive awareness to enhance decision-making processes",
                "expected_output": "Decision-making framework enhanced by metacognitive awareness"
            },
            {
                "type": "metacognitive_development",
                "name": "Develop Metacognitive Skills",
                "description": "Continuously develop and refine metacognitive abilities",
                "expected_output": "Metacognitive skill development plan with practice strategies"
            }
        ]

class DunningKrugerEffectMentalModel(MentalModel):
    """Dunning-Kruger Effect mental model - cognitive bias where people with limited knowledge overestimate their competence."""
    
    def __init__(self):
        """Initialize the Dunning-Kruger Effect model."""
        super().__init__(
            name=MentalModelType.DUNNING_KRUGER_EFFECT.value,
            description="Recognize and mitigate overconfidence bias from limited knowledge or experience"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Dunning-Kruger Effect principles."""
        return [
            {
                "type": "competence_assessment",
                "name": "Assess True Competence Level",
                "description": f"Objectively evaluate actual knowledge and skill level in {task}",
                "expected_output": "Honest assessment of current competence with evidence-based evaluation"
            },
            {
                "type": "knowledge_gaps",
                "name": "Identify Knowledge Gaps",
                "description": "Systematically identify what you don't know or understand",
                "expected_output": "Comprehensive inventory of knowledge gaps and learning needs"
            },
            {
                "type": "expert_consultation",
                "name": "Seek Expert Perspectives",
                "description": "Consult with genuine experts to calibrate understanding and competence",
                "expected_output": "Expert feedback that provides realistic competence calibration"
            },
            {
                "type": "overconfidence_monitoring",
                "name": "Monitor for Overconfidence",
                "description": "Actively watch for signs of overconfidence and unwarranted certainty",
                "expected_output": "Overconfidence monitoring system with corrective mechanisms"
            },
            {
                "type": "learning_humility",
                "name": "Cultivate Learning Humility",
                "description": "Develop intellectual humility and openness to being wrong",
                "expected_output": "Humility framework that promotes continuous learning"
            },
            {
                "type": "feedback_seeking",
                "name": "Actively Seek Feedback",
                "description": "Regularly seek honest feedback about performance and understanding",
                "expected_output": "Feedback system that provides accurate performance insights"
            },
            {
                "type": "competence_calibration",
                "name": "Calibrate Confidence with Competence",
                "description": "Align confidence levels with actual competence and evidence",
                "expected_output": "Calibration framework that matches confidence to competence"
            },
            {
                "type": "continuous_learning",
                "name": "Embrace Continuous Learning",
                "description": "Maintain a learning mindset that acknowledges ongoing knowledge gaps",
                "expected_output": "Learning strategy that prevents overconfidence through continuous growth"
            },
            {
                "type": "decision_quality",
                "name": "Improve Decision Quality",
                "description": "Make better decisions by accounting for competence limitations",
                "expected_output": "Decision-making framework that accounts for knowledge limitations"
            }
        ]

class ImpostorSyndromeMentalModel(MentalModel):
    """Impostor Syndrome mental model - persistent feeling of being a fraud despite evidence of competence."""
    
    def __init__(self):
        """Initialize the Impostor Syndrome model."""
        super().__init__(
            name=MentalModelType.IMPOSTOR_SYNDROME.value,
            description="Recognize and overcome impostor syndrome to build authentic confidence"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Impostor Syndrome principles."""
        return [
            {
                "type": "syndrome_recognition",
                "name": "Recognize Impostor Feelings",
                "description": f"Identify when impostor syndrome is affecting confidence and performance in {task}",
                "expected_output": "Recognition framework for identifying impostor syndrome patterns"
            },
            {
                "type": "evidence_collection",
                "name": "Collect Evidence of Competence",
                "description": "Systematically document achievements, skills, and positive feedback",
                "expected_output": "Evidence portfolio demonstrating actual competence and achievements"
            },
            {
                "type": "thought_challenging",
                "name": "Challenge Negative Self-Talk",
                "description": "Question and reframe negative thoughts about competence and worthiness",
                "expected_output": "Cognitive reframing techniques for impostor-related thoughts"
            },
            {
                "type": "attribution_reframing",
                "name": "Reframe Success Attribution",
                "description": "Attribute successes to skill and effort rather than luck or external factors",
                "expected_output": "Attribution framework that recognizes personal contribution to success"
            },
            {
                "type": "perfectionism_management",
                "name": "Manage Perfectionism",
                "description": "Address perfectionist tendencies that fuel impostor feelings",
                "expected_output": "Perfectionism management strategy that promotes healthy standards"
            },
            {
                "type": "peer_comparison",
                "name": "Reframe Peer Comparisons",
                "description": "Develop healthy perspectives on comparing yourself to others",
                "expected_output": "Comparison framework that focuses on personal growth over competition"
            },
            {
                "type": "mentorship_seeking",
                "name": "Seek Mentorship and Support",
                "description": "Connect with mentors and peers who can provide perspective and encouragement",
                "expected_output": "Support network that provides realistic feedback and encouragement"
            },
            {
                "type": "growth_mindset",
                "name": "Adopt Growth Mindset",
                "description": "Focus on learning and development rather than proving competence",
                "expected_output": "Growth mindset approach that reduces impostor syndrome pressure"
            },
            {
                "type": "authentic_confidence",
                "name": "Build Authentic Confidence",
                "description": "Develop genuine confidence based on actual skills and continuous learning",
                "expected_output": "Authentic confidence framework grounded in real competence and growth"
            }
        ]

class BeginnersMindMentalModel(MentalModel):
    """Beginner's Mind mental model - approaching situations with openness, eagerness, and freedom from preconceptions."""
    
    def __init__(self):
        """Initialize the Beginner's Mind model."""
        super().__init__(
            name=MentalModelType.BEGINNERS_MIND.value,
            description="Approach challenges with openness, curiosity, and freedom from limiting preconceptions"
        )
    
    async def generate_steps(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate planning steps using Beginner's Mind principles."""
        return [
            {
                "type": "preconception_awareness",
                "name": "Identify Preconceptions",
                "description": f"Recognize existing assumptions and preconceptions about {task}",
                "expected_output": "Inventory of assumptions and preconceptions that might limit thinking"
            },
            {
                "type": "curiosity_cultivation",
                "name": "Cultivate Curiosity",
                "description": "Approach the situation with genuine curiosity and wonder",
                "expected_output": "Curiosity framework that promotes exploration and discovery"
            },
            {
                "type": "fresh_perspective",
                "name": "Seek Fresh Perspectives",
                "description": "Look at the situation as if seeing it for the first time",
                "expected_output": "Fresh perspective approach that reveals new insights and possibilities"
            },
            {
                "type": "question_generation",
                "name": "Generate Naive Questions",
                "description": "Ask basic, fundamental questions without worrying about appearing ignorant",
                "expected_output": "Question framework that uncovers fundamental insights"
            },
            {
                "type": "assumption_suspension",
                "name": "Suspend Assumptions",
                "description": "Temporarily set aside what you think you know to see new possibilities",
                "expected_output": "Assumption suspension technique that opens new pathways"
            },
            {
                "type": "learning_eagerness",
                "name": "Embrace Learning Eagerness",
                "description": "Approach with enthusiasm for learning and discovery",
                "expected_output": "Learning eagerness that drives exploration and growth"
            },
            {
                "type": "expert_beginner_balance",
                "name": "Balance Expertise with Openness",
                "description": "Use existing knowledge while remaining open to new insights",
                "expected_output": "Balance framework that leverages expertise without limiting openness"
            },
            {
                "type": "mindful_presence",
                "name": "Practice Mindful Presence",
                "description": "Stay present and attentive to what is actually happening",
                "expected_output": "Mindfulness practice that enhances awareness and openness"
            },
            {
                "type": "beginner_benefits",
                "name": "Leverage Beginner's Advantages",
                "description": "Recognize and utilize the unique advantages of a beginner's perspective",
                "expected_output": "Strategy for leveraging beginner's mind advantages in problem-solving"
            }
        ]

# Registry of available mental models
_MENTAL_MODELS: Dict[str, Type[MentalModel]] = {
    MentalModelType.DEFAULT.value: DefaultMentalModel,
    MentalModelType.FIRST_PRINCIPLES.value: FirstPrinciplesMentalModel,
    MentalModelType.SYSTEMS_THINKING.value: SystemsThinkingMentalModel,
    MentalModelType.CRITICAL_PATH.value: CriticalPathMentalModel,
    MentalModelType.DECISION_TREE.value: DecisionTreeMentalModel,
    MentalModelType.OCCAMS_RAZOR.value: OccamsRazorMentalModel,
    MentalModelType.SWOT_ANALYSIS.value: SWOTAnalysisMentalModel,
    MentalModelType.PARETO_PRINCIPLE.value: ParetoPrincipleMentalModel,
    MentalModelType.ROOT_CAUSE_ANALYSIS.value: RootCauseAnalysisMentalModel,
    MentalModelType.OPPORTUNITY_COST.value: OpportunityCostMentalModel,
    MentalModelType.FIVE_WHYS.value: FiveWhysMentalModel,
    MentalModelType.DESIGN_THINKING.value: DesignThinkingMentalModel,
    MentalModelType.LEAN_STARTUP.value: LeanStartupMentalModel,
    MentalModelType.FEEDBACK_LOOPS.value: FeedbackLoopsMentalModel,
    MentalModelType.LOSS_AVERSION.value: LossAversionMentalModel,
    MentalModelType.HANLONS_RAZOR.value: HanlonsRazorMentalModel,
    MentalModelType.CONFIRMATION_BIAS_AWARENESS.value: ConfirmationBiasAwarenessMentalModel,
    MentalModelType.ANCHORING_BIAS.value: AnchoringBiasMentalModel,
    MentalModelType.AVAILABILITY_HEURISTIC.value: AvailabilityHeuristicMentalModel,
    MentalModelType.PORTERS_FIVE_FORCES.value: PortersFiveForcesModel,
    MentalModelType.BLUE_OCEAN_STRATEGY.value: BlueOceanStrategyMentalModel,
    MentalModelType.JOBS_TO_BE_DONE.value: JobsToBeDoneMentalModel,
    MentalModelType.EXPECTED_VALUE_CALCULATION.value: ExpectedValueCalculationMentalModel,
    MentalModelType.MONTE_CARLO_SIMULATION.value: MonteCarloSimulationMentalModel,
    MentalModelType.REGRESSION_TO_MEAN.value: RegressionToMeanMentalModel,
    MentalModelType.COMPOUND_INTEREST.value: CompoundInterestMentalModel,
    MentalModelType.NETWORK_EFFECTS.value: NetworkEffectsMentalModel,
    MentalModelType.ECONOMIES_OF_SCALE.value: EconomiesOfScaleMentalModel,
    MentalModelType.BOTTLENECK_THEORY.value: BottleneckTheoryMentalModel,
    MentalModelType.MINIMUM_VIABLE_PRODUCT.value: MinimumViableProductMentalModel,
    MentalModelType.SOCIAL_PROOF.value: SocialProofMentalModel,
    MentalModelType.RECIPROCITY_PRINCIPLE.value: ReciprocityPrincipleMentalModel,
    MentalModelType.COMMITMENT_CONSISTENCY.value: CommitmentConsistencyMentalModel,
    MentalModelType.SCARCITY_PRINCIPLE.value: ScarcityPrincipleMentalModel,
    MentalModelType.FISHBONE_DIAGRAM.value: FishboneDiagramMentalModel,
    MentalModelType.LATERAL_THINKING.value: LateralThinkingMentalModel,
    MentalModelType.SUNK_COST_FALLACY.value: SunkCostFallacyMentalModel,
    MentalModelType.TIME_VALUE_OF_MONEY.value: TimeValueOfMoneyMentalModel,
    MentalModelType.RISK_RETURN_TRADEOFF.value: RiskReturnTradeoffMentalModel,
    MentalModelType.DIVERSIFICATION.value: DiversificationMentalModel,
    MentalModelType.PYRAMID_PRINCIPLE.value: PyramidPrincipleMentalModel,
    MentalModelType.STORYTELLING_FRAMEWORK.value: StorytellingFrameworkMentalModel,
    MentalModelType.ACTIVE_LISTENING.value: ActiveListeningMentalModel,
    MentalModelType.NONVIOLENT_COMMUNICATION.value: NonviolentCommunicationMentalModel,
    MentalModelType.INFLUENCE_MAPPING.value: InfluenceMappingMentalModel,
    MentalModelType.GROWTH_MINDSET.value: GrowthMindsetMentalModel,
    MentalModelType.DELIBERATE_PRACTICE.value: DeliberatePracticeMentalModel,
    MentalModelType.DOUBLE_LOOP_LEARNING.value: DoubleLoopLearningMentalModel,
    MentalModelType.ANTIFRAGILITY.value: AntifragilityMentalModel,
    MentalModelType.BLACK_SWAN_EVENTS.value: BlackSwanEventsMentalModel,
    MentalModelType.METACOGNITION.value: MetacognitionMentalModel,
    MentalModelType.DUNNING_KRUGER_EFFECT.value: DunningKrugerEffectMentalModel,
    MentalModelType.IMPOSTOR_SYNDROME.value: ImpostorSyndromeMentalModel,
    MentalModelType.BEGINNERS_MIND.value: BeginnersMindMentalModel
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