
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

### [contacts](hubspot_crm_py/resources/contacts/README.md)

* [create](hubspot_crm_py/resources/contacts/README.md#create) - Create a contact
* [delete](hubspot_crm_py/resources/contacts/README.md#delete) - Archive a contact
* [gdpr_delete](hubspot_crm_py/resources/contacts/README.md#gdpr_delete) - Permanently delete a contact (GDPR-compliant)
* [get](hubspot_crm_py/resources/contacts/README.md#get) - Retrieve a contact
* [list](hubspot_crm_py/resources/contacts/README.md#list) - Retrieve contacts
* [merge](hubspot_crm_py/resources/contacts/README.md#merge) - Merge two contacts
* [patch](hubspot_crm_py/resources/contacts/README.md#patch) - Update a contact
* [search](hubspot_crm_py/resources/contacts/README.md#search) - Search for contacts

### [contacts.batch](hubspot_crm_py/resources/contacts/batch/README.md)

* [archive](hubspot_crm_py/resources/contacts/batch/README.md#archive) - Archive a batch of contacts
* [create](hubspot_crm_py/resources/contacts/batch/README.md#create) - Create a batch of contacts
* [read](hubspot_crm_py/resources/contacts/batch/README.md#read) - Retrieve a batch of contacts
* [update](hubspot_crm_py/resources/contacts/batch/README.md#update) - Update a batch of contacts
* [upsert](hubspot_crm_py/resources/contacts/batch/README.md#upsert) - Create or update a batch of contacts

### [meetings](hubspot_crm_py/resources/meetings/README.md)

* [create](hubspot_crm_py/resources/meetings/README.md#create) - Create
* [delete](hubspot_crm_py/resources/meetings/README.md#delete) - Archive
* [get](hubspot_crm_py/resources/meetings/README.md#get) - Read
* [list](hubspot_crm_py/resources/meetings/README.md#list) - List
* [patch](hubspot_crm_py/resources/meetings/README.md#patch) - Update
* [search](hubspot_crm_py/resources/meetings/README.md#search) - Search meetings

### [meetings.batch](hubspot_crm_py/resources/meetings/batch/README.md)

* [archive](hubspot_crm_py/resources/meetings/batch/README.md#archive) - Archive a batch of meetings by ID
* [create](hubspot_crm_py/resources/meetings/batch/README.md#create) - Create a batch of meetings
* [read](hubspot_crm_py/resources/meetings/batch/README.md#read) - Read a batch of meetings by internal ID, or unique property values
* [update](hubspot_crm_py/resources/meetings/batch/README.md#update) - Update a batch of meetings by internal ID, or unique property values
* [upsert](hubspot_crm_py/resources/meetings/batch/README.md#upsert) - Create or update a batch of meetings by unique property values

<!-- MODULE DOCS END -->
