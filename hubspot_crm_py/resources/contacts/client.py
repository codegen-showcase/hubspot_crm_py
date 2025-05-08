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
from hubspot_crm_py.resources.contacts.batch import AsyncBatchClient, BatchClient
from hubspot_crm_py.types import models, params


class ContactsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.batch = BatchClient(base_client=self._base_client)

    def delete(
        self,
        *,
        contact_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Archive a contact

        Delete a contact by ID. Deleted contacts can be restored within 90 days of deletion. Learn more about the [data impacted by contact deletions](https://knowledge.hubspot.com/privacy-and-consent/understand-restorable-and-permanent-contact-deletions) and how to [restore archived records](https://knowledge.hubspot.com/records/restore-deleted-records).

        DELETE /crm/v3/objects/contacts/{contactId}

        Args:
            contactId: The ID of the contact to delete.
            request_options: Additional options to customize the HTTP request

        Returns:
            No content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.contacts.delete(contact_id="string")
        ```
        """
        self._base_client.request(
            method="DELETE",
            path=f"/crm/v3/objects/contacts/{contact_id}",
            service_name="contacts",
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
        Retrieve contacts

        Retrieve all contacts, using query parameters to specify the information that gets returned.

        GET /crm/v3/objects/contacts

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
        client.contacts.list()
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
            path="/crm/v3/objects/contacts",
            service_name="contacts",
            auth_names=["private_apps"],
            query_params=_query,
            cast_to=models.CollectionResponseSimplePublicObjectWithAssociationsForwardPaging,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        contact_id: str,
        archived: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        associations: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
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
        Retrieve a contact

        Retrieve a contact by its ID (`contactId`) or by a unique property (`idProperty`). You can specify what is returned using the `properties` query parameter.

        GET /crm/v3/objects/contacts/{contactId}

        Args:
            archived: Whether to return only results that have been archived.
            associations: A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
            properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
            propertiesWithHistory: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored.
            contactId: The ID of the contact to retrieve.
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.contacts.get(contact_id="string")
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
            path=f"/crm/v3/objects/contacts/{contact_id}",
            service_name="contacts",
            auth_names=["private_apps"],
            query_params=_query,
            cast_to=models.SimplePublicObjectWithAssociations,
            request_options=request_options or default_request_options(),
        )

    def patch(
        self,
        *,
        contact_id: str,
        properties: params.SimplePublicObjectInputProperties,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SimplePublicObject:
        """
        Update a contact

        Update a contact by ID (`contactId`) or unique property value (`idProperty`). Provided property values will be overwritten. Read-only and non-existent properties will result in an error. Properties values can be cleared by passing an empty string.

        PATCH /crm/v3/objects/contacts/{contactId}

        Args:
            contactId: The ID of the contact to update.
            properties: SimplePublicObjectInputProperties
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.contacts.patch(contact_id="string", properties={})
        ```
        """
        _json = to_encodable(
            item={"properties": properties},
            dump_with=params._SerializerSimplePublicObjectInput,
        )
        return self._base_client.request(
            method="PATCH",
            path=f"/crm/v3/objects/contacts/{contact_id}",
            service_name="contacts",
            auth_names=["private_apps"],
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
        Create a contact

        Create a single contact. Include a `properties` object to define [property values](https://developers.hubspot.com/docs/guides/api/crm/properties) for the contact, along with an `associations` array to define [associations](https://developers.hubspot.com/docs/guides/api/crm/associations/associations-v4) with other CRM records.

        POST /crm/v3/objects/contacts

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
        client.contacts.create(
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
            path="/crm/v3/objects/contacts",
            service_name="contacts",
            auth_names=["private_apps"],
            json=_json,
            cast_to=models.SimplePublicObject,
            request_options=request_options or default_request_options(),
        )

    def gdpr_delete(
        self,
        *,
        object_id: str,
        id_property: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Permanently delete a contact (GDPR-compliant)

        Permanently delete a contact and all associated content to follow GDPR. Use optional property `idProperty` set to `email` to identify contact by email address. If email address is not found, the email address will be added to a blocklist and prevent it from being used in the future. Learn more about [permanently deleting contacts](https://knowledge.hubspot.com/privacy-and-consent/how-do-i-perform-a-gdpr-delete-in-hubspot).

        POST /crm/v3/objects/contacts/gdpr-delete

        Args:
            idProperty: The name of a property whose values are unique for this object. An alternative to identifying a contact by ID.
            objectId: The ID of the contact to permanently delete.
            request_options: Additional options to customize the HTTP request

        Returns:
            No content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.contacts.gdpr_delete(object_id="string")
        ```
        """
        _json = to_encodable(
            item={"id_property": id_property, "object_id": object_id},
            dump_with=params._SerializerPublicGdprDeleteInput,
        )
        self._base_client.request(
            method="POST",
            path="/crm/v3/objects/contacts/gdpr-delete",
            service_name="contacts",
            auth_names=["private_apps"],
            json=_json,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def merge(
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
        client.contacts.merge(object_id_to_merge="string", primary_object_id="string")
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

    def search(
        self,
        *,
        after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        filter_groups: typing.Union[
            typing.Optional[typing.List[params.FilterGroup]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        properties: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        query: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        sorts: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CollectionResponseWithTotalSimplePublicObjectForwardPaging:
        """
        Search for contacts

        Search for contacts by filtering on properties, searching through associations, and sorting results. Learn more about [CRM search](https://developers.hubspot.com/docs/guides/api/crm/search#make-a-search-request).

        POST /crm/v3/objects/contacts/search

        Args:
            after: str
            filterGroups: typing.List[FilterGroup]
            limit: int
            properties: typing.List[str]
            query: str
            sorts: typing.List[str]
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.contacts.search()
        ```
        """
        _json = to_encodable(
            item={
                "after": after,
                "filter_groups": filter_groups,
                "limit": limit,
                "properties": properties,
                "query": query,
                "sorts": sorts,
            },
            dump_with=params._SerializerPublicObjectSearchRequest,
        )
        return self._base_client.request(
            method="POST",
            path="/crm/v3/objects/contacts/search",
            service_name="contacts",
            auth_names=["private_apps"],
            json=_json,
            cast_to=models.CollectionResponseWithTotalSimplePublicObjectForwardPaging,
            request_options=request_options or default_request_options(),
        )


class AsyncContactsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.batch = AsyncBatchClient(base_client=self._base_client)

    async def delete(
        self,
        *,
        contact_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Archive a contact

        Delete a contact by ID. Deleted contacts can be restored within 90 days of deletion. Learn more about the [data impacted by contact deletions](https://knowledge.hubspot.com/privacy-and-consent/understand-restorable-and-permanent-contact-deletions) and how to [restore archived records](https://knowledge.hubspot.com/records/restore-deleted-records).

        DELETE /crm/v3/objects/contacts/{contactId}

        Args:
            contactId: The ID of the contact to delete.
            request_options: Additional options to customize the HTTP request

        Returns:
            No content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.contacts.delete(contact_id="string")
        ```
        """
        await self._base_client.request(
            method="DELETE",
            path=f"/crm/v3/objects/contacts/{contact_id}",
            service_name="contacts",
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
        Retrieve contacts

        Retrieve all contacts, using query parameters to specify the information that gets returned.

        GET /crm/v3/objects/contacts

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
        await client.contacts.list()
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
            path="/crm/v3/objects/contacts",
            service_name="contacts",
            auth_names=["private_apps"],
            query_params=_query,
            cast_to=models.CollectionResponseSimplePublicObjectWithAssociationsForwardPaging,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        contact_id: str,
        archived: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        associations: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
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
        Retrieve a contact

        Retrieve a contact by its ID (`contactId`) or by a unique property (`idProperty`). You can specify what is returned using the `properties` query parameter.

        GET /crm/v3/objects/contacts/{contactId}

        Args:
            archived: Whether to return only results that have been archived.
            associations: A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
            properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
            propertiesWithHistory: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored.
            contactId: The ID of the contact to retrieve.
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.contacts.get(contact_id="string")
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
            path=f"/crm/v3/objects/contacts/{contact_id}",
            service_name="contacts",
            auth_names=["private_apps"],
            query_params=_query,
            cast_to=models.SimplePublicObjectWithAssociations,
            request_options=request_options or default_request_options(),
        )

    async def patch(
        self,
        *,
        contact_id: str,
        properties: params.SimplePublicObjectInputProperties,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SimplePublicObject:
        """
        Update a contact

        Update a contact by ID (`contactId`) or unique property value (`idProperty`). Provided property values will be overwritten. Read-only and non-existent properties will result in an error. Properties values can be cleared by passing an empty string.

        PATCH /crm/v3/objects/contacts/{contactId}

        Args:
            contactId: The ID of the contact to update.
            properties: SimplePublicObjectInputProperties
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.contacts.patch(contact_id="string", properties={})
        ```
        """
        _json = to_encodable(
            item={"properties": properties},
            dump_with=params._SerializerSimplePublicObjectInput,
        )
        return await self._base_client.request(
            method="PATCH",
            path=f"/crm/v3/objects/contacts/{contact_id}",
            service_name="contacts",
            auth_names=["private_apps"],
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
        Create a contact

        Create a single contact. Include a `properties` object to define [property values](https://developers.hubspot.com/docs/guides/api/crm/properties) for the contact, along with an `associations` array to define [associations](https://developers.hubspot.com/docs/guides/api/crm/associations/associations-v4) with other CRM records.

        POST /crm/v3/objects/contacts

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
        await client.contacts.create(
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
            path="/crm/v3/objects/contacts",
            service_name="contacts",
            auth_names=["private_apps"],
            json=_json,
            cast_to=models.SimplePublicObject,
            request_options=request_options or default_request_options(),
        )

    async def gdpr_delete(
        self,
        *,
        object_id: str,
        id_property: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Permanently delete a contact (GDPR-compliant)

        Permanently delete a contact and all associated content to follow GDPR. Use optional property `idProperty` set to `email` to identify contact by email address. If email address is not found, the email address will be added to a blocklist and prevent it from being used in the future. Learn more about [permanently deleting contacts](https://knowledge.hubspot.com/privacy-and-consent/how-do-i-perform-a-gdpr-delete-in-hubspot).

        POST /crm/v3/objects/contacts/gdpr-delete

        Args:
            idProperty: The name of a property whose values are unique for this object. An alternative to identifying a contact by ID.
            objectId: The ID of the contact to permanently delete.
            request_options: Additional options to customize the HTTP request

        Returns:
            No content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.contacts.gdpr_delete(object_id="string")
        ```
        """
        _json = to_encodable(
            item={"id_property": id_property, "object_id": object_id},
            dump_with=params._SerializerPublicGdprDeleteInput,
        )
        await self._base_client.request(
            method="POST",
            path="/crm/v3/objects/contacts/gdpr-delete",
            service_name="contacts",
            auth_names=["private_apps"],
            json=_json,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def merge(
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
        await client.contacts.merge(
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

    async def search(
        self,
        *,
        after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        filter_groups: typing.Union[
            typing.Optional[typing.List[params.FilterGroup]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        properties: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        query: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        sorts: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CollectionResponseWithTotalSimplePublicObjectForwardPaging:
        """
        Search for contacts

        Search for contacts by filtering on properties, searching through associations, and sorting results. Learn more about [CRM search](https://developers.hubspot.com/docs/guides/api/crm/search#make-a-search-request).

        POST /crm/v3/objects/contacts/search

        Args:
            after: str
            filterGroups: typing.List[FilterGroup]
            limit: int
            properties: typing.List[str]
            query: str
            sorts: typing.List[str]
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.contacts.search()
        ```
        """
        _json = to_encodable(
            item={
                "after": after,
                "filter_groups": filter_groups,
                "limit": limit,
                "properties": properties,
                "query": query,
                "sorts": sorts,
            },
            dump_with=params._SerializerPublicObjectSearchRequest,
        )
        return await self._base_client.request(
            method="POST",
            path="/crm/v3/objects/contacts/search",
            service_name="contacts",
            auth_names=["private_apps"],
            json=_json,
            cast_to=models.CollectionResponseWithTotalSimplePublicObjectForwardPaging,
            request_options=request_options or default_request_options(),
        )
