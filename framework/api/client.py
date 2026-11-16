import requests


class APIClient:
    def __init__(self, base_url: str, timeout: int = 10) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def _build_url(self, endpoint: str) -> str:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        return url

    def _check_response(self, response: requests.Response) -> requests.Response:
        response.raise_for_status()
        return response

    def get(self, endpoint: str) -> requests.Response:
        url = self._build_url(endpoint)
        response = requests.get(url, timeout=self.timeout)
        return self._check_response(response)

    def post(self, endpoint: str, data: dict[str, object]) -> requests.Response:
        url = self._build_url(endpoint)
        response = requests.post(url, json=data, timeout=self.timeout)
        return self._check_response(response)

    def put(self, endpoint: str, data: dict[str, object]) -> requests.Response:
        url = self._build_url(endpoint)
        response = requests.put(url, json=data, timeout=self.timeout)
        return self._check_response(response)

    def patch(self, endpoint: str, data: dict[str, object]) -> requests.Response:
        url = self._build_url(endpoint)
        response = requests.patch(url, json=data, timeout=self.timeout)
        return self._check_response(response)

    def delete(self, endpoint: str) -> requests.Response:
        url = self._build_url(endpoint)
        response = requests.delete(url, timeout=self.timeout)
        return self._check_response(response)
