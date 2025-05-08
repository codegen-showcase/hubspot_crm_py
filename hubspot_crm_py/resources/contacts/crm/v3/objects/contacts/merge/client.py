import typing

from hubspot_crm_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
)
from hubspot_crm_py.types import models, params


class MergeClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        object_id_to_merge: str,
        primary_object_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SimplePublicObject:
        """
        Merge two contacts

        Merge two contact records. Learn more about [merging records](https://knowledge.hubspot.com/records/merge-records).

        POST /crm/v3/objects/contacts/merge

        Args:
            objectIdToMerge: str
            primaryObjectId: str
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.contacts.crm.v3.objects.contacts.merge.create(
            object_id_to_merge="string", primary_object_id="string"
        )
        ```
        """
        _json = to_encodable(
            item={
                "object_id_to_merge": object_id_to_merge,
                "primary_object_id": primary_object_id,
            },
            dump_with=params._SerializerPublicMergeInput,
        )
        return self._base_client.request(
            method="POST",
            path="/crm/v3/objects/contacts/merge",
            service_name="contacts",
            auth_names=["private_apps"],
            json=_json,
            cast_to=models.SimplePublicObject,
            request_options=request_options or default_request_options(),
        )


class AsyncMergeClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        object_id_to_merge: str,
        primary_object_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SimplePublicObject:
        """
        Merge two contacts

        Merge two contact records. Learn more about [merging records](https://knowledge.hubspot.com/records/merge-records).

        POST /crm/v3/objects/contacts/merge

        Args:
            objectIdToMerge: str
            primaryObjectId: str
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.contacts.crm.v3.objects.contacts.merge.create(
            object_id_to_merge="string", primary_object_id="string"
        )
        ```
        """
        _json = to_encodable(
            item={
                "object_id_to_merge": object_id_to_merge,
                "primary_object_id": primary_object_id,
            },
            dump_with=params._SerializerPublicMergeInput,
        )
        return await self._base_client.request(
            method="POST",
            path="/crm/v3/objects/contacts/merge",
            service_name="contacts",
            auth_names=["private_apps"],
            json=_json,
            cast_to=models.SimplePublicObject,
            request_options=request_options or default_request_options(),
        )
