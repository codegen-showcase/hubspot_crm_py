import pydantic
import typing
import typing_extensions

from .simple_public_object_batch_input_upsert_properties import (
    SimplePublicObjectBatchInputUpsertProperties,
    _SerializerSimplePublicObjectBatchInputUpsertProperties,
)


class SimplePublicObjectBatchInputUpsert(typing_extensions.TypedDict):
    """
    SimplePublicObjectBatchInputUpsert
    """

    id: typing_extensions.Required[str]

    id_property: typing_extensions.NotRequired[str]
    """
    The name of a property whose values are unique for this object
    """

    object_write_trace_id: typing_extensions.NotRequired[str]

    properties: typing_extensions.Required[SimplePublicObjectBatchInputUpsertProperties]


class _SerializerSimplePublicObjectBatchInputUpsert(pydantic.BaseModel):
    """
    Serializer for SimplePublicObjectBatchInputUpsert handling case conversions
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
    properties: _SerializerSimplePublicObjectBatchInputUpsertProperties = (
        pydantic.Field(
            alias="properties",
        )
    )
