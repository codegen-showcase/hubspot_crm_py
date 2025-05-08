import pydantic
import typing
import typing_extensions

from .simple_public_object_id import (
    SimplePublicObjectId,
    _SerializerSimplePublicObjectId,
)


class BatchInputSimplePublicObjectId(typing_extensions.TypedDict):
    """
    BatchInputSimplePublicObjectId
    """

    inputs: typing_extensions.Required[typing.List[SimplePublicObjectId]]


class _SerializerBatchInputSimplePublicObjectId(pydantic.BaseModel):
    """
    Serializer for BatchInputSimplePublicObjectId handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    inputs: typing.List[_SerializerSimplePublicObjectId] = pydantic.Field(
        alias="inputs",
    )
