# PandA (Planning and Auditing) MCP Server

PandA is a Model Context Protocol (MCP) server designed to enhance LLM capabilities in task planning and result auditing. It provides structured frameworks that LLMs can use to improve their planning processes and validate their outputs.

## Features

### PandA Plan (`panda_plan`)
- Sequential planning with state management
- Multiple mental model support
- Extensible planning frameworks
- Default general-purpose planning for any knowledge domain
- Session management for multi-step planning processes

### PandA Audit (`panda_audit`)
- Comprehensive auditing frameworks
- Support for multiple content types (code, text, etc.)
- Extensible auditing commands
- Default general-purpose auditing for any content type
- Session management for multi-step auditing processes

## Installation

```bash
pip install panda-mcp
```

## Quick Start

```python
from panda_mcp import PandaServer

server = PandaServer()
server.start()
```

## Development

### Prerequisites
- Python 3.10+
- FastMCP
- Docker (for deployment)

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

## Deployment

This project is configured for deployment on Smithery.ai. The deployment process is automated through GitHub Actions when pushing to the main branch.

## Documentation

For detailed documentation, please visit our [documentation site](https://docs.smithery.ai/panda).

## Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on how to submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
