import pydantic
import typing
import typing_extensions

from .batch_response_simple_public_object_links import (
    BatchResponseSimplePublicObjectLinks,
)
from .simple_public_object import SimplePublicObject


class BatchResponseSimplePublicObject(pydantic.BaseModel):
    """
    BatchResponseSimplePublicObject
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    completed_at: str = pydantic.Field(
        alias="completedAt",
    )
    links: typing.Optional[BatchResponseSimplePublicObjectLinks] = pydantic.Field(
        alias="links", default=None
    )
    requested_at: typing.Optional[str] = pydantic.Field(
        alias="requestedAt", default=None
    )
    results: typing.List[SimplePublicObject] = pydantic.Field(
        alias="results",
    )
    started_at: str = pydantic.Field(
        alias="startedAt",
    )
    status: typing_extensions.Literal[
        "CANCELED", "COMPLETE", "PENDING", "PROCESSING"
    ] = pydantic.Field(
        alias="status",
    )
