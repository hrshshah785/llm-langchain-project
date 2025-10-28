import os
from models.llm_interface import LLMInterface
from agents.agent_workflow import AgentWorkflow
from evaluation.eval_tools import SimpleEvaluator  # <-- Add this import

def load_config():
    # Load configuration from environment variables
    return {
        'api_key': os.getenv('OPENAI_API_KEY', 'your-openai-api-key'),  # Set your key here or via env
        'model_name': os.getenv('MODEL_NAME', 'gpt-3.5-turbo'),
        'temperature': float(os.getenv('MODEL_TEMPERATURE', 0.7)),
    }

def main():
    # Load config
    config = load_config()

    # Initialize LLM
    llm_interface = LLMInterface(
        api_key=config['api_key'],
        model_name=config['model_name'],
        temperature=config['temperature']
    )
    llm_interface.initialize()

    # Define prompt template
    prompt_template = "You are a helpful assistant. Answer the following: {input}"

    # Initialize Agent Workflow
    agent_workflow = AgentWorkflow(llm=llm_interface.llm, prompt_template=prompt_template)
    agent_workflow.create_agent()

    # Run agent
    user_input = "What is LangChain?"
    result = agent_workflow.run_agent(user_input)
    print("Agent response:", result)

    # --- Evaluation step ---
    reference_answers = {
        "What is LangChain?": "LangChain is a framework for developing applications powered by language models."
    }
    evaluator = SimpleEvaluator(reference_answers)
    evaluation_result = evaluator.evaluate(user_input, result)
    print("Evaluation:", evaluation_result)

if __name__ == "__main__":
    main()