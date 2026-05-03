# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Iterable, cast
from typing_extensions import Literal

import httpx

from ..types import agent_automate_params, agent_research_params, agent_automate_input_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import is_given, path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._constants import DEFAULT_TIMEOUT
from .._streaming import Stream, AsyncStream
from .._base_client import make_request_options
from ..types.automate_event import AutomateEvent
from ..types.research_event import ResearchEvent
from ..types.agent_automate_input_response import AgentAutomateInputResponse

__all__ = ["AgentResource", "AsyncAgentResource"]


class AgentResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AgentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Mozilla-Ocho/tabstack-python#accessing-raw-response-data-eg-headers
        """
        return AgentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Mozilla-Ocho/tabstack-python#with_streaming_response
        """
        return AgentResourceWithStreamingResponse(self)

    def automate(
        self,
        *,
        task: str,
        data: object | Omit = omit,
        geo_target: agent_automate_params.GeoTarget | Omit = omit,
        guardrails: str | Omit = omit,
        interactive: bool | Omit = omit,
        max_iterations: int | Omit = omit,
        max_validation_attempts: int | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[AutomateEvent]:
        """
        Execute AI-powered browser automation tasks using natural language with optional
        geotargeting. This endpoint **always streams** responses using Server-Sent
        Events (SSE).

        **Streaming Response:**

        - All responses are streamed using Server-Sent Events (`text/event-stream`)
        - Real-time progress updates and results as they're generated

        **Geotargeting:**

        - Optionally specify a country code for geotargeted browsing

        **Use Cases:**

        - Web scraping and data extraction
        - Form filling and interaction
        - Navigation and information gathering
        - Multi-step web workflows
        - Content analysis from web pages

        Args:
          task: The task description in natural language

          data: JSON data to provide context for form filling or complex tasks

          geo_target: Optional geotargeting parameters for proxy requests

          guardrails: Safety constraints for execution

          interactive: Enable interactive mode to allow human-in-the-loop input during task execution

          max_iterations: Maximum task iterations

          max_validation_attempts: Maximum validation attempts

          url: Starting URL for the task

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not is_given(timeout) and self._client.timeout == DEFAULT_TIMEOUT:
            timeout = 600
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/automate",
            body=maybe_transform(
                {
                    "task": task,
                    "data": data,
                    "geo_target": geo_target,
                    "guardrails": guardrails,
                    "interactive": interactive,
                    "max_iterations": max_iterations,
                    "max_validation_attempts": max_validation_attempts,
                    "url": url,
                },
                agent_automate_params.AgentAutomateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                synthesize_event_and_data=True,
            ),
            cast_to=cast(Any, AutomateEvent),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=Stream[AutomateEvent],
        )

    def automate_input(
        self,
        request_id: str,
        *,
        cancelled: bool | Omit = omit,
        fields: Iterable[agent_automate_input_params.Field] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentAutomateInputResponse:
        """
        Submit a response to an interactive form data request from an in-progress
        automation task. When the AI agent encounters a form requiring user data, it
        emits an `interactive:form_data:request` or `interactive:form_data:error` SSE
        event containing a `requestId`. Use this endpoint to provide the requested data
        or cancel the request.

        **Lifecycle:**

        - Input requests expire after 2 minutes by default
        - Expired or already-answered requests return `410 Gone`
        - Successful submissions return `202 Accepted` (fire-and-forget from caller's
          perspective)

        Args:
          cancelled: Set to true to cancel/decline the request

          fields: Field values as array of {ref, value} pairs (required when not cancelled)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return self._post(
            path_template("/automate/{request_id}/input", request_id=request_id),
            body=maybe_transform(
                {
                    "cancelled": cancelled,
                    "fields": fields,
                },
                agent_automate_input_params.AgentAutomateInputParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentAutomateInputResponse,
        )

    def research(
        self,
        *,
        query: str,
        fetch_timeout: int | Omit = omit,
        mode: Literal["fast", "balanced"] | Omit = omit,
        nocache: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[ResearchEvent]:
        """
        Execute AI-powered research queries that search the web, analyze sources, and
        synthesize comprehensive answers. This endpoint **always streams** responses
        using Server-Sent Events (SSE).

        **Streaming Response:**

        - All responses are streamed using Server-Sent Events (`text/event-stream`)
        - Real-time progress updates as research progresses through phases

        **Research Modes:**

        - `fast` - Quick answers with minimal web searches (default)
        - `balanced` - Standard research with multiple iterations

        **Use Cases:**

        - Answering complex questions with cited sources
        - Synthesizing information from multiple web sources
        - Research reports on specific topics
        - Fact-checking and verification tasks

        Args:
          query: The research query or question to answer. Maximum 10,000 characters.

          fetch_timeout: Timeout in seconds for fetching web pages

          mode: Research mode: fast (quick answers, default), balanced (standard research)

          nocache: Skip cache and force fresh research

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not is_given(timeout) and self._client.timeout == DEFAULT_TIMEOUT:
            timeout = 600
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/research",
            body=maybe_transform(
                {
                    "query": query,
                    "fetch_timeout": fetch_timeout,
                    "mode": mode,
                    "nocache": nocache,
                },
                agent_research_params.AgentResearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                synthesize_event_and_data=True,
            ),
            cast_to=cast(Any, ResearchEvent),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=Stream[ResearchEvent],
        )


class AsyncAgentResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAgentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Mozilla-Ocho/tabstack-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Mozilla-Ocho/tabstack-python#with_streaming_response
        """
        return AsyncAgentResourceWithStreamingResponse(self)

    async def automate(
        self,
        *,
        task: str,
        data: object | Omit = omit,
        geo_target: agent_automate_params.GeoTarget | Omit = omit,
        guardrails: str | Omit = omit,
        interactive: bool | Omit = omit,
        max_iterations: int | Omit = omit,
        max_validation_attempts: int | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[AutomateEvent]:
        """
        Execute AI-powered browser automation tasks using natural language with optional
        geotargeting. This endpoint **always streams** responses using Server-Sent
        Events (SSE).

        **Streaming Response:**

        - All responses are streamed using Server-Sent Events (`text/event-stream`)
        - Real-time progress updates and results as they're generated

        **Geotargeting:**

        - Optionally specify a country code for geotargeted browsing

        **Use Cases:**

        - Web scraping and data extraction
        - Form filling and interaction
        - Navigation and information gathering
        - Multi-step web workflows
        - Content analysis from web pages

        Args:
          task: The task description in natural language

          data: JSON data to provide context for form filling or complex tasks

          geo_target: Optional geotargeting parameters for proxy requests

          guardrails: Safety constraints for execution

          interactive: Enable interactive mode to allow human-in-the-loop input during task execution

          max_iterations: Maximum task iterations

          max_validation_attempts: Maximum validation attempts

          url: Starting URL for the task

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not is_given(timeout) and self._client.timeout == DEFAULT_TIMEOUT:
            timeout = 600
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/automate",
            body=await async_maybe_transform(
                {
                    "task": task,
                    "data": data,
                    "geo_target": geo_target,
                    "guardrails": guardrails,
                    "interactive": interactive,
                    "max_iterations": max_iterations,
                    "max_validation_attempts": max_validation_attempts,
                    "url": url,
                },
                agent_automate_params.AgentAutomateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                synthesize_event_and_data=True,
            ),
            cast_to=cast(Any, AutomateEvent),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=AsyncStream[AutomateEvent],
        )

    async def automate_input(
        self,
        request_id: str,
        *,
        cancelled: bool | Omit = omit,
        fields: Iterable[agent_automate_input_params.Field] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentAutomateInputResponse:
        """
        Submit a response to an interactive form data request from an in-progress
        automation task. When the AI agent encounters a form requiring user data, it
        emits an `interactive:form_data:request` or `interactive:form_data:error` SSE
        event containing a `requestId`. Use this endpoint to provide the requested data
        or cancel the request.

        **Lifecycle:**

        - Input requests expire after 2 minutes by default
        - Expired or already-answered requests return `410 Gone`
        - Successful submissions return `202 Accepted` (fire-and-forget from caller's
          perspective)

        Args:
          cancelled: Set to true to cancel/decline the request

          fields: Field values as array of {ref, value} pairs (required when not cancelled)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return await self._post(
            path_template("/automate/{request_id}/input", request_id=request_id),
            body=await async_maybe_transform(
                {
                    "cancelled": cancelled,
                    "fields": fields,
                },
                agent_automate_input_params.AgentAutomateInputParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentAutomateInputResponse,
        )

    async def research(
        self,
        *,
        query: str,
        fetch_timeout: int | Omit = omit,
        mode: Literal["fast", "balanced"] | Omit = omit,
        nocache: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[ResearchEvent]:
        """
        Execute AI-powered research queries that search the web, analyze sources, and
        synthesize comprehensive answers. This endpoint **always streams** responses
        using Server-Sent Events (SSE).

        **Streaming Response:**

        - All responses are streamed using Server-Sent Events (`text/event-stream`)
        - Real-time progress updates as research progresses through phases

        **Research Modes:**

        - `fast` - Quick answers with minimal web searches (default)
        - `balanced` - Standard research with multiple iterations

        **Use Cases:**

        - Answering complex questions with cited sources
        - Synthesizing information from multiple web sources
        - Research reports on specific topics
        - Fact-checking and verification tasks

        Args:
          query: The research query or question to answer. Maximum 10,000 characters.

          fetch_timeout: Timeout in seconds for fetching web pages

          mode: Research mode: fast (quick answers, default), balanced (standard research)

          nocache: Skip cache and force fresh research

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not is_given(timeout) and self._client.timeout == DEFAULT_TIMEOUT:
            timeout = 600
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/research",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "fetch_timeout": fetch_timeout,
                    "mode": mode,
                    "nocache": nocache,
                },
                agent_research_params.AgentResearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                synthesize_event_and_data=True,
            ),
            cast_to=cast(Any, ResearchEvent),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=AsyncStream[ResearchEvent],
        )


class AgentResourceWithRawResponse:
    def __init__(self, agent: AgentResource) -> None:
        self._agent = agent

        self.automate = to_raw_response_wrapper(
            agent.automate,
        )
        self.automate_input = to_raw_response_wrapper(
            agent.automate_input,
        )
        self.research = to_raw_response_wrapper(
            agent.research,
        )


class AsyncAgentResourceWithRawResponse:
    def __init__(self, agent: AsyncAgentResource) -> None:
        self._agent = agent

        self.automate = async_to_raw_response_wrapper(
            agent.automate,
        )
        self.automate_input = async_to_raw_response_wrapper(
            agent.automate_input,
        )
        self.research = async_to_raw_response_wrapper(
            agent.research,
        )


class AgentResourceWithStreamingResponse:
    def __init__(self, agent: AgentResource) -> None:
        self._agent = agent

        self.automate = to_streamed_response_wrapper(
            agent.automate,
        )
        self.automate_input = to_streamed_response_wrapper(
            agent.automate_input,
        )
        self.research = to_streamed_response_wrapper(
            agent.research,
        )


class AsyncAgentResourceWithStreamingResponse:
    def __init__(self, agent: AsyncAgentResource) -> None:
        self._agent = agent

        self.automate = async_to_streamed_response_wrapper(
            agent.automate,
        )
        self.automate_input = async_to_streamed_response_wrapper(
            agent.automate_input,
        )
        self.research = async_to_streamed_response_wrapper(
            agent.research,
        )
