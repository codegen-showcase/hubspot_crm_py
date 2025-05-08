import pydantic
import typing
import typing_extensions

from .simple_public_object_batch_input_for_create import (
    SimplePublicObjectBatchInputForCreate,
    _SerializerSimplePublicObjectBatchInputForCreate,
)


class BatchInputSimplePublicObjectBatchInputForCreate(typing_extensions.TypedDict):
    """
    BatchInputSimplePublicObjectBatchInputForCreate
    """

    inputs: typing_extensions.Required[
        typing.List[SimplePublicObjectBatchInputForCreate]
    ]


class _SerializerBatchInputSimplePublicObjectBatchInputForCreate(pydantic.BaseModel):
    """
    Serializer for BatchInputSimplePublicObjectBatchInputForCreate handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    inputs: typing.List[_SerializerSimplePublicObjectBatchInputForCreate] = (
        pydantic.Field(
            alias="inputs",
        )
    )
