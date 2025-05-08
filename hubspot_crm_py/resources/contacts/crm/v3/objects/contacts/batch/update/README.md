
### Update a batch of contacts <a name="create"></a>

Update a batch of contacts by ID (`contactId`) or unique property value (`idProperty`). Provided property values will be overwritten. Read-only and non-existent properties will result in an error. Properties values can be cleared by passing an empty string.

**API Endpoint**: `POST /crm/v3/objects/contacts/batch/update`

#### Synchronous Client

```python
from hubspot_crm_py import Client
from os import getenv

client = Client(
    private_apps_api_key=getenv("API_KEY"),
    private_apps_api_key_legacy=getenv("API_KEY"),
)
res = client.contacts.crm.v3.objects.contacts.batch.update.create(
    inputs=[{"id": "1", "properties": {}}]
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
res = await client.contacts.crm.v3.objects.contacts.batch.update.create(
    inputs=[{"id": "1", "properties": {}}]
)
```
