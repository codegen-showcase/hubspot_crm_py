import pydantic
import typing

from .simple_public_object_properties import SimplePublicObjectProperties
from .simple_public_object_properties_with_history import (
    SimplePublicObjectPropertiesWithHistory,
)


class SimplePublicObject(pydantic.BaseModel):
    """
    SimplePublicObject
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    archived: typing.Optional[bool] = pydantic.Field(alias="archived", default=None)
    archived_at: typing.Optional[str] = pydantic.Field(alias="archivedAt", default=None)
    created_at: str = pydantic.Field(
        alias="createdAt",
    )
    id: str = pydantic.Field(
        alias="id",
    )
    object_write_trace_id: typing.Optional[str] = pydantic.Field(
        alias="objectWriteTraceId", default=None
    )
    properties: SimplePublicObjectProperties = pydantic.Field(
        alias="properties",
    )
    properties_with_history: typing.Optional[
        SimplePublicObjectPropertiesWithHistory
    ] = pydantic.Field(alias="propertiesWithHistory", default=None)
    updated_at: str = pydantic.Field(
        alias="updatedAt",
    )
