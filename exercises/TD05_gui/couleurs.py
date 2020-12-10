import tkinter as tk
from random import randint

##################################### Fonctions #####################################

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def draw_pixel(i, j, color):
    canvas.create_rectangle((i, j)*2, outline='', fill=color)


def ecran_aleatoire():
    for i in range(l):
        for j in range(l):
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            color = get_color(r, g, b)
            draw_pixel(i, j, color)      


def degrade_gris():
    for i in range(0, 255):
        gris = get_color(i, i, i)
        canvas.create_rectangle(i, 0, i, 255, outline='', fill=gris)


def degrade_2D():
    for i in range(0, 255):
        for j in range(0, 255):
            degrade = get_color(i, 0, j)
            canvas.create_rectangle(i, j, i, j, outline='', fill=degrade)
        

##################################### Variables #####################################

width, height = 511, 255
l = 255

##################################### Fenetre #####################################

racine = tk.Tk()
canvas = tk.Canvas(racine, width = l, height = l, bg = 'black')
canvas.grid(column = 1, row = 0, rowspan = 12)

aleatoire = tk.Button(racine, text = "Aléatoire", font = ("helvetica", "26"), command = ecran_aleatoire)
aleatoire.grid(column = 0, row = 2)

gris = tk.Button(racine, text = "Dégradé gris", font = ("helvetica", "26"), command = degrade_gris)
gris.grid(column = 0, row = 5)

degrade_2d = tk.Button(racine, text = "Dégradé 2D", font = ("helvetica", "26"), command = degrade_2D)
degrade_2d.grid(column = 0, row = 8)




racine.mainloop()
