import pydantic
import typing_extensions


class SimplePublicObjectId(typing_extensions.TypedDict):
    """
    SimplePublicObjectId
    """

    id: typing_extensions.Required[str]


class _SerializerSimplePublicObjectId(pydantic.BaseModel):
    """
    Serializer for SimplePublicObjectId handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(
        alias="id",
    )
