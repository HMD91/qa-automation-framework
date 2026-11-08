from framework.ui.cart_page import CartPage


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