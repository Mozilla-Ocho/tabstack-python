"""Internal HTTP client for TABStack AI SDK."""
import http.client
import json
from typing import Any, Dict, Iterator, Optional
from urllib.parse import urlparse

from .exceptions import (
    APIError,
    BadRequestError,
    InvalidURLError,
    ServerError,
    ServiceUnavailableError,
    TABStackError,
    UnauthorizedError,
)


class HTTPClient:
    """HTTP client for making requests to TABStack API."""

    def __init__(self, api_key: str, base_url: str = "https://api.tabstack.ai/") -> None:
        """Initialize HTTP client.

        Args:
            api_key: API key for authentication
            base_url: Base URL for the API
        """
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.parsed_url = urlparse(self.base_url)

        # Determine if we should use HTTPS
        self.use_https = self.parsed_url.scheme == "https"

    def _get_connection(self) -> http.client.HTTPConnection:
        """Get HTTP or HTTPS connection.

        Returns:
            HTTP connection instance
        """
        host = self.parsed_url.netloc
        if self.use_https:
            return http.client.HTTPSConnection(host, timeout=60)
        else:
            return http.client.HTTPConnection(host, timeout=60)

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
        try:
            error_data = json.loads(body.decode("utf-8"))
            error_message = error_data.get("error", "Unknown error")
        except (json.JSONDecodeError, UnicodeDecodeError):
            error_message = body.decode("utf-8", errors="replace") if body else "Unknown error"

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

    def post(self, path: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make a POST request.

        Args:
            path: API endpoint path
            data: Request body data

        Returns:
            Response data as dictionary

        Raises:
            TABStackError: On API errors
        """
        conn = self._get_connection()
        try:
            # Prepare request body
            body = json.dumps(data) if data else "{}"
            headers = self._get_headers()

            # Make request
            full_path = f"{self.parsed_url.path}/{path.lstrip('/')}"
            conn.request("POST", full_path, body=body, headers=headers)

            # Get response
            response = conn.getresponse()
            response_body = response.read()

            # Handle errors
            if response.status >= 400:
                self._handle_error_response(response.status, response_body)

            # Parse successful response
            if response_body:
                return json.loads(response_body.decode("utf-8"))
            else:
                return {}

        finally:
            conn.close()

    def post_stream(self, path: str, data: Optional[Dict[str, Any]] = None) -> Iterator[str]:
        """Make a POST request with streaming response (Server-Sent Events).

        Args:
            path: API endpoint path
            data: Request body data

        Yields:
            Lines from the streaming response

        Raises:
            TABStackError: On API errors
        """
        conn = self._get_connection()
        try:
            # Prepare request body
            body = json.dumps(data) if data else "{}"
            headers = self._get_headers()
            headers["Accept"] = "text/event-stream"

            # Make request
            full_path = f"{self.parsed_url.path}/{path.lstrip('/')}"
            conn.request("POST", full_path, body=body, headers=headers)

            # Get response
            response = conn.getresponse()

            # Check for errors first (non-streaming error responses)
            if response.status >= 400:
                error_body = response.read()
                self._handle_error_response(response.status, error_body)

            # Stream the response
            buffer = b""
            while True:
                chunk = response.read(1024)
                if not chunk:
                    break

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

        finally:
            conn.close()
