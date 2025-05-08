
# Hubspot CRM Demo Python SDK

#### Synchronous Client

```python
from hubspot_crm_py import Client
from os import getenv

client = Client(
    private_apps_api_key=getenv("API_KEY"),
    private_apps_api_key_legacy=getenv("API_KEY"),
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
```

## Module Documentation and Snippets

### [contacts.crm.v3.objects.contacts](hubspot_crm_py/resources/contacts/crm/v3/objects/contacts/README.md)

* [create](hubspot_crm_py/resources/contacts/crm/v3/objects/contacts/README.md#create) - Create a contact
* [delete](hubspot_crm_py/resources/contacts/crm/v3/objects/contacts/README.md#delete) - Archive a contact
* [get](hubspot_crm_py/resources/contacts/crm/v3/objects/contacts/README.md#get) - Retrieve a contact
* [list](hubspot_crm_py/resources/contacts/crm/v3/objects/contacts/README.md#list) - Retrieve contacts
* [patch](hubspot_crm_py/resources/contacts/crm/v3/objects/contacts/README.md#patch) - Update a contact

### [contacts.crm.v3.objects.contacts.batch.archive](hubspot_crm_py/resources/contacts/crm/v3/objects/contacts/batch/archive/README.md)

* [create](hubspot_crm_py/resources/contacts/crm/v3/objects/contacts/batch/archive/README.md#create) - Archive a batch of contacts

### [contacts.crm.v3.objects.contacts.batch.create](hubspot_crm_py/resources/contacts/crm/v3/objects/contacts/batch/create/README.md)

* [create](hubspot_crm_py/resources/contacts/crm/v3/objects/contacts/batch/create/README.md#create) - Create a batch of contacts

### [contacts.crm.v3.objects.contacts.batch.read](hubspot_crm_py/resources/contacts/crm/v3/objects/contacts/batch/read/README.md)

* [create](hubspot_crm_py/resources/contacts/crm/v3/objects/contacts/batch/read/README.md#create) - Retrieve a batch of contacts

### [contacts.crm.v3.objects.contacts.batch.update](hubspot_crm_py/resources/contacts/crm/v3/objects/contacts/batch/update/README.md)

* [create](hubspot_crm_py/resources/contacts/crm/v3/objects/contacts/batch/update/README.md#create) - Update a batch of contacts

### [contacts.crm.v3.objects.contacts.batch.upsert](hubspot_crm_py/resources/contacts/crm/v3/objects/contacts/batch/upsert/README.md)

* [create](hubspot_crm_py/resources/contacts/crm/v3/objects/contacts/batch/upsert/README.md#create) - Create or update a batch of contacts

### [contacts.crm.v3.objects.contacts.gdpr_delete](hubspot_crm_py/resources/contacts/crm/v3/objects/contacts/gdpr_delete/README.md)

* [create](hubspot_crm_py/resources/contacts/crm/v3/objects/contacts/gdpr_delete/README.md#create) - Permanently delete a contact (GDPR-compliant)

### [contacts.crm.v3.objects.contacts.merge](hubspot_crm_py/resources/contacts/crm/v3/objects/contacts/merge/README.md)

* [create](hubspot_crm_py/resources/contacts/crm/v3/objects/contacts/merge/README.md#create) - Merge two contacts

### [contacts.crm.v3.objects.contacts.search](hubspot_crm_py/resources/contacts/crm/v3/objects/contacts/search/README.md)

* [create](hubspot_crm_py/resources/contacts/crm/v3/objects/contacts/search/README.md#create) - Search for contacts

### [meetings.crm.v3.objects.meetings](hubspot_crm_py/resources/meetings/crm/v3/objects/meetings/README.md)

* [create](hubspot_crm_py/resources/meetings/crm/v3/objects/meetings/README.md#create) - Create
* [delete](hubspot_crm_py/resources/meetings/crm/v3/objects/meetings/README.md#delete) - Archive
* [get](hubspot_crm_py/resources/meetings/crm/v3/objects/meetings/README.md#get) - Read
* [list](hubspot_crm_py/resources/meetings/crm/v3/objects/meetings/README.md#list) - List
* [patch](hubspot_crm_py/resources/meetings/crm/v3/objects/meetings/README.md#patch) - Update

### [meetings.crm.v3.objects.meetings.batch.archive](hubspot_crm_py/resources/meetings/crm/v3/objects/meetings/batch/archive/README.md)

* [create](hubspot_crm_py/resources/meetings/crm/v3/objects/meetings/batch/archive/README.md#create) - Archive a batch of meetings by ID

### [meetings.crm.v3.objects.meetings.batch.create](hubspot_crm_py/resources/meetings/crm/v3/objects/meetings/batch/create/README.md)

* [create](hubspot_crm_py/resources/meetings/crm/v3/objects/meetings/batch/create/README.md#create) - Create a batch of meetings

### [meetings.crm.v3.objects.meetings.batch.read](hubspot_crm_py/resources/meetings/crm/v3/objects/meetings/batch/read/README.md)

* [create](hubspot_crm_py/resources/meetings/crm/v3/objects/meetings/batch/read/README.md#create) - Read a batch of meetings by internal ID, or unique property values

### [meetings.crm.v3.objects.meetings.batch.update](hubspot_crm_py/resources/meetings/crm/v3/objects/meetings/batch/update/README.md)

* [create](hubspot_crm_py/resources/meetings/crm/v3/objects/meetings/batch/update/README.md#create) - Update a batch of meetings by internal ID, or unique property values

### [meetings.crm.v3.objects.meetings.batch.upsert](hubspot_crm_py/resources/meetings/crm/v3/objects/meetings/batch/upsert/README.md)

* [create](hubspot_crm_py/resources/meetings/crm/v3/objects/meetings/batch/upsert/README.md#create) - Create or update a batch of meetings by unique property values

### [meetings.crm.v3.objects.meetings.search](hubspot_crm_py/resources/meetings/crm/v3/objects/meetings/search/README.md)

* [create](hubspot_crm_py/resources/meetings/crm/v3/objects/meetings/search/README.md#create) - Search meetings

<!-- MODULE DOCS END -->
