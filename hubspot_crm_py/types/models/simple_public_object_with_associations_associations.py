import pydantic
import typing

from .collection_response_associated_id import CollectionResponseAssociatedId


class SimplePublicObjectWithAssociationsAssociations(pydantic.BaseModel):
    """
    SimplePublicObjectWithAssociationsAssociations
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, CollectionResponseAssociatedId]
