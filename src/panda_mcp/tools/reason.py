"""
PandA Reason - Sequential Reasoning Tool for LLMs
"""
from typing import Any, Dict, List, Optional
from ..core.sequencer.sequential import SequentialExecutor
from .plan import PandaPlan
from .audit import PandaAudit

async def panda_reason(
    steps: List[Dict[str, Any]],
    context: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Provides a sequential reasoning capability for an LLM.

    This tool takes a list of planning and auditing steps, executes them
    in sequence, and returns the results. It allows an LLM to chain
    multiple thoughts and analyses together to solve complex problems.

    Args:
        steps: A list of dictionaries, where each dictionary defines a
               step with a 'tool' ('panda_plan' or 'panda_audit') and
               'parameters' for that tool.
        context: An optional dictionary representing the initial context
                 to be shared across all steps.

    Returns:
        A dictionary containing the final context and the results of
        each step in the sequence.
    """
    try:
        plan_tool = PandaPlan()
        audit_tool = PandaAudit()
        
        executor = SequentialExecutor(
            steps=steps,
            plan_tool=plan_tool,
            audit_tool=audit_tool,
            initial_context=context
        )
        
        result = await executor.run()
        
        return {
            "status": "success",
            "result": result
        }

    except Exception as e:
        return {
            "status": "error",
            "message": f"Sequential reasoning failed: {str(e)}"
        } 