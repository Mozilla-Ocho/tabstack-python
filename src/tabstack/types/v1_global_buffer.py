# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["V1GlobalBuffer", "Buffer"]


class Buffer(BaseModel):
    byte_length: float = FieldInfo(alias="byteLength")


class V1GlobalBuffer(BaseModel):
    buffer: Buffer

    byte_length: float = FieldInfo(alias="byteLength")

    byte_offset: float = FieldInfo(alias="byteOffset")

    bytes_per_element: float = FieldInfo(alias="BYTES_PER_ELEMENT")

    length: float

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, float] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> float: ...
    else:
        __pydantic_extra__: Dict[str, float]
