import os
from datetime import datetime

import pytest
from dotenv import load_dotenv

from http_clients.gectaro_http_client import GectaroHttpClient


@pytest.fixture(scope="session")
def gectaro_client():
    load_dotenv()
    return GectaroHttpClient(
        base_url=os.getenv("BASE_URL", "https://api.gectaro.com"),
        token=os.getenv("TOKEN"),
        company_id=int(os.getenv("COMPANY_ID", "7323")),
        project_id=int(os.getenv("PROJECT_ID", "85998")),
    )


@pytest.fixture()
def create_resource(gectaro_client):
    data = {
        "name": "resource",
        "needed_at": int(datetime.now().timestamp()),
        "project_id": gectaro_client.project_id,
        "type": 1,
        "volume": 5,
    }
    response = gectaro_client.create_resource(data)
    resource_id = response.json()["id"]

    yield resource_id

    gectaro_client.delete_resource(resource_id)


@pytest.fixture()
def create_resource_requests(request, gectaro_client, create_resource):
    data = {
        "project_tasks_resource_id": create_resource,
        "volume": 5,
        "cost": 0,
        "needed_at": int(datetime.now().timestamp()),
        "is_over_budget": True,
    }
    ids = []
    for _ in range(request.param):
        response = gectaro_client.create_resource_request(data)
        resource_request_id = response.json()["id"]
        ids.append(resource_request_id)

    yield ids

    for id_ in ids:
        gectaro_client.delete_resource_request(id_)
