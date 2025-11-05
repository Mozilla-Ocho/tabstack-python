"""Main client for TABStack AI SDK."""
from typing import Optional

from ._http_client import HTTPClient
from .automate import Automate
from .extract import Extract
from .generate import Generate


class TABStack:
    """TABStack AI client for web content extraction, generation, and automation.

    This is the main entry point for the TABStack AI SDK. Initialize it with your
    API key to access the extract, generate, and automate operators.

    Example:
        >>> import os
        >>> from tabstack_ai import TABStack
        >>> tabs = TABStack(api_key=os.getenv('TABSTACK_API_KEY'))
        >>> result = tabs.extract.markdown(url="https://example.com")
        >>> print(result.content)
    """

    def __init__(self, api_key: str, base_url: str = "https://api.tabstack.ai/") -> None:
        """Initialize TABStack client.

        Args:
            api_key: Your TABStack API key for authentication
            base_url: Base URL for the TABStack API (default: https://api.tabstack.ai/)

        Raises:
            ValueError: If api_key is empty or None

        Example:
            >>> tabs = TABStack(api_key="your-api-key-here")
        """
        if not api_key:
            raise ValueError("api_key is required")

        self._http_client = HTTPClient(api_key=api_key, base_url=base_url)

        # Initialize operators
        self.extract = Extract(self._http_client)
        self.generate = Generate(self._http_client)
        self.automate = Automate(self._http_client)

    def __repr__(self) -> str:
        """String representation of the client."""
        return f"TABStack(base_url='{self._http_client.base_url}')"
