# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tabstack import Tabstack, AsyncTabstack
from tests.utils import assert_matches_type
from tabstack.types import GenerateCreateJsonResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGenerate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_json(self, client: Tabstack) -> None:
        generate = client.generate.create_json(
            instructions="For each story, categorize it (tech/business/science/other) and write a one-sentence summary explaining what it's about in simple terms.",
            json_schema={
                "type": "object",
                "properties": {
                    "summaries": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "title": {
                                    "type": "string",
                                    "description": "Story title",
                                },
                                "category": {
                                    "type": "string",
                                    "description": "Story category (tech/business/science/etc)",
                                },
                                "summary": {
                                    "type": "string",
                                    "description": "One-sentence summary of the story",
                                },
                            },
                        },
                    }
                },
            },
            url="https://news.ycombinator.com",
        )
        assert_matches_type(GenerateCreateJsonResponse, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_json_with_all_params(self, client: Tabstack) -> None:
        generate = client.generate.create_json(
            instructions="For each story, categorize it (tech/business/science/other) and write a one-sentence summary explaining what it's about in simple terms.",
            json_schema={
                "type": "object",
                "properties": {
                    "summaries": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "title": {
                                    "type": "string",
                                    "description": "Story title",
                                },
                                "category": {
                                    "type": "string",
                                    "description": "Story category (tech/business/science/etc)",
                                },
                                "summary": {
                                    "type": "string",
                                    "description": "One-sentence summary of the story",
                                },
                            },
                        },
                    }
                },
            },
            url="https://news.ycombinator.com",
            nocache=False,
        )
        assert_matches_type(GenerateCreateJsonResponse, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_json(self, client: Tabstack) -> None:
        response = client.generate.with_raw_response.create_json(
            instructions="For each story, categorize it (tech/business/science/other) and write a one-sentence summary explaining what it's about in simple terms.",
            json_schema={
                "type": "object",
                "properties": {
                    "summaries": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "title": {
                                    "type": "string",
                                    "description": "Story title",
                                },
                                "category": {
                                    "type": "string",
                                    "description": "Story category (tech/business/science/etc)",
                                },
                                "summary": {
                                    "type": "string",
                                    "description": "One-sentence summary of the story",
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
        generate = response.parse()
        assert_matches_type(GenerateCreateJsonResponse, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_json(self, client: Tabstack) -> None:
        with client.generate.with_streaming_response.create_json(
            instructions="For each story, categorize it (tech/business/science/other) and write a one-sentence summary explaining what it's about in simple terms.",
            json_schema={
                "type": "object",
                "properties": {
                    "summaries": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "title": {
                                    "type": "string",
                                    "description": "Story title",
                                },
                                "category": {
                                    "type": "string",
                                    "description": "Story category (tech/business/science/etc)",
                                },
                                "summary": {
                                    "type": "string",
                                    "description": "One-sentence summary of the story",
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

            generate = response.parse()
            assert_matches_type(GenerateCreateJsonResponse, generate, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGenerate:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_json(self, async_client: AsyncTabstack) -> None:
        generate = await async_client.generate.create_json(
            instructions="For each story, categorize it (tech/business/science/other) and write a one-sentence summary explaining what it's about in simple terms.",
            json_schema={
                "type": "object",
                "properties": {
                    "summaries": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "title": {
                                    "type": "string",
                                    "description": "Story title",
                                },
                                "category": {
                                    "type": "string",
                                    "description": "Story category (tech/business/science/etc)",
                                },
                                "summary": {
                                    "type": "string",
                                    "description": "One-sentence summary of the story",
                                },
                            },
                        },
                    }
                },
            },
            url="https://news.ycombinator.com",
        )
        assert_matches_type(GenerateCreateJsonResponse, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_json_with_all_params(self, async_client: AsyncTabstack) -> None:
        generate = await async_client.generate.create_json(
            instructions="For each story, categorize it (tech/business/science/other) and write a one-sentence summary explaining what it's about in simple terms.",
            json_schema={
                "type": "object",
                "properties": {
                    "summaries": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "title": {
                                    "type": "string",
                                    "description": "Story title",
                                },
                                "category": {
                                    "type": "string",
                                    "description": "Story category (tech/business/science/etc)",
                                },
                                "summary": {
                                    "type": "string",
                                    "description": "One-sentence summary of the story",
                                },
                            },
                        },
                    }
                },
            },
            url="https://news.ycombinator.com",
            nocache=False,
        )
        assert_matches_type(GenerateCreateJsonResponse, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_json(self, async_client: AsyncTabstack) -> None:
        response = await async_client.generate.with_raw_response.create_json(
            instructions="For each story, categorize it (tech/business/science/other) and write a one-sentence summary explaining what it's about in simple terms.",
            json_schema={
                "type": "object",
                "properties": {
                    "summaries": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "title": {
                                    "type": "string",
                                    "description": "Story title",
                                },
                                "category": {
                                    "type": "string",
                                    "description": "Story category (tech/business/science/etc)",
                                },
                                "summary": {
                                    "type": "string",
                                    "description": "One-sentence summary of the story",
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
        generate = await response.parse()
        assert_matches_type(GenerateCreateJsonResponse, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_json(self, async_client: AsyncTabstack) -> None:
        async with async_client.generate.with_streaming_response.create_json(
            instructions="For each story, categorize it (tech/business/science/other) and write a one-sentence summary explaining what it's about in simple terms.",
            json_schema={
                "type": "object",
                "properties": {
                    "summaries": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "title": {
                                    "type": "string",
                                    "description": "Story title",
                                },
                                "category": {
                                    "type": "string",
                                    "description": "Story category (tech/business/science/etc)",
                                },
                                "summary": {
                                    "type": "string",
                                    "description": "One-sentence summary of the story",
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

            generate = await response.parse()
            assert_matches_type(GenerateCreateJsonResponse, generate, path=["response"])

        assert cast(Any, response.is_closed) is True
