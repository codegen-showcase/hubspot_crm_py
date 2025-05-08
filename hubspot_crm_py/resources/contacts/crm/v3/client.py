from hubspot_crm_py.core import AsyncBaseClient, SyncBaseClient
from hubspot_crm_py.resources.contacts.crm.v3.objects import (
    AsyncObjectsClient,
    ObjectsClient,
)


class V3Client:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.objects = ObjectsClient(base_client=self._base_client)


class AsyncV3Client:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.objects = AsyncObjectsClient(base_client=self._base_client)
