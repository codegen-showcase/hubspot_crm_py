import pydantic
import typing
import typing_extensions


class SimplePublicObjectBatchInputProperties(typing_extensions.TypedDict, total=False):
    """
    SimplePublicObjectBatchInputProperties
    """


class _SerializerSimplePublicObjectBatchInputProperties(pydantic.BaseModel):
    """
    Serializer for SimplePublicObjectBatchInputProperties handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
