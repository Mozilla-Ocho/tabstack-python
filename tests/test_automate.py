"""Tests for Automate operator."""

import json
from typing import Any

import pytest

from tabstack.automate import Automate
from tabstack.types import AutomateEvent


class TestAutomateExecute:
    """Tests for automate execution."""

    async def test_execute_streaming(self, mocker: Any, mock_automate_events: list[str]) -> None:
        """Test automate execute with streaming events."""
        mock_http = mocker.AsyncMock()

        # Mock the streaming response
        async def mock_stream():  # type: ignore
            for event_line in mock_automate_events:
                yield event_line

        mock_http.post_stream.return_value = mock_stream()

        automate = Automate(mock_http)
        events = []
        async for event in automate.execute(task="Extract data", url="https://example.com"):
            events.append(event)

        # Should have received all events
        assert len(events) == 4
        assert all(isinstance(e, AutomateEvent) for e in events)

        # Check event types
        assert events[0].type == "start"
        assert events[1].type == "agent:navigating"
        assert events[2].type == "agent:extracted"
        assert events[3].type == "task:completed"

        # Verify API was called correctly
        mock_http.post_stream.assert_called_once_with(
            "/api/automate",
            data={
                "task": "Extract data",
                "url": "https://example.com",
                "schema": None,
            },
        )

    async def test_execute_with_schema(self, mocker: Any, json_schema: dict[str, Any]) -> None:
        """Test automate execute with JSON schema."""
        mock_http = mocker.AsyncMock()

        async def mock_stream():  # type: ignore
            yield 'event: task:completed\ndata: {"finalAnswer": "Done", "success": true}'

        mock_http.post_stream.return_value = mock_stream()

        automate = Automate(mock_http)
        events = []
        async for event in automate.execute(
            task="Extract data", url="https://example.com", schema=json_schema
        ):
            events.append(event)

        # Verify schema was passed
        call_args = mock_http.post_stream.call_args
        assert call_args[1]["data"]["schema"] == json_schema

    async def test_execute_validates_schema(self, mocker: Any) -> None:
        """Test automate validates schema before sending."""
        mock_http = mocker.AsyncMock()
        automate = Automate(mock_http)

        # Invalid schema should raise ValueError
        invalid_schema = {"missing": "type"}
        with pytest.raises(ValueError, match="Schema must have a 'type' field"):
            async for _ in automate.execute(
                task="Test", url="https://example.com", schema=invalid_schema
            ):
                pass

    async def test_execute_parses_event_data(self, mocker: Any) -> None:
        """Test automate correctly parses event data."""
        mock_http = mocker.AsyncMock()

        async def mock_stream():  # type: ignore
            yield (
                "event: agent:extracted\n"
                'data: {"extractedData": {"title": "Test Title", "count": 42}}'
            )

        mock_http.post_stream.return_value = mock_stream()

        automate = Automate(mock_http)
        events = []
        async for event in automate.execute(task="Test", url="https://example.com"):
            events.append(event)

        assert len(events) == 1
        event = events[0]
        assert event.type == "agent:extracted"
        # Access via snake_case (converted from camelCase)
        assert event.data.extracted_data["title"] == "Test Title"
        assert event.data.extracted_data["count"] == 42

    async def test_execute_handles_malformed_sse(self, mocker: Any) -> None:
        """Test automate handles malformed SSE gracefully."""
        mock_http = mocker.AsyncMock()

        async def mock_stream():  # type: ignore
            yield "event: start"  # Missing data line
            yield "data: not-json"  # Invalid JSON
            yield 'event: valid\ndata: {"message": "ok"}'  # Valid event

        mock_http.post_stream.return_value = mock_stream()

        automate = Automate(mock_http)
        events = []
        async for event in automate.execute(task="Test", url="https://example.com"):
            events.append(event)

        # Should have at least parsed the valid event
        # (implementation may vary on how it handles malformed events)
        assert len(events) >= 1

    async def test_execute_with_empty_task(self, mocker: Any) -> None:
        """Test automate with empty task string."""
        mock_http = mocker.AsyncMock()

        async def mock_stream():  # type: ignore
            yield 'event: task:completed\ndata: {"finalAnswer": "Done"}'

        mock_http.post_stream.return_value = mock_stream()

        automate = Automate(mock_http)
        events = []
        async for event in automate.execute(task="", url="https://example.com"):
            events.append(event)

        # Should still call API (API will validate)
        mock_http.post_stream.assert_called_once()

    async def test_execute_event_types(self, mocker: Any) -> None:
        """Test various event types are parsed correctly."""
        mock_http = mocker.AsyncMock()

        async def mock_stream():  # type: ignore
            # Various event types from the API
            yield 'event: start\ndata: {"message": "Starting"}'
            yield 'event: agent:navigating\ndata: {"url": "https://test.com"}'
            yield 'event: agent:thinking\ndata: {"thought": "Analyzing page"}'
            yield 'event: agent:extracted\ndata: {"extractedData": {}}'
            yield 'event: agent:action\ndata: {"action": "click", "selector": "button"}'
            yield 'event: task:completed\ndata: {"finalAnswer": "Done", "success": true}'

        mock_http.post_stream.return_value = mock_stream()

        automate = Automate(mock_http)
        events = []
        async for event in automate.execute(task="Test", url="https://example.com"):
            events.append(event)

        assert len(events) == 6
        event_types = [e.type for e in events]
        assert "start" in event_types
        assert "agent:navigating" in event_types
        assert "agent:thinking" in event_types
        assert "agent:extracted" in event_types
        assert "agent:action" in event_types
        assert "task:completed" in event_types
