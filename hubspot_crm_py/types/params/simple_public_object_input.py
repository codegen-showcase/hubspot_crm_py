import pydantic
import typing_extensions

from .simple_public_object_input_properties import (
    SimplePublicObjectInputProperties,
    _SerializerSimplePublicObjectInputProperties,
)


class SimplePublicObjectInput(typing_extensions.TypedDict):
    """
    SimplePublicObjectInput
    """

    properties: typing_extensions.Required[SimplePublicObjectInputProperties]


class _SerializerSimplePublicObjectInput(pydantic.BaseModel):
    """
    Serializer for SimplePublicObjectInput handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    properties: _SerializerSimplePublicObjectInputProperties = pydantic.Field(
        alias="properties",
    )
