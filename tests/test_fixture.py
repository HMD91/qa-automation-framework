from playwright.sync_api import expect


def test_connexion_donnees_json(page, cas):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill(cas["username"])
    page.get_by_placeholder("Password").fill(cas["password"])

    page.get_by_role("button", name="Login").click()

    expect(page.get_by_text(cas["resultat_attendu"])).to_be_visible()
    

    