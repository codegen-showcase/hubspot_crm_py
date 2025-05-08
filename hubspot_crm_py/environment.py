import enum
import typing
import typing_extensions


class Environment(enum.Enum):
    """Pre-defined base URLs for the API"""

    ENVIRONMENT = "https://api.hubapi.com"
    ENVIRONMENT_1 = "https://api.hubapi.com"
    HUBSPOT_CONTACTS_MOCK_SERVER = (
        "https://api.sideko.dev/v1/mock/public/hubspot-contacts/0.1.0"
    )
    HUBSPOT_MEETINGS_MOCK_SERVER = (
        "https://api.sideko.dev/v1/mock/public/hubspot-meetings/0.1.0"
    )


class ServerGroup(typing_extensions.TypedDict):
    """Pre-defined set of base URLs for the APIs serviced by this SDK"""

    contacts: typing_extensions.NotRequired[typing.Union[Environment, str]]
    meetings: typing_extensions.NotRequired[typing.Union[Environment, str]]


DEFAULT: ServerGroup = {
    "contacts": Environment.ENVIRONMENT.value,
    "meetings": Environment.ENVIRONMENT_1.value,
}

SIDEKO_MOCK_SERVER: ServerGroup = {
    "contacts": Environment.HUBSPOT_CONTACTS_MOCK_SERVER.value,
    "meetings": Environment.HUBSPOT_MEETINGS_MOCK_SERVER.value,
}


def _get_base_url(
    server_group: ServerGroup,
    api: typing.Literal["contacts", "meetings"],
    default: typing.Union[Environment, str],
) -> str:
    env_or_str = server_group.get(api, default)
    if isinstance(env_or_str, Environment):
        return env_or_str.value
    else:
        return str(env_or_str)
