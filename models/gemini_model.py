import os

from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings

from .base_model import BaseAIModel


class GeminiModel(BaseAIModel):
    def __init__(self):
        super().__init__()

        self.api_key = os.getenv("GOOGLE_API_KEY")
        self.default_variant = "gemini-2.0-flash"

    def load(self, variant=None):
        if not self.api_key:
            raise ValueError("The environment variable GOOGLE_API_KEY is missing.")

        model_variant = variant or self.default_variant

        self.llm = ChatGoogleGenerativeAI(
            model=model_variant,
            api_key=self.api_key,
            temperature=0.7,
        )

    def get_embeddings(self):
        if self.embeddings is None:
            self.embeddings = GoogleGenerativeAIEmbeddings(
                model="models/text-embedding-004"
            )

        return self.embeddings

    def get_settings(self, variant=None):
        return {
            "dimension": 768,
        }

    def name(self):
        return "Gemini"

    def get_variants(self):
        return {
            "gemini-2.0-flash": "Gemini 2 Flash (1m context)",
        }
