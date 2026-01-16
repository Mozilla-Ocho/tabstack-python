# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ExtractMarkdownParams"]


class ExtractMarkdownParams(TypedDict, total=False):
    url: Required[str]
    """URL to fetch and convert to markdown"""

    metadata: bool
    """
    Include extracted metadata (Open Graph and HTML metadata) as a separate field in
    the response
    """

    nocache: bool
    """Bypass cache and force fresh data retrieval"""
