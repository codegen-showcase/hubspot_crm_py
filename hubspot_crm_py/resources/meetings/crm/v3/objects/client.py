from hubspot_crm_py.core import AsyncBaseClient, SyncBaseClient
from hubspot_crm_py.resources.meetings.crm.v3.objects.meetings import (
    AsyncMeetingsClient,
    MeetingsClient,
)


class ObjectsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.meetings = MeetingsClient(base_client=self._base_client)


class AsyncObjectsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.meetings = AsyncMeetingsClient(base_client=self._base_client)
