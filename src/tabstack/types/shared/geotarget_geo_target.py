# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["GeotargetGeoTarget"]


class GeotargetGeoTarget(BaseModel):
    country: Optional[str] = None
    """
    Country code using ISO 3166-1 alpha-2 standard (2 letters, e.g., "US", "GB",
    "JP"). See: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
    """
