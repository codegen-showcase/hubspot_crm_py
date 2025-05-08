import pydantic


class AssociatedId(pydantic.BaseModel):
    """
    AssociatedId
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = pydantic.Field(
        alias="id",
    )
    type_: str = pydantic.Field(
        alias="type",
    )
