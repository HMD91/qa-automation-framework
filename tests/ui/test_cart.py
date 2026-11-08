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