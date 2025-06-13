"""
Tests for PandA task execution engine
"""

import pytest
from datetime import datetime
from src.panda_mcp.core.planning.execution import (
    TaskExecutionEngine,
    ExecutionStep,
    StepStatus
)

class TestExecutionStep:
    """Test ExecutionStep functionality."""
    
    def test_step_creation(self):
        """Test creating an execution step."""
        step = ExecutionStep(
            step_id="test_step_1",
            name="Test Step",
            description="A test step",
            step_type="action",
            expected_output="Test output"
        )
        
        assert step.step_id == "test_step_1"
        assert step.name == "Test Step"
        assert step.description == "A test step"
        assert step.step_type == "action"
        assert step.expected_output == "Test output"
        assert step.status == StepStatus.PENDING
        assert step.result is None
        assert step.error is None
    
    def test_step_start(self):
        """Test starting a step."""
        step = ExecutionStep("test_step", "Test", "Description")
        step.start()
        
        assert step.status == StepStatus.IN_PROGRESS
        assert step.started_at is not None
        assert len(step.execution_log) == 1
        assert step.execution_log[0]["event_type"] == "step_started"
    
    def test_step_complete(self):
        """Test completing a step."""
        step = ExecutionStep("test_step", "Test", "Description")
        step.start()
        
        result = {"output": "test result"}
        step.complete(result)
        
        assert step.status == StepStatus.COMPLETED
        assert step.result == result
        assert step.completed_at is not None
        assert len(step.execution_log) == 2
        assert step.execution_log[1]["event_type"] == "step_completed"
    
    def test_step_fail(self):
        """Test failing a step."""
        step = ExecutionStep("test_step", "Test", "Description")
        step.start()
        
        error = "Test error"
        step.fail(error)
        
        assert step.status == StepStatus.FAILED
        assert step.error == error
        assert step.completed_at is not None
        assert len(step.execution_log) == 2
        assert step.execution_log[1]["event_type"] == "step_failed"
    
    def test_step_skip(self):
        """Test skipping a step."""
        step = ExecutionStep("test_step", "Test", "Description")
        
        reason = "Test skip reason"
        step.skip(reason)
        
        assert step.status == StepStatus.SKIPPED
        assert step.error == reason
        assert step.completed_at is not None
        assert len(step.execution_log) == 1
        assert step.execution_log[0]["event_type"] == "step_skipped"
    
    def test_step_to_dict(self):
        """Test converting step to dictionary."""
        step = ExecutionStep(
            step_id="test_step",
            name="Test Step",
            description="Description",
            metadata={"key": "value"}
        )
        step.start()
        
        step_dict = step.to_dict()
        
        assert step_dict["step_id"] == "test_step"
        assert step_dict["name"] == "Test Step"
        assert step_dict["description"] == "Description"
        assert step_dict["status"] == "in_progress"
        assert step_dict["metadata"] == {"key": "value"}
        assert step_dict["started_at"] is not None

class TestTaskExecutionEngine:
    """Test TaskExecutionEngine functionality."""
    
    def test_engine_creation(self):
        """Test creating an execution engine."""
        engine = TaskExecutionEngine("test_session")
        
        assert engine.session_id == "test_session"
        assert len(engine.steps) == 0
        assert len(engine.step_order) == 0
        assert engine.current_step_index == 0
        assert not engine.execution_started
        assert not engine.execution_completed
    
    def test_add_step(self):
        """Test adding a step to the engine."""
        engine = TaskExecutionEngine("test_session")
        step = ExecutionStep("step1", "Step 1", "First step")
        
        engine.add_step(step)
        
        assert len(engine.steps) == 1
        assert len(engine.step_order) == 1
        assert engine.steps["step1"] == step
        assert engine.step_order[0] == "step1"
    
    def test_add_multiple_steps(self):
        """Test adding multiple steps."""
        engine = TaskExecutionEngine("test_session")
        steps = [
            ExecutionStep("step1", "Step 1", "First step"),
            ExecutionStep("step2", "Step 2", "Second step"),
            ExecutionStep("step3", "Step 3", "Third step")
        ]
        
        engine.add_steps(steps)
        
        assert len(engine.steps) == 3
        assert len(engine.step_order) == 3
        assert engine.step_order == ["step1", "step2", "step3"]
    
    def test_get_current_step(self):
        """Test getting the current step."""
        engine = TaskExecutionEngine("test_session")
        step1 = ExecutionStep("step1", "Step 1", "First step")
        step2 = ExecutionStep("step2", "Step 2", "Second step")
        
        engine.add_steps([step1, step2])
        
        current = engine.get_current_step()
        assert current == step1
        
        engine.advance_step()
        current = engine.get_current_step()
        assert current == step2
    
    def test_start_execution(self):
        """Test starting execution."""
        engine = TaskExecutionEngine("test_session")
        step = ExecutionStep("step1", "Step 1", "First step")
        engine.add_step(step)
        
        result = engine.start_execution()
        
        assert result["status"] == "started"
        assert engine.execution_started
        assert step.status == StepStatus.IN_PROGRESS
        assert result["current_step"]["step_id"] == "step1"
        assert result["total_steps"] == 1
    
    def test_start_execution_no_steps(self):
        """Test starting execution with no steps."""
        engine = TaskExecutionEngine("test_session")
        
        result = engine.start_execution()
        
        assert result["status"] == "error"
        assert result["message"] == "No steps to execute"
    
    def test_complete_current_step(self):
        """Test completing the current step."""
        engine = TaskExecutionEngine("test_session")
        step1 = ExecutionStep("step1", "Step 1", "First step")
        step2 = ExecutionStep("step2", "Step 2", "Second step")
        engine.add_steps([step1, step2])
        
        engine.start_execution()
        
        result = engine.complete_current_step({"output": "step1 result"})
        
        assert result["status"] == "step_completed"
        assert step1.status == StepStatus.COMPLETED
        assert step1.result == {"output": "step1 result"}
        assert step2.status == StepStatus.IN_PROGRESS
        assert result["next_step"]["step_id"] == "step2"
    
    def test_complete_final_step(self):
        """Test completing the final step."""
        engine = TaskExecutionEngine("test_session")
        step = ExecutionStep("step1", "Step 1", "Only step")
        engine.add_step(step)
        
        engine.start_execution()
        
        result = engine.complete_current_step({"output": "final result"})
        
        assert result["status"] == "execution_completed"
        assert engine.execution_completed
        assert step.status == StepStatus.COMPLETED
        assert "summary" in result
    
    def test_fail_current_step(self):
        """Test failing the current step."""
        engine = TaskExecutionEngine("test_session")
        step = ExecutionStep("step1", "Step 1", "First step")
        engine.add_step(step)
        
        engine.start_execution()
        
        result = engine.fail_current_step("Test error")
        
        assert result["status"] == "step_failed"
        assert step.status == StepStatus.FAILED
        assert step.error == "Test error"
        assert result["can_retry"]
        assert result["can_skip"]
    
    def test_skip_current_step(self):
        """Test skipping the current step."""
        engine = TaskExecutionEngine("test_session")
        step1 = ExecutionStep("step1", "Step 1", "First step")
        step2 = ExecutionStep("step2", "Step 2", "Second step")
        engine.add_steps([step1, step2])
        
        engine.start_execution()
        
        result = engine.skip_current_step("Skip reason")
        
        assert result["status"] == "step_skipped"
        assert step1.status == StepStatus.SKIPPED
        assert step1.error == "Skip reason"
        assert step2.status == StepStatus.IN_PROGRESS
        assert result["next_step"]["step_id"] == "step2"
    
    def test_retry_current_step(self):
        """Test retrying a failed step."""
        engine = TaskExecutionEngine("test_session")
        step = ExecutionStep("step1", "Step 1", "First step")
        engine.add_step(step)
        
        engine.start_execution()
        engine.fail_current_step("Test error")
        
        result = engine.retry_current_step()
        
        assert result["status"] == "step_retrying"
        assert step.status == StepStatus.IN_PROGRESS
        assert step.error is None
        assert step.result is None
    
    def test_get_execution_status(self):
        """Test getting execution status."""
        engine = TaskExecutionEngine("test_session")
        steps = [
            ExecutionStep("step1", "Step 1", "First step"),
            ExecutionStep("step2", "Step 2", "Second step")
        ]
        engine.add_steps(steps)
        
        status = engine.get_execution_status()
        
        assert status["session_id"] == "test_session"
        assert not status["execution_started"]
        assert not status["execution_completed"]
        assert status["total_steps"] == 2
        assert status["current_step_index"] == 0
        assert status["progress_percentage"] == 0
        
        engine.start_execution()
        status = engine.get_execution_status()
        
        assert status["execution_started"]
        assert status["current_step"]["step_id"] == "step1"
    
    def test_get_execution_summary(self):
        """Test getting execution summary."""
        engine = TaskExecutionEngine("test_session")
        step1 = ExecutionStep("step1", "Step 1", "First step")
        step2 = ExecutionStep("step2", "Step 2", "Second step")
        engine.add_steps([step1, step2])
        
        engine.start_execution()
        engine.complete_current_step({"output": "result1"})
        engine.complete_current_step({"output": "result2"})
        
        summary = engine.get_execution_summary()
        
        assert summary["session_id"] == "test_session"
        assert summary["total_steps"] == 2
        assert summary["execution_completed"]
        assert summary["status_counts"]["completed"] == 2
        assert len(summary["steps"]) == 2
        assert summary["steps"][0]["name"] == "Step 1"
        assert summary["steps"][0]["status"] == "completed"

if __name__ == "__main__":
    pytest.main([__file__]) 