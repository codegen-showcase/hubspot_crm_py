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


class ReadClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
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
        client.meetings.crm.v3.objects.meetings.batch.read.create(
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


class AsyncReadClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
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
        await client.meetings.crm.v3.objects.meetings.batch.read.create(
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
