import pydantic
import typing

from .forward_paging import ForwardPaging
from .simple_public_object_with_associations import SimplePublicObjectWithAssociations


class CollectionResponseSimplePublicObjectWithAssociationsForwardPaging(
    pydantic.BaseModel
):
    """
    CollectionResponseSimplePublicObjectWithAssociationsForwardPaging
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    paging: typing.Optional[ForwardPaging] = pydantic.Field(
        alias="paging", default=None
    )
    results: typing.List[SimplePublicObjectWithAssociations] = pydantic.Field(
        alias="results",
    )
