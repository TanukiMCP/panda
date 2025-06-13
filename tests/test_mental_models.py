"""
Tests for PandA mental models
"""

import pytest
from src.panda_mcp.core.planning.mental_models import (
    DefaultMentalModel,
    FirstPrinciplesMentalModel,
    SystemsThinkingMentalModel,
    CriticalPathMentalModel,
    DecisionTreeMentalModel,
    get_mental_model,
    register_mental_model,
    MentalModelType
)

class TestDefaultMentalModel:
    """Test DefaultMentalModel functionality."""
    
    @pytest.mark.asyncio
    async def test_generate_steps(self):
        """Test generating steps with default mental model."""
        model = DefaultMentalModel()
        task = "Build a web application"
        context = {"domain": "e-commerce"}
        
        steps = await model.generate_steps(task, context)
        
        assert len(steps) == 4
        assert steps[0]["type"] == "analysis"
        assert steps[0]["name"] == "Analyze Requirements"
        assert steps[1]["type"] == "planning"
        assert steps[2]["type"] == "execution"
        assert steps[3]["type"] == "validation"
        
        # Check that task is mentioned in description
        assert task in steps[0]["description"]

class TestFirstPrinciplesMentalModel:
    """Test FirstPrinciplesMentalModel functionality."""
    
    @pytest.mark.asyncio
    async def test_generate_steps(self):
        """Test generating steps with first principles model."""
        model = FirstPrinciplesMentalModel()
        task = "Optimize database performance"
        context = {"database": "PostgreSQL"}
        
        steps = await model.generate_steps(task, context)
        
        assert len(steps) == 3
        assert steps[0]["type"] == "decomposition"
        assert steps[0]["name"] == "Break Down Problem"
        assert steps[1]["type"] == "analysis"
        assert steps[2]["type"] == "synthesis"
        
        # Check that task is mentioned in description
        assert task in steps[0]["description"]

class TestSystemsThinkingMentalModel:
    """Test SystemsThinkingMentalModel functionality."""
    
    @pytest.mark.asyncio
    async def test_generate_steps(self):
        """Test generating steps with systems thinking model."""
        model = SystemsThinkingMentalModel()
        task = "Improve team productivity"
        context = {"team_size": 10}
        
        steps = await model.generate_steps(task, context)
        
        assert len(steps) == 5
        assert steps[0]["type"] == "mapping"
        assert steps[0]["name"] == "Map System Components"
        assert steps[1]["type"] == "relationships"
        assert steps[2]["type"] == "leverage_points"
        assert steps[3]["type"] == "intervention"
        assert steps[4]["type"] == "feedback"
        
        # Check that task is mentioned in description
        assert task in steps[0]["description"]

class TestCriticalPathMentalModel:
    """Test CriticalPathMentalModel functionality."""
    
    @pytest.mark.asyncio
    async def test_generate_steps(self):
        """Test generating steps with critical path model."""
        model = CriticalPathMentalModel()
        task = "Launch new product"
        context = {"deadline": "3 months"}
        
        steps = await model.generate_steps(task, context)
        
        assert len(steps) == 6
        assert steps[0]["type"] == "task_breakdown"
        assert steps[0]["name"] == "Break Down Tasks"
        assert steps[1]["type"] == "dependencies"
        assert steps[2]["type"] == "estimation"
        assert steps[3]["type"] == "critical_path"
        assert steps[4]["type"] == "optimization"
        assert steps[5]["type"] == "monitoring"
        
        # Check that task is mentioned in description
        assert task in steps[0]["description"]

class TestDecisionTreeMentalModel:
    """Test DecisionTreeMentalModel functionality."""
    
    @pytest.mark.asyncio
    async def test_generate_steps(self):
        """Test generating steps with decision tree model."""
        model = DecisionTreeMentalModel()
        task = "Choose technology stack"
        context = {"project_type": "web_app"}
        
        steps = await model.generate_steps(task, context)
        
        assert len(steps) == 7
        assert steps[0]["type"] == "problem_definition"
        assert steps[0]["name"] == "Define Decision Problem"
        assert steps[1]["type"] == "alternatives"
        assert steps[2]["type"] == "criteria"
        assert steps[3]["type"] == "outcomes"
        assert steps[4]["type"] == "probabilities"
        assert steps[5]["type"] == "evaluation"
        assert steps[6]["type"] == "selection"
        
        # Check that task is mentioned in description
        assert task in steps[0]["description"]

class TestMentalModelRegistry:
    """Test mental model registry functionality."""
    
    def test_get_mental_model_default(self):
        """Test getting default mental model."""
        model = get_mental_model("default")
        assert isinstance(model, DefaultMentalModel)
        assert model.name == "default"
    
    def test_get_mental_model_first_principles(self):
        """Test getting first principles mental model."""
        model = get_mental_model("first_principles")
        assert isinstance(model, FirstPrinciplesMentalModel)
        assert model.name == "first_principles"
    
    def test_get_mental_model_systems_thinking(self):
        """Test getting systems thinking mental model."""
        model = get_mental_model("systems_thinking")
        assert isinstance(model, SystemsThinkingMentalModel)
        assert model.name == "systems_thinking"
    
    def test_get_mental_model_critical_path(self):
        """Test getting critical path mental model."""
        model = get_mental_model("critical_path")
        assert isinstance(model, CriticalPathMentalModel)
        assert model.name == "critical_path"
    
    def test_get_mental_model_decision_tree(self):
        """Test getting decision tree mental model."""
        model = get_mental_model("decision_tree")
        assert isinstance(model, DecisionTreeMentalModel)
        assert model.name == "decision_tree"
    
    def test_get_mental_model_invalid(self):
        """Test getting invalid mental model."""
        model = get_mental_model("invalid_model")
        assert model is None
    
    def test_register_mental_model(self):
        """Test registering a custom mental model."""
        from src.panda_mcp.core.planning.mental_models import MentalModel
        
        class CustomMentalModel(MentalModel):
            def __init__(self):
                super().__init__("custom", "Custom model")
            
            async def generate_steps(self, task, context):
                return [{"type": "custom", "name": "Custom Step"}]
        
        register_mental_model("custom", CustomMentalModel)
        
        model = get_mental_model("custom")
        assert isinstance(model, CustomMentalModel)
        assert model.name == "custom"

class TestMentalModelTypes:
    """Test MentalModelType enum."""
    
    def test_mental_model_types(self):
        """Test that all mental model types are defined."""
        assert MentalModelType.DEFAULT.value == "default"
        assert MentalModelType.FIRST_PRINCIPLES.value == "first_principles"
        assert MentalModelType.SYSTEMS_THINKING.value == "systems_thinking"
        assert MentalModelType.CRITICAL_PATH.value == "critical_path"
        assert MentalModelType.DECISION_TREE.value == "decision_tree"
    
    def test_all_types_have_implementations(self):
        """Test that all mental model types have implementations."""
        for model_type in MentalModelType:
            model = get_mental_model(model_type.value)
            assert model is not None
            assert model.name == model_type.value

if __name__ == "__main__":
    pytest.main([__file__]) 