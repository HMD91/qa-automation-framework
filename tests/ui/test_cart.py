from decimal import ROUND_HALF_UP, Decimal

import allure
import pytest

from framework.ui.cart_page import CartPage
from framework.ui.checkout_complete_page import CheckoutCompletePage
from framework.ui.checkout_overview_page import CheckoutOverviewPage
from framework.ui.checkout_page import CheckoutPage

pytestmark = pytest.mark.ui


@allure.epic("QA Automation Framework")
@allure.feature("UI Testing")
@allure.story("Product Selection")
@allure.title("Sélectionner le premier produit disponible")
def test_selection_premier_produit_disponible(utilisateur_connecte):
    nom_produit = utilisateur_connecte.recuperer_premier_produit_disponible()

    assert nom_produit

@allure.epic("QA Automation Framework")
@allure.feature("UI Testing")
@allure.story("Shopping Cart")
@allure.title("Ajouter un produit au panier")
def test_ajout_produit_au_panier(utilisateur_connecte):
    nom_produit = utilisateur_connecte.recuperer_premier_produit_disponible()

    utilisateur_connecte.ajouter_au_panier(nom_produit)

    utilisateur_connecte.verifier_bouton_remove(nom_produit)
    

@allure.epic("QA Automation Framework")
@allure.feature("UI Testing")
@allure.story("Shopping Cart")
@allure.title("Vérifier l'incrémentation du compteur du panier")
def test_incrementation_compteur_panier(utilisateur_connecte):
    nom_produit = utilisateur_connecte.recuperer_premier_produit_disponible()

    utilisateur_connecte.ajouter_au_panier(nom_produit)

    utilisateur_connecte.verifier_compteur_panier(1)
    
@allure.epic("QA Automation Framework")
@allure.feature("UI Testing")
@allure.story("Shopping Cart")
@allure.title("Retirer un produit du panier")
def test_retrait_produit_du_panier(utilisateur_connecte):
    nom_produit = utilisateur_connecte.recuperer_premier_produit_disponible()

    utilisateur_connecte.ajouter_au_panier(nom_produit)

    utilisateur_connecte.retirer_du_panier(nom_produit)

    utilisateur_connecte.verifier_bouton_add_to_cart(nom_produit)
    
@allure.epic("QA Automation Framework")
@allure.feature("UI Testing")
@allure.story("Shopping Cart")
@allure.title("Vérifier la disparition du compteur après retrait") 
def test_compteur_disparait_apres_retrait(utilisateur_connecte):
    nom_produit = utilisateur_connecte.recuperer_premier_produit_disponible()

    utilisateur_connecte.ajouter_au_panier(nom_produit)
    utilisateur_connecte.retirer_du_panier(nom_produit)

    utilisateur_connecte.verifier_panier_vide()
    
@allure.epic("QA Automation Framework")
@allure.feature("UI Testing")
@allure.story("Shopping Cart")
@allure.title("Ouvrir le panier")  
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
    
@allure.epic("QA Automation Framework")
@allure.feature("UI Testing")
@allure.story("Shopping Cart")
@allure.title("Retirer un produit depuis la page des produits")   
def test_retrait_produit_depuis_inventory(utilisateur_connecte):
    nom_produit = utilisateur_connecte.recuperer_premier_produit_disponible()

    utilisateur_connecte.ajouter_au_panier(nom_produit)
    utilisateur_connecte.ouvrir_panier()

    cart_page = CartPage(utilisateur_connecte.page)
    cart_page.retirer_produit(nom_produit)
    cart_page.verifier_produit_absent(nom_produit)
    
    cart_page.verifier_produit_absent(nom_produit)
    cart_page.verifier_panier_vide()
    
@allure.epic("QA Automation Framework")
@allure.feature("Navigation")
@allure.story("Product Navigation")
@allure.title("Revenir à la liste des produits")    
def test_retour_aux_produits(utilisateur_connecte):
    utilisateur_connecte.ouvrir_panier()

    cart_page = CartPage(utilisateur_connecte.page)
    cart_page.continuer_achats()

    utilisateur_connecte.verifier_page_affichee()

@allure.epic("QA Automation Framework")
@allure.feature("UI Testing")
@allure.story("Checkout")
@allure.title("Accéder à la page de commande")    
def test_ouvrir_checkout(utilisateur_connecte):
    utilisateur_connecte.ouvrir_panier()

    cart_page = CartPage(utilisateur_connecte.page)
    cart_page.aller_au_checkout()

    checkout_page = CheckoutPage(utilisateur_connecte.page)
    checkout_page.verifier_page_affichee()
    

@allure.epic("QA Automation Framework")
@allure.feature("UI Testing")
@allure.story("Checkout")
@allure.title("Renseigner les informations de livraison")
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
    
@allure.epic("QA Automation Framework")
@allure.feature("UI Testing")
@allure.story("Checkout")
@allure.title("Vérifier le récapitulatif de la commande")   
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
    
    
@allure.epic("QA Automation Framework")
@allure.feature("UI Testing")
@allure.story("Checkout")
@allure.title("Finaliser une commande")   
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