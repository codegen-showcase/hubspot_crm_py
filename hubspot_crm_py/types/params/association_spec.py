import pydantic
import typing_extensions


class AssociationSpec(typing_extensions.TypedDict):
    """
    AssociationSpec
    """

    association_category: typing_extensions.Required[
        typing_extensions.Literal[
            "HUBSPOT_DEFINED", "INTEGRATOR_DEFINED", "USER_DEFINED"
        ]
    ]

    association_type_id: typing_extensions.Required[int]


class _SerializerAssociationSpec(pydantic.BaseModel):
    """
    Serializer for AssociationSpec handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    association_category: typing_extensions.Literal[
        "HUBSPOT_DEFINED", "INTEGRATOR_DEFINED", "USER_DEFINED"
    ] = pydantic.Field(
        alias="associationCategory",
    )
    association_type_id: int = pydantic.Field(
        alias="associationTypeId",
    )
