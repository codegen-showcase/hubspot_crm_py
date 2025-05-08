import pydantic
import typing

from .value_with_timestamp import ValueWithTimestamp


class SimplePublicObjectWithAssociationsPropertiesWithHistory(pydantic.BaseModel):
    """
    SimplePublicObjectWithAssociationsPropertiesWithHistory
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, typing.List[ValueWithTimestamp]]
