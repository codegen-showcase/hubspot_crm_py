import pydantic
import typing

from .forward_paging import ForwardPaging
from .simple_public_object import SimplePublicObject


class CollectionResponseWithTotalSimplePublicObjectForwardPaging(pydantic.BaseModel):
    """
    CollectionResponseWithTotalSimplePublicObjectForwardPaging
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    paging: typing.Optional[ForwardPaging] = pydantic.Field(
        alias="paging", default=None
    )
    results: typing.List[SimplePublicObject] = pydantic.Field(
        alias="results",
    )
    total: int = pydantic.Field(
        alias="total",
    )
