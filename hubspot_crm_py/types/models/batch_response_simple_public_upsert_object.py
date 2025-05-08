import pydantic
import typing
import typing_extensions

from .batch_response_simple_public_upsert_object_links import (
    BatchResponseSimplePublicUpsertObjectLinks,
)
from .simple_public_upsert_object import SimplePublicUpsertObject


class BatchResponseSimplePublicUpsertObject(pydantic.BaseModel):
    """
    BatchResponseSimplePublicUpsertObject
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    completed_at: str = pydantic.Field(
        alias="completedAt",
    )
    links: typing.Optional[BatchResponseSimplePublicUpsertObjectLinks] = pydantic.Field(
        alias="links", default=None
    )
    requested_at: typing.Optional[str] = pydantic.Field(
        alias="requestedAt", default=None
    )
    results: typing.List[SimplePublicUpsertObject] = pydantic.Field(
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
