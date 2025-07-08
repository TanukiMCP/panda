"""
Sequential Executor for PandA MCP

This module provides a SequentialExecutor class that can run a series of
planning and auditing steps.
"""

from typing import Any, Dict, List, Optional

class SequentialExecutor:
    """
    Manages the execution of a sequence of steps defined by an LLM.

    Each step in the sequence is a dictionary that specifies a tool to use
    (`panda_plan` or `panda_audit`) and the parameters to pass to it.
    The executor maintains a shared context across all steps.
    """

    def __init__(
        self,
        steps: List[Dict[str, Any]],
        plan_tool: Any,
        audit_tool: Any,
        initial_context: Optional[Dict[str, Any]] = None
    ):
        """
        Initializes the SequentialExecutor.

        Args:
            steps: A list of steps to execute.
            plan_tool: An instance of the PandaPlan tool.
            audit_tool: An instance of the PandaAudit tool.
            initial_context: An optional dictionary for the initial context.
        """
        self.steps = steps
        self.plan_tool = plan_tool
        self.audit_tool = audit_tool
        self.context = initial_context or {}
        self._initialize_steps()

    def _initialize_steps(self):
        """Initialize the status of each step."""
        for step in self.steps:
            step["status"] = "pending"
            step["result"] = None

    async def run(self) -> Dict[str, Any]:
        """
        Executes the entire sequence of steps.

        Returns:
            A dictionary containing the final context and the results of all steps.
        """
        for i in range(len(self.steps)):
            await self._execute_step(i)
        
        return {
            "final_context": self.context,
            "steps": self.steps
        }

    async def _execute_step(self, step_index: int):
        """
        Executes a single step in the sequence.

        Args:
            step_index: The index of the step to execute.
        """
        if step_index >= len(self.steps):
            return

        step = self.steps[step_index]
        step["status"] = "in_progress"

        try:
            tool_name = step.get("tool")
            parameters = step.get("parameters", {})

            # Inject context into parameters
            parameters["context"] = self.context

            if tool_name == "panda_plan":
                result = await self.plan_tool.enhance_planning(**parameters)
            elif tool_name == "panda_audit":
                result = await self.audit_tool.analyze_content(**parameters)
            else:
                raise ValueError(f"Unknown tool: {tool_name}")

            step["result"] = result
            step["status"] = "completed"

            # Update context with the result of the step
            self.context[f"step_{step_index+1}_result"] = result

        except Exception as e:
            step["status"] = "failed"
            step["result"] = {"error": str(e)} 