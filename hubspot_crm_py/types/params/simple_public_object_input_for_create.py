import pydantic
import typing
import typing_extensions

from .public_associations_for_object import (
    PublicAssociationsForObject,
    _SerializerPublicAssociationsForObject,
)
from .simple_public_object_input_for_create_properties import (
    SimplePublicObjectInputForCreateProperties,
    _SerializerSimplePublicObjectInputForCreateProperties,
)


class SimplePublicObjectInputForCreate(typing_extensions.TypedDict):
    """
    SimplePublicObjectInputForCreate
    """

    associations: typing_extensions.NotRequired[
        typing.List[PublicAssociationsForObject]
    ]

    properties: typing_extensions.Required[SimplePublicObjectInputForCreateProperties]


class _SerializerSimplePublicObjectInputForCreate(pydantic.BaseModel):
    """
    Serializer for SimplePublicObjectInputForCreate handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    associations: typing.Optional[
        typing.List[_SerializerPublicAssociationsForObject]
    ] = pydantic.Field(alias="associations", default=None)
    properties: _SerializerSimplePublicObjectInputForCreateProperties = pydantic.Field(
        alias="properties",
    )
