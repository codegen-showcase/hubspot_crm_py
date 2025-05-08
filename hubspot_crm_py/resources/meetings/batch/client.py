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
        client.meetings.batch.archive(inputs=[{"id": "string"}])
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

    def create(
        self,
        *,
        inputs: typing.List[params.SimplePublicObjectBatchInputForCreate],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BatchResponseSimplePublicObject:
        """
        Create a batch of meetings

        POST /crm/v3/objects/meetings/batch/create

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
        client.meetings.batch.create(inputs=[{"properties": {}}])
        ```
        """
        _json = to_encodable(
            item={"inputs": inputs},
            dump_with=params._SerializerBatchInputSimplePublicObjectBatchInputForCreate,
        )
        return self._base_client.request(
            method="POST",
            path="/crm/v3/objects/meetings/batch/create",
            service_name="meetings",
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
        Read a batch of meetings by internal ID, or unique property values

        Retrieve records by record ID or include the `idProperty` parameter to retrieve records by a custom unique value property.

        POST /crm/v3/objects/meetings/batch/read

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
        client.meetings.batch.read(
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
            path="/crm/v3/objects/meetings/batch/read",
            service_name="meetings",
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
        Update a batch of meetings by internal ID, or unique property values

        POST /crm/v3/objects/meetings/batch/update

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
        client.meetings.batch.update(inputs=[{"id": "1", "properties": {}}])
        ```
        """
        _json = to_encodable(
            item={"inputs": inputs},
            dump_with=params._SerializerBatchInputSimplePublicObjectBatchInput,
        )
        return self._base_client.request(
            method="POST",
            path="/crm/v3/objects/meetings/batch/update",
            service_name="meetings",
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
        Create or update a batch of meetings by unique property values

        Create or update records identified by a unique property value as specified by the `idProperty` query param. `idProperty` query param refers to a property whose values are unique for the object.

        POST /crm/v3/objects/meetings/batch/upsert

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
        client.meetings.batch.upsert(inputs=[{"id": "string", "properties": {}}])
        ```
        """
        _json = to_encodable(
            item={"inputs": inputs},
            dump_with=params._SerializerBatchInputSimplePublicObjectBatchInputUpsert,
        )
        return self._base_client.request(
            method="POST",
            path="/crm/v3/objects/meetings/batch/upsert",
            service_name="meetings",
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
        await client.meetings.batch.archive(inputs=[{"id": "string"}])
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

    async def create(
        self,
        *,
        inputs: typing.List[params.SimplePublicObjectBatchInputForCreate],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BatchResponseSimplePublicObject:
        """
        Create a batch of meetings

        POST /crm/v3/objects/meetings/batch/create

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
        await client.meetings.batch.create(inputs=[{"properties": {}}])
        ```
        """
        _json = to_encodable(
            item={"inputs": inputs},
            dump_with=params._SerializerBatchInputSimplePublicObjectBatchInputForCreate,
        )
        return await self._base_client.request(
            method="POST",
            path="/crm/v3/objects/meetings/batch/create",
            service_name="meetings",
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
        Read a batch of meetings by internal ID, or unique property values

        Retrieve records by record ID or include the `idProperty` parameter to retrieve records by a custom unique value property.

        POST /crm/v3/objects/meetings/batch/read

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
        await client.meetings.batch.read(
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
            path="/crm/v3/objects/meetings/batch/read",
            service_name="meetings",
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
        Update a batch of meetings by internal ID, or unique property values

        POST /crm/v3/objects/meetings/batch/update

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
        await client.meetings.batch.update(inputs=[{"id": "1", "properties": {}}])
        ```
        """
        _json = to_encodable(
            item={"inputs": inputs},
            dump_with=params._SerializerBatchInputSimplePublicObjectBatchInput,
        )
        return await self._base_client.request(
            method="POST",
            path="/crm/v3/objects/meetings/batch/update",
            service_name="meetings",
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
        Create or update a batch of meetings by unique property values

        Create or update records identified by a unique property value as specified by the `idProperty` query param. `idProperty` query param refers to a property whose values are unique for the object.

        POST /crm/v3/objects/meetings/batch/upsert

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
        await client.meetings.batch.upsert(inputs=[{"id": "string", "properties": {}}])
        ```
        """
        _json = to_encodable(
            item={"inputs": inputs},
            dump_with=params._SerializerBatchInputSimplePublicObjectBatchInputUpsert,
        )
        return await self._base_client.request(
            method="POST",
            path="/crm/v3/objects/meetings/batch/upsert",
            service_name="meetings",
            auth_names=["private_apps"],
            json=_json,
            cast_to=models.BatchResponseSimplePublicUpsertObject,
            request_options=request_options or default_request_options(),
        )
