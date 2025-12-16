# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tabstack import Tabstack, AsyncTabstack
from tests.utils import assert_matches_type
from tabstack.types import (
    ExtractCreateJsonResponse,
    ExtractCreateMarkdownResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExtract:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_json(self, client: Tabstack) -> None:
        extract = client.extract.create_json(
            json_schema={
                "type": "object",
                "properties": {
                    "stories": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "title": {
                                    "type": "string",
                                    "description": "Story title",
                                },
                                "points": {
                                    "type": "number",
                                    "description": "Story points",
                                },
                                "author": {
                                    "type": "string",
                                    "description": "Author username",
                                },
                            },
                        },
                    }
                },
            },
            url="https://news.ycombinator.com",
        )
        assert_matches_type(ExtractCreateJsonResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_json_with_all_params(self, client: Tabstack) -> None:
        extract = client.extract.create_json(
            json_schema={
                "type": "object",
                "properties": {
                    "stories": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "title": {
                                    "type": "string",
                                    "description": "Story title",
                                },
                                "points": {
                                    "type": "number",
                                    "description": "Story points",
                                },
                                "author": {
                                    "type": "string",
                                    "description": "Author username",
                                },
                            },
                        },
                    }
                },
            },
            url="https://news.ycombinator.com",
            nocache=False,
        )
        assert_matches_type(ExtractCreateJsonResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_json(self, client: Tabstack) -> None:
        response = client.extract.with_raw_response.create_json(
            json_schema={
                "type": "object",
                "properties": {
                    "stories": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "title": {
                                    "type": "string",
                                    "description": "Story title",
                                },
                                "points": {
                                    "type": "number",
                                    "description": "Story points",
                                },
                                "author": {
                                    "type": "string",
                                    "description": "Author username",
                                },
                            },
                        },
                    }
                },
            },
            url="https://news.ycombinator.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = response.parse()
        assert_matches_type(ExtractCreateJsonResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_json(self, client: Tabstack) -> None:
        with client.extract.with_streaming_response.create_json(
            json_schema={
                "type": "object",
                "properties": {
                    "stories": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "title": {
                                    "type": "string",
                                    "description": "Story title",
                                },
                                "points": {
                                    "type": "number",
                                    "description": "Story points",
                                },
                                "author": {
                                    "type": "string",
                                    "description": "Author username",
                                },
                            },
                        },
                    }
                },
            },
            url="https://news.ycombinator.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = response.parse()
            assert_matches_type(ExtractCreateJsonResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_markdown(self, client: Tabstack) -> None:
        extract = client.extract.create_markdown(
            url="https://example.com/blog/article",
        )
        assert_matches_type(ExtractCreateMarkdownResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_markdown_with_all_params(self, client: Tabstack) -> None:
        extract = client.extract.create_markdown(
            url="https://example.com/blog/article",
            metadata=True,
            nocache=False,
        )
        assert_matches_type(ExtractCreateMarkdownResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_markdown(self, client: Tabstack) -> None:
        response = client.extract.with_raw_response.create_markdown(
            url="https://example.com/blog/article",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = response.parse()
        assert_matches_type(ExtractCreateMarkdownResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_markdown(self, client: Tabstack) -> None:
        with client.extract.with_streaming_response.create_markdown(
            url="https://example.com/blog/article",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = response.parse()
            assert_matches_type(ExtractCreateMarkdownResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExtract:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_json(self, async_client: AsyncTabstack) -> None:
        extract = await async_client.extract.create_json(
            json_schema={
                "type": "object",
                "properties": {
                    "stories": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "title": {
                                    "type": "string",
                                    "description": "Story title",
                                },
                                "points": {
                                    "type": "number",
                                    "description": "Story points",
                                },
                                "author": {
                                    "type": "string",
                                    "description": "Author username",
                                },
                            },
                        },
                    }
                },
            },
            url="https://news.ycombinator.com",
        )
        assert_matches_type(ExtractCreateJsonResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_json_with_all_params(self, async_client: AsyncTabstack) -> None:
        extract = await async_client.extract.create_json(
            json_schema={
                "type": "object",
                "properties": {
                    "stories": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "title": {
                                    "type": "string",
                                    "description": "Story title",
                                },
                                "points": {
                                    "type": "number",
                                    "description": "Story points",
                                },
                                "author": {
                                    "type": "string",
                                    "description": "Author username",
                                },
                            },
                        },
                    }
                },
            },
            url="https://news.ycombinator.com",
            nocache=False,
        )
        assert_matches_type(ExtractCreateJsonResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_json(self, async_client: AsyncTabstack) -> None:
        response = await async_client.extract.with_raw_response.create_json(
            json_schema={
                "type": "object",
                "properties": {
                    "stories": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "title": {
                                    "type": "string",
                                    "description": "Story title",
                                },
                                "points": {
                                    "type": "number",
                                    "description": "Story points",
                                },
                                "author": {
                                    "type": "string",
                                    "description": "Author username",
                                },
                            },
                        },
                    }
                },
            },
            url="https://news.ycombinator.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = await response.parse()
        assert_matches_type(ExtractCreateJsonResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_json(self, async_client: AsyncTabstack) -> None:
        async with async_client.extract.with_streaming_response.create_json(
            json_schema={
                "type": "object",
                "properties": {
                    "stories": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "title": {
                                    "type": "string",
                                    "description": "Story title",
                                },
                                "points": {
                                    "type": "number",
                                    "description": "Story points",
                                },
                                "author": {
                                    "type": "string",
                                    "description": "Author username",
                                },
                            },
                        },
                    }
                },
            },
            url="https://news.ycombinator.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = await response.parse()
            assert_matches_type(ExtractCreateJsonResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_markdown(self, async_client: AsyncTabstack) -> None:
        extract = await async_client.extract.create_markdown(
            url="https://example.com/blog/article",
        )
        assert_matches_type(ExtractCreateMarkdownResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_markdown_with_all_params(self, async_client: AsyncTabstack) -> None:
        extract = await async_client.extract.create_markdown(
            url="https://example.com/blog/article",
            metadata=True,
            nocache=False,
        )
        assert_matches_type(ExtractCreateMarkdownResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_markdown(self, async_client: AsyncTabstack) -> None:
        response = await async_client.extract.with_raw_response.create_markdown(
            url="https://example.com/blog/article",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = await response.parse()
        assert_matches_type(ExtractCreateMarkdownResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_markdown(self, async_client: AsyncTabstack) -> None:
        async with async_client.extract.with_streaming_response.create_markdown(
            url="https://example.com/blog/article",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = await response.parse()
            assert_matches_type(ExtractCreateMarkdownResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True
