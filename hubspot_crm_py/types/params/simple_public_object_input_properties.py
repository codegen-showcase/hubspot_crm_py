import pydantic
import typing
import typing_extensions


class SimplePublicObjectInputProperties(typing_extensions.TypedDict, total=False):
    """
    SimplePublicObjectInputProperties
    """


class _SerializerSimplePublicObjectInputProperties(pydantic.BaseModel):
    """
    Serializer for SimplePublicObjectInputProperties handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
