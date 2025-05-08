
### Merge two contacts <a name="create"></a>

Merge two contact records. Learn more about [merging records](https://knowledge.hubspot.com/records/merge-records). 

**API Endpoint**: `POST /crm/v3/objects/contacts/merge`

#### Synchronous Client

```python
from hubspot_crm_py import Client
from os import getenv

client = Client(
    private_apps_api_key=getenv("API_KEY"),
    private_apps_api_key_legacy=getenv("API_KEY"),
)
res = client.contacts.crm.v3.objects.contacts.merge.create(
    object_id_to_merge="string", primary_object_id="string"
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
res = await client.contacts.crm.v3.objects.contacts.merge.create(
    object_id_to_merge="string", primary_object_id="string"
)
```
