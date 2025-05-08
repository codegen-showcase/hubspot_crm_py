import pydantic
import pytest

from hubspot_crm_py import AsyncClient, Client
from hubspot_crm_py.environment import SIDEKO_MOCK_SERVER
from hubspot_crm_py.types import models


def test_upsert_200_success_default():
    """Tests a POST request to the /crm/v3/objects/meetings/batch/upsert endpoint.

    Operation: upsert
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.BatchResponseSimplePublicUpsertObject

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
    response = client.meetings.batch.upsert(inputs=[{"id": "string", "properties": {}}])
    try:
        pydantic.TypeAdapter(
            models.BatchResponseSimplePublicUpsertObject
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_upsert_200_success_default():
    """Tests a POST request to the /crm/v3/objects/meetings/batch/upsert endpoint.

    Operation: upsert
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.BatchResponseSimplePublicUpsertObject

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
    response = await client.meetings.batch.upsert(
        inputs=[{"id": "string", "properties": {}}]
    )
    try:
        pydantic.TypeAdapter(
            models.BatchResponseSimplePublicUpsertObject
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_update_200_success_default():
    """Tests a POST request to the /crm/v3/objects/meetings/batch/update endpoint.

    Operation: update
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
    response = client.meetings.batch.update(inputs=[{"id": "1", "properties": {}}])
    try:
        pydantic.TypeAdapter(models.BatchResponseSimplePublicObject).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_200_success_default():
    """Tests a POST request to the /crm/v3/objects/meetings/batch/update endpoint.

    Operation: update
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
    response = await client.meetings.batch.update(
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


def test_read_200_success_default():
    """Tests a POST request to the /crm/v3/objects/meetings/batch/read endpoint.

    Operation: read
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
    response = client.meetings.batch.read(
        inputs=[{"id": "string"}],
        properties=["string"],
        properties_with_history=["string"],
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
async def test_await_read_200_success_default():
    """Tests a POST request to the /crm/v3/objects/meetings/batch/read endpoint.

    Operation: read
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
    response = await client.meetings.batch.read(
        inputs=[{"id": "string"}],
        properties=["string"],
        properties_with_history=["string"],
    )
    try:
        pydantic.TypeAdapter(models.BatchResponseSimplePublicObject).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_create_201_success_default():
    """Tests a POST request to the /crm/v3/objects/meetings/batch/create endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 201
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
    response = client.meetings.batch.create(inputs=[{"properties": {}}])
    try:
        pydantic.TypeAdapter(models.BatchResponseSimplePublicObject).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_201_success_default():
    """Tests a POST request to the /crm/v3/objects/meetings/batch/create endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 201
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
    response = await client.meetings.batch.create(inputs=[{"properties": {}}])
    try:
        pydantic.TypeAdapter(models.BatchResponseSimplePublicObject).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_archive_204_success_default():
    """Tests a POST request to the /crm/v3/objects/meetings/batch/archive endpoint.

    Operation: archive
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
    response = client.meetings.batch.archive(inputs=[{"id": "string"}])
    assert response is None


@pytest.mark.asyncio
async def test_await_archive_204_success_default():
    """Tests a POST request to the /crm/v3/objects/meetings/batch/archive endpoint.

    Operation: archive
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
    response = await client.meetings.batch.archive(inputs=[{"id": "string"}])
    assert response is None
