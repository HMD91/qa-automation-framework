from playwright.sync_api import expect


class InventoryPage:

    def __init__(self, page):
        self.page = page

    def verifier_page_affichee(self):
        expect(
            self.page.get_by_text("Products")
        ).to_be_visible()