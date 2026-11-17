import allure
import pytest

pytestmark = pytest.mark.api


@allure.epic("QA Automation Framework")
@allure.feature("API Testing")
@allure.story("API Client")
@allure.title("Construire une URL API")

def test_build_url(api_client):
    url = api_client._build_url("/posts/1")

    assert url == "https://jsonplaceholder.typicode.com/posts/1"
