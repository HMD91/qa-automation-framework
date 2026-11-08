from framework.ui.login_page import LoginPage


def test_connexion_donnees_json(page, cas):
    login_page = LoginPage(page)

    login_page.ouvrir()

    login_page.se_connecter(
        cas["username"],
        cas["password"],
    )
    
    login_page.verifier_resultat(cas["resultat_attendu"])


    

    
