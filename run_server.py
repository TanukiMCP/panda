import sys
import os

# Add src to the path so we can import modules
sys.path.append(os.path.abspath("src"))

try:
    from panda_mcp import PandaServer
    
    print("Starting PandA MCP Server...")
    server = PandaServer()
    server.start(host="127.0.0.1", port=8000)
except Exception as e:
    print(f"Error starting server: {e}")
    import traceback
    traceback.print_exc() 