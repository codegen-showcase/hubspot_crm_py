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
        Archive a batch of meetings by ID

        POST /crm/v3/objects/meetings/batch/archive

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
        client.meetings.crm.v3.objects.meetings.batch.archive.create(
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
            path="/crm/v3/objects/meetings/batch/archive",
            service_name="meetings",
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
        Archive a batch of meetings by ID

        POST /crm/v3/objects/meetings/batch/archive

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
        await client.meetings.crm.v3.objects.meetings.batch.archive.create(
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
            path="/crm/v3/objects/meetings/batch/archive",
            service_name="meetings",
            auth_names=["private_apps"],
            json=_json,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
