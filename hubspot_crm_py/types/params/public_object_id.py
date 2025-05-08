import pydantic
import typing_extensions


class PublicObjectId(typing_extensions.TypedDict):
    """
    PublicObjectId
    """

    id: typing_extensions.Required[str]


class _SerializerPublicObjectId(pydantic.BaseModel):
    """
    Serializer for PublicObjectId handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(
        alias="id",
    )
