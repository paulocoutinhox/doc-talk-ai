from models.gemini_model import GeminiModel
from models.openai_model import OpenAIModel


def load_models():
    # Add fixed models
    models = []
    models.append(OpenAIModel())
    models.append(GeminiModel())

    return models
