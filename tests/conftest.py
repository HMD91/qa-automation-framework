import base64
import json
import logging
from pathlib import Path

import pytest
import pytest_html

from framework.ui.inventory_page import InventoryPage
from framework.ui.login_page import LoginPage

# Configuration du système de logs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("reports/logs/execution.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger(__name__)
# Clé permettant de conserver les logs entre les phases d'un test
logs_key = pytest.StashKey[list[str]]()

@pytest.fixture(scope="session")
def navigateur_reel():
    from playwright.sync_api import sync_playwright

    with sync_playwright() as playwright:
        logger.info("Démarrage du navigateur Chromium")

        navigateur = playwright.chromium.launch(headless=True)

        yield navigateur

        logger.info("Fermeture du navigateur Chromium")
        navigateur.close()
    
    

@pytest.fixture
def page(navigateur_reel):
    page = navigateur_reel.new_page()
    logger.info("Création d'une nouvelle page")
    
    try:  # exécute le test.
        yield page
        
    finally:  # s'assure que la page est fermée après le test,
        logger.info("Fermeture de la page")
        page.close()


def pytest_generate_tests(metafunc):
    if "cas" in metafunc.fixturenames:

        chemin_fichier = (
            Path(__file__).parent.parent
            / "test_data"
            / "users"
            / "login_cases.json"
        )

        with open(chemin_fichier, encoding="utf-8") as fichier:
            donnees = json.load(fichier)

        metafunc.parametrize(
            "cas",
            donnees,
            ids=[cas["id"] for cas in donnees]
        )
        


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rapport = outcome.get_result()

    # Initialisation du stockage des logs
    if logs_key not in item.stash:
        item.stash[logs_key] = []

    # Récupération des logs de chaque phase
    if rapport.caplog:
        item.stash[logs_key].append(
            f"--- {rapport.when.upper()} ---\n{rapport.caplog}"
        )

    # Ajout des logs complets au rapport HTML
    if rapport.when == "teardown":
        logs_complets = "\n\n".join(item.stash[logs_key])

        extras = getattr(rapport, "extras", [])
        extras.append(
            pytest_html.extras.text(
                logs_complets,
                name="Logs complets du test",
            )
        )
        rapport.extras = extras

    # Capture d'écran en cas d'échec
    if rapport.when == "call" and rapport.failed:
        page = item.funcargs.get("page")

        if page:
            chemin_capture = (
                Path("reports/screenshots") / f"{item.name}.png"
            )

            page.screenshot(path=str(chemin_capture))

            with open(chemin_capture, "rb") as fichier:
                image_base64 = base64.b64encode(
                    fichier.read()
                ).decode("utf-8")

            extras = getattr(rapport, "extras", [])

            extras.append(
                pytest_html.extras.html(
                    f"""
                    <div>
                        <h4>Capture d'écran de l'échec</h4>
                        <img
                            src="data:image/png;base64,{image_base64}"
                            alt="Capture d'écran du test échoué"
                            style="max-width: 100%; height: auto;"
                        >
                    </div>
                    """
                )
            )

            rapport.extras = extras

            print(f"\nCapture enregistrée : {chemin_capture}")
            
            

def pytest_runtest_call(item):
    logger.info("Exécution du test : %s", item.name)       


@pytest.fixture()
def utilisateur_connecte(page):
    login_page = LoginPage(page)
    
    login_page.ouvrir()
    login_page.se_connecter(
        "standard_user", "secret_sauce"
        )
    
    inventory_page = InventoryPage(page)
    inventory_page.verifier_page_affichee()
    return inventory_page