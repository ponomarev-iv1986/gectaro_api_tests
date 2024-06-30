from typing import Any

import requests
from requests import Response


class GectaroHttpClient:
    def __init__(
        self, base_url: str, token: str, company_id: int, project_id: int
    ) -> None:
        self.session = requests.Session()
        self.session.headers["Authorization"] = f"Bearer {token}"
        self.base_url = base_url
        self.company_id = company_id
        self.project_id = project_id

    def create_resource(self, data: dict[str, Any]) -> Response:
        return self.session.post(
            f"{self.base_url}/v1/projects/{self.project_id}/resources",
            json=data,
        )

    def delete_resource(self, resource_id: int) -> Response:
        return self.session.delete(
            f"{self.base_url}/v1/projects/{self.project_id}/resources/{resource_id}",
        )

    def list_resource_requests(self) -> Response:
        return self.session.get(
            f"{self.base_url}/v1/projects/{self.project_id}/resource-requests",
        )

    def create_resource_request(self, data: dict[str, Any]) -> Response:
        return self.session.post(
            f"{self.base_url}/v1/projects/{self.project_id}/resource-requests",
            json=data,
        )

    def retrieve_resource_request(self, resource_request_id: int) -> Response:
        return self.session.get(
            f"{self.base_url}/v1/projects/{self.project_id}"
            f"/resource-requests/{resource_request_id}"
        )

    def update_resource_request(
        self, resource_request_id: int, data: dict[str, Any]
    ) -> Response:
        return self.session.put(
            f"{self.base_url}/v1/projects/{self.project_id}"
            f"/resource-requests/{resource_request_id}",
            json=data,
        )

    def delete_resource_request(self, resource_request_id: int) -> Response:
        return self.session.delete(
            f"{self.base_url}/v1/projects/{self.project_id}"
            f"/resource-requests/{resource_request_id}"
        )

    def list_resource_requests_by_company(self) -> Response:
        return self.session.get(
            f"{self.base_url}/v1/companies/{self.company_id}/resource-requests",
        )
