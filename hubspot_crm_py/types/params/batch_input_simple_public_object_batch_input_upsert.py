import pydantic
import typing
import typing_extensions

from .simple_public_object_batch_input_upsert import (
    SimplePublicObjectBatchInputUpsert,
    _SerializerSimplePublicObjectBatchInputUpsert,
)


class BatchInputSimplePublicObjectBatchInputUpsert(typing_extensions.TypedDict):
    """
    BatchInputSimplePublicObjectBatchInputUpsert
    """

    inputs: typing_extensions.Required[typing.List[SimplePublicObjectBatchInputUpsert]]


class _SerializerBatchInputSimplePublicObjectBatchInputUpsert(pydantic.BaseModel):
    """
    Serializer for BatchInputSimplePublicObjectBatchInputUpsert handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    inputs: typing.List[_SerializerSimplePublicObjectBatchInputUpsert] = pydantic.Field(
        alias="inputs",
    )
