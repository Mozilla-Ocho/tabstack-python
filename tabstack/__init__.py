"""TABStack AI Python SDK.

This SDK provides a Python interface to the TABStack AI API for web content
extraction, AI-powered content generation, and browser automation.

The SDK provides three main operators:

- **Extract**: Convert web content to markdown or extract structured data
- **Generate**: Transform and enhance web data using AI
- **Automate**: Execute complex browser automation tasks with natural language

The SDK supports both async (TABStack) and sync (TABStackSync) clients:

Async Example:
    >>> import asyncio
    >>> import os
    >>> from tabstack import TABStack
    >>>
    >>> async def main():
    ...     async with TABStack(api_key=os.getenv('TABSTACK_API_KEY')) as tabs:
    ...         # Extract markdown from a URL
    ...         result = await tabs.extract.markdown(url="https://example.com")
    ...         print(result.content)
    >>>
    >>> asyncio.run(main())

Sync Example:
    >>> import os
    >>> from tabstack import TABStackSync
    >>>
    >>> with TABStackSync(api_key=os.getenv('TABSTACK_API_KEY')) as tabs:
    ...     # Extract markdown from a URL (no async/await needed)
    ...     result = tabs.extract.markdown(url="https://example.com")
    ...     print(result.content)

Workflow: Extract → Transform
    >>> async def extract_and_transform():
    ...     async with TABStack(api_key=os.getenv('TABSTACK_API_KEY')) as tabs:
    ...         # Define schema for transformed output
    ...         summary_schema = {
    ...             "type": "object",
    ...             "properties": {
    ...                 "summaries": {
    ...                     "type": "array",
    ...                     "items": {
    ...                         "type": "object",
    ...                         "properties": {
    ...                             "title": {"type": "string"},
    ...                             "category": {"type": "string"},
    ...                             "summary": {"type": "string"}
    ...                         }
    ...                     }
    ...                 }
    ...             }
    ...         }
    ...
    ...         # Generate transformed content with AI
    ...         result = await tabs.generate.json(
    ...             url="https://news.ycombinator.com",
    ...             schema=summary_schema,
    ...             instructions="Categorize each story and write a brief summary"
    ...         )
    ...         print(result.data)

Workflow: Browser Automation
    >>> async def automate_task():
    ...     async with TABStack(api_key=os.getenv('TABSTACK_API_KEY')) as tabs:
    ...         # Execute complex web automation tasks
    ...         async for event in tabs.agent.automate(
    ...             task="Extract the top 5 trending repositories",
    ...             url="https://github.com/trending"
    ...         ):
    ...             if event.type == "task:completed":
    ...                 print(f"Task complete: {event.data.get('finalAnswer')}")
"""

from .agent import Agent
from .agent_sync import AgentSync
from .client import TABStack
from .client_sync import TABStackSync
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
from .extract_sync import ExtractSync
from .generate import Generate
from .generate_sync import GenerateSync
from .types import (
    AutomateEvent,
    EventData,
    JsonResponse,
    MarkdownResponse,
    Metadata,
)

__version__ = "1.0.0"
__all__ = [
    # Main clients
    "TABStack",  # Async client
    "TABStackSync",  # Sync client
    # Async operators
    "Extract",
    "Generate",
    "Agent",
    # Sync operators
    "ExtractSync",
    "GenerateSync",
    "AgentSync",
    # Response types
    "MarkdownResponse",
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
