from hubspot_crm_py.core import AsyncBaseClient, SyncBaseClient
from hubspot_crm_py.resources.meetings.crm import AsyncCrmClient, CrmClient


class MeetingsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.crm = CrmClient(base_client=self._base_client)


class AsyncMeetingsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.crm = AsyncCrmClient(base_client=self._base_client)
