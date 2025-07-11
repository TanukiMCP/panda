# PandA (Planning and Auditing) MCP Server

PandA is a Model Context Protocol (MCP) server that provides **atomic tools** to enhance LLM planning and auditing capabilities. Following MCP principles, PandA acts as a **vehicle** that the LLM **drives**, providing focused enhancement rather than replacement intelligence.

## Design Philosophy

**LLM = DRIVER, Tool = VEHICLE**

PandA follows the core MCP principle that tools should enhance LLM reasoning, not replace it with fake intelligence. Our tools are:

- **Atomic**: Single-purpose methods with clear inputs/outputs
- **Stateless**: No session management or complex state tracking  
- **Enhancement-focused**: Augment LLM capabilities rather than provide hardcoded responses
- **Pattern-based**: Use real analysis techniques like regex matching and AST parsing

## Tools

### `panda_plan` - Planning Enhancement
Enhances LLM planning with structured frameworks and progress tracking.

**Method**: `enhance_planning(thought, framework, context, step_number, previous_steps)`

**Frameworks Available**:
- `first_principles` - Break down to fundamental truths
- `systems_thinking` - Analyze interconnections and feedback loops
- `design_thinking` - Human-centered problem solving
- `critical_path` - Identify dependencies and bottlenecks
- `swot_analysis` - Strengths, weaknesses, opportunities, threats

**Example**:
```python
# LLM calls panda_plan to enhance its planning process
result = panda_plan.enhance_planning(
    thought="Need to design a user authentication system",
    framework="systems_thinking", 
    context="Web application with security requirements",
    step_number=1,
    previous_steps=[]
)
```

### `panda_audit` - Content Analysis
Provides real analysis capabilities for code, text, and other content types.

**Method**: `analyze_content(content, analysis_type, context, focus_areas)`

**Analysis Types**:
- `security` - Pattern-based security vulnerability detection
- `complexity` - AST-based complexity metrics for code
- `quality` - Content quality assessment with real metrics
- `structure` - Structural analysis and organization review

**Example**:
```python
# LLM calls panda_audit to analyze code quality
result = panda_audit.analyze_content(
    content=python_code,
    analysis_type="complexity",
    context="Python web service",
    focus_areas=["cyclomatic_complexity", "function_length"]
)
```

## Installation

```bash
pip install panda-mcp
```

## MCP Server Configuration

Add to your MCP client configuration:

```json
{
  "mcpServers": {
    "panda": {
      "command": "python",
      "args": ["-m", "panda_mcp.mcp_server"],
      "env": {}
    }
  }
}
```

## Development

### Prerequisites
- Python 3.10+
- MCP SDK

### Setup
1. Clone the repository:
```bash
git clone https://github.com/tanukimcp/panda.git
cd panda
```

2. Install dependencies:
```bash
pip install -e ".[dev]"
```

3. Run tests:
```bash
pytest
```

### Architecture

```
src/panda_mcp/
├── mcp_server.py          # MCP server registration
├── tools/
│   ├── plan.py           # Planning enhancement tool
│   └── audit.py          # Content analysis tool
└── utils/
    ├── frameworks.py     # Planning framework patterns
    └── analyzers.py      # Content analysis utilities
```

## Key Principles

1. **No Fake Intelligence**: Tools use real techniques (regex, AST parsing, metrics)
2. **Atomic Operations**: Each tool has one clear purpose
3. **Stateless Design**: No session management or complex state
4. **LLM Enhancement**: Augment rather than replace LLM reasoning
5. **Pattern-Based**: Use proven analysis patterns and frameworks

## Comparison to Sequential Thinking

PandA follows the same MCP principles as Sequential Thinking (245K+ monthly calls):
- Tools enhance LLM capabilities
- No hardcoded responses or fake intelligence  
- Atomic, focused functionality
- Stateless operation

## Contributing

Contributions welcome! Please ensure new tools follow MCP principles:
- Single atomic methods
- Real analysis techniques
- No fake intelligence or hardcoded responses
- Enhance rather than replace LLM reasoning

## License

MIT License - see [LICENSE](LICENSE) file for details.
