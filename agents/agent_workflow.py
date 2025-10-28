
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from langsmith import traceable

class AgentWorkflow:
    def __init__(self, llm, prompt_template):
        self.llm = llm
        self.prompt_template = prompt_template
        self.agent_executor = None
        self.langsmith_enabled = bool(os.getenv("LANGSMITH_API_KEY"))

    def create_agent(self):
        prompt = PromptTemplate(template=self.prompt_template, input_variables=["input"])
        agent = create_openai_functions_agent(self.llm, prompt)
        if self.langsmith_enabled:
            # Wrap agent with LangSmith tracing
            self.agent_executor = traceable(agent)
        else:
            self.agent_executor = agent

    def run_agent(self, input_data):
        if not self.agent_executor:
            raise Exception("Agent not created. Call create_agent() first.")
        return self.agent_executor.run(input_data)

    def set_llm(self, llm):
        self.llm = llm
        self.create_agent()  # Recreate the agent with the new LLM

    def get_agent_info(self):
        return {
            "llm": str(self.llm),
            "prompt_template": self.prompt_template,
            "langsmith_enabled": self.langsmith_enabled
        }