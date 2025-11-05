"""Generate operator for TABStack AI SDK."""

from typing import Any, Dict

from ._http_client import HTTPClient
from .schema import Schema
from .types import JsonResponse


class Generate:
    """Generate operator for AI-powered content transformation.

    This class provides async methods for generating transformed content from URLs using AI,
    allowing you to create summaries, restructure data, and enhance content based on
    custom instructions.
    """

    def __init__(self, http_client: HTTPClient) -> None:
        """Initialize Generate operator.

        Args:
            http_client: HTTP client for making API requests
        """
        self._http = http_client

    async def json(
        self, url: str, schema: Schema, instructions: str, nocache: bool = False
    ) -> JsonResponse:
        """Generate transformed JSON with AI.

        Fetches URL content, extracts data, and transforms it using AI based on custom
        instructions. Use this to generate new content, summaries, or restructured data.

        Args:
            url: URL to fetch content from
            schema: Schema object defining the structure of the transformed output
            instructions: Instructions describing how to transform the data
            nocache: Bypass cache and force fresh data retrieval

        Returns:
            JsonResponse containing the transformed data matching the schema

        Raises:
            BadRequestError: If URL, schema, or instructions are missing or invalid
            UnauthorizedError: If API key is invalid
            InvalidURLError: If URL is invalid
            ServerError: If server encounters an error

        Example:
            >>> from tabstack_ai.schema import Schema, String, Array, Object
            >>> async with TABStack(api_key="your-key") as tabs:
            ...     schema = Schema(
            ...         summaries=Array(
            ...             Object(
            ...                 title=String,
            ...                 category=String,
            ...                 summary=String,
            ...             )
            ...         )
            ...     )
            ...     result = await tabs.generate.json(
            ...         url="https://news.ycombinator.com",
            ...         schema=schema,
            ...         instructions="Categorize each story and write a one-sentence summary"
            ...     )
            ...     print(result.data["summaries"])
        """
        request_data: Dict[str, Any] = {
            "url": url,
            "json_schema": schema.to_json_schema(),
            "instructions": instructions,
        }
        if nocache:
            request_data["nocache"] = nocache

        response = await self._http.post("v1/generate/json", request_data)
        return JsonResponse.from_dict(response)
