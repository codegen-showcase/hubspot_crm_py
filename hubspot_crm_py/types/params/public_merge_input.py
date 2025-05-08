import pydantic
import typing_extensions


class PublicMergeInput(typing_extensions.TypedDict):
    """
    PublicMergeInput
    """

    object_id_to_merge: typing_extensions.Required[str]

    primary_object_id: typing_extensions.Required[str]


class _SerializerPublicMergeInput(pydantic.BaseModel):
    """
    Serializer for PublicMergeInput handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    object_id_to_merge: str = pydantic.Field(
        alias="objectIdToMerge",
    )
    primary_object_id: str = pydantic.Field(
        alias="primaryObjectId",
    )
