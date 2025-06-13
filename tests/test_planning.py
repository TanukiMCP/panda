"""
Tests for PandA planning framework
"""

import pytest
from typing import Dict, Any

from panda_mcp.core.planning import (
    PlanningSession,
    SequentialPlanner,
    DefaultMentalModel,
    FirstPrinciplesMentalModel
)

@pytest.fixture
def session() -> PlanningSession:
    """Create a test planning session."""
    return PlanningSession("test_session")

@pytest.fixture
def planner() -> SequentialPlanner:
    """Create a test sequential planner."""
    return SequentialPlanner()

def test_planning_session_initialization(session: PlanningSession):
    """Test planning session initialization."""
    assert session.session_id == "test_session"
    assert session.state["steps"] == []
    assert session.state["current_step"] == 0
    assert session.state["mental_models"] == []
    assert session.state["status"] == "initialized"

def test_planning_session_step_management(session: PlanningSession):
    """Test planning session step management."""
    # Add steps
    step1 = {"name": "Step 1", "description": "First step"}
    step2 = {"name": "Step 2", "description": "Second step"}
    
    session.add_step(step1)
    session.add_step(step2)
    
    assert len(session.state["steps"]) == 2
    assert session.get_current_step() == step1
    
    # Advance step
    assert session.advance_step() is True
    assert session.get_current_step() == step2
    
    # Try to advance beyond last step
    assert session.advance_step() is False

def test_planning_session_mental_models(session: PlanningSession):
    """Test planning session mental model management."""
    session.add_mental_model("default")
    session.add_mental_model("first_principles")
    
    assert "default" in session.state["mental_models"]
    assert "first_principles" in session.state["mental_models"]
    
    # Test duplicate addition
    session.add_mental_model("default")
    assert session.state["mental_models"].count("default") == 1

@pytest.mark.asyncio
async def test_sequential_planner_execution(planner: SequentialPlanner):
    """Test sequential planner execution."""
    # Create planning session
    session_id = planner.create_session()
    
    # Execute plan
    result = await planner.plan(
        session_id,
        {
            "task": "Test task",
            "mental_models": ["default"]
        }
    )
    
    assert result["status"] == "success"
    assert result["session_id"] == session_id
    assert "current_step" in result
    assert result["total_steps"] > 0
    assert "mental_models" in result

@pytest.mark.asyncio
async def test_default_mental_model():
    """Test default mental model step generation."""
    model = DefaultMentalModel()
    steps = await model.generate_steps(
        "Test task",
        {}
    )
    
    assert len(steps) == 4  # Analysis, Planning, Execution, Validation
    assert all("type" in step for step in steps)
    assert all("name" in step for step in steps)
    assert all("description" in step for step in steps)
    assert all("expected_output" in step for step in steps)

@pytest.mark.asyncio
async def test_first_principles_mental_model():
    """Test first principles mental model step generation."""
    model = FirstPrinciplesMentalModel()
    steps = await model.generate_steps(
        "Test task",
        {}
    )
    
    assert len(steps) == 3  # Decomposition, Analysis, Synthesis
    assert all("type" in step for step in steps)
    assert all("name" in step for step in steps)
    assert all("description" in step for step in steps)
    assert all("expected_output" in step for step in steps)

@pytest.mark.asyncio
async def test_sequential_planner_validation(planner: SequentialPlanner):
    """Test sequential planner parameter validation."""
    session_id = planner.create_session()
    
    # Test with invalid parameters
    result = await planner.plan(
        session_id,
        {"task": "Test task"}  # Missing mental_models
    )
    assert result["status"] == "error"
    assert "Invalid parameters" in result["message"]
    
    # Test with invalid mental model
    result = await planner.plan(
        session_id,
        {
            "task": "Test task",
            "mental_models": ["invalid_model"]
        }
    )
    assert result["status"] == "error"
    assert "Unknown mental models" in result["message"] 