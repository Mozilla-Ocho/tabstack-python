"""TABStack AI Python SDK.

This SDK provides a Python interface to the TABStack AI API for web content
extraction, AI-powered content generation, and browser automation.

Example:
    >>> import os
    >>> from tabstack_ai import TABStack
    >>> from tabstack_ai.schema import Schema, String, Number, Array, Object
    >>>
    >>> # Initialize the client
    >>> tabs = TABStack(api_key=os.getenv('TABSTACK_API_KEY'))
    >>>
    >>> # Extract markdown
    >>> result = tabs.extract.markdown(url="https://example.com")
    >>> print(result.content)
    >>>
    >>> # Extract structured JSON
    >>> schema = Schema(
    ...     stories=Array(
    ...         Object(
    ...             title=String,
    ...             points=Number,
    ...             author=String,
    ...         )
    ...     )
    ... )
    >>> data = tabs.extract.json(url="https://news.ycombinator.com", schema=schema)
    >>> print(data.data)
"""

from .automate import Automate
from .client import TABStack
from .exceptions import (
    APIError,
    BadRequestError,
    InvalidURLError,
    ServerError,
    ServiceUnavailableError,
    TABStackError,
    UnauthorizedError,
)
from .extract import Extract
from .generate import Generate
from .types import (
    AutomateEvent,
    EventData,
    JsonResponse,
    SchemaResponse,
    MarkdownResponse,
    Metadata,
)

__version__ = "1.0.0"
__all__ = [
    # Main client
    "TABStack",
    # Operators
    "Extract",
    "Generate",
    "Automate",
    # Response types
    "MarkdownResponse",
    "SchemaResponse",
    "JsonResponse",
    "Metadata",
    "AutomateEvent",
    "EventData",
    # Exceptions
    "TABStackError",
    "BadRequestError",
    "UnauthorizedError",
    "InvalidURLError",
    "ServerError",
    "ServiceUnavailableError",
    "APIError",
]
