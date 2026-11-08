from playwright.sync_api import expect


class LoginPage:

    def __init__(self, page):
        self.page = page
        self.champ_username = page.get_by_placeholder("Username")
        self.champ_password = page.get_by_placeholder("Password")
        self.bouton_login = page.get_by_role("button", name="Login")

    def ouvrir(self):
        self.page.goto("https://www.saucedemo.com/")

    def se_connecter(self, username, password):
        self.champ_username.fill(username)
        self.champ_password.fill(password)
        self.bouton_login.click()

    def verifier_resultat(self, resultat_attendu):
        expect(
            self.page.get_by_text(resultat_attendu)
        ).to_be_visible()