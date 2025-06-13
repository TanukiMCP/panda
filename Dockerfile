FROM python:3.10-slim

WORKDIR /app

# Copy project files
COPY pyproject.toml README.md ./
COPY src ./src
COPY tests ./tests

# Install dependencies
RUN pip install --no-cache-dir -e .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "panda_mcp.server:app", "--host", "0.0.0.0", "--port", "8000"] 