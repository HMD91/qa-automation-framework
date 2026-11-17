from unittest.mock import patch

import allure
import pytest
import requests

from framework.api.client import APIClient
from framework.config import API_BASE_URL

pytestmark = pytest.mark.api



@allure.epic("QA Automation Framework")
@allure.feature("API Testing")
@allure.story("Network Errors")
@allure.title("Gérer les erreurs réseau sur les méthodes HTTP")
@pytest.mark.parametrize(
    "methode, endpoint, data, exception",
    [
        ("GET", "/posts", None, requests.exceptions.ConnectionError),
        ("GET", "/posts", None, requests.exceptions.Timeout),
        (
            "POST",
            "/posts",
            {"title": "Test", "body": "Contenu", "userId": 1},
            requests.exceptions.ConnectionError,
        ),
        (
            "POST",
            "/posts",
            {"title": "Test", "body": "Contenu", "userId": 1},
            requests.exceptions.Timeout,
        ),
        (
            "PUT",
            "/posts/1",
            {"id": 1, "title": "Titre modifié", "body": "Contenu modifié", "userId": 1},
            requests.exceptions.ConnectionError,
        ),
        (
            "PUT",
            "/posts/1",
            {"id": 1, "title": "Titre modifié", "body": "Contenu modifié", "userId": 1},
            requests.exceptions.Timeout,
        ),
        (
            "PATCH",
            "/posts/1",
            {"title": "Nouveau titre"},
            requests.exceptions.ConnectionError,
        ),
        (
            "PATCH",
            "/posts/1",
            {"title": "Nouveau titre"},
            requests.exceptions.Timeout,
        ),
        ("DELETE", "/posts/1", None, requests.exceptions.ConnectionError),
        ("DELETE", "/posts/1", None, requests.exceptions.Timeout),
    ],
)


@allure.epic("QA Automation Framework")
@allure.feature("API Testing")
@allure.story("Network Errors")
@allure.title("Gérer les erreurs réseau")

def test_network_error(
    api_client, methode, endpoint, data, exception
):  # test_network_error = test_connection_error et test_network_error
    with patch(f"requests.{methode.lower()}") as mock_request:
        mock_request.side_effect = exception

        with pytest.raises(exception):
            if data is None:
                getattr(api_client, methode.lower())(endpoint)
            else:
                getattr(api_client, methode.lower())(endpoint, data)

        if data is None:
            mock_request.assert_called_once_with(
                f"{api_client.base_url}{endpoint}",
                timeout=10,
            )
        else:
            mock_request.assert_called_once_with(
                f"{api_client.base_url}{endpoint}",
                json=data,
                timeout=10,
            )


@allure.epic("QA Automation Framework")
@allure.feature("API Testing")
@allure.story("Timeout")
@allure.title("Appliquer un délai d'attente personnalisé")

def test_get_custom_timeout():
    client = APIClient(API_BASE_URL, timeout=20)

    with patch("requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.Timeout

        with pytest.raises(requests.exceptions.Timeout):
            client.get("/posts/1")

        mock_get.assert_called_once_with(f"{client.base_url}/posts/1", timeout=20)



@allure.epic("QA Automation Framework")
@allure.feature("API Testing")
@allure.story("Server Errors")
@allure.title("Gérer une erreur serveur GET")


def test_get_server_error(api_client):
    with patch(
        "requests.get"
    ) as mock_get:  # patch() remplace temporairement requests.get
        response = (
            requests.Response()
        )  # requests.Response() crée une réponse HTTP artificielle
        response.status_code = 500  # simule une erreur serveur
        mock_get.return_value = (
            response  # return_value: configure la réponse retournée par le mock
        )

        with pytest.raises(
            requests.exceptions.HTTPError
        ):  # pytest.raises() vérifie que api_client.get() déclenche bien une HTTPError.
            api_client.get("/posts/1")


@allure.epic("QA Automation Framework")
@allure.feature("API Testing")
@allure.story("Server Errors")
@allure.title("Gérer une erreur serveur POST")


def test_post_server_error(api_client):
    with patch("requests.post") as mock_post:
        response = requests.Response()
        response.status_code = 500
        mock_post.return_value = response

        post_data = {"title": "Test", "body": "Contenu", "userId": 1}

        with pytest.raises(requests.exceptions.HTTPError):
            api_client.post("/posts", post_data)



@allure.epic("QA Automation Framework")
@allure.feature("API Testing")
@allure.story("Server Errors")
@allure.title("Gérer une erreur serveur PUT")

def test_put_server_error(api_client):
    with patch("requests.put") as mock_put:
        response = requests.Response()
        response.status_code = 500
        mock_put.return_value = response

        put_data = {
            "id": 1,
            "title": "Titre modifié",
            "body": "Contenu modifié",
            "userId": 1,
        }

        with pytest.raises(requests.exceptions.HTTPError):
            api_client.put("/posts/1", put_data)



@allure.epic("QA Automation Framework")
@allure.feature("API Testing")
@allure.story("Server Errors")
@allure.title("Gérer une erreur serveur PATCH")


def test_patch_server_error(api_client):
    with patch("requests.patch") as mock_patch:
        response = requests.Response()
        response.status_code = 500
        mock_patch.return_value = response

        patch_data = {"title": "Nouveau titre"}

        with pytest.raises(requests.exceptions.HTTPError):
            api_client.patch("/posts/1", patch_data)


@allure.epic("QA Automation Framework")
@allure.feature("API Testing")
@allure.story("Server Errors")
@allure.title("Gérer une erreur serveur DELETE")

def test_delete_server_error(api_client):
    with patch("requests.delete") as mock_delete:
        response = requests.Response()
        response.status_code = 500
        mock_delete.return_value = response

        with pytest.raises(requests.exceptions.HTTPError):
            api_client.delete("/posts/1")


@allure.epic("QA Automation Framework")
@allure.feature("API Testing")
@allure.story("HTTP Requests")
@allure.title("Vérifier les données envoyées avec GET")

def test_get_sends_correct_data(api_client):
    with patch("requests.get") as mock_get:
        response = requests.Response()
        response.status_code = 200

        mock_get.return_value = response

        api_client.get("/posts/1")
        mock_get.assert_called_once_with(f"{api_client.base_url}/posts/1", timeout=10)


@allure.epic("QA Automation Framework")
@allure.feature("API Testing")
@allure.story("HTTP Requests")
@allure.title("Vérifier les données envoyées avec POST")

def test_post_sends_correct_data(api_client):
    with patch("requests.post") as mock_post:
        response = requests.Response()
        response.status_code = 200
        mock_post.return_value = response

        post_data = {"title": "Test", "body": "Contenu", "userId": 1}
        api_client.post("/posts", post_data)
        mock_post.assert_called_once_with(
            f"{api_client.base_url}/posts", json=post_data, timeout=10
        )
        
        
        
        
@allure.epic("QA Automation Framework")
@allure.feature("API Testing")
@allure.story("HTTP Requests")
@allure.title("Vérifier les données envoyées avec PUT")

def test_put_sends_correct_data(api_client):
    with patch("requests.put") as mock_put:
        response = requests.Response()
        response.status_code = 200
        mock_put.return_value = response

        put_data = {
            "id": 1,
            "title": "Titre modifié",
            "body": "Contenu modifié",
            "userId": 1,
        }

        api_client.put("/posts/1", put_data)
        mock_put.assert_called_once_with(
            f"{api_client.base_url}/posts/1", json=put_data, timeout=10
        )
        
        
        
@allure.epic("QA Automation Framework")
@allure.feature("API Testing")
@allure.story("HTTP Requests")
@allure.title("Vérifier les données envoyées avec PATCH")

def test_patch_sends_correct_data(api_client):
    with patch("requests.patch") as mock_patch:
        response = requests.Response()
        response.status_code = 200
        mock_patch.return_value = response

        patch_data = {"title": "Nouveau titre"}

        api_client.patch("/posts/1", patch_data)
        mock_patch.assert_called_once_with(
            f"{api_client.base_url}/posts/1", json=patch_data, timeout=10
        )
        
        
@allure.epic("QA Automation Framework")
@allure.feature("API Testing")
@allure.story("HTTP Requests")
@allure.title("Vérifier les données envoyées avec DELETE")

def test_delete_data(api_client):
    with patch("requests.delete") as mock_delete:
        response = requests.Response()
        response.status_code = 200

        mock_delete.return_value = response

        api_client.delete("/posts/1")
        mock_delete.assert_called_once_with(
            f"{api_client.base_url}/posts/1", timeout=10
        )
