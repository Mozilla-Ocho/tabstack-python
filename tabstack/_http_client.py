"""Internal HTTP client for TABStack AI SDK."""

import json
from typing import Any, AsyncIterator, Dict, Optional

import httpx

from .exceptions import (
    APIError,
    BadRequestError,
    InvalidURLError,
    ServerError,
    ServiceUnavailableError,
    UnauthorizedError,
)


class HTTPClient:
    """Internal async HTTP client for TABStack API requests.

    Handles HTTP communication with the TABStack API, including:
    - Connection pooling and keepalive for performance
    - Request authentication with API keys
    - Error response parsing and exception mapping
    - Server-Sent Events (SSE) streaming for automate endpoint

    This is an internal class. Users should use the TABStack client instead.
    """

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.tabstack.ai/",
        max_connections: int = 100,
        max_keepalive_connections: int = 20,
        keepalive_expiry: float = 30.0,
        timeout: float = 60.0,
    ) -> None:
        """Initialize async HTTP client with connection pooling.

        Args:
            api_key: API key for authentication
            base_url: Base URL for the API
            max_connections: Maximum number of connections in the pool
            max_keepalive_connections: Maximum number of idle connections to keep alive
            keepalive_expiry: Time in seconds to keep idle connections alive
            timeout: Default timeout for requests in seconds
        """
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

        # Configure connection pooling limits
        limits = httpx.Limits(
            max_connections=max_connections,
            max_keepalive_connections=max_keepalive_connections,
            keepalive_expiry=keepalive_expiry,
        )

        # Create async client with connection pooling
        self._client: Optional[httpx.AsyncClient] = None
        self._limits = limits
        self._timeout = timeout

    async def _get_client(self) -> httpx.AsyncClient:
        """Get or create the async HTTP client.

        Returns:
            Configured async HTTP client
        """
        if self._client is None:
            self._client = httpx.AsyncClient(
                base_url=self.base_url,
                limits=self._limits,
                timeout=self._timeout,
            )
        return self._client

    async def close(self) -> None:
        """Close the HTTP client and release connections."""
        if self._client is not None:
            await self._client.aclose()
            self._client = None

    async def __aenter__(self) -> "HTTPClient":
        """Async context manager entry."""
        return self

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Async context manager exit."""
        await self.close()

    def _get_headers(self, content_type: str = "application/json") -> Dict[str, str]:
        """Get default headers for requests.

        Args:
            content_type: Content type for the request

        Returns:
            Dictionary of headers
        """
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": content_type,
            "Accept": "application/json",
            "User-Agent": "tabstack-ai-python/1.0.0",
        }

    def _handle_error_response(self, status: int, body: bytes) -> None:
        """Handle error responses and raise appropriate exceptions.

        Args:
            status: HTTP status code
            body: Response body

        Raises:
            TABStackError: Appropriate exception based on status code
        """
        # Try to parse JSON error response, fall back to raw text if not JSON
        try:
            error_data = json.loads(body.decode("utf-8"))
            error_message = error_data.get("error", "Unknown error")
        except (json.JSONDecodeError, UnicodeDecodeError):
            error_message = body.decode("utf-8", errors="replace") if body else "Unknown error"

        # Map HTTP status codes to specific exception types
        if status == 400:
            raise BadRequestError(error_message)
        elif status == 401:
            raise UnauthorizedError(error_message)
        elif status == 422:
            raise InvalidURLError(error_message)
        elif status == 500:
            raise ServerError(error_message)
        elif status == 503:
            raise ServiceUnavailableError(error_message)
        else:
            raise APIError(error_message, status)

    async def post(self, path: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make an async POST request.

        Args:
            path: API endpoint path
            data: Request body data

        Returns:
            Response data as dictionary

        Raises:
            TABStackError: On API errors
        """
        client = await self._get_client()
        headers = self._get_headers()

        # Make the request
        response = await client.post(
            path,
            json=data,
            headers=headers,
        )

        # Handle errors
        if response.status_code >= 400:
            self._handle_error_response(response.status_code, response.content)

        # Parse successful response
        if response.content:
            return response.json()
        else:
            return {}

    async def post_stream(
        self, path: str, data: Optional[Dict[str, Any]] = None
    ) -> AsyncIterator[str]:
        """Make an async POST request with streaming response (Server-Sent Events).

        Args:
            path: API endpoint path
            data: Request body data

        Yields:
            Lines from the streaming response

        Raises:
            TABStackError: On API errors
        """
        client = await self._get_client()
        headers = self._get_headers()
        headers["Accept"] = "text/event-stream"

        # Make streaming request
        async with client.stream("POST", path, json=data, headers=headers) as response:
            # Check for errors first
            if response.status_code >= 400:
                error_body = await response.aread()
                self._handle_error_response(response.status_code, error_body)

            # SSE streams are line-based; buffer bytes until we have complete lines
            buffer = b""
            async for chunk in response.aiter_bytes(chunk_size=1024):
                buffer += chunk
                # Process complete lines
                while b"\n" in buffer:
                    line_bytes, buffer = buffer.split(b"\n", 1)
                    line = line_bytes.decode("utf-8", errors="replace").rstrip("\r")
                    if line:  # Skip empty lines
                        yield line

            # Process any remaining data
            if buffer:
                line = buffer.decode("utf-8", errors="replace").rstrip("\r\n")
                if line:
                    yield line
