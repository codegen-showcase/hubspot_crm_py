import pydantic
import typing

from .associated_id import AssociatedId
from .paging import Paging


class CollectionResponseAssociatedId(pydantic.BaseModel):
    """
    CollectionResponseAssociatedId
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    paging: typing.Optional[Paging] = pydantic.Field(alias="paging", default=None)
    results: typing.List[AssociatedId] = pydantic.Field(
        alias="results",
    )
