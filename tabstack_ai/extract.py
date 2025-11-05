"""Extract operator for TABStack AI SDK."""

from typing import Any, Dict, Optional

from ._http_client import HTTPClient
from .schema import Schema
from .types import JsonResponse, MarkdownResponse, SchemaResponse


class Extract:
    """Extract operator for converting and extracting web content.

    This class provides async methods for extracting content from URLs in various formats:
    - Markdown conversion
    - Schema generation
    - Structured JSON extraction
    """

    def __init__(self, http_client: HTTPClient) -> None:
        """Initialize Extract operator.

        Args:
            http_client: HTTP client for making API requests
        """
        self._http = http_client

    async def markdown(
        self, url: str, metadata: bool = False, nocache: bool = False
    ) -> MarkdownResponse:
        """Convert URL content to Markdown format.

        Fetches a URL and converts its HTML content to clean Markdown format with
        optional metadata extraction.

        Args:
            url: URL to fetch and convert to markdown
            metadata: Include extracted metadata as a separate field in the response.
                     If False, metadata is included as YAML frontmatter in the content.
            nocache: Bypass cache and force fresh data retrieval

        Returns:
            MarkdownResponse containing the converted content and optional metadata

        Raises:
            BadRequestError: If URL is missing or invalid
            UnauthorizedError: If API key is invalid
            InvalidURLError: If URL is invalid or inaccessible
            ServerError: If server encounters an error

        Example:
            >>> async with TABStack(api_key="your-key") as tabs:
            ...     result = await tabs.extract.markdown(
            ...         url="https://example.com/blog/article",
            ...         metadata=True
            ...     )
            ...     print(result.content)
            ...     print(result.metadata.title)
        """
        request_data: Dict[str, Any] = {"url": url}
        if metadata:
            request_data["metadata"] = metadata
        if nocache:
            request_data["nocache"] = nocache

        response = await self._http.post("v1/extract/markdown", request_data)
        return MarkdownResponse.from_dict(response)

    async def schema(
        self, url: str, instructions: Optional[str] = None, nocache: bool = False
    ) -> SchemaResponse:
        """Generate schema from URL content.

        Analyzes URL content and generates a schema that describes the structure
        of the data. Use this to create schemas for the json() method.

        Args:
            url: URL to analyze and extract schema from
            instructions: Optional instructions to guide schema generation (max 1000 chars)
            nocache: Bypass cache and force fresh data retrieval

        Returns:
            SchemaResponse containing the generated Schema object

        Raises:
            BadRequestError: If URL is missing or instructions are invalid
            UnauthorizedError: If API key is invalid
            InvalidURLError: If URL is invalid
            ServerError: If server encounters an error

        Example:
            >>> async with TABStack(api_key="your-key") as tabs:
            ...     result = await tabs.extract.schema(
            ...         url="https://news.ycombinator.com",
            ...         instructions="extract top stories with title, points, and author"
            ...     )
            ...     # result.schema is a Schema object
            ...     data = await tabs.extract.json(
            ...         url="https://news.ycombinator.com",
            ...         schema=result.schema
            ...     )
        """
        request_data: Dict[str, Any] = {"url": url}
        if instructions:
            request_data["instructions"] = instructions
        if nocache:
            request_data["nocache"] = nocache

        response = await self._http.post("v1/extract/json/schema", request_data)
        return SchemaResponse.from_dict(response)

    async def json(self, url: str, schema: Schema, nocache: bool = False) -> JsonResponse:
        """Extract structured JSON from URL content.

        Fetches a URL and extracts structured data according to the provided JSON schema.

        Args:
            url: URL to fetch and extract data from
            schema: Schema object defining the structure of data to extract
            nocache: Bypass cache and force fresh data retrieval

        Returns:
            JsonResponse containing the extracted data matching the schema

        Raises:
            BadRequestError: If URL or schema is missing or invalid
            UnauthorizedError: If API key is invalid
            InvalidURLError: If URL is invalid
            ServerError: If server encounters an error

        Example:
            >>> from tabstack_ai.schema import Schema, String, Number, Array, Object
            >>> async with TABStack(api_key="your-key") as tabs:
            ...     schema = Schema(
            ...         stories=Array(
            ...             Object(
            ...                 title=String,
            ...                 points=Number,
            ...                 author=String,
            ...             )
            ...         )
            ...     )
            ...     result = await tabs.extract.json(
            ...         url="https://news.ycombinator.com",
            ...         schema=schema
            ...     )
            ...     print(result.data["stories"])
        """
        request_data: Dict[str, Any] = {
            "url": url,
            "json_schema": schema.to_json_schema(),
        }
        if nocache:
            request_data["nocache"] = nocache

        response = await self._http.post("v1/extract/json", request_data)
        return JsonResponse.from_dict(response)
