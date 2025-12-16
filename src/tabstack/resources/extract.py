# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import extract_create_json_params, extract_create_markdown_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.extract_create_json_response import ExtractCreateJsonResponse
from ..types.extract_create_markdown_response import ExtractCreateMarkdownResponse

__all__ = ["ExtractResource", "AsyncExtractResource"]


class ExtractResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExtractResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tabstack-python#accessing-raw-response-data-eg-headers
        """
        return ExtractResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExtractResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tabstack-python#with_streaming_response
        """
        return ExtractResourceWithStreamingResponse(self)

    def create_json(
        self,
        *,
        json_schema: object,
        url: str,
        nocache: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractCreateJsonResponse:
        """
        Fetches a URL and extracts structured data according to a provided JSON schema

        Args:
          json_schema: JSON schema definition that describes the structure of data to extract.

          url: URL to fetch and extract data from

          nocache: Bypass cache and force fresh data retrieval

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/extract/json",
            body=maybe_transform(
                {
                    "json_schema": json_schema,
                    "url": url,
                    "nocache": nocache,
                },
                extract_create_json_params.ExtractCreateJsonParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractCreateJsonResponse,
        )

    def create_markdown(
        self,
        *,
        url: str,
        metadata: bool | Omit = omit,
        nocache: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractCreateMarkdownResponse:
        """
        Fetches a URL and converts its HTML content to clean Markdown format with
        optional metadata extraction

        Args:
          url: URL to fetch and convert to markdown

          metadata: Include extracted metadata (Open Graph and HTML metadata) as a separate field in
              the response

          nocache: Bypass cache and force fresh data retrieval

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/extract/markdown",
            body=maybe_transform(
                {
                    "url": url,
                    "metadata": metadata,
                    "nocache": nocache,
                },
                extract_create_markdown_params.ExtractCreateMarkdownParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractCreateMarkdownResponse,
        )


class AsyncExtractResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExtractResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tabstack-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExtractResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExtractResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tabstack-python#with_streaming_response
        """
        return AsyncExtractResourceWithStreamingResponse(self)

    async def create_json(
        self,
        *,
        json_schema: object,
        url: str,
        nocache: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractCreateJsonResponse:
        """
        Fetches a URL and extracts structured data according to a provided JSON schema

        Args:
          json_schema: JSON schema definition that describes the structure of data to extract.

          url: URL to fetch and extract data from

          nocache: Bypass cache and force fresh data retrieval

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/extract/json",
            body=await async_maybe_transform(
                {
                    "json_schema": json_schema,
                    "url": url,
                    "nocache": nocache,
                },
                extract_create_json_params.ExtractCreateJsonParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractCreateJsonResponse,
        )

    async def create_markdown(
        self,
        *,
        url: str,
        metadata: bool | Omit = omit,
        nocache: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractCreateMarkdownResponse:
        """
        Fetches a URL and converts its HTML content to clean Markdown format with
        optional metadata extraction

        Args:
          url: URL to fetch and convert to markdown

          metadata: Include extracted metadata (Open Graph and HTML metadata) as a separate field in
              the response

          nocache: Bypass cache and force fresh data retrieval

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/extract/markdown",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "metadata": metadata,
                    "nocache": nocache,
                },
                extract_create_markdown_params.ExtractCreateMarkdownParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractCreateMarkdownResponse,
        )


class ExtractResourceWithRawResponse:
    def __init__(self, extract: ExtractResource) -> None:
        self._extract = extract

        self.create_json = to_raw_response_wrapper(
            extract.create_json,
        )
        self.create_markdown = to_raw_response_wrapper(
            extract.create_markdown,
        )


class AsyncExtractResourceWithRawResponse:
    def __init__(self, extract: AsyncExtractResource) -> None:
        self._extract = extract

        self.create_json = async_to_raw_response_wrapper(
            extract.create_json,
        )
        self.create_markdown = async_to_raw_response_wrapper(
            extract.create_markdown,
        )


class ExtractResourceWithStreamingResponse:
    def __init__(self, extract: ExtractResource) -> None:
        self._extract = extract

        self.create_json = to_streamed_response_wrapper(
            extract.create_json,
        )
        self.create_markdown = to_streamed_response_wrapper(
            extract.create_markdown,
        )


class AsyncExtractResourceWithStreamingResponse:
    def __init__(self, extract: AsyncExtractResource) -> None:
        self._extract = extract

        self.create_json = async_to_streamed_response_wrapper(
            extract.create_json,
        )
        self.create_markdown = async_to_streamed_response_wrapper(
            extract.create_markdown,
        )
