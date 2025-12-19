# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AgentAutomateResponse"]


class AgentAutomateResponse(BaseModel):
    data: Optional[object] = None
    """Event payload data"""

    event: Optional[str] = None
    """The event type (e.g., start, agent:processing, complete)"""
