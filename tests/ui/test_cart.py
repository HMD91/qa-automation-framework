from decimal import ROUND_HALF_UP, Decimal

from framework.ui.cart_page import CartPage
from framework.ui.checkout_complete_page import CheckoutCompletePage
from framework.ui.checkout_overview_page import CheckoutOverviewPage
from framework.ui.checkout_page import CheckoutPage


def test_selection_premier_produit_disponible(utilisateur_connecte):
    nom_produit = utilisateur_connecte.recuperer_premier_produit_disponible()

    assert nom_produit

def test_ajout_produit_au_panier(utilisateur_connecte):
    nom_produit = utilisateur_connecte.recuperer_premier_produit_disponible()

    utilisateur_connecte.ajouter_au_panier(nom_produit)

    utilisateur_connecte.verifier_bouton_remove(nom_produit)
    
    
def test_incrementation_compteur_panier(utilisateur_connecte):
    nom_produit = utilisateur_connecte.recuperer_premier_produit_disponible()

    utilisateur_connecte.ajouter_au_panier(nom_produit)

    utilisateur_connecte.verifier_compteur_panier(1)
    
    
def test_retrait_produit_du_panier(utilisateur_connecte):
    nom_produit = utilisateur_connecte.recuperer_premier_produit_disponible()

    utilisateur_connecte.ajouter_au_panier(nom_produit)

    utilisateur_connecte.retirer_du_panier(nom_produit)

    utilisateur_connecte.verifier_bouton_add_to_cart(nom_produit)
    
    
def test_compteur_disparait_apres_retrait(utilisateur_connecte):
    nom_produit = utilisateur_connecte.recuperer_premier_produit_disponible()

    utilisateur_connecte.ajouter_au_panier(nom_produit)
    utilisateur_connecte.retirer_du_panier(nom_produit)

    utilisateur_connecte.verifier_panier_vide()
    
    
def test_ouvrir_panier(utilisateur_connecte):
    nom_produit = utilisateur_connecte.recuperer_premier_produit_disponible()

    prix_produit = utilisateur_connecte.recuperer_prix_produit(nom_produit)
    
    utilisateur_connecte.ajouter_au_panier(nom_produit)
    utilisateur_connecte.ouvrir_panier()

    cart_page = CartPage(utilisateur_connecte.page)
    cart_page.verifier_page_affichee()
    
    cart_page.verifier_page_affichee()
    cart_page.verifier_produit_present(nom_produit)
    
    cart_page.verifier_quantite_produit(1)
    
    cart_page.verifier_prix_produit(prix_produit)
    
    
def test_retrait_produit_depuis_inventory(utilisateur_connecte):
    nom_produit = utilisateur_connecte.recuperer_premier_produit_disponible()

    utilisateur_connecte.ajouter_au_panier(nom_produit)
    utilisateur_connecte.ouvrir_panier()

    cart_page = CartPage(utilisateur_connecte.page)
    cart_page.retirer_produit(nom_produit)
    cart_page.verifier_produit_absent(nom_produit)
    
    cart_page.verifier_produit_absent(nom_produit)
    cart_page.verifier_panier_vide()
    
    
def test_retour_aux_produits(utilisateur_connecte):
    utilisateur_connecte.ouvrir_panier()

    cart_page = CartPage(utilisateur_connecte.page)
    cart_page.continuer_achats()

    utilisateur_connecte.verifier_page_affichee()
    
def test_ouvrir_checkout(utilisateur_connecte):
    utilisateur_connecte.ouvrir_panier()

    cart_page = CartPage(utilisateur_connecte.page)
    cart_page.aller_au_checkout()

    checkout_page = CheckoutPage(utilisateur_connecte.page)
    checkout_page.verifier_page_affichee()
    

def test_remplir_informations_checkout(utilisateur_connecte):
    utilisateur_connecte.ouvrir_panier()

    cart_page = CartPage(utilisateur_connecte.page)
    cart_page.aller_au_checkout()

    checkout_page = CheckoutPage(utilisateur_connecte.page)
    checkout_page.verifier_page_affichee()

    checkout_page.remplir_informations(
        "Ahmed",
        "Test",
        "31000"
    )
    
    checkout_page.verifier_informations(
    "Ahmed",
    "Test",
    "31000"
    )
    
    
def test_verifier_recapitulatif_commande(utilisateur_connecte):
    nom_produit = utilisateur_connecte.recuperer_premier_produit_disponible()
    prix_produit = utilisateur_connecte.recuperer_prix_produit(nom_produit)

    utilisateur_connecte.ajouter_au_panier(nom_produit)
    utilisateur_connecte.ouvrir_panier()

    cart_page = CartPage(utilisateur_connecte.page)
    cart_page.aller_au_checkout()

    checkout_page = CheckoutPage(utilisateur_connecte.page)
    checkout_page.remplir_informations(
        "Ahmed",
        "Test",
        "31000"
    )
    checkout_page.continuer()

    overview_page = CheckoutOverviewPage(utilisateur_connecte.page)
    overview_page.verifier_page_affichee()
    overview_page.verifier_produit_present(nom_produit)
    overview_page.verifier_quantite_produit(1)
    
    overview_page.verifier_prix_produit(prix_produit)
    
    overview_page.verifier_sous_total(prix_produit)
    
    prix_numerique = Decimal(prix_produit.replace("$", ""))

    taxes = (prix_numerique * Decimal("0.08")).quantize(
       Decimal("0.01"),
       rounding=ROUND_HALF_UP
    ) 

    overview_page.verifier_taxes(f"${taxes:.2f}")
    
    total = prix_numerique + taxes
    
    overview_page.verifier_total(f"${total:.2f}")
    
    
    
def test_finaliser_commande(utilisateur_connecte):
    nom_produit = utilisateur_connecte.recuperer_premier_produit_disponible()

    utilisateur_connecte.ajouter_au_panier(nom_produit)
    utilisateur_connecte.ouvrir_panier()

    cart_page = CartPage(utilisateur_connecte.page)
    cart_page.aller_au_checkout()

    checkout_page = CheckoutPage(utilisateur_connecte.page)
    checkout_page.remplir_informations("Ahmed", "Test", "31000")
    checkout_page.continuer()

    overview_page = CheckoutOverviewPage(utilisateur_connecte.page)
    overview_page.verifier_page_affichee()
    overview_page.finaliser_commande()

    complete_page = CheckoutCompletePage(utilisateur_connecte.page)
    complete_page.verifier_page_affichee()
    complete_page.verifier_confirmation_commande()