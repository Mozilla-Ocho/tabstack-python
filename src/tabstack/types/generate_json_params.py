# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .shared_params.geotarget_geo_target import GeotargetGeoTarget

__all__ = ["GenerateJsonParams"]


class GenerateJsonParams(TypedDict, total=False):
    instructions: Required[str]
    """Instructions describing how to transform the data. Maximum 20,000 characters."""

    json_schema: Required[object]
    """JSON schema defining the structure of the transformed output"""

    url: Required[str]
    """URL to fetch content from"""

    effort: Literal["min", "standard", "max"]
    """Fetch effort level controlling speed vs.

    capability tradeoff. "min": fastest, no fallback (1-5s). "standard": balanced
    with enhanced reliability (default, 3-15s). "max": full browser rendering for
    JS-heavy sites (15-60s).
    """

    geo_target: GeotargetGeoTarget
    """Optional geotargeting parameters for proxy requests"""

    nocache: bool
    """Bypass cache and force fresh data retrieval"""
