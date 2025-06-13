"""
PandA Server - Main server implementation
"""

from fastapi import FastAPI
from fastmcp import FastMCP

from ..tools import PandaPlan, PandaAudit

class PandaServer(FastMCP):
    """PandA MCP Server implementation."""
    
    def __init__(self):
        """Initialize the PandA server."""
        # Initialize FastMCP
        super().__init__()
        
        # Create tool instances
        plan_tool = PandaPlan()
        audit_tool = PandaAudit()
        
        # Register tools with metadata
        self.tool(
            name="panda_plan",
            description="Structured planning framework for LLMs with step-by-step execution. Actions: create_session, plan, advance_step, step_action, get_status"
        )(plan_tool.execute)
        
        self.tool(
            name="panda_audit",
            description="Structured auditing framework for LLMs with step-by-step execution. Actions: create_session, audit, advance_step, step_action, get_status"
        )(audit_tool.execute)
    
    def start(self, host: str = "0.0.0.0", port: int = 8000) -> None:
        """Start the PandA server."""
        # Run the MCP server with streamable-http transport and /mcp path
        self.run(transport="streamable-http", host=host, port=port, path="/mcp") 