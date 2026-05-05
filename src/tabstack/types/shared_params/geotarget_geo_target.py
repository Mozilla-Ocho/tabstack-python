# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["GeotargetGeoTarget"]


class GeotargetGeoTarget(TypedDict, total=False):
    country: str
    """
    Country code using ISO 3166-1 alpha-2 standard (2 letters, e.g., "US", "GB",
    "JP"). See: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
    """
