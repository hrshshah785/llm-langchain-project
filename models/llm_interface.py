from langchain.llms import OpenAI

class LLMInterface:
    def __init__(self, api_key: str, model_name: str = "gpt-3.5-turbo", temperature: float = 0.7):
        self.api_key = api_key
        self.model_name = model_name
        self.temperature = temperature
        self.llm = None

    def initialize(self):
        self.llm = OpenAI(
            openai_api_key=self.api_key,
            model_name=self.model_name,
            temperature=self.temperature
        )

    def generate(self, prompt: str) -> str:
        if not self.llm:
            raise Exception("LLM not initialized. Call initialize() first.")
        return self.llm(prompt)

    def get_info(self):
        return {
            "model_name": self.model_name,
            "temperature": self.temperature
        }