import allure
import pytest

from framework.ui.login_page import LoginPage

pytestmark = pytest.mark.ui

@allure.epic("QA Automation Framework")
@allure.feature("UI Testing")
@allure.story("Authentication")
@allure.title("Vérifier la connexion avec plusieurs jeux de données")
def test_connexion_donnees_json(page, cas):
    login_page = LoginPage(page)

    login_page.ouvrir()

    login_page.se_connecter(
        cas["username"],
        cas["password"],
    )
    
    login_page.verifier_resultat(cas["resultat_attendu"])


    

    
