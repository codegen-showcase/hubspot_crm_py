import pydantic
import typing
import typing_extensions


class PublicGdprDeleteInput(typing_extensions.TypedDict):
    """
    PublicGdprDeleteInput
    """

    id_property: typing_extensions.NotRequired[str]
    """
    The name of a property whose values are unique for this object. An alternative to identifying a contact by ID.
    """

    object_id: typing_extensions.Required[str]
    """
    The ID of the contact to permanently delete.
    """


class _SerializerPublicGdprDeleteInput(pydantic.BaseModel):
    """
    Serializer for PublicGdprDeleteInput handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id_property: typing.Optional[str] = pydantic.Field(alias="idProperty", default=None)
    object_id: str = pydantic.Field(
        alias="objectId",
    )
