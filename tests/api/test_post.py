import allure
import pytest
import requests  # requests accéder à la classe d'exception requests.exceptions.Timeout

pytestmark = pytest.mark.api



@allure.epic("QA Automation Framework")
@allure.feature("API Testing")
@allure.story("Get Posts")
@allure.title("Récupérer la liste des articles")
@allure.description(
    "Vérifie que l'API retourne une liste d'articles "
    "et contrôle la présence, le type et la validité des champs."
)
@allure.severity(allure.severity_level.NORMAL)

def test_get_posts(api_client):
    response = api_client.get("/posts")

    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0
    assert isinstance(data[0], dict)
    for article in data:
        assert "id" in article
        assert isinstance(article["id"], int)
        for key in ["userId", "title", "body"]:
            assert key in article

        for key in ["title", "body"]:
            assert isinstance(article[key], str)
            assert len(article[key]) > 0



@allure.epic("QA Automation Framework")
@allure.feature("API Testing")
@allure.story("Create Post")
@allure.title("Créer un article via POST")
def test_get_second_post(api_client):
    response = api_client.get("/posts/2")

    data = response.json()

    assert response.status_code == 200
    assert data["userId"] == 1
    assert data["id"] == 2
    assert data["title"] != ""
    assert data["body"] != ""


@allure.epic("QA Automation Framework")
@allure.feature("API Testing")
@allure.story("Create Post")
@allure.title("Créer un article via POST")
@allure.description(
    "Vérifie la création d'un article via l'API "
    "et valide les données retournées dans la réponse JSON."
)
@allure.severity(allure.severity_level.CRITICAL)

def test_create_post(api_client):
    with allure.step("Préparer les données de l'article"):
        post_data = {"title": "Test API", "userId": 1, "published": True}

    with allure.step("Envoyer la requête POST et récupérer la réponse"):
        response = api_client.post("/posts", data=post_data)
        response_data = response.json()

    with allure.step("Vérifier le statut HTTP 201"):
        assert response.status_code == 201

    with allure.step("Vérifier la structure de la réponse"):
        assert isinstance(response_data, dict)
        for key in ["id", "title", "userId", "published"]:
            assert key in response_data

    with allure.step("Vérifier les types et les valeurs"):
        for key in ["id", "userId"]:
            assert isinstance(response_data[key], int)

        assert isinstance(response_data["title"], str)
        assert len(response_data["title"]) > 0
        assert isinstance(response_data["published"], bool)




@allure.epic("QA Automation Framework")
@allure.feature("API Testing")
@allure.story("Error Handling")
@allure.title("Vérifier la gestion d'une erreur 404")

def test_get_post_not_found(api_client):
    with pytest.raises(requests.exceptions.HTTPError) as exc_info:
        api_client.get("/posts/9999")

    assert exc_info.value.response.status_code == 404




@allure.epic("QA Automation Framework")
@allure.feature("API Testing")
@allure.story("Update Post")
@allure.title("Modifier un article avec PUT")

def test_update_post(api_client):
    post_data = {
        "id": 1,
        "title": "Titre modifié",
        "body": "Contenu modifié",
        "userId": 1,
    }

    response = api_client.put("/posts/1", data=post_data)
    response_data = response.json()
    assert response.status_code == 200

    assert response_data["title"] == post_data["title"]
    assert response_data["body"] == post_data["body"]
    assert response_data["userId"] == post_data["userId"]

    assert isinstance(response_data, dict)



@allure.epic("QA Automation Framework")
@allure.feature("API Testing")
@allure.story("Update Post")
@allure.title("Modifier partiellement un article avec PATCH")

def test_patch_post(api_client):
    post_data = {"title": "Nouveau titre"}

    response = api_client.patch("/posts/1", data=post_data)
    response_data = response.json()
    assert response.status_code == 200

    assert response_data["title"] == post_data["title"]

    assert isinstance(response_data, dict)



@allure.epic("QA Automation Framework")
@allure.feature("API Testing")
@allure.story("Delete Post")
@allure.title("Supprimer un article avec DELETE")
def test_delete_post(api_client):
    response = api_client.delete("/posts/1")
    data = response.json()

    assert response.status_code == 200
    assert data == {}
