import pydantic
import typing

from .next_page import NextPage
from .previous_page import PreviousPage


class Paging(pydantic.BaseModel):
    """
    Paging
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    next: typing.Optional[NextPage] = pydantic.Field(alias="next", default=None)
    prev: typing.Optional[PreviousPage] = pydantic.Field(alias="prev", default=None)
