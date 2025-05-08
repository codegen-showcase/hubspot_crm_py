import pydantic
import typing


class NextPage(pydantic.BaseModel):
    """
    NextPage
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    after: str = pydantic.Field(
        alias="after",
    )
    link: typing.Optional[str] = pydantic.Field(alias="link", default=None)
