
### Read a batch of meetings by internal ID, or unique property values <a name="create"></a>

Retrieve records by record ID or include the `idProperty` parameter to retrieve records by a custom unique value property. 

**API Endpoint**: `POST /crm/v3/objects/meetings/batch/read`

#### Synchronous Client

```python
from hubspot_crm_py import Client
from os import getenv

client = Client(
    private_apps_api_key=getenv("API_KEY"),
    private_apps_api_key_legacy=getenv("API_KEY"),
)
res = client.meetings.crm.v3.objects.meetings.batch.read.create(
    inputs=[{"id": "string"}], properties=["string"], properties_with_history=["string"]
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
res = await client.meetings.crm.v3.objects.meetings.batch.read.create(
    inputs=[{"id": "string"}], properties=["string"], properties_with_history=["string"]
)
```
