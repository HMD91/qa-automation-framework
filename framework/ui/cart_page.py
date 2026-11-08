from playwright.sync_api import expect


class CartPage:
    
    def __init__(self, page):
        self.page = page
        
        self.titre_page = self.page.get_by_text("Your Cart")
        self.bouton_checkout = self.page.get_by_role(
            "button", 
            name="Checkout"
            )
        
  
        self.bouton_continue_shopping = page.get_by_role(
            "button",
            name="Continue Shopping"
            )
        
    def verifier_page_affichee(self):
        expect(self.titre_page).to_be_visible()
        
        
    def verifier_produit_present(self, nom_produit):
        expect(
            self.page.get_by_text(nom_produit)
        ).to_be_visible()
        
        
    def verifier_quantite_produit(self, quantite_attendue):
        expect(
            self.page.locator(".cart_quantity")
        ).to_have_text(str(quantite_attendue))
        
        
    def verifier_prix_produit(self, prix_attendu):
        expect(
            self.page.locator(".inventory_item_price")
        ).to_have_text(prix_attendu)
    
    
    def retirer_produit(self, nom_produit):
        produit = self.page.locator(".cart_item").filter(
            has_text=nom_produit
        )
        produit.get_by_role("button", name="Remove").click()
    
    
    def verifier_produit_absent(self, nom_produit):
        expect(
            self.page.locator(".cart_item").filter(
                has_text=nom_produit
            )
        ).to_have_count(0)
        
    def verifier_panier_vide(self):
        expect(
            self.page.locator(".cart_item")
        ).to_have_count(0)
        
        
    def continuer_achats(self):
        self.bouton_continue_shopping.click()
        
        
    def aller_au_checkout(self):
        self.bouton_checkout.click()