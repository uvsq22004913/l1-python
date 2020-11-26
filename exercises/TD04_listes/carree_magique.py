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
    for i in range(len(carre)):
        carre_i = list(carre[i])
        somme_ligne = sum(carre_i)
        if somme_ligne != somme:
            somme = -1
            return somme
    return somme


def testColonnesEgales(carre):
    """ Renvoie la somme des éléments d'une colonne de la liste 2D carre si toutes les colonnes ont la même somme, et -1 sinon """    
    som = []
    test = True
    for j in range(4):
        s = 0
        for i in range(4):
            s = s + carre[i][j]
        som.append(s)
        if s != som[j-1]:
            test = False
            break
    if test == True:
        return som[0]
    else:
        return (-1)


def testDiagonalesEgales(carre):
    """ Renvoie la somme des éléments d'une diagonale de la liste 2D carre si les 2 diagonales ont la même somme, et -1 sinon """
    test = True
    som = []
    
    s = carre[3][0] + carre[2][1] + carre[1][2] + carre[0][3]
    som.append(s)
    s = carre[0][0] + carre[1][1] + carre[2][2] + carre[3][3]
    som.append(s)

    for i in range(2):
        if som[i] != som[0]:
            test = False
    if test == True:
        return som[0]
    else:
        return (-1)


def estCarreMagique(carre):
    """ Renvoie True si c'est un carre magique et False sinon"""
    test = True
    if testColonnesEgales(carre) == -1:
        test = False
    if testLignesEgales(carre) == -1:
        test = False
    if testDiagonalesEgales(carre) == -1:
        test = False
    return test


def estNormal(carre):
    """ Retourne True si contient toutes les valeurs de 1 à n^2 où n est la taille 
        du carré, et False sinon """
    n = 4   
    liste = []
    for i in range(n):
        for j in range(n):
            liste.append(carre[i][j] ** 2)

    print("Liste:", liste)
    liste.sort()
    print("Liste triée :", liste)

    test = True
    for i in range(n ** 2):
        if liste[i] != i + 1:
            test = False

    return test



"""
afficheCarre(carre_mag)
afficheCarre(carre_pas_mag)
print(testLignesEgales(carre_mag))
print(testLignesEgales(carre_pas_mag))
print(testColonnesEgales(carre_mag))
print(testColonnesEgales(carre_pas_mag))
print(estCarreMagique(carre_mag))
print(estCarreMagique(carre_pas_mag))
"""
print(testDiagonalesEgales(carre_mag))
print(testDiagonalesEgales(carre_pas_mag))

print(estNormal(carre_mag))
print(estNormal(carre_pas_mag))
