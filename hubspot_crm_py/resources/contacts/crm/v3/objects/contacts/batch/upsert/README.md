
### Create or update a batch of contacts <a name="create"></a>

Upsert a batch of contacts. The `inputs` array can contain a `properties` object to define property values for each record.

**API Endpoint**: `POST /crm/v3/objects/contacts/batch/upsert`

#### Synchronous Client

```python
from hubspot_crm_py import Client
from os import getenv

client = Client(
    private_apps_api_key=getenv("API_KEY"),
    private_apps_api_key_legacy=getenv("API_KEY"),
)
res = client.contacts.crm.v3.objects.contacts.batch.upsert.create(
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
res = await client.contacts.crm.v3.objects.contacts.batch.upsert.create(
    inputs=[{"id": "string", "properties": {}}]
)
```
