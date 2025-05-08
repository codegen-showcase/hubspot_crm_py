import pydantic
import pytest

from hubspot_crm_py import AsyncClient, Client
from hubspot_crm_py.environment import SIDEKO_MOCK_SERVER
from hubspot_crm_py.types import models


def test_create_200_success_default():
    """Tests a POST request to the /crm/v3/objects/contacts/batch/update endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.BatchResponseSimplePublicObject

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(
        private_apps_api_key="API_KEY",
        private_apps_api_key_legacy="API_KEY",
        environment=SIDEKO_MOCK_SERVER,
    )
    response = client.contacts.crm.v3.objects.contacts.batch.update.create(
        inputs=[{"id": "1", "properties": {}}]
    )
    try:
        pydantic.TypeAdapter(models.BatchResponseSimplePublicObject).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_default():
    """Tests a POST request to the /crm/v3/objects/contacts/batch/update endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.BatchResponseSimplePublicObject

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(
        private_apps_api_key="API_KEY",
        private_apps_api_key_legacy="API_KEY",
        environment=SIDEKO_MOCK_SERVER,
    )
    response = await client.contacts.crm.v3.objects.contacts.batch.update.create(
        inputs=[{"id": "1", "properties": {}}]
    )
    try:
        pydantic.TypeAdapter(models.BatchResponseSimplePublicObject).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
