"""End-to-end integration tests with mocked HTTP."""

from typing import Any

import pytest

from tabstack import Tabstack


class TestExtractTransformWorkflow:
    """Test workflow: extract → transform."""

    async def test_extract_markdown_then_transform(self, mocker: Any) -> None:
        """Test extracting markdown and then transforming it with AI."""
        # Markdown extraction response
        mock_response_1 = mocker.Mock()
        mock_response_1.status_code = 200
        mock_response_1.json.return_value = {
            "url": "https://example.com",
            "content": "# Article Title\n\nThis is a long article about technology...",
        }
        mock_response_1.content = b"{}"

        # Transform response
        mock_response_2 = mocker.Mock()
        mock_response_2.status_code = 200
        mock_response_2.json.return_value = {
            "summary": "A brief summary",
            "topics": ["technology", "innovation"],
        }
        mock_response_2.content = b"{}"

        mock_httpx_client = mocker.AsyncMock()
        mock_httpx_client.post.side_effect = [mock_response_1, mock_response_2]

        async with Tabstack(api_key="test_key") as tabs:
            tabs._http_client._client = mock_httpx_client

            # Step 1: Extract markdown (just to test the workflow)
            await tabs.extract.markdown(url="https://example.com")

            # Step 2: Transform with AI
            transform_schema = {
                "type": "object",
                "properties": {
                    "summary": {"type": "string"},
                    "topics": {"type": "array", "items": {"type": "string"}},
                },
            }
            transform_result = await tabs.generate.json(
                url="https://example.com",
                schema=transform_schema,
                instructions="Summarize and extract topics",
            )

            assert "summary" in transform_result.data
            assert len(transform_result.data["topics"]) == 2


class TestBrowserAutomationWorkflow:
    """Test workflow: automate with schema."""

    async def test_automate_with_structured_output(self, mocker: Any) -> None:
        """Test browser automation with structured data extraction."""
        mock_response = mocker.AsyncMock()
        mock_response.status_code = 200

        # Simulate SSE stream
        async def mock_aiter_bytes(chunk_size: int):  # type: ignore
            yield b'event: start\ndata: {"message": "Starting automation"}\n\n'
            yield b'event: agent:navigating\ndata: {"url": "https://example.com"}\n\n'
            yield (
                b"event: agent:extracted\n"
                b'data: {"extractedData": {"results": ["item1", "item2"]}}\n\n'
            )
            yield (
                b"event: task:completed\n"
                b'data: {"finalAnswer": "Extracted 2 items", "success": true}\n\n'
            )

        mock_response.aiter_bytes = mock_aiter_bytes

        # Create proper async context manager mock
        mock_stream_cm = mocker.MagicMock()
        mock_stream_cm.__aenter__ = mocker.AsyncMock(return_value=mock_response)
        mock_stream_cm.__aexit__ = mocker.AsyncMock(return_value=None)

        mock_httpx_client = mocker.AsyncMock()
        mock_httpx_client.stream = mocker.MagicMock(return_value=mock_stream_cm)

        async with Tabstack(api_key="test_key") as tabs:
            tabs._http_client._client = mock_httpx_client

            schema = {
                "type": "object",
                "properties": {"results": {"type": "array", "items": {"type": "string"}}},
            }

            events = []
            async for event in tabs.agent.automate(
                task="Find and extract results",
                url="https://example.com",
                schema=schema,
            ):
                events.append(event)

            # Verify we received events
            assert len(events) == 4

            # Find the extraction event
            extracted_events = [e for e in events if e.type == "agent:extracted"]
            assert len(extracted_events) == 1
            assert "results" in extracted_events[0].data.extracted_data


class TestErrorHandlingWorkflow:
    """Test error handling across workflow."""

    async def test_invalid_url_handling(self, mocker: Any) -> None:
        """Test handling of invalid URL error."""
        from tabstack.exceptions import InvalidURLError

        mock_response = mocker.Mock()
        mock_response.status_code = 422
        mock_response.content = b'{"error": "URL not found"}'

        mock_httpx_client = mocker.AsyncMock()
        mock_httpx_client.post.return_value = mock_response

        async with Tabstack(api_key="test_key") as tabs:
            tabs._http_client._client = mock_httpx_client

            with pytest.raises(InvalidURLError, match="URL not found"):
                await tabs.extract.markdown(url="https://invalid-url.example.com")

    async def test_unauthorized_handling(self, mocker: Any) -> None:
        """Test handling of unauthorized error."""
        from tabstack.exceptions import UnauthorizedError

        mock_response = mocker.Mock()
        mock_response.status_code = 401
        mock_response.content = b'{"error": "Invalid API key"}'

        mock_httpx_client = mocker.AsyncMock()
        mock_httpx_client.post.return_value = mock_response

        async with Tabstack(api_key="bad_key") as tabs:
            tabs._http_client._client = mock_httpx_client

            with pytest.raises(UnauthorizedError, match="Invalid API key"):
                await tabs.extract.markdown(url="https://example.com")

    async def test_server_error_handling(self, mocker: Any) -> None:
        """Test handling of server error."""
        from tabstack.exceptions import ServerError

        mock_response = mocker.Mock()
        mock_response.status_code = 500
        mock_response.content = b'{"error": "Internal server error"}'

        mock_httpx_client = mocker.AsyncMock()
        mock_httpx_client.post.return_value = mock_response

        async with Tabstack(api_key="test_key") as tabs:
            tabs._http_client._client = mock_httpx_client

            with pytest.raises(ServerError, match="Internal server error"):
                await tabs.extract.markdown(url="https://example.com")


class TestMultipleOperations:
    """Test multiple operations in sequence."""

    async def test_multiple_extractions(self, mocker: Any) -> None:
        """Test multiple extraction operations."""
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"url": "https://example.com", "content": "# Test"}
        mock_response.content = b"{}"

        mock_httpx_client = mocker.AsyncMock()
        mock_httpx_client.post.return_value = mock_response

        async with Tabstack(api_key="test_key") as tabs:
            tabs._http_client._client = mock_httpx_client

            # Perform multiple operations
            result1 = await tabs.extract.markdown(url="https://example1.com")
            result2 = await tabs.extract.markdown(url="https://example2.com")
            result3 = await tabs.extract.markdown(url="https://example3.com")

            assert result1.url == "https://example.com"
            assert result2.url == "https://example.com"
            assert result3.url == "https://example.com"
            assert mock_httpx_client.post.call_count == 3
