# langchain-genai-app

## Overview
The `langchain-genai-app` is a production-grade application designed for building and deploying Generative AI solutions using the LangChain ecosystem. This project integrates large language models, dynamic agent workflows, evaluation tools, and deployment capabilities to create a robust framework for AI applications.

## Project Structure
```
langchain-genai-app
├── src
│   ├── main.py                # Entry point for the application
│   ├── agents
│   │   └── agent_workflow.py  # Dynamic agent workflow management
│   ├── models
│   │   └── llm.py             # Large language model implementations
│   ├── evaluation
│   │   └── eval_tools.py      # Evaluation tools for performance assessment
│   ├── deployment
│   │   └── deploy.py          # Deployment management using LangServe
│   └── utils
│       └── helpers.py         # Utility functions and helpers
├── requirements.txt            # Project dependencies
├── README.md                   # Project documentation
└── .gitignore                  # Files to ignore in version control

# LangChain GenAI App

## Overview
This project is a production-grade Generative AI application using the LangChain ecosystem. It orchestrates large language models with modular agent workflows, robust evaluation, and API deployment.

## Features
- Modular agent workflow (LangChain, LangGraph)
- LLM interface abstraction
- Evaluation tools (SimpleEvaluator, LangSmith-ready)
- API deployment with LangServe
- System resilience, traceability, and scalability

## Setup
1. Clone the repository.
2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    pip install langserve
    ```
3. Set your OpenAI API key:
    - Option 1: Set environment variable `OPENAI_API_KEY`
    - Option 2: Edit `src/main.py` and `src/deployment/deploy.py` to include your key

## Running Locally
- Run the main workflow:
   ```sh
   python src/main.py
   ```
- Deploy the API:
   ```sh
   python src/deployment/deploy.py
   ```
- Test the API:
   ```powershell
   Invoke-WebRequest -Uri "http://localhost:8080/run" -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"input": "What is LangChain?"}'
   ```

## API Endpoint
- `POST /run`
   - Request body: `{ "input": "<your question>" }`
   - Response: `{ "output": "<agent response>" }`

## Customization
- Edit `src/models/llm_interface.py` to use other LLM providers
- Update `src/agents/agent_workflow.py` for custom agent logic
- Add more evaluation logic in `src/evaluation/eval_tools.py`

## Security & Monitoring
- Add authentication to API endpoints for production
- Integrate LangSmith for observability and tracing

## License
MIT
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd langchain-genai-app
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the application, execute the following command:
```
python src/main.py
```

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.