
### Archive a batch of contacts <a name="archive"></a>

Archive a batch of contacts by ID. Archived contacts can be restored within 90 days of deletion. Learn more about the [data impacted by contact deletions](https://knowledge.hubspot.com/privacy-and-consent/understand-restorable-and-permanent-contact-deletions) and how to [restore archived records](https://knowledge.hubspot.com/records/restore-deleted-records).

**API Endpoint**: `POST /crm/v3/objects/contacts/batch/archive`

#### Synchronous Client

```python
from hubspot_crm_py import Client
from os import getenv

client = Client(
    private_apps_api_key=getenv("API_KEY"),
    private_apps_api_key_legacy=getenv("API_KEY"),
)
res = client.contacts.batch.archive(inputs=[{"id": "string"}])
```

#### Asynchronous Client

```python
from hubspot_crm_py import AsyncClient
from os import getenv

client = AsyncClient(
    private_apps_api_key=getenv("API_KEY"),
    private_apps_api_key_legacy=getenv("API_KEY"),
)
res = await client.contacts.batch.archive(inputs=[{"id": "string"}])
```

### Create a batch of contacts <a name="create"></a>

Create a batch of contacts. The `inputs` array can contain a `properties` object to define property values for each record, along with an `associations` array to define [associations](https://developers.hubspot.com/docs/guides/api/crm/associations/associations-v4) with other CRM records.

**API Endpoint**: `POST /crm/v3/objects/contacts/batch/create`

#### Synchronous Client

```python
from hubspot_crm_py import Client
from os import getenv

client = Client(
    private_apps_api_key=getenv("API_KEY"),
    private_apps_api_key_legacy=getenv("API_KEY"),
)
res = client.contacts.batch.create(inputs=[{"properties": {}}])
```

#### Asynchronous Client

```python
from hubspot_crm_py import AsyncClient
from os import getenv

client = AsyncClient(
    private_apps_api_key=getenv("API_KEY"),
    private_apps_api_key_legacy=getenv("API_KEY"),
)
res = await client.contacts.batch.create(inputs=[{"properties": {}}])
```

### Retrieve a batch of contacts <a name="read"></a>

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
res = client.contacts.batch.read(
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
res = await client.contacts.batch.read(
    inputs=[{"id": "string"}], properties=["string"], properties_with_history=["string"]
)
```

### Update a batch of contacts <a name="update"></a>

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
res = client.contacts.batch.update(inputs=[{"id": "1", "properties": {}}])
```

#### Asynchronous Client

```python
from hubspot_crm_py import AsyncClient
from os import getenv

client = AsyncClient(
    private_apps_api_key=getenv("API_KEY"),
    private_apps_api_key_legacy=getenv("API_KEY"),
)
res = await client.contacts.batch.update(inputs=[{"id": "1", "properties": {}}])
```

### Create or update a batch of contacts <a name="upsert"></a>

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
res = client.contacts.batch.upsert(inputs=[{"id": "string", "properties": {}}])
```

#### Asynchronous Client

```python
from hubspot_crm_py import AsyncClient
from os import getenv

client = AsyncClient(
    private_apps_api_key=getenv("API_KEY"),
    private_apps_api_key_legacy=getenv("API_KEY"),
)
res = await client.contacts.batch.upsert(inputs=[{"id": "string", "properties": {}}])
```
