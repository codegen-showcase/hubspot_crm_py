import typing

from hubspot_crm_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
)
from hubspot_crm_py.types import models, params


class UpdateClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        inputs: typing.List[params.SimplePublicObjectBatchInput],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BatchResponseSimplePublicObject:
        """
        Update a batch of contacts

        Update a batch of contacts by ID (`contactId`) or unique property value (`idProperty`). Provided property values will be overwritten. Read-only and non-existent properties will result in an error. Properties values can be cleared by passing an empty string.

        POST /crm/v3/objects/contacts/batch/update

        Args:
            inputs: typing.List[SimplePublicObjectBatchInput]
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.contacts.crm.v3.objects.contacts.batch.update.create(
            inputs=[{"id": "1", "properties": {}}]
        )
        ```
        """
        _json = to_encodable(
            item={"inputs": inputs},
            dump_with=params._SerializerBatchInputSimplePublicObjectBatchInput,
        )
        return self._base_client.request(
            method="POST",
            path="/crm/v3/objects/contacts/batch/update",
            service_name="contacts",
            auth_names=["private_apps"],
            json=_json,
            cast_to=models.BatchResponseSimplePublicObject,
            request_options=request_options or default_request_options(),
        )


class AsyncUpdateClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        inputs: typing.List[params.SimplePublicObjectBatchInput],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BatchResponseSimplePublicObject:
        """
        Update a batch of contacts

        Update a batch of contacts by ID (`contactId`) or unique property value (`idProperty`). Provided property values will be overwritten. Read-only and non-existent properties will result in an error. Properties values can be cleared by passing an empty string.

        POST /crm/v3/objects/contacts/batch/update

        Args:
            inputs: typing.List[SimplePublicObjectBatchInput]
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.contacts.crm.v3.objects.contacts.batch.update.create(
            inputs=[{"id": "1", "properties": {}}]
        )
        ```
        """
        _json = to_encodable(
            item={"inputs": inputs},
            dump_with=params._SerializerBatchInputSimplePublicObjectBatchInput,
        )
        return await self._base_client.request(
            method="POST",
            path="/crm/v3/objects/contacts/batch/update",
            service_name="contacts",
            auth_names=["private_apps"],
            json=_json,
            cast_to=models.BatchResponseSimplePublicObject,
            request_options=request_options or default_request_options(),
        )
