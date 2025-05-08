import pydantic
import typing


class ValueWithTimestamp(pydantic.BaseModel):
    """
    ValueWithTimestamp
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    source_id: typing.Optional[str] = pydantic.Field(alias="sourceId", default=None)
    source_label: typing.Optional[str] = pydantic.Field(
        alias="sourceLabel", default=None
    )
    source_type: str = pydantic.Field(
        alias="sourceType",
    )
    timestamp: str = pydantic.Field(
        alias="timestamp",
    )
    updated_by_user_id: typing.Optional[int] = pydantic.Field(
        alias="updatedByUserId", default=None
    )
    value: str = pydantic.Field(
        alias="value",
    )
