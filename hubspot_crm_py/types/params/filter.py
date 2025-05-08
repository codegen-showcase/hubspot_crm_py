import pydantic
import typing
import typing_extensions


class Filter(typing_extensions.TypedDict):
    """
    Filter
    """

    high_value: typing_extensions.NotRequired[str]

    operator: typing_extensions.Required[
        typing_extensions.Literal[
            "BETWEEN",
            "CONTAINS_TOKEN",
            "EQ",
            "GT",
            "GTE",
            "HAS_PROPERTY",
            "IN",
            "LT",
            "LTE",
            "NEQ",
            "NOT_CONTAINS_TOKEN",
            "NOT_HAS_PROPERTY",
            "NOT_IN",
        ]
    ]
    """
    null
    """

    property_name: typing_extensions.Required[str]

    value: typing_extensions.NotRequired[str]

    values: typing_extensions.NotRequired[typing.List[str]]


class _SerializerFilter(pydantic.BaseModel):
    """
    Serializer for Filter handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    high_value: typing.Optional[str] = pydantic.Field(alias="highValue", default=None)
    operator: typing_extensions.Literal[
        "BETWEEN",
        "CONTAINS_TOKEN",
        "EQ",
        "GT",
        "GTE",
        "HAS_PROPERTY",
        "IN",
        "LT",
        "LTE",
        "NEQ",
        "NOT_CONTAINS_TOKEN",
        "NOT_HAS_PROPERTY",
        "NOT_IN",
    ] = pydantic.Field(
        alias="operator",
    )
    property_name: str = pydantic.Field(
        alias="propertyName",
    )
    value: typing.Optional[str] = pydantic.Field(alias="value", default=None)
    values: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="values", default=None
    )
