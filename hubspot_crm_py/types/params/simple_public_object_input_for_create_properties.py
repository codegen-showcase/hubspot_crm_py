import pydantic
import typing
import typing_extensions


class SimplePublicObjectInputForCreateProperties(
    typing_extensions.TypedDict, total=False
):
    """
    SimplePublicObjectInputForCreateProperties
    """


class _SerializerSimplePublicObjectInputForCreateProperties(pydantic.BaseModel):
    """
    Serializer for SimplePublicObjectInputForCreateProperties handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
