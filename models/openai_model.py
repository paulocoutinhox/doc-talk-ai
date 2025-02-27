import os

from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from .base_model import BaseAIModel


class OpenAIModel(BaseAIModel):
    def __init__(self):
        super().__init__()

        self.api_key = os.getenv("OPENAI_API_KEY")
        self.default_variant = "gpt-4o-mini"

    def load(self, variant=None):
        if not self.api_key:
            raise ValueError("The environment variable OPENAI_API_KEY is missing.")

        model_variant = variant or self.default_variant

        self.llm = ChatOpenAI(
            model=model_variant, api_key=self.api_key, temperature=0.7
        )

    def get_embeddings(self):
        if self.embeddings is None:
            self.embeddings = OpenAIEmbeddings(api_key=self.api_key)

        return self.embeddings

    def get_settings(self, variant=None):
        return {
            "dimension": 1536,
        }

    def name(self):
        return "OpenAI"

    def get_variants(self):
        return {
            "gpt-4o": "GPT-4o (128k context)",
            "chatgpt-4o-latest": "ChatGPT-4o (128k context)",
            "gpt-4o-mini": "GPT-4o Mini (128k context)",
            "gpt-4-turbo": "GPT-4 Turbo (128k context)",
            "gpt-4": "GPT-4 (8k context)",
        }
