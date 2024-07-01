from datetime import datetime

import pytest

from models.gectaro_models import ListResourceRequest, ResourceRequest


@pytest.mark.parametrize(
    "volume, cost, is_over_budget",
    [
        pytest.param(5, 0, True),
        pytest.param(2, 4, False),
    ],
)
def test_create_resource_request_positive(
    gectaro_client,
    create_resource,
    volume,
    cost,
    is_over_budget,
):
    data = {
        "project_tasks_resource_id": create_resource,
        "volume": volume,
        "cost": cost,
        "needed_at": int(datetime.now().timestamp()),
        "is_over_budget": is_over_budget,
    }
    response = gectaro_client.create_resource_request(data)
    body = response.json()

    assert response.status_code == 201
    ResourceRequest(**body)
    assert body["volume"] == volume
    assert body["cost"] == cost
    assert body["is_over_budget"] == is_over_budget


@pytest.mark.parametrize(
    "volume, cost",
    [
        pytest.param("qwe", 0),
        pytest.param(2, "qwe"),
    ],
)
def test_create_resource_request_negative(
    gectaro_client,
    create_resource,
    volume,
    cost,
):
    data = {
        "project_tasks_resource_id": create_resource,
        "volume": volume,
        "cost": cost,
        "needed_at": int(datetime.now().timestamp()),
        "is_over_budget": True,
    }
    response = gectaro_client.create_resource_request(data)

    assert response.status_code == 422


@pytest.mark.parametrize("create_resource_requests", [3], indirect=True)
def test_list_resource_requests(
    gectaro_client,
    create_resource_requests,
):
    response = gectaro_client.list_resource_requests()
    body = response.json()

    assert response.status_code == 200
    ListResourceRequest(resource_requests=body)


@pytest.mark.parametrize("create_resource_requests", [1], indirect=True)
def test_retrieve_resource_request_positive(
    gectaro_client,
    create_resource_requests,
):
    response = gectaro_client.retrieve_resource_request(create_resource_requests[0])
    body = response.json()

    assert response.status_code == 200
    ResourceRequest(**body)


@pytest.mark.parametrize("create_resource_requests", [1], indirect=True)
def test_retrieve_resource_request_negative(
    gectaro_client,
    create_resource_requests,
):
    gectaro_client.delete_resource_request(create_resource_requests[0])
    response = gectaro_client.retrieve_resource_request(create_resource_requests[0])

    assert response.status_code == 404


@pytest.mark.parametrize("create_resource_requests", [1], indirect=True)
@pytest.mark.parametrize(
    "volume, cost",
    [
        pytest.param(8, 3),
        pytest.param(10, 5),
    ],
)
def test_update_resource_request_positive(
    gectaro_client,
    create_resource_requests,
    volume,
    cost,
):
    data = {
        "volume": volume,
        "cost": cost,
    }
    response = gectaro_client.update_resource_request(
        create_resource_requests[0],
        data,
    )
    body = response.json()

    assert response.status_code == 200
    ResourceRequest(**body)
    assert body["volume"] == volume
    assert body["cost"] == cost


@pytest.mark.parametrize("create_resource_requests", [1], indirect=True)
@pytest.mark.parametrize(
    "volume, cost",
    [
        pytest.param("qwe", 3),
        pytest.param(10, "qwe"),
    ],
)
def test_update_resource_request_negative(
    gectaro_client,
    create_resource_requests,
    volume,
    cost,
):
    data = {
        "volume": volume,
        "cost": cost,
    }
    response = gectaro_client.update_resource_request(
        create_resource_requests[0],
        data,
    )

    assert response.status_code == 422


@pytest.mark.parametrize("create_resource_requests", [1], indirect=True)
def test_delete_resource_request_positive(
    gectaro_client,
    create_resource_requests,
):
    response = gectaro_client.delete_resource_request(create_resource_requests[0])

    assert response.status_code == 204


@pytest.mark.parametrize("create_resource_requests", [1], indirect=True)
def test_delete_resource_request_negative(
    gectaro_client,
    create_resource_requests,
):
    gectaro_client.delete_resource_request(create_resource_requests[0])
    response = gectaro_client.delete_resource_request(create_resource_requests[0])

    assert response.status_code == 404


@pytest.mark.parametrize("create_resource_requests", [3], indirect=True)
def test_list_resource_requests_by_company(
    gectaro_client,
    create_resource_requests,
):
    response = gectaro_client.list_resource_requests_by_company()
    body = response.json()

    assert response.status_code == 200
    ListResourceRequest(resource_requests=body)
