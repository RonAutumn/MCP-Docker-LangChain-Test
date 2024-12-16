# MCP-Docker-LangChain-Test

A test project demonstrating LangChain and Docker integration with MCP agents.

## Project Structure

- `main.py`: Contains a basic LangChain implementation with a mock chain
- `Dockerfile`: Configuration for containerizing the application
- `requirements.txt`: Python package dependencies

## Setup and Usage

### Local Development

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

### Docker Usage

1. Build the Docker image:
   ```bash
   docker build -t mcp-langchain-test .
   ```

2. Run the container:
   ```bash
   docker run mcp-langchain-test
   ```

## Implementation Details

- Uses a mock LangChain implementation for testing
- Demonstrates basic chain setup and execution
- Containerized for consistent deployment