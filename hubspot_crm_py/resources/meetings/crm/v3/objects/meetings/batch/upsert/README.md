
### Create or update a batch of meetings by unique property values <a name="create"></a>

Create or update records identified by a unique property value as specified by the `idProperty` query param. `idProperty` query param refers to a property whose values are unique for the object.

**API Endpoint**: `POST /crm/v3/objects/meetings/batch/upsert`

#### Synchronous Client

```python
from hubspot_crm_py import Client
from os import getenv

client = Client(
    private_apps_api_key=getenv("API_KEY"),
    private_apps_api_key_legacy=getenv("API_KEY"),
)
res = client.meetings.crm.v3.objects.meetings.batch.upsert.create(
    inputs=[{"id": "string", "properties": {}}]
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
res = await client.meetings.crm.v3.objects.meetings.batch.upsert.create(
    inputs=[{"id": "string", "properties": {}}]
)
```
