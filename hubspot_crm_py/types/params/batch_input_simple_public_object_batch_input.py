import pydantic
import typing
import typing_extensions

from .simple_public_object_batch_input import (
    SimplePublicObjectBatchInput,
    _SerializerSimplePublicObjectBatchInput,
)


class BatchInputSimplePublicObjectBatchInput(typing_extensions.TypedDict):
    """
    BatchInputSimplePublicObjectBatchInput
    """

    inputs: typing_extensions.Required[typing.List[SimplePublicObjectBatchInput]]


class _SerializerBatchInputSimplePublicObjectBatchInput(pydantic.BaseModel):
    """
    Serializer for BatchInputSimplePublicObjectBatchInput handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    inputs: typing.List[_SerializerSimplePublicObjectBatchInput] = pydantic.Field(
        alias="inputs",
    )
