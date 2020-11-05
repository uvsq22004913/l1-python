
def tempsSecondes(temps):
    sec = temps[0] * 86400 + temps[1] * 3600 + temps[2] * 60 + temps[3]
    return sec


def secondesTemps(secondes):
    tupletemps = (secondes // 86400 , (secondes % 86400) // 3600 , ((secondes % 86400) % 3600) // 60 , (((secondes % 86400) % 3600) % 60))
    return tupletemps


def pluriel(temps):
    if int(temps) > 1 :
        return("s")
    else :
        return("")
    

def afficheTemps(temps):
    affiche = ("jour", "heure", "minute", "seconde")
    for i in range(0,len(temps)):
        print(temps[i], " ", affiche[i], pluriel(temps[i]), sep="", end=" ")


def demandeTemps():
    test = False
    while test != True :
        j = input("\nEntrez un nombre de jours\n")
        h = input("\nEntrez un nombre d'heures\n")
        m = input("\nEntrez un nombre de minutes\n")
        s = input("\nEntrez un nombre de secondes\n")
        temps = (j, h, m, s)

        if int(temps[1]) > 23 :
            test = False
            print("Entrez un temps correcte.")
        elif int(temps[2]) > 59 :
            test = False
            print("Entrez un temps correcte.")
        elif int(temps[3]) > 59 :
            test = False
            print("Entrez un temps correcte.")
        else :
            test = True
    return temps


temps = (3, 21, 10, 35)
secondes = 335435

"""
print(tempsSecondes(temps), "secondes")
temps = secondesTemps(secondes)
afficheTemps(temps)
afficheTemps(demandeTemps())
"""