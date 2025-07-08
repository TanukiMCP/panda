"""
PandA MCP Server - Production-ready FastMCP implementation with streamable HTTP transport.

This server provides two main tools:
- panda_plan: Enhanced planning with mental models and frameworks
- panda_audit: Content analysis with security, quality, and consistency checks

The server follows MCP principles where LLM = DRIVER, Tool = VEHICLE.
"""

import logging
import os
from typing import Any, Dict, List, Optional

from fastmcp import FastMCP
from .tools.plan import PandaPlan
from .tools.audit import PandaAudit

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastMCP server
mcp = FastMCP(
    name="PandA MCP Server"
)

# Initialize tool instances
plan_tool = PandaPlan()
audit_tool = PandaAudit()

@mcp.tool
async def panda_plan(
    thought: str,
    framework: Optional[str] = None,
    context: Optional[Dict[str, Any]] = None,
    step_number: Optional[int] = None,
    previous_steps: Optional[List[Dict[str, Any]]] = None
) -> Dict[str, Any]:
    """
    Enhanced planning tool that provides structured frameworks and sequential reasoning capabilities.
    
    Supports multiple mental models including first principles, systems thinking, design thinking,
    critical path analysis, and SWOT analysis.
    
    Args:
        thought: The planning thought or question to enhance
        framework: Optional framework to apply (first_principles, systems_thinking, design_thinking, critical_path, swot_analysis)
        context: Optional context about the planning task
        step_number: Optional current step number in a sequence
        previous_steps: Optional list of previous planning steps
        
    Returns:
        Enhanced planning analysis with framework guidance and structure
    """
    try:
        logger.info(f"panda_plan called with thought: {thought[:100]}..." if len(thought) > 100 else f"panda_plan called with thought: {thought}")
        
        # Call the existing planning tool
        result = await plan_tool.enhance_planning(
            thought=thought,
            framework=framework,
            context=context,
            step_number=step_number,
            previous_steps=previous_steps or []
        )
        
        # FastMCP automatically handles JSON serialization
        return result
        
    except Exception as e:
        logger.error(f"Error in panda_plan: {str(e)}", exc_info=True)
        return {
            "status": "error",
            "message": f"Planning enhancement failed: {str(e)}",
            "tool": "panda_plan"
        }

@mcp.tool
async def panda_audit(
    audit_objective: str,
    framework: Optional[str] = None,
    context: Optional[Dict[str, Any]] = None,
    phase: Optional[str] = None,
    evidence_collected: Optional[List[Dict[str, Any]]] = None
) -> Dict[str, Any]:
    """
    Cognitive audit framework tool that provides systematic investigation guidance
    through professional auditing methodologies.
    
    Supports multiple cognitive audit frameworks including security, compliance, quality,
    process, financial, and IT audits with systematic investigation guidance.
    
    Args:
        audit_objective: The audit objective or investigation question
        framework: Optional specific framework (security_audit, compliance_audit, quality_audit, process_audit, financial_audit, it_audit)
        context: Optional audit context (scope, timeline, stakeholders, etc.)
        phase: Optional current audit phase (planning, information_gathering, testing_and_evaluation, analysis_and_reporting)
        evidence_collected: Optional list of evidence collected in previous phases
        
    Returns:
        Cognitive audit framework guidance with investigation questions and methodology
    """
    try:
        logger.info(f"panda_audit called with objective: {audit_objective[:100]}..." if len(audit_objective) > 100 else f"panda_audit called with objective: {audit_objective}")
        
        # Call the new cognitive audit tool
        result = await audit_tool.enhance_audit(
            audit_objective=audit_objective,
            framework=framework,
            context=context,
            phase=phase,
            evidence_collected=evidence_collected or []
        )
        
        # FastMCP automatically handles JSON serialization
        return result
        
    except Exception as e:
        logger.error(f"Error in panda_audit: {str(e)}", exc_info=True)
        return {
            "status": "error",
            "message": f"Cognitive audit framework failed: {str(e)}",
            "tool": "panda_audit"
        }



def get_server() -> FastMCP:
    """Get the FastMCP server instance."""
    return mcp

def main():
    """Main entry point for the server."""
    # Get configuration from environment
    transport = os.getenv("MCP_TRANSPORT", "http").lower()
    host = os.getenv("MCP_HOST", "0.0.0.0")
    port = int(os.getenv("MCP_PORT", "8090"))
    log_level = os.getenv("MCP_LOG_LEVEL", "INFO")
    
    # Configure logging level
    logging.getLogger().setLevel(getattr(logging, log_level.upper()))
    
    logger.info(f"Starting PandA MCP Server with {transport} transport on {host}:{port}")
    
    if transport == "stdio":
        # For stdio transport (used by Claude Desktop, etc.)
        mcp.run(transport="stdio")
    else:
                 # For HTTP transport (streamable HTTP)
         mcp.run(
             transport="streamable-http",
             host=host,
             port=port
         )

if __name__ == "__main__":
    main() 