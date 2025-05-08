import typing

from hubspot_crm_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
)
from hubspot_crm_py.types import models, params


class UpsertClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        inputs: typing.List[params.SimplePublicObjectBatchInputUpsert],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BatchResponseSimplePublicUpsertObject:
        """
        Create or update a batch of contacts

        Upsert a batch of contacts. The `inputs` array can contain a `properties` object to define property values for each record.

        POST /crm/v3/objects/contacts/batch/upsert

        Args:
            inputs: typing.List[SimplePublicObjectBatchInputUpsert]
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.contacts.crm.v3.objects.contacts.batch.upsert.create(
            inputs=[{"id": "string", "properties": {}}]
        )
        ```
        """
        _json = to_encodable(
            item={"inputs": inputs},
            dump_with=params._SerializerBatchInputSimplePublicObjectBatchInputUpsert,
        )
        return self._base_client.request(
            method="POST",
            path="/crm/v3/objects/contacts/batch/upsert",
            service_name="contacts",
            auth_names=["private_apps"],
            json=_json,
            cast_to=models.BatchResponseSimplePublicUpsertObject,
            request_options=request_options or default_request_options(),
        )


class AsyncUpsertClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        inputs: typing.List[params.SimplePublicObjectBatchInputUpsert],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BatchResponseSimplePublicUpsertObject:
        """
        Create or update a batch of contacts

        Upsert a batch of contacts. The `inputs` array can contain a `properties` object to define property values for each record.

        POST /crm/v3/objects/contacts/batch/upsert

        Args:
            inputs: typing.List[SimplePublicObjectBatchInputUpsert]
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.contacts.crm.v3.objects.contacts.batch.upsert.create(
            inputs=[{"id": "string", "properties": {}}]
        )
        ```
        """
        _json = to_encodable(
            item={"inputs": inputs},
            dump_with=params._SerializerBatchInputSimplePublicObjectBatchInputUpsert,
        )
        return await self._base_client.request(
            method="POST",
            path="/crm/v3/objects/contacts/batch/upsert",
            service_name="contacts",
            auth_names=["private_apps"],
            json=_json,
            cast_to=models.BatchResponseSimplePublicUpsertObject,
            request_options=request_options or default_request_options(),
        )
