# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

__all__ = ["AgentAutomateInputParams", "Field"]


class AgentAutomateInputParams(TypedDict, total=False):
    cancelled: bool
    """Set to true to cancel/decline the request"""

    fields: Iterable[Field]
    """Field values as array of {ref, value} pairs (required when not cancelled)"""


class Field(TypedDict, total=False):
    ref: str

    value: str
