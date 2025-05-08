
### Archive <a name="delete"></a>

Move an Object identified by `{meetingId}` to the recycling bin.

**API Endpoint**: `DELETE /crm/v3/objects/meetings/{meetingId}`

#### Synchronous Client

```python
from hubspot_crm_py import Client
from os import getenv

client = Client(
    private_apps_api_key=getenv("API_KEY"),
    private_apps_api_key_legacy=getenv("API_KEY"),
)
res = client.meetings.delete(meeting_id="string")
```

#### Asynchronous Client

```python
from hubspot_crm_py import AsyncClient
from os import getenv

client = AsyncClient(
    private_apps_api_key=getenv("API_KEY"),
    private_apps_api_key_legacy=getenv("API_KEY"),
)
res = await client.meetings.delete(meeting_id="string")
```

### List <a name="list"></a>

Read a page of meetings. Control what is returned via the `properties` query param.

**API Endpoint**: `GET /crm/v3/objects/meetings`

#### Synchronous Client

```python
from hubspot_crm_py import Client
from os import getenv

client = Client(
    private_apps_api_key=getenv("API_KEY"),
    private_apps_api_key_legacy=getenv("API_KEY"),
)
res = client.meetings.list()
```

#### Asynchronous Client

```python
from hubspot_crm_py import AsyncClient
from os import getenv

client = AsyncClient(
    private_apps_api_key=getenv("API_KEY"),
    private_apps_api_key_legacy=getenv("API_KEY"),
)
res = await client.meetings.list()
```

### Read <a name="get"></a>

Read an Object identified by `{meetingId}`. `{meetingId}` refers to the internal object ID by default, or optionally any unique property value as specified by the `idProperty` query param.  Control what is returned via the `properties` query param.

**API Endpoint**: `GET /crm/v3/objects/meetings/{meetingId}`

#### Synchronous Client

```python
from hubspot_crm_py import Client
from os import getenv

client = Client(
    private_apps_api_key=getenv("API_KEY"),
    private_apps_api_key_legacy=getenv("API_KEY"),
)
res = client.meetings.get(meeting_id="string")
```

#### Asynchronous Client

```python
from hubspot_crm_py import AsyncClient
from os import getenv

client = AsyncClient(
    private_apps_api_key=getenv("API_KEY"),
    private_apps_api_key_legacy=getenv("API_KEY"),
)
res = await client.meetings.get(meeting_id="string")
```

### Update <a name="patch"></a>

Perform a partial update of an Object identified by `{meetingId}`or optionally a unique property value as specified by the `idProperty` query param. `{meetingId}` refers to the internal object ID by default, and the `idProperty` query param refers to a property whose values are unique for the object. Provided property values will be overwritten. Read-only and non-existent properties will result in an error. Properties values can be cleared by passing an empty string.

**API Endpoint**: `PATCH /crm/v3/objects/meetings/{meetingId}`

#### Synchronous Client

```python
from hubspot_crm_py import Client
from os import getenv

client = Client(
    private_apps_api_key=getenv("API_KEY"),
    private_apps_api_key_legacy=getenv("API_KEY"),
)
res = client.meetings.patch(meeting_id="string", properties={})
```

#### Asynchronous Client

```python
from hubspot_crm_py import AsyncClient
from os import getenv

client = AsyncClient(
    private_apps_api_key=getenv("API_KEY"),
    private_apps_api_key_legacy=getenv("API_KEY"),
)
res = await client.meetings.patch(meeting_id="string", properties={})
```

### Create <a name="create"></a>

Create a meeting with the given properties and return a copy of the object, including the ID. Documentation and examples for creating standard meetings is provided.

**API Endpoint**: `POST /crm/v3/objects/meetings`

#### Synchronous Client

```python
from hubspot_crm_py import Client
from os import getenv

client = Client(
    private_apps_api_key=getenv("API_KEY"),
    private_apps_api_key_legacy=getenv("API_KEY"),
)
res = client.meetings.create(
    properties={},
    associations=[
        {
            "to": {"id": "101"},
            "types": [
                {"association_category": "HUBSPOT_DEFINED", "association_type_id": 2}
            ],
        }
    ],
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
res = await client.meetings.create(
    properties={},
    associations=[
        {
            "to": {"id": "101"},
            "types": [
                {"association_category": "HUBSPOT_DEFINED", "association_type_id": 2}
            ],
        }
    ],
)
```

### Search meetings <a name="search"></a>



**API Endpoint**: `POST /crm/v3/objects/meetings/search`

#### Synchronous Client

```python
from hubspot_crm_py import Client
from os import getenv

client = Client(
    private_apps_api_key=getenv("API_KEY"),
    private_apps_api_key_legacy=getenv("API_KEY"),
)
res = client.meetings.search()
```

#### Asynchronous Client

```python
from hubspot_crm_py import AsyncClient
from os import getenv

client = AsyncClient(
    private_apps_api_key=getenv("API_KEY"),
    private_apps_api_key_legacy=getenv("API_KEY"),
)
res = await client.meetings.search()
```
