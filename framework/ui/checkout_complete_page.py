from playwright.sync_api import expect


class CheckoutCompletePage:

    def __init__(self, page):
        self.page = page

        self.titre_page = page.get_by_text("Checkout: Complete!")
        self.message_confirmation = page.get_by_text(
            "Thank you for your order!"
        )

    def verifier_page_affichee(self):
        expect(self.titre_page).to_be_visible()

    def verifier_confirmation_commande(self):
        expect(self.message_confirmation).to_be_visible()