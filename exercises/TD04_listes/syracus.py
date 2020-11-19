def syracuse(n):
    liste = []
    while n != 1:
        if (n % 2) == 0:
            n /= 2
        else:
            n = n * 3 + 1
        liste.append(n)
    print(liste)
    return(liste)


def testeConjecture(n_max):
    for i in range(1, n_max):
        syracuse(i)
    return True


def tempsVol(n):
    """ Retourne le temps de vol de n """
    return(len(syracuse(n)))


def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    liste_temps_vol = []
    for i in range(1, n_max):
        liste_temps_vol.append(tempsVol(i))
    print("\n \n \n")
    return liste_temps_vol


def maxTempsVol(n_max):
    liste_temps_vol = tempsVolListe(n_max)
    max = 0
    for i in range(1, len(liste_temps_vol)):     
        if (liste_temps_vol[i]) > max :
            max = liste_temps_vol[i]
    return max


def altitudeMax(n_max):
    max = 0
    for i in range(1, n_max):
        syra = syracuse(i)
        for j in range(1, len(syra)):     
            if (syra[j]) > max :
                max = syra[j]
                n = i
    print("Altitude maximum :", max, ", atteinte pour n =", n)
    return(max)




#syracuse(5)
#print(testeConjecture(10000))
#print("Le temps de vol de", 5, "est", tempsVol(5))
#print(tempsVolListe(10000))
#print(maxTempsVol(10000))
#altitudeMax(10000)
