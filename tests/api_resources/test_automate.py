# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tabstack import Tabstack, AsyncTabstack

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAutomate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    def test_method_execute(self, client: Tabstack) -> None:
        automate_stream = client.automate.execute(
            task="Find the top 3 trending repositories and extract their names, descriptions, and star counts",
        )
        automate_stream.response.close()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    def test_method_execute_with_all_params(self, client: Tabstack) -> None:
        automate_stream = client.automate.execute(
            task="Find the top 3 trending repositories and extract their names, descriptions, and star counts",
            data={
                "language": "Python",
                "timeRange": "today",
            },
            guardrails="browse and extract only, don't interact with repositories",
            max_iterations=50,
            max_validation_attempts=3,
            url="https://github.com/trending",
        )
        automate_stream.response.close()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    def test_raw_response_execute(self, client: Tabstack) -> None:
        response = client.automate.with_raw_response.execute(
            task="Find the top 3 trending repositories and extract their names, descriptions, and star counts",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    def test_streaming_response_execute(self, client: Tabstack) -> None:
        with client.automate.with_streaming_response.execute(
            task="Find the top 3 trending repositories and extract their names, descriptions, and star counts",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True


class TestAsyncAutomate:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    async def test_method_execute(self, async_client: AsyncTabstack) -> None:
        automate_stream = await async_client.automate.execute(
            task="Find the top 3 trending repositories and extract their names, descriptions, and star counts",
        )
        await automate_stream.response.aclose()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    async def test_method_execute_with_all_params(self, async_client: AsyncTabstack) -> None:
        automate_stream = await async_client.automate.execute(
            task="Find the top 3 trending repositories and extract their names, descriptions, and star counts",
            data={
                "language": "Python",
                "timeRange": "today",
            },
            guardrails="browse and extract only, don't interact with repositories",
            max_iterations=50,
            max_validation_attempts=3,
            url="https://github.com/trending",
        )
        await automate_stream.response.aclose()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    async def test_raw_response_execute(self, async_client: AsyncTabstack) -> None:
        response = await async_client.automate.with_raw_response.execute(
            task="Find the top 3 trending repositories and extract their names, descriptions, and star counts",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    async def test_streaming_response_execute(self, async_client: AsyncTabstack) -> None:
        async with async_client.automate.with_streaming_response.execute(
            task="Find the top 3 trending repositories and extract their names, descriptions, and star counts",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True
