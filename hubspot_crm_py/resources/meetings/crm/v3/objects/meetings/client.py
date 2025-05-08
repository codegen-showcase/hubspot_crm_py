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
from hubspot_crm_py.resources.meetings.crm.v3.objects.meetings.batch import (
    AsyncBatchClient,
    BatchClient,
)
from hubspot_crm_py.resources.meetings.crm.v3.objects.meetings.search import (
    AsyncSearchClient,
    SearchClient,
)
from hubspot_crm_py.types import models, params


class MeetingsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.batch = BatchClient(base_client=self._base_client)
        self.search = SearchClient(base_client=self._base_client)

    def delete(
        self,
        *,
        meeting_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Archive

        Move an Object identified by `{meetingId}` to the recycling bin.

        DELETE /crm/v3/objects/meetings/{meetingId}

        Args:
            meetingId: str
            request_options: Additional options to customize the HTTP request

        Returns:
            No content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.meetings.crm.v3.objects.meetings.delete(meeting_id="string")
        ```
        """
        self._base_client.request(
            method="DELETE",
            path=f"/crm/v3/objects/meetings/{meeting_id}",
            service_name="meetings",
            auth_names=["private_apps"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        archived: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        associations: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        properties: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        properties_with_history: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CollectionResponseSimplePublicObjectWithAssociationsForwardPaging:
        """
        List

        Read a page of meetings. Control what is returned via the `properties` query param.

        GET /crm/v3/objects/meetings

        Args:
            after: The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.
            archived: Whether to return only results that have been archived.
            associations: A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
            limit: The maximum number of results to display per page.
            properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
            propertiesWithHistory: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored. Usage of this parameter will reduce the maximum number of objects that can be read by a single request.
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.meetings.crm.v3.objects.meetings.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(after, type_utils.NotGiven):
            encode_query_param(
                _query,
                "after",
                to_encodable(item=after, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(archived, type_utils.NotGiven):
            encode_query_param(
                _query,
                "archived",
                to_encodable(item=archived, dump_with=bool),
                style="form",
                explode=True,
            )
        if not isinstance(associations, type_utils.NotGiven):
            encode_query_param(
                _query,
                "associations",
                to_encodable(item=associations, dump_with=typing.List[str]),
                style="form",
                explode=True,
            )
        if not isinstance(limit, type_utils.NotGiven):
            encode_query_param(
                _query,
                "limit",
                to_encodable(item=limit, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(properties, type_utils.NotGiven):
            encode_query_param(
                _query,
                "properties",
                to_encodable(item=properties, dump_with=typing.List[str]),
                style="form",
                explode=True,
            )
        if not isinstance(properties_with_history, type_utils.NotGiven):
            encode_query_param(
                _query,
                "propertiesWithHistory",
                to_encodable(item=properties_with_history, dump_with=typing.List[str]),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/crm/v3/objects/meetings",
            service_name="meetings",
            auth_names=["private_apps"],
            query_params=_query,
            cast_to=models.CollectionResponseSimplePublicObjectWithAssociationsForwardPaging,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        meeting_id: str,
        archived: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        associations: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id_property: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        properties: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        properties_with_history: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SimplePublicObjectWithAssociations:
        """
        Read

        Read an Object identified by `{meetingId}`. `{meetingId}` refers to the internal object ID by default, or optionally any unique property value as specified by the `idProperty` query param.  Control what is returned via the `properties` query param.

        GET /crm/v3/objects/meetings/{meetingId}

        Args:
            archived: Whether to return only results that have been archived.
            associations: A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
            idProperty: The name of a property whose values are unique for this object
            properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
            propertiesWithHistory: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored.
            meetingId: str
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.meetings.crm.v3.objects.meetings.get(meeting_id="string")
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
        if not isinstance(associations, type_utils.NotGiven):
            encode_query_param(
                _query,
                "associations",
                to_encodable(item=associations, dump_with=typing.List[str]),
                style="form",
                explode=True,
            )
        if not isinstance(id_property, type_utils.NotGiven):
            encode_query_param(
                _query,
                "idProperty",
                to_encodable(item=id_property, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(properties, type_utils.NotGiven):
            encode_query_param(
                _query,
                "properties",
                to_encodable(item=properties, dump_with=typing.List[str]),
                style="form",
                explode=True,
            )
        if not isinstance(properties_with_history, type_utils.NotGiven):
            encode_query_param(
                _query,
                "propertiesWithHistory",
                to_encodable(item=properties_with_history, dump_with=typing.List[str]),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path=f"/crm/v3/objects/meetings/{meeting_id}",
            service_name="meetings",
            auth_names=["private_apps"],
            query_params=_query,
            cast_to=models.SimplePublicObjectWithAssociations,
            request_options=request_options or default_request_options(),
        )

    def patch(
        self,
        *,
        meeting_id: str,
        properties: params.SimplePublicObjectInputProperties,
        id_property: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SimplePublicObject:
        """
        Update

        Perform a partial update of an Object identified by `{meetingId}`or optionally a unique property value as specified by the `idProperty` query param. `{meetingId}` refers to the internal object ID by default, and the `idProperty` query param refers to a property whose values are unique for the object. Provided property values will be overwritten. Read-only and non-existent properties will result in an error. Properties values can be cleared by passing an empty string.

        PATCH /crm/v3/objects/meetings/{meetingId}

        Args:
            idProperty: The name of a property whose values are unique for this object
            meetingId: str
            properties: SimplePublicObjectInputProperties
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.meetings.crm.v3.objects.meetings.patch(
            meeting_id="string", properties={}
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(id_property, type_utils.NotGiven):
            encode_query_param(
                _query,
                "idProperty",
                to_encodable(item=id_property, dump_with=str),
                style="form",
                explode=True,
            )
        _json = to_encodable(
            item={"properties": properties},
            dump_with=params._SerializerSimplePublicObjectInput,
        )
        return self._base_client.request(
            method="PATCH",
            path=f"/crm/v3/objects/meetings/{meeting_id}",
            service_name="meetings",
            auth_names=["private_apps"],
            query_params=_query,
            json=_json,
            cast_to=models.SimplePublicObject,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        properties: params.SimplePublicObjectInputForCreateProperties,
        associations: typing.Union[
            typing.Optional[typing.List[params.PublicAssociationsForObject]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SimplePublicObject:
        """
        Create

        Create a meeting with the given properties and return a copy of the object, including the ID. Documentation and examples for creating standard meetings is provided.

        POST /crm/v3/objects/meetings

        Args:
            associations: typing.List[PublicAssociationsForObject]
            properties: SimplePublicObjectInputForCreateProperties
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.meetings.crm.v3.objects.meetings.create(
            properties={},
            associations=[
                {
                    "to": {"id": "101"},
                    "types": [
                        {
                            "association_category": "HUBSPOT_DEFINED",
                            "association_type_id": 2,
                        }
                    ],
                }
            ],
        )
        ```
        """
        _json = to_encodable(
            item={"associations": associations, "properties": properties},
            dump_with=params._SerializerSimplePublicObjectInputForCreate,
        )
        return self._base_client.request(
            method="POST",
            path="/crm/v3/objects/meetings",
            service_name="meetings",
            auth_names=["private_apps"],
            json=_json,
            cast_to=models.SimplePublicObject,
            request_options=request_options or default_request_options(),
        )


class AsyncMeetingsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.batch = AsyncBatchClient(base_client=self._base_client)
        self.search = AsyncSearchClient(base_client=self._base_client)

    async def delete(
        self,
        *,
        meeting_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Archive

        Move an Object identified by `{meetingId}` to the recycling bin.

        DELETE /crm/v3/objects/meetings/{meetingId}

        Args:
            meetingId: str
            request_options: Additional options to customize the HTTP request

        Returns:
            No content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.meetings.crm.v3.objects.meetings.delete(meeting_id="string")
        ```
        """
        await self._base_client.request(
            method="DELETE",
            path=f"/crm/v3/objects/meetings/{meeting_id}",
            service_name="meetings",
            auth_names=["private_apps"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        archived: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        associations: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        properties: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        properties_with_history: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CollectionResponseSimplePublicObjectWithAssociationsForwardPaging:
        """
        List

        Read a page of meetings. Control what is returned via the `properties` query param.

        GET /crm/v3/objects/meetings

        Args:
            after: The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.
            archived: Whether to return only results that have been archived.
            associations: A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
            limit: The maximum number of results to display per page.
            properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
            propertiesWithHistory: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored. Usage of this parameter will reduce the maximum number of objects that can be read by a single request.
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.meetings.crm.v3.objects.meetings.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(after, type_utils.NotGiven):
            encode_query_param(
                _query,
                "after",
                to_encodable(item=after, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(archived, type_utils.NotGiven):
            encode_query_param(
                _query,
                "archived",
                to_encodable(item=archived, dump_with=bool),
                style="form",
                explode=True,
            )
        if not isinstance(associations, type_utils.NotGiven):
            encode_query_param(
                _query,
                "associations",
                to_encodable(item=associations, dump_with=typing.List[str]),
                style="form",
                explode=True,
            )
        if not isinstance(limit, type_utils.NotGiven):
            encode_query_param(
                _query,
                "limit",
                to_encodable(item=limit, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(properties, type_utils.NotGiven):
            encode_query_param(
                _query,
                "properties",
                to_encodable(item=properties, dump_with=typing.List[str]),
                style="form",
                explode=True,
            )
        if not isinstance(properties_with_history, type_utils.NotGiven):
            encode_query_param(
                _query,
                "propertiesWithHistory",
                to_encodable(item=properties_with_history, dump_with=typing.List[str]),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/crm/v3/objects/meetings",
            service_name="meetings",
            auth_names=["private_apps"],
            query_params=_query,
            cast_to=models.CollectionResponseSimplePublicObjectWithAssociationsForwardPaging,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        meeting_id: str,
        archived: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        associations: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id_property: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        properties: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        properties_with_history: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SimplePublicObjectWithAssociations:
        """
        Read

        Read an Object identified by `{meetingId}`. `{meetingId}` refers to the internal object ID by default, or optionally any unique property value as specified by the `idProperty` query param.  Control what is returned via the `properties` query param.

        GET /crm/v3/objects/meetings/{meetingId}

        Args:
            archived: Whether to return only results that have been archived.
            associations: A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
            idProperty: The name of a property whose values are unique for this object
            properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
            propertiesWithHistory: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored.
            meetingId: str
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.meetings.crm.v3.objects.meetings.get(meeting_id="string")
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
        if not isinstance(associations, type_utils.NotGiven):
            encode_query_param(
                _query,
                "associations",
                to_encodable(item=associations, dump_with=typing.List[str]),
                style="form",
                explode=True,
            )
        if not isinstance(id_property, type_utils.NotGiven):
            encode_query_param(
                _query,
                "idProperty",
                to_encodable(item=id_property, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(properties, type_utils.NotGiven):
            encode_query_param(
                _query,
                "properties",
                to_encodable(item=properties, dump_with=typing.List[str]),
                style="form",
                explode=True,
            )
        if not isinstance(properties_with_history, type_utils.NotGiven):
            encode_query_param(
                _query,
                "propertiesWithHistory",
                to_encodable(item=properties_with_history, dump_with=typing.List[str]),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path=f"/crm/v3/objects/meetings/{meeting_id}",
            service_name="meetings",
            auth_names=["private_apps"],
            query_params=_query,
            cast_to=models.SimplePublicObjectWithAssociations,
            request_options=request_options or default_request_options(),
        )

    async def patch(
        self,
        *,
        meeting_id: str,
        properties: params.SimplePublicObjectInputProperties,
        id_property: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SimplePublicObject:
        """
        Update

        Perform a partial update of an Object identified by `{meetingId}`or optionally a unique property value as specified by the `idProperty` query param. `{meetingId}` refers to the internal object ID by default, and the `idProperty` query param refers to a property whose values are unique for the object. Provided property values will be overwritten. Read-only and non-existent properties will result in an error. Properties values can be cleared by passing an empty string.

        PATCH /crm/v3/objects/meetings/{meetingId}

        Args:
            idProperty: The name of a property whose values are unique for this object
            meetingId: str
            properties: SimplePublicObjectInputProperties
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.meetings.crm.v3.objects.meetings.patch(
            meeting_id="string", properties={}
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(id_property, type_utils.NotGiven):
            encode_query_param(
                _query,
                "idProperty",
                to_encodable(item=id_property, dump_with=str),
                style="form",
                explode=True,
            )
        _json = to_encodable(
            item={"properties": properties},
            dump_with=params._SerializerSimplePublicObjectInput,
        )
        return await self._base_client.request(
            method="PATCH",
            path=f"/crm/v3/objects/meetings/{meeting_id}",
            service_name="meetings",
            auth_names=["private_apps"],
            query_params=_query,
            json=_json,
            cast_to=models.SimplePublicObject,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        properties: params.SimplePublicObjectInputForCreateProperties,
        associations: typing.Union[
            typing.Optional[typing.List[params.PublicAssociationsForObject]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SimplePublicObject:
        """
        Create

        Create a meeting with the given properties and return a copy of the object, including the ID. Documentation and examples for creating standard meetings is provided.

        POST /crm/v3/objects/meetings

        Args:
            associations: typing.List[PublicAssociationsForObject]
            properties: SimplePublicObjectInputForCreateProperties
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.meetings.crm.v3.objects.meetings.create(
            properties={},
            associations=[
                {
                    "to": {"id": "101"},
                    "types": [
                        {
                            "association_category": "HUBSPOT_DEFINED",
                            "association_type_id": 2,
                        }
                    ],
                }
            ],
        )
        ```
        """
        _json = to_encodable(
            item={"associations": associations, "properties": properties},
            dump_with=params._SerializerSimplePublicObjectInputForCreate,
        )
        return await self._base_client.request(
            method="POST",
            path="/crm/v3/objects/meetings",
            service_name="meetings",
            auth_names=["private_apps"],
            json=_json,
            cast_to=models.SimplePublicObject,
            request_options=request_options or default_request_options(),
        )
