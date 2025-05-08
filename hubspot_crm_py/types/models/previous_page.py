import pydantic
import typing


class PreviousPage(pydantic.BaseModel):
    """
    PreviousPage
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    before: str = pydantic.Field(
        alias="before",
    )
    link: typing.Optional[str] = pydantic.Field(alias="link", default=None)
