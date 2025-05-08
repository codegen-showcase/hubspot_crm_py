import typing

from hubspot_crm_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
)
from hubspot_crm_py.types import params


class ArchiveClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        inputs: typing.List[params.SimplePublicObjectId],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Archive a batch of contacts

        Archive a batch of contacts by ID. Archived contacts can be restored within 90 days of deletion. Learn more about the [data impacted by contact deletions](https://knowledge.hubspot.com/privacy-and-consent/understand-restorable-and-permanent-contact-deletions) and how to [restore archived records](https://knowledge.hubspot.com/records/restore-deleted-records).

        POST /crm/v3/objects/contacts/batch/archive

        Args:
            inputs: typing.List[SimplePublicObjectId]
            request_options: Additional options to customize the HTTP request

        Returns:
            No content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.contacts.crm.v3.objects.contacts.batch.archive.create(
            inputs=[{"id": "string"}]
        )
        ```
        """
        _json = to_encodable(
            item={"inputs": inputs},
            dump_with=params._SerializerBatchInputSimplePublicObjectId,
        )
        self._base_client.request(
            method="POST",
            path="/crm/v3/objects/contacts/batch/archive",
            service_name="contacts",
            auth_names=["private_apps"],
            json=_json,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )


class AsyncArchiveClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        inputs: typing.List[params.SimplePublicObjectId],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Archive a batch of contacts

        Archive a batch of contacts by ID. Archived contacts can be restored within 90 days of deletion. Learn more about the [data impacted by contact deletions](https://knowledge.hubspot.com/privacy-and-consent/understand-restorable-and-permanent-contact-deletions) and how to [restore archived records](https://knowledge.hubspot.com/records/restore-deleted-records).

        POST /crm/v3/objects/contacts/batch/archive

        Args:
            inputs: typing.List[SimplePublicObjectId]
            request_options: Additional options to customize the HTTP request

        Returns:
            No content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.contacts.crm.v3.objects.contacts.batch.archive.create(
            inputs=[{"id": "string"}]
        )
        ```
        """
        _json = to_encodable(
            item={"inputs": inputs},
            dump_with=params._SerializerBatchInputSimplePublicObjectId,
        )
        await self._base_client.request(
            method="POST",
            path="/crm/v3/objects/contacts/batch/archive",
            service_name="contacts",
            auth_names=["private_apps"],
            json=_json,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
