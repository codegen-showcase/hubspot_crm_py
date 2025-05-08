import pydantic
import typing
import typing_extensions

from .simple_public_object_batch_input_properties import (
    SimplePublicObjectBatchInputProperties,
    _SerializerSimplePublicObjectBatchInputProperties,
)


class SimplePublicObjectBatchInput(typing_extensions.TypedDict):
    """
    SimplePublicObjectBatchInput
    """

    id: typing_extensions.Required[str]
    """
    The id to be updated. This can be the object id, or the unique property value of the idProperty property
    """

    id_property: typing_extensions.NotRequired[str]
    """
    The name of a property whose values are unique for this object
    """

    object_write_trace_id: typing_extensions.NotRequired[str]

    properties: typing_extensions.Required[SimplePublicObjectBatchInputProperties]


class _SerializerSimplePublicObjectBatchInput(pydantic.BaseModel):
    """
    Serializer for SimplePublicObjectBatchInput handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(
        alias="id",
    )
    id_property: typing.Optional[str] = pydantic.Field(alias="idProperty", default=None)
    object_write_trace_id: typing.Optional[str] = pydantic.Field(
        alias="objectWriteTraceId", default=None
    )
    properties: _SerializerSimplePublicObjectBatchInputProperties = pydantic.Field(
        alias="properties",
    )
