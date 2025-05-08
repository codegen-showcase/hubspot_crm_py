import typing

from hubspot_crm_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from hubspot_crm_py.types import params


class GdprDeleteClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
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
        client.contacts.crm.v3.objects.contacts.gdpr_delete.create(object_id="string")
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


class AsyncGdprDeleteClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
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
        await client.contacts.crm.v3.objects.contacts.gdpr_delete.create(
            object_id="string"
        )
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
