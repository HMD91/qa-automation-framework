from playwright.sync_api import expect


class CheckoutOverviewPage:

    def __init__(self, page):
        self.page = page

        self.titre_page = page.get_by_text("Checkout: Overview")
        self.bouton_finish = page.get_by_role(
            "button",
            name="Finish"
        )

    def verifier_page_affichee(self):
        expect(self.titre_page).to_be_visible()
        
        
    def verifier_produit_present(self, nom_produit):
        expect(
            self.page.locator(".cart_item").filter(
                has_text=nom_produit
            )
        ).to_be_visible()
        
    def verifier_quantite_produit(self, quantite_attendue):
        expect(
            self.page.locator(".cart_quantity")
        ).to_have_text(str(quantite_attendue))
        
        
    def verifier_prix_produit(self, prix_attendu):
        expect(
            self.page.locator(".inventory_item_price")
        ).to_have_text(prix_attendu)
        
        
    def verifier_sous_total(self, sous_total_attendu):
        expect(
            self.page.locator(".summary_subtotal_label")
        ).to_have_text(f"Item total: {sous_total_attendu}")
        
    def verifier_taxes(self, taxes_attendues):
        expect(
            self.page.locator(".summary_tax_label")
        ).to_have_text(f"Tax: {taxes_attendues}")
        
        
    def verifier_total(self, total_attendu):
        expect(
            self.page.locator(".summary_total_label")
        ).to_have_text(f"Total: {total_attendu}")
        
        
    def finaliser_commande(self):
        self.bouton_finish.click()