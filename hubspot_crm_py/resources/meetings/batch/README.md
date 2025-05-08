
### Archive a batch of meetings by ID <a name="archive"></a>



**API Endpoint**: `POST /crm/v3/objects/meetings/batch/archive`

#### Synchronous Client

```python
from hubspot_crm_py import Client
from os import getenv

client = Client(
    private_apps_api_key=getenv("API_KEY"),
    private_apps_api_key_legacy=getenv("API_KEY"),
)
res = client.meetings.batch.archive(inputs=[{"id": "string"}])
```

#### Asynchronous Client

```python
from hubspot_crm_py import AsyncClient
from os import getenv

client = AsyncClient(
    private_apps_api_key=getenv("API_KEY"),
    private_apps_api_key_legacy=getenv("API_KEY"),
)
res = await client.meetings.batch.archive(inputs=[{"id": "string"}])
```

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
res = client.meetings.batch.create(inputs=[{"properties": {}}])
```

#### Asynchronous Client

```python
from hubspot_crm_py import AsyncClient
from os import getenv

client = AsyncClient(
    private_apps_api_key=getenv("API_KEY"),
    private_apps_api_key_legacy=getenv("API_KEY"),
)
res = await client.meetings.batch.create(inputs=[{"properties": {}}])
```

### Read a batch of meetings by internal ID, or unique property values <a name="read"></a>

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
res = client.meetings.batch.read(
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
res = await client.meetings.batch.read(
    inputs=[{"id": "string"}], properties=["string"], properties_with_history=["string"]
)
```

### Update a batch of meetings by internal ID, or unique property values <a name="update"></a>



**API Endpoint**: `POST /crm/v3/objects/meetings/batch/update`

#### Synchronous Client

```python
from hubspot_crm_py import Client
from os import getenv

client = Client(
    private_apps_api_key=getenv("API_KEY"),
    private_apps_api_key_legacy=getenv("API_KEY"),
)
res = client.meetings.batch.update(inputs=[{"id": "1", "properties": {}}])
```

#### Asynchronous Client

```python
from hubspot_crm_py import AsyncClient
from os import getenv

client = AsyncClient(
    private_apps_api_key=getenv("API_KEY"),
    private_apps_api_key_legacy=getenv("API_KEY"),
)
res = await client.meetings.batch.update(inputs=[{"id": "1", "properties": {}}])
```

### Create or update a batch of meetings by unique property values <a name="upsert"></a>

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
res = client.meetings.batch.upsert(inputs=[{"id": "string", "properties": {}}])
```

#### Asynchronous Client

```python
from hubspot_crm_py import AsyncClient
from os import getenv

client = AsyncClient(
    private_apps_api_key=getenv("API_KEY"),
    private_apps_api_key_legacy=getenv("API_KEY"),
)
res = await client.meetings.batch.upsert(inputs=[{"id": "string", "properties": {}}])
```
