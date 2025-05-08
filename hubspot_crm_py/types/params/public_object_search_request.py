import pydantic
import typing
import typing_extensions

from .filter_group import FilterGroup, _SerializerFilterGroup


class PublicObjectSearchRequest(typing_extensions.TypedDict):
    """
    PublicObjectSearchRequest
    """

    after: typing_extensions.NotRequired[str]

    filter_groups: typing_extensions.NotRequired[typing.List[FilterGroup]]

    limit: typing_extensions.NotRequired[int]

    properties: typing_extensions.NotRequired[typing.List[str]]

    query: typing_extensions.NotRequired[str]

    sorts: typing_extensions.NotRequired[typing.List[str]]


class _SerializerPublicObjectSearchRequest(pydantic.BaseModel):
    """
    Serializer for PublicObjectSearchRequest handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    after: typing.Optional[str] = pydantic.Field(alias="after", default=None)
    filter_groups: typing.Optional[typing.List[_SerializerFilterGroup]] = (
        pydantic.Field(alias="filterGroups", default=None)
    )
    limit: typing.Optional[int] = pydantic.Field(alias="limit", default=None)
    properties: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="properties", default=None
    )
    query: typing.Optional[str] = pydantic.Field(alias="query", default=None)
    sorts: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="sorts", default=None
    )
