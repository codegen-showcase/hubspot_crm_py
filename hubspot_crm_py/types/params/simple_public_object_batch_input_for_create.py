import pydantic
import typing
import typing_extensions

from .public_associations_for_object import (
    PublicAssociationsForObject,
    _SerializerPublicAssociationsForObject,
)
from .simple_public_object_batch_input_for_create_properties import (
    SimplePublicObjectBatchInputForCreateProperties,
    _SerializerSimplePublicObjectBatchInputForCreateProperties,
)


class SimplePublicObjectBatchInputForCreate(typing_extensions.TypedDict):
    """
    SimplePublicObjectBatchInputForCreate
    """

    associations: typing_extensions.NotRequired[
        typing.List[PublicAssociationsForObject]
    ]

    object_write_trace_id: typing_extensions.NotRequired[str]

    properties: typing_extensions.Required[
        SimplePublicObjectBatchInputForCreateProperties
    ]


class _SerializerSimplePublicObjectBatchInputForCreate(pydantic.BaseModel):
    """
    Serializer for SimplePublicObjectBatchInputForCreate handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    associations: typing.Optional[
        typing.List[_SerializerPublicAssociationsForObject]
    ] = pydantic.Field(alias="associations", default=None)
    object_write_trace_id: typing.Optional[str] = pydantic.Field(
        alias="objectWriteTraceId", default=None
    )
    properties: _SerializerSimplePublicObjectBatchInputForCreateProperties = (
        pydantic.Field(
            alias="properties",
        )
    )
