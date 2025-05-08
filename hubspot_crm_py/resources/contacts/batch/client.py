import typing

from hubspot_crm_py.core import (
    AsyncBaseClient,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_query_param,
    to_encodable,
    type_utils,
)
from hubspot_crm_py.types import models, params


class BatchClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def archive(
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
        client.contacts.batch.archive(inputs=[{"id": "string"}])
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

    def create(
        self,
        *,
        inputs: typing.List[params.SimplePublicObjectBatchInputForCreate],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BatchResponseSimplePublicObject:
        """
        Create a batch of contacts

        Create a batch of contacts. The `inputs` array can contain a `properties` object to define property values for each record, along with an `associations` array to define [associations](https://developers.hubspot.com/docs/guides/api/crm/associations/associations-v4) with other CRM records.

        POST /crm/v3/objects/contacts/batch/create

        Args:
            inputs: typing.List[SimplePublicObjectBatchInputForCreate]
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.contacts.batch.create(inputs=[{"properties": {}}])
        ```
        """
        _json = to_encodable(
            item={"inputs": inputs},
            dump_with=params._SerializerBatchInputSimplePublicObjectBatchInputForCreate,
        )
        return self._base_client.request(
            method="POST",
            path="/crm/v3/objects/contacts/batch/create",
            service_name="contacts",
            auth_names=["private_apps"],
            json=_json,
            cast_to=models.BatchResponseSimplePublicObject,
            request_options=request_options or default_request_options(),
        )

    def read(
        self,
        *,
        inputs: typing.List[params.SimplePublicObjectId],
        properties: typing.List[str],
        properties_with_history: typing.List[str],
        archived: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id_property: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BatchResponseSimplePublicObject:
        """
        Retrieve a batch of contacts

        Retrieve a batch of contacts by ID (`contactId`) or unique property value (`idProperty`).

        POST /crm/v3/objects/contacts/batch/read

        Args:
            archived: Whether to return only results that have been archived.
            idProperty: When using a custom unique value property to retrieve records, the name of the property. Do not include this parameter if retrieving by record ID.
            inputs: typing.List[SimplePublicObjectId]
            properties: typing.List[str]
            propertiesWithHistory: typing.List[str]
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.contacts.batch.read(
            inputs=[{"id": "string"}],
            properties=["string"],
            properties_with_history=["string"],
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(archived, type_utils.NotGiven):
            encode_query_param(
                _query,
                "archived",
                to_encodable(item=archived, dump_with=bool),
                style="form",
                explode=True,
            )
        _json = to_encodable(
            item={
                "id_property": id_property,
                "inputs": inputs,
                "properties": properties,
                "properties_with_history": properties_with_history,
            },
            dump_with=params._SerializerBatchReadInputSimplePublicObjectId,
        )
        return self._base_client.request(
            method="POST",
            path="/crm/v3/objects/contacts/batch/read",
            service_name="contacts",
            auth_names=["private_apps"],
            query_params=_query,
            json=_json,
            cast_to=models.BatchResponseSimplePublicObject,
            request_options=request_options or default_request_options(),
        )

    def update(
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
        client.contacts.batch.update(inputs=[{"id": "1", "properties": {}}])
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

    def upsert(
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
        client.contacts.batch.upsert(inputs=[{"id": "string", "properties": {}}])
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


class AsyncBatchClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def archive(
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
        await client.contacts.batch.archive(inputs=[{"id": "string"}])
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

    async def create(
        self,
        *,
        inputs: typing.List[params.SimplePublicObjectBatchInputForCreate],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BatchResponseSimplePublicObject:
        """
        Create a batch of contacts

        Create a batch of contacts. The `inputs` array can contain a `properties` object to define property values for each record, along with an `associations` array to define [associations](https://developers.hubspot.com/docs/guides/api/crm/associations/associations-v4) with other CRM records.

        POST /crm/v3/objects/contacts/batch/create

        Args:
            inputs: typing.List[SimplePublicObjectBatchInputForCreate]
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.contacts.batch.create(inputs=[{"properties": {}}])
        ```
        """
        _json = to_encodable(
            item={"inputs": inputs},
            dump_with=params._SerializerBatchInputSimplePublicObjectBatchInputForCreate,
        )
        return await self._base_client.request(
            method="POST",
            path="/crm/v3/objects/contacts/batch/create",
            service_name="contacts",
            auth_names=["private_apps"],
            json=_json,
            cast_to=models.BatchResponseSimplePublicObject,
            request_options=request_options or default_request_options(),
        )

    async def read(
        self,
        *,
        inputs: typing.List[params.SimplePublicObjectId],
        properties: typing.List[str],
        properties_with_history: typing.List[str],
        archived: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id_property: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BatchResponseSimplePublicObject:
        """
        Retrieve a batch of contacts

        Retrieve a batch of contacts by ID (`contactId`) or unique property value (`idProperty`).

        POST /crm/v3/objects/contacts/batch/read

        Args:
            archived: Whether to return only results that have been archived.
            idProperty: When using a custom unique value property to retrieve records, the name of the property. Do not include this parameter if retrieving by record ID.
            inputs: typing.List[SimplePublicObjectId]
            properties: typing.List[str]
            propertiesWithHistory: typing.List[str]
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.contacts.batch.read(
            inputs=[{"id": "string"}],
            properties=["string"],
            properties_with_history=["string"],
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(archived, type_utils.NotGiven):
            encode_query_param(
                _query,
                "archived",
                to_encodable(item=archived, dump_with=bool),
                style="form",
                explode=True,
            )
        _json = to_encodable(
            item={
                "id_property": id_property,
                "inputs": inputs,
                "properties": properties,
                "properties_with_history": properties_with_history,
            },
            dump_with=params._SerializerBatchReadInputSimplePublicObjectId,
        )
        return await self._base_client.request(
            method="POST",
            path="/crm/v3/objects/contacts/batch/read",
            service_name="contacts",
            auth_names=["private_apps"],
            query_params=_query,
            json=_json,
            cast_to=models.BatchResponseSimplePublicObject,
            request_options=request_options or default_request_options(),
        )

    async def update(
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
        await client.contacts.batch.update(inputs=[{"id": "1", "properties": {}}])
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

    async def upsert(
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
        await client.contacts.batch.upsert(inputs=[{"id": "string", "properties": {}}])
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
