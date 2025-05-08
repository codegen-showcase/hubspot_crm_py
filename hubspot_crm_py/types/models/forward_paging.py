import pydantic
import typing

from .next_page import NextPage


class ForwardPaging(pydantic.BaseModel):
    """
    ForwardPaging
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    next: typing.Optional[NextPage] = pydantic.Field(alias="next", default=None)
