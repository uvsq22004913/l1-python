import tkinter as tk
from random import randint

##################################### Fonctions #####################################


def cercle():
    global objets
    x = randint(50, width - 50)
    y = randint(50, height - 50)
    cercle = canvas.create_oval(x-50, y-50, x+50, y+50, fill=couleur, outline="white")
    objets.append(cercle) 


def carre():
    global objets
    x = randint(50, width - 50)
    y = randint(50, height - 50)
    carre = canvas.create_rectangle(x-50, y-50, x+50, y+50, fill = couleur, outline="white")
    objets.append(carre)
    

def croix():
    global objets, ligne1, ligne2
    x = randint(50, width - 50)
    y = randint(50, height - 50)
    ligne1 = canvas.create_line(x-50, y-50, x+50, y+50, fill = couleur)
    ligne2 = canvas.create_line(x-50, y+50, x+50, y-50, fill = couleur)
    objets.append(ligne1)
    objets.append(ligne2)


def choisir_couleur():
    global couleur
    couleur = input("Ecrire votre couleur :")


def undo():
    global objets
    if len(objets) > 0:
        if canvas.type(objets[-1]) == 'line':
            canvas.delete(objets[-1])
            objets.remove(objets[-1])
            canvas.delete(objets[-1])
            objets.remove(objets[-1])
        else:
            canvas.delete(objets[-1])
            objets.remove(objets[-1])


##################################### Variables #####################################

width, height = 600, 600
couleur = 'blue'
liste_couleur = ['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow']
objets = []

##################################### Fenetre #####################################

racine = tk.Tk()
racine.title("Mon dessin")

canvas = tk.Canvas(racine, width = width, height = height, bg = 'black')
canvas.grid(column = 1, row = 1, rowspan = 10, columnspan = 10)

b_couleur = tk.Button(racine, text = "Choisir une couleur", font = ("helvetica", "26"), command = choisir_couleur)
b_couleur.grid(column = 3, row = 0)

b_cercle = tk.Button(racine, text = "Cercle", font = ("helvetica", "26"), command = cercle)
b_cercle.grid(column = 0, row = 3)

b_carre = tk.Button(racine, text = "Carré", font = ("helvetica", "26"), command = carre)
b_carre.grid(column = 0, row = 6)

b_croix = tk.Button(racine, text = "Croix", font = ("helvetica", "26"), command = croix)
b_croix.grid(column = 0, row = 9)

b_undo = tk.Button(racine, text = "Undo", font = ("helvetica", "26"), command = undo)
b_undo.grid(column = 7, row = 0)

racine.mainloop()
