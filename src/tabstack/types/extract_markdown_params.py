# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .shared_params.geotarget_geo_target import GeotargetGeoTarget

__all__ = ["ExtractMarkdownParams"]


class ExtractMarkdownParams(TypedDict, total=False):
    url: Required[str]
    """URL to fetch and convert to markdown"""

    effort: Literal["min", "standard", "max"]
    """Fetch effort level controlling speed vs.

    capability tradeoff. "min": fastest, no fallback (1-5s). "standard": balanced
    with enhanced reliability (default, 3-15s). "max": full browser rendering for
    JS-heavy sites (15-60s).
    """

    geo_target: GeotargetGeoTarget
    """Optional geotargeting parameters for proxy requests"""

    metadata: bool
    """
    Include extracted metadata (Open Graph and HTML metadata) as a separate field in
    the response
    """

    nocache: bool
    """Bypass cache and force fresh data retrieval"""
