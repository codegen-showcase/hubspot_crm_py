import pydantic
import typing
import typing_extensions


class SimplePublicObjectBatchInputForCreateProperties(
    typing_extensions.TypedDict, total=False
):
    """
    SimplePublicObjectBatchInputForCreateProperties
    """


class _SerializerSimplePublicObjectBatchInputForCreateProperties(pydantic.BaseModel):
    """
    Serializer for SimplePublicObjectBatchInputForCreateProperties handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
