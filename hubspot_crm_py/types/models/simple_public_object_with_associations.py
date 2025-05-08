import pydantic
import typing

from .simple_public_object_with_associations_associations import (
    SimplePublicObjectWithAssociationsAssociations,
)
from .simple_public_object_with_associations_properties import (
    SimplePublicObjectWithAssociationsProperties,
)
from .simple_public_object_with_associations_properties_with_history import (
    SimplePublicObjectWithAssociationsPropertiesWithHistory,
)


class SimplePublicObjectWithAssociations(pydantic.BaseModel):
    """
    SimplePublicObjectWithAssociations
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    archived: typing.Optional[bool] = pydantic.Field(alias="archived", default=None)
    archived_at: typing.Optional[str] = pydantic.Field(alias="archivedAt", default=None)
    associations: typing.Optional[SimplePublicObjectWithAssociationsAssociations] = (
        pydantic.Field(alias="associations", default=None)
    )
    created_at: str = pydantic.Field(
        alias="createdAt",
    )
    id: str = pydantic.Field(
        alias="id",
    )
    object_write_trace_id: typing.Optional[str] = pydantic.Field(
        alias="objectWriteTraceId", default=None
    )
    properties: SimplePublicObjectWithAssociationsProperties = pydantic.Field(
        alias="properties",
    )
    properties_with_history: typing.Optional[
        SimplePublicObjectWithAssociationsPropertiesWithHistory
    ] = pydantic.Field(alias="propertiesWithHistory", default=None)
    updated_at: str = pydantic.Field(
        alias="updatedAt",
    )
