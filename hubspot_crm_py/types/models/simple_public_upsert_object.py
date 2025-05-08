import pydantic
import typing

from .simple_public_upsert_object_properties import SimplePublicUpsertObjectProperties
from .simple_public_upsert_object_properties_with_history import (
    SimplePublicUpsertObjectPropertiesWithHistory,
)


class SimplePublicUpsertObject(pydantic.BaseModel):
    """
    SimplePublicUpsertObject
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
    new: bool = pydantic.Field(
        alias="new",
    )
    object_write_trace_id: typing.Optional[str] = pydantic.Field(
        alias="objectWriteTraceId", default=None
    )
    properties: SimplePublicUpsertObjectProperties = pydantic.Field(
        alias="properties",
    )
    properties_with_history: typing.Optional[
        SimplePublicUpsertObjectPropertiesWithHistory
    ] = pydantic.Field(alias="propertiesWithHistory", default=None)
    updated_at: str = pydantic.Field(
        alias="updatedAt",
    )
