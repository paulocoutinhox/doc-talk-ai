from abc import ABC, abstractmethod


class BaseAIModel(ABC):
    """
    Abstract base class for AI models.

    This class defines the standard interface for all AI models used in the application.
    Subclasses must implement the `load`, `run`, `name`, and `get_embeddings` methods.
    """

    def __init__(self):
        """
        Initializes the base model attributes.

        Attributes:
            default_variant (str): The default model variant to be used if none is specified.
            llm (object): The loaded AI model instance.
            embeddings (object): The embedding model instance for text vectorization.
        """
        self.default_variant = None
        self.llm = None
        self.embeddings = None

    @abstractmethod
    def load(self, variant=None):
        """
        Load the AI model with the specified variant.

        This method must be implemented in each subclass to properly initialize the AI model.

        Args:
            variant (str, optional): The model variant to load. Defaults to None.

        Raises:
            Exception: If the model cannot be loaded due to missing dependencies
                       or invalid configurations.
        """
        pass

    @abstractmethod
    def name(self):
        """
        Get the display name of the AI model.

        Returns:
            str: A user-friendly name of the AI model, e.g., "OpenAI GPT-4".
        """
        pass

    @abstractmethod
    def get_embeddings(self):
        """
        Get the embeddings model used for vectorizing text.

        This method must be implemented in each subclass to provide the correct embedding model.

        Returns:
            object: The embedding model instance used for text processing.
        """
        pass

    @abstractmethod
    def get_settings(self, variant=None):
        """
        Get model-specific settings, including embedding dimensions.

        Args:
            variant (str, optional): The model variant to use. Defaults to None.

        Returns:
            dict: A dictionary containing settings such as:
                - "dimension" (int): The expected embedding size.
        """
        pass

    def get_variants(self):
        """
        Retrieve the available variants of the model.

        This method should be overridden by subclasses that support multiple variants.

        Returns:
            dict or None: A dictionary where:
                - Key (str): Internal model identifier used in API calls.
                - Value (str): User-friendly name for display in the UI.

            If no variants are available, returns None.
        """
        return None

    def get_default_variant(self):
        """
        Retrieve the default variant for the model.

        Returns:
            str: The internal identifier of the default variant.
        """
        return self.default_variant

    def get_model(self, variant=None):
        """
        Retrieve the loaded AI model instance.

        Ensures the model is loaded before returning it.

        Args:
            variant (str, optional): The model variant to use. Defaults to None.

        Returns:
            object: The AI model instance.
        """
        if self.llm is None:
            self.load(variant)
        return self.llm
