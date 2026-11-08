from playwright.sync_api import expect


class CheckoutPage:

    def __init__(self, page):
        self.page = page

        self.champ_prenom = page.get_by_placeholder("First Name")
        self.champ_nom = page.get_by_placeholder("Last Name")
        self.champ_code_postal = page.get_by_placeholder("Zip/Postal Code")
        
        self.bouton_continue = self.page.get_by_role(
            "button",
            name="Continue"
            )

    def verifier_page_affichee(self):
        expect(
            self.page.get_by_text("Checkout: Your Information")
        ).to_be_visible()
        
        
    def remplir_informations(self, prenom, nom, code_postal):
        self.champ_prenom.fill(prenom)
        self.champ_nom.fill(nom)
        self.champ_code_postal.fill(code_postal)
        
        
    def verifier_informations(self, prenom, nom, code_postal):
        expect(self.champ_prenom).to_have_value(prenom)
        expect(self.champ_nom).to_have_value(nom)
        expect(self.champ_code_postal).to_have_value(code_postal)
        
        
    def continuer(self):
        self.bouton_continue.click()