import pydantic
import pytest

from hubspot_crm_py import AsyncClient, Client
from hubspot_crm_py.environment import SIDEKO_MOCK_SERVER
from hubspot_crm_py.types import models


def test_create_201_success_default():
    """Tests a POST request to the /crm/v3/objects/meetings endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.SimplePublicObject

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
    response = client.meetings.crm.v3.objects.meetings.create(
        properties={},
        associations=[
            {
                "to": {"id": "101"},
                "types": [
                    {
                        "association_category": "HUBSPOT_DEFINED",
                        "association_type_id": 2,
                    }
                ],
            }
        ],
    )
    try:
        pydantic.TypeAdapter(models.SimplePublicObject).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_201_success_default():
    """Tests a POST request to the /crm/v3/objects/meetings endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.SimplePublicObject

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
    response = await client.meetings.crm.v3.objects.meetings.create(
        properties={},
        associations=[
            {
                "to": {"id": "101"},
                "types": [
                    {
                        "association_category": "HUBSPOT_DEFINED",
                        "association_type_id": 2,
                    }
                ],
            }
        ],
    )
    try:
        pydantic.TypeAdapter(models.SimplePublicObject).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_patch_200_success_default():
    """Tests a PATCH request to the /crm/v3/objects/meetings/{meetingId} endpoint.

    Operation: patch
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.SimplePublicObject

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
    response = client.meetings.crm.v3.objects.meetings.patch(
        meeting_id="string", properties={}
    )
    try:
        pydantic.TypeAdapter(models.SimplePublicObject).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_patch_200_success_default():
    """Tests a PATCH request to the /crm/v3/objects/meetings/{meetingId} endpoint.

    Operation: patch
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.SimplePublicObject

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
    response = await client.meetings.crm.v3.objects.meetings.patch(
        meeting_id="string", properties={}
    )
    try:
        pydantic.TypeAdapter(models.SimplePublicObject).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_get_200_generated_success():
    """Tests a GET request to the /crm/v3/objects/meetings/{meetingId} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.SimplePublicObjectWithAssociations

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
    response = client.meetings.crm.v3.objects.meetings.get(meeting_id="string")
    try:
        pydantic.TypeAdapter(models.SimplePublicObjectWithAssociations).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Tests a GET request to the /crm/v3/objects/meetings/{meetingId} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.SimplePublicObjectWithAssociations

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
    response = await client.meetings.crm.v3.objects.meetings.get(meeting_id="string")
    try:
        pydantic.TypeAdapter(models.SimplePublicObjectWithAssociations).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_list_200_generated_success():
    """Tests a GET request to the /crm/v3/objects/meetings endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.CollectionResponseSimplePublicObjectWithAssociationsForwardPaging

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
    response = client.meetings.crm.v3.objects.meetings.list()
    try:
        pydantic.TypeAdapter(
            models.CollectionResponseSimplePublicObjectWithAssociationsForwardPaging
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Tests a GET request to the /crm/v3/objects/meetings endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.CollectionResponseSimplePublicObjectWithAssociationsForwardPaging

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
    response = await client.meetings.crm.v3.objects.meetings.list()
    try:
        pydantic.TypeAdapter(
            models.CollectionResponseSimplePublicObjectWithAssociationsForwardPaging
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_delete_204_generated_success():
    """Tests a DELETE request to the /crm/v3/objects/meetings/{meetingId} endpoint.

    Operation: delete
    Test Case ID: generated_success
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
    response = client.meetings.crm.v3.objects.meetings.delete(meeting_id="string")
    assert response is None


@pytest.mark.asyncio
async def test_await_delete_204_generated_success():
    """Tests a DELETE request to the /crm/v3/objects/meetings/{meetingId} endpoint.

    Operation: delete
    Test Case ID: generated_success
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
    response = await client.meetings.crm.v3.objects.meetings.delete(meeting_id="string")
    assert response is None
