from hubspot_crm_py.core import AsyncBaseClient, SyncBaseClient
from hubspot_crm_py.resources.contacts.crm.v3.objects.contacts.batch.archive import (
    ArchiveClient,
    AsyncArchiveClient,
)
from hubspot_crm_py.resources.contacts.crm.v3.objects.contacts.batch.create import (
    AsyncCreateClient,
    CreateClient,
)
from hubspot_crm_py.resources.contacts.crm.v3.objects.contacts.batch.read import (
    AsyncReadClient,
    ReadClient,
)
from hubspot_crm_py.resources.contacts.crm.v3.objects.contacts.batch.update import (
    AsyncUpdateClient,
    UpdateClient,
)
from hubspot_crm_py.resources.contacts.crm.v3.objects.contacts.batch.upsert import (
    AsyncUpsertClient,
    UpsertClient,
)


class BatchClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.archive = ArchiveClient(base_client=self._base_client)
        self.create = CreateClient(base_client=self._base_client)
        self.read = ReadClient(base_client=self._base_client)
        self.update = UpdateClient(base_client=self._base_client)
        self.upsert = UpsertClient(base_client=self._base_client)


class AsyncBatchClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.archive = AsyncArchiveClient(base_client=self._base_client)
        self.create = AsyncCreateClient(base_client=self._base_client)
        self.read = AsyncReadClient(base_client=self._base_client)
        self.update = AsyncUpdateClient(base_client=self._base_client)
        self.upsert = AsyncUpsertClient(base_client=self._base_client)
