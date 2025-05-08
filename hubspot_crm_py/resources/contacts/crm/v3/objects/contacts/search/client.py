import typing

from hubspot_crm_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from hubspot_crm_py.types import models, params


class SearchClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
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
        client.contacts.crm.v3.objects.contacts.search.create()
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


class AsyncSearchClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
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
        await client.contacts.crm.v3.objects.contacts.search.create()
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
