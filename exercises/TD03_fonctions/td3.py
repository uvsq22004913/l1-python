
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
    affiche = ("année", "jour", "heure", "minute", "seconde")
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


def sommeTempslong(temps1, temps2):
    j = temps1[0] + temps2[0]
    h = temps1[1] + temps2[1]
    m = temps1[2] + temps2[2]
    s = temps1[3] + temps2[3]
    somme = (j, h, m, s)
    print(somme)

    if int(somme[3]) > 59 :
        s = somme [3] - 60
        m += 1    
    if int(somme[2]) > 59 :
        m = somme[2] - 60
        h += 1
    if int(somme[1]) > 23 :
        h = int(somme[1]) - 24
        j += 1

    somme = (j, h, m, s)
    return(somme)


def sommeTemps(temps1, temps2):
    temps1Sec = tempsSecondes(temps1)
    temps2Sec = tempsSecondes(temps2)
    somme = temps1Sec + temps2Sec
    somme = secondesTemps(somme)
    return(somme)


def proportionTemps(temps, proportion):
    secondes = tempsSecondes(temps)
    propSecondes = int(secondes * proportion)
    propTemps = secondesTemps(propSecondes)
    return(afficheTemps(propTemps))


def tempsDate(temps):
    secondes = tempsSecondes(temps)
    a = 2020 + (secondes // (3600*24*365))
    j = (secondes % (3600*24*365)) // (3600*24)
    h = ((secondes % (3600*24*365)) % (3600*24)) // 3600
    m = (((secondes % (3600*24*365)) % (3600*24)) % 3600) // 60
    s = (((secondes % (3600*24*365)) % (3600*24)) % 3600) % 60
    date = (a, j, h, m, s)
    return date


def afficheDate(date):
    afficheTemps(tempsDate(temps))


def time():
    import time

    seconde = int(time.time())
    print(seconde, "secondes")

    temps = secondesTemps(seconde)
    afficheTemps(temps)
    print("affichetemps")

    date = tempsDate(temps)
    afficheDate(date)
    print("affichedate")


def bisextile(jour):
    date = tempsDate(secondesTemps(jour * 3600 * 24))
    anneeBisextile = 0
    year = date[0]
    print("année = ", year)
    for i in range(2020, year+1):
        if i % 4 == 0 and i %100 != 0 or i % 400 == 0 :
            anneeBisextile += 1
            print(i)
        else :
            pass
    return anneeBisextile


def nombreBisextile(jour):
    date = tempsDate(secondesTemps(jour * 3600 * 24))
    anneeBisextile = 0
    year = date[0]
    print("année = ", year)
    for i in range(2020, year+1):
        if i % 4 == 0 and i %100 != 0 or i % 400 == 0 :
            anneeBisextile += 1
        else :
            pass
    return anneeBisextile

print(bisextile(20000))


"""
secondes = 335435
print(tempsSecondes(temps), "secondes")
temps = secondesTemps(secondes)
afficheTemps(temps)
afficheTemps(demandeTemps())
print(sommeTemps((2, 3, 4, 25),(5, 22, 57, 1)))
proportionTemps(temps, 0.2)
temps = secondesTemps(1000000000)
afficheDate(temps)
"""
temps = (2, 0, 36, 0)
