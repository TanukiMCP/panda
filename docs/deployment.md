# PandA Deployment Guide

This guide explains how to deploy the PandA MCP server to Smithery.ai.

## Prerequisites

1. GitHub account with access to the repository
2. Smithery.ai account and API key
3. Docker installed locally (for testing)

## Configuration Files

### smithery.yaml

The `smithery.yaml` file in the root directory contains the Smithery.ai deployment configuration:

```yaml
name: panda-mcp
version: 0.1.0
deployment:
  type: docker
  image: ghcr.io/tanukimcp/panda:latest
  port: 8000
  healthcheck:
    path: /health
    interval: 30s
    timeout: 10s
    retries: 3
```

### Dockerfile

The `Dockerfile` defines how the application is containerized:

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY pyproject.toml README.md ./
COPY src ./src
COPY tests ./tests
RUN pip install --no-cache-dir -e .
EXPOSE 8000
CMD ["uvicorn", "panda_mcp.server:app", "--host", "0.0.0.0", "--port", "8000"]
```

## CI/CD Pipeline

The project uses GitHub Actions for continuous integration and deployment:

1. On every push and pull request:
   - Run tests
   - Type checking
   - Linting

2. On push to main:
   - Build Docker image
   - Push to GitHub Container Registry
   - Deploy to Smithery.ai

## Setting Up Deployment

1. Add GitHub Secrets:
   ```bash
   SMITHERY_API_KEY=your-api-key
   ```

2. Enable GitHub Container Registry:
   - Go to repository settings
   - Enable "Improved container support"
   - Enable "Read and write permissions" for Actions

3. Configure Smithery.ai:
   - Create a new project
   - Connect to GitHub repository
   - Add deployment environment variables

## Manual Deployment

If needed, you can deploy manually:

1. Build locally:
   ```bash
   docker build -t ghcr.io/tanukimcp/panda:latest .
   ```

2. Test locally:
   ```bash
   docker run -p 8000:8000 ghcr.io/tanukimcp/panda:latest
   ```

3. Push to registry:
   ```bash
   docker push ghcr.io/tanukimcp/panda:latest
   ```

4. Deploy to Smithery.ai:
   ```bash
   smithery deploy --config smithery.yaml
   ```

## Monitoring

- Health check endpoint: `/health`
- Metrics endpoint: `/metrics`
- Logs available in Smithery.ai dashboard

## Troubleshooting

1. Check container logs:
   ```bash
   docker logs <container-id>
   ```

2. Verify health check:
   ```bash
   curl http://localhost:8000/health
   ```

3. Common issues:
   - Port conflicts: Change port in `smithery.yaml`
   - Memory limits: Adjust in `smithery.yaml`
   - API key issues: Verify in Smithery.ai dashboard

## Security

- API keys stored as secrets
- CORS configured for Smithery.ai domains
- Container runs as non-root user
- Regular security updates via dependabot 