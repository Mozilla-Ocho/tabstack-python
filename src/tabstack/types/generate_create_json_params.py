# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["GenerateCreateJsonParams"]


class GenerateCreateJsonParams(TypedDict, total=False):
    instructions: Required[str]
    """Instructions describing how to transform the data"""

    json_schema: Required[object]
    """JSON schema defining the structure of the transformed output"""

    url: Required[str]
    """URL to fetch content from"""

    nocache: bool
    """Bypass cache and force fresh data retrieval"""
