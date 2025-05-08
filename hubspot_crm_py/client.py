import httpx
import typing

from hubspot_crm_py.core import AsyncBaseClient, AuthKeyHeader, SyncBaseClient
from hubspot_crm_py.environment import DEFAULT, Environment, ServerGroup, _get_base_url
from hubspot_crm_py.resources.contacts import AsyncContactsClient, ContactsClient
from hubspot_crm_py.resources.meetings import AsyncMeetingsClient, MeetingsClient


class Client:
    def __init__(
        self,
        *,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.Client] = None,
        environment: ServerGroup = DEFAULT,
        private_apps_api_key: typing.Optional[str] = None,
        private_apps_api_key_legacy: typing.Optional[str] = None,
    ):
        """Initialize root client"""
        self._base_client = SyncBaseClient(
            base_url={
                "contacts": _get_base_url(
                    environment, "contacts", Environment.ENVIRONMENT.value
                ),
                "meetings": _get_base_url(
                    environment, "meetings", Environment.ENVIRONMENT_1.value
                ),
            },
            httpx_client=httpx.Client(timeout=timeout)
            if httpx_client is None
            else httpx_client,
        )
        self._base_client.register_auth(
            "private_apps",
            AuthKeyHeader(header_name="private-app", val=private_apps_api_key),
        )
        self._base_client.register_auth(
            "private_apps_legacy",
            AuthKeyHeader(
                header_name="private-app-legacy", val=private_apps_api_key_legacy
            ),
        )
        self.contacts = ContactsClient(base_client=self._base_client)
        self.meetings = MeetingsClient(base_client=self._base_client)


class AsyncClient:
    def __init__(
        self,
        *,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        environment: ServerGroup = DEFAULT,
        private_apps_api_key: typing.Optional[str] = None,
        private_apps_api_key_legacy: typing.Optional[str] = None,
    ):
        """Initialize root client"""
        self._base_client = AsyncBaseClient(
            base_url={
                "contacts": _get_base_url(
                    environment, "contacts", Environment.ENVIRONMENT.value
                ),
                "meetings": _get_base_url(
                    environment, "meetings", Environment.ENVIRONMENT_1.value
                ),
            },
            httpx_client=httpx.AsyncClient(timeout=timeout)
            if httpx_client is None
            else httpx_client,
        )
        self._base_client.register_auth(
            "private_apps",
            AuthKeyHeader(header_name="private-app", val=private_apps_api_key),
        )
        self._base_client.register_auth(
            "private_apps_legacy",
            AuthKeyHeader(
                header_name="private-app-legacy", val=private_apps_api_key_legacy
            ),
        )
        self.contacts = AsyncContactsClient(base_client=self._base_client)
        self.meetings = AsyncMeetingsClient(base_client=self._base_client)
