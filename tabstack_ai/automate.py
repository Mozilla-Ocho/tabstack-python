"""Automate operator for TABStack AI SDK."""
import json
from typing import Any, AsyncIterator, Dict, Optional

from ._http_client import HTTPClient
from .types import AutomateEvent


class Automate:
    """Automate operator for AI-powered web automation.

    This class provides async methods for executing complex web automation tasks using
    natural language instructions. The automation runs in a browser and streams
    real-time progress updates.
    """

    def __init__(self, http_client: HTTPClient) -> None:
        """Initialize Automate operator.

        Args:
            http_client: HTTP client for making API requests
        """
        self._http = http_client

    async def execute(
        self,
        task: str,
        url: Optional[str] = None,
        data: Optional[Dict[str, Any]] = None,
        guardrails: Optional[str] = None,
        max_iterations: int = 50,
        max_validation_attempts: int = 3,
    ) -> AsyncIterator[AutomateEvent]:
        """Execute AI-powered browser automation task with streaming updates.

        This method streams real-time progress updates as Server-Sent Events (SSE).
        Use this for web scraping, form filling, navigation, and multi-step workflows.

        Args:
            task: The task description in natural language
            url: Optional starting URL for the task
            data: Optional JSON data to provide context for form filling or complex tasks
            guardrails: Optional safety constraints for execution
            max_iterations: Maximum task iterations (1-100, default 50)
            max_validation_attempts: Maximum validation attempts (1-10, default 3)

        Yields:
            AutomateEvent objects representing different stages of task execution

        Raises:
            BadRequestError: If task is missing or parameters are invalid
            UnauthorizedError: If API key is invalid
            ServerError: If server encounters an error
            ServiceUnavailableError: If automate service is not available

        Example:
            >>> async with TABStack(api_key="your-key") as tabs:
            ...     async for event in tabs.automate.execute(
            ...         task="Find the top 3 trending repositories",
            ...         url="https://github.com/trending",
            ...         guardrails="browse and extract only"
            ...     ):
            ...         if event.type == "task:completed":
            ...             print(f"Result: {event.data.final_answer}")
            ...         elif event.type == "agent:extracted":
            ...             print(f"Extracted: {event.data.extracted_data}")
            ...         elif event.type == "error":
            ...             print(f"Error: {event.data.get('error')}")

        Event Types:
            Task Events:
                - start: Task initialization
                - task:setup: Task configuration
                - task:started: Task execution begins
                - task:completed: Task finished successfully
                - task:aborted: Task was terminated
                - task:validated: Task completion validation
                - task:validation_error: Validation failed

            Agent Events:
                - agent:processing: Agent thinking/planning
                - agent:status: Status updates and plans
                - agent:step: Processing step iterations
                - agent:action: Actions being performed
                - agent:reasoned: Agent reasoning output
                - agent:extracted: Data extraction results
                - agent:waiting: Agent waiting for operations

            Browser Events:
                - browser:navigated: Page navigation events
                - browser:action_started: Browser action initiated
                - browser:action_completed: Browser action finished
                - browser:screenshot_captured: Screenshot taken

            System Events:
                - system:debug_compression: Debug compression info
                - system:debug_message: Debug messages

            Stream Control:
                - complete: End of stream with results
                - done: Stream termination
                - error: Error occurred
        """
        request_data: Dict[str, Any] = {
            "task": task,
            "maxIterations": max_iterations,
            "maxValidationAttempts": max_validation_attempts,
        }

        if url:
            request_data["url"] = url
        if data:
            request_data["data"] = data
        if guardrails:
            request_data["guardrails"] = guardrails

        # Stream the response and parse SSE events
        current_event_type: Optional[str] = None
        current_event_data: str = ""

        async for line in self._http.post_stream("v1/automate", request_data):
            # SSE format: "event: <type>" or "data: <json>"
            if line.startswith("event:"):
                # If we have a pending event, yield it before starting a new one
                if current_event_type and current_event_data:
                    yield self._parse_event(current_event_type, current_event_data)
                    current_event_data = ""

                # Extract event type
                current_event_type = line[6:].strip()

            elif line.startswith("data:"):
                # Accumulate event data (can be multiline)
                data_line = line[5:].strip()
                if current_event_data:
                    current_event_data += "\n" + data_line
                else:
                    current_event_data = data_line

            elif line == "":
                # Empty line marks the end of an event
                if current_event_type and current_event_data:
                    yield self._parse_event(current_event_type, current_event_data)
                    current_event_type = None
                    current_event_data = ""

        # Yield any remaining event
        if current_event_type and current_event_data:
            yield self._parse_event(current_event_type, current_event_data)

    def _parse_event(self, event_type: str, event_data: str) -> AutomateEvent:
        """Parse SSE event data.

        Args:
            event_type: Type of the event
            event_data: JSON string containing event data

        Returns:
            AutomateEvent instance
        """
        try:
            data = json.loads(event_data)
        except json.JSONDecodeError:
            # If data is not valid JSON, return it as-is
            data = {"raw": event_data}

        return AutomateEvent(type=event_type, data=data)
