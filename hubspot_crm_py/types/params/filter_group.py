import pydantic
import typing
import typing_extensions

from .filter import Filter, _SerializerFilter


class FilterGroup(typing_extensions.TypedDict):
    """
    FilterGroup
    """

    filters: typing_extensions.Required[typing.List[Filter]]


class _SerializerFilterGroup(pydantic.BaseModel):
    """
    Serializer for FilterGroup handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    filters: typing.List[_SerializerFilter] = pydantic.Field(
        alias="filters",
    )
