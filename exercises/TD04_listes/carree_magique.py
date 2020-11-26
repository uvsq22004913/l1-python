carre_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]
carre_pas_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 7, 13]]


def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    for i in range(0, len(carre)):
        print(carre_mag[i])
    print()


def testLignesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si toutes les lignes ont la même somme, et -1 sinon """
    somme_ligne = 0
    somme = sum(list(carre[0]))
    for i in range(0, len(carre)):
        carre_i = list(carre[i])
        somme_ligne = sum(carre_i)
        if somme_ligne != somme:
            somme = -1
            return somme
    return somme


def testColonnesEgales(carre):
    """ Renvoie la somme des éléments d'une colonne de la liste 2D carre si toutes les colonnes ont la même somme, et -1 sinon """
    


"""
afficheCarre(carre_mag)
afficheCarre(carre_pas_mag)
print(testLignesEgales(carre_mag))
print(testLignesEgales(carre_pas_mag))
"""
print(testColonnesEgales(carre_mag))
print(testColonnesEgales(carre_pas_mag))
