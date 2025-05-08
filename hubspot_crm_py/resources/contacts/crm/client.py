from hubspot_crm_py.core import AsyncBaseClient, SyncBaseClient
from hubspot_crm_py.resources.contacts.crm.v3 import AsyncV3Client, V3Client


class CrmClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.v3 = V3Client(base_client=self._base_client)


class AsyncCrmClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.v3 = AsyncV3Client(base_client=self._base_client)
