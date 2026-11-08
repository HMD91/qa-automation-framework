from playwright.sync_api import expect


class InventoryPage:

    def __init__(self, page):
        self.page = page
        self.bouton_panier = page.locator(".shopping_cart_link")
        
    def ouvrir_panier(self):
        self.bouton_panier.click()
    
    
    def verifier_page_affichee(self):
        expect(
            self.page.get_by_text("Products")
        ).to_be_visible()

    def ajouter_au_panier(self, nom_produit):
        produit = self.page.locator(".inventory_item").filter(
            has_text=nom_produit
        )
        produit.get_by_role("button", name="Add to cart").click()

    def verifier_ajout_au_panier(self, nom_produit):
        produit = self.page.locator(".inventory_item").filter(
            has_text=nom_produit
        )

        expect(
            produit.get_by_role("button", name="Remove")
        ).to_be_visible()

        expect(
            self.page.locator(".shopping_cart_badge")
        ).to_have_text("1")
    
        
    def recuperer_premier_produit_disponible(self):
        produits = self.page.locator(".inventory_item")

        for i in range(produits.count()):
            produit = produits.nth(i)

            bouton = produit.get_by_role(
                "button",
                name="Add to cart"
            )

            if bouton.is_visible():
                nom_produit = produit.locator(
                    ".inventory_item_name"
                ).inner_text()

                return nom_produit
        raise AssertionError("Aucun produit disponible sur la page")
    
    def verifier_bouton_remove(self, nom_produit):
        produit = self.page.locator(".inventory_item").filter(
            has_text=nom_produit
        )

        expect(
            produit.get_by_role("button", name="Remove")
        ).to_be_visible()
        
        
    def verifier_compteur_panier(self, nombre_attendu):
        expect(
            self.page.locator(".shopping_cart_badge")
        ).to_have_text(str(nombre_attendu))
        
        
    def retirer_du_panier(self, nom_produit):
        produit = self.page.locator(".inventory_item").filter(
            has_text=nom_produit
        )

        produit.get_by_role("button", name="Remove").click()
        
        
    def verifier_bouton_add_to_cart(self, nom_produit):
        produit = self.page.locator(".inventory_item").filter(
            has_text=nom_produit
        )

        expect(
            produit.get_by_role("button", name="Add to cart")
        ).to_be_visible()
        
        
    def verifier_panier_vide(self):
        expect(
            self.page.locator(".shopping_cart_badge")
        ).to_have_count(0)
        
        
    def recuperer_prix_produit(self, nom_produit):
        produit = self.page.locator(".inventory_item").filter(
            has_text=nom_produit
        )
        return produit.locator(".inventory_item_price").inner_text()