from hubspot_crm_py.core import AsyncBaseClient, SyncBaseClient
from hubspot_crm_py.resources.contacts.crm.v3.objects.contacts import (
    AsyncContactsClient,
    ContactsClient,
)


class ObjectsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.contacts = ContactsClient(base_client=self._base_client)


class AsyncObjectsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.contacts = AsyncContactsClient(base_client=self._base_client)
