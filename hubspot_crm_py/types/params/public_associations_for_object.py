import pydantic
import typing
import typing_extensions

from .association_spec import AssociationSpec, _SerializerAssociationSpec
from .public_object_id import PublicObjectId, _SerializerPublicObjectId


class PublicAssociationsForObject(typing_extensions.TypedDict):
    """
    PublicAssociationsForObject
    """

    to: typing_extensions.Required[PublicObjectId]

    types: typing_extensions.Required[typing.List[AssociationSpec]]


class _SerializerPublicAssociationsForObject(pydantic.BaseModel):
    """
    Serializer for PublicAssociationsForObject handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    to: _SerializerPublicObjectId = pydantic.Field(
        alias="to",
    )
    types: typing.List[_SerializerAssociationSpec] = pydantic.Field(
        alias="types",
    )
