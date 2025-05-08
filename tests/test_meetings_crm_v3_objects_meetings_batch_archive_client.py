import pytest

from hubspot_crm_py import AsyncClient, Client
from hubspot_crm_py.environment import SIDEKO_MOCK_SERVER


def test_create_204_success_default():
    """Tests a POST request to the /crm/v3/objects/meetings/batch/archive endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 204
    Mode: Synchronous execution

    Empty response expected

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
    response = client.meetings.crm.v3.objects.meetings.batch.archive.create(
        inputs=[{"id": "string"}]
    )
    assert response is None


@pytest.mark.asyncio
async def test_await_create_204_success_default():
    """Tests a POST request to the /crm/v3/objects/meetings/batch/archive endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 204
    Mode: Asynchronous execution

    Empty response expected

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
    response = await client.meetings.crm.v3.objects.meetings.batch.archive.create(
        inputs=[{"id": "string"}]
    )
    assert response is None
