#!/usr/bin/env python3
"""
PandA MCP Server Runner

Starts the PandA FastMCP server with streamable HTTP transport on port 8090.
"""

import sys
import os
import logging

# Add src to the path so we can import modules
sys.path.append(os.path.abspath("src"))

def main():
    """Main entry point for starting the PandA MCP server."""
    try:
        # Import the FastMCP server
        from panda_mcp.mcp_server import main as server_main
        
        # Set environment variables for configuration
        os.environ.setdefault("MCP_TRANSPORT", "streamable-http")
        os.environ.setdefault("MCP_HOST", "0.0.0.0")
        os.environ.setdefault("MCP_PORT", "8090")
        os.environ.setdefault("MCP_LOG_LEVEL", "INFO")
        
        print("=" * 60)
        print("🐼 PandA MCP Server - Production Ready")
        print("=" * 60)
        print(f"🚀 Starting server on {os.environ['MCP_HOST']}:{os.environ['MCP_PORT']}")
        print(f"🌐 Transport: {os.environ['MCP_TRANSPORT']}")
        print(f"📊 Log Level: {os.environ['MCP_LOG_LEVEL']}")
        print("=" * 60)
        print()
        print("Available tools:")
        print("  • panda_plan  - Enhanced planning with mental models")
        print("  • panda_audit - Content analysis and security auditing")
        print()
        print("Press Ctrl+C to stop the server")
        print("=" * 60)
        
        # Start the FastMCP server
        server_main()
        
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("💡 Make sure FastMCP is installed: pip install fastmcp")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        print("\n🔍 Debug information:")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main() 