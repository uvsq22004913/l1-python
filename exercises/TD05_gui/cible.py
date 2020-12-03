import tkinter as tk

##################################### Variables #####################################

width, height = 600, 600
decalage = width // 70
cpt = 0
couleur = ['blue', 'green', 'black', 'yellow', 'magenta', 'red']

##################################### Fenetre #####################################

racine = tk.Tk()
canvas = tk.Canvas(racine, width = width, height = height, bg = 'black')
canvas.grid(column = 1, row = 1)

for i in range(0, ((width//2) // decalage) - 1):
    cercle = canvas.create_oval(i * decalage, i * decalage, width - i * decalage, width - i * decalage, fill=couleur[i%6]) 

racine.mainloop()
