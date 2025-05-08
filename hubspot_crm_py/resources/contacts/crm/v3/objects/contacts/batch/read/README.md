
### Retrieve a batch of contacts <a name="create"></a>

Retrieve a batch of contacts by ID (`contactId`) or unique property value (`idProperty`). 

**API Endpoint**: `POST /crm/v3/objects/contacts/batch/read`

#### Synchronous Client

```python
from hubspot_crm_py import Client
from os import getenv

client = Client(
    private_apps_api_key=getenv("API_KEY"),
    private_apps_api_key_legacy=getenv("API_KEY"),
)
res = client.contacts.crm.v3.objects.contacts.batch.read.create(
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
res = await client.contacts.crm.v3.objects.contacts.batch.read.create(
    inputs=[{"id": "string"}], properties=["string"], properties_with_history=["string"]
)
```
