# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ExtractCreateJsonParams"]


class ExtractCreateJsonParams(TypedDict, total=False):
    json_schema: Required[object]
    """JSON schema definition that describes the structure of data to extract."""

    url: Required[str]
    """URL to fetch and extract data from"""

    nocache: bool
    """Bypass cache and force fresh data retrieval"""
