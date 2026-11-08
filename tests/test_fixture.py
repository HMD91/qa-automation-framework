from framework.ui.inventory_page import InventoryPage
from framework.ui.login_page import LoginPage


def test_connexion_donnees_json(page, cas):
    login_page = LoginPage(page)

    login_page.ouvrir()

    login_page.se_connecter(
        cas["username"],
        cas["password"],
    )
    
    if cas["resultat_attendu"] == "Products":
        inventory_page = InventoryPage(page)
        inventory_page.verifier_page_affichee()
    else:
        login_page.verifier_resultat(cas["resultat_attendu"])

    

    
