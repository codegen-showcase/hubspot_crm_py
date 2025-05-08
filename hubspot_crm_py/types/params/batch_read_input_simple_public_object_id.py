import pydantic
import typing
import typing_extensions

from .simple_public_object_id import (
    SimplePublicObjectId,
    _SerializerSimplePublicObjectId,
)


class BatchReadInputSimplePublicObjectId(typing_extensions.TypedDict):
    """
    BatchReadInputSimplePublicObjectId
    """

    id_property: typing_extensions.NotRequired[str]
    """
    When using a custom unique value property to retrieve records, the name of the property. Do not include this parameter if retrieving by record ID.
    """

    inputs: typing_extensions.Required[typing.List[SimplePublicObjectId]]

    properties: typing_extensions.Required[typing.List[str]]

    properties_with_history: typing_extensions.Required[typing.List[str]]


class _SerializerBatchReadInputSimplePublicObjectId(pydantic.BaseModel):
    """
    Serializer for BatchReadInputSimplePublicObjectId handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id_property: typing.Optional[str] = pydantic.Field(alias="idProperty", default=None)
    inputs: typing.List[_SerializerSimplePublicObjectId] = pydantic.Field(
        alias="inputs",
    )
    properties: typing.List[str] = pydantic.Field(
        alias="properties",
    )
    properties_with_history: typing.List[str] = pydantic.Field(
        alias="propertiesWithHistory",
    )
