from playwright.sync_api import expect


class InventoryPage:

    def __init__(self, page):
        self.page = page

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