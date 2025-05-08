
### Create a batch of meetings <a name="create"></a>



**API Endpoint**: `POST /crm/v3/objects/meetings/batch/create`

#### Synchronous Client

```python
from hubspot_crm_py import Client
from os import getenv

client = Client(
    private_apps_api_key=getenv("API_KEY"),
    private_apps_api_key_legacy=getenv("API_KEY"),
)
res = client.meetings.crm.v3.objects.meetings.batch.create.create(
    inputs=[{"properties": {}}]
)
```

#### Asynchronous Client

```python
from hubspot_crm_py import AsyncClient
from os import getenv

client = AsyncClient(
    private_apps_api_key=getenv("API_KEY"),
    private_apps_api_key_legacy=getenv("API_KEY"),
)
res = await client.meetings.crm.v3.objects.meetings.batch.create.create(
    inputs=[{"properties": {}}]
)
```
