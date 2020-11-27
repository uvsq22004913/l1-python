import tkinter as tk

HEIGHT = 800
WIDTH = 800

racine = tk.Tk() # Création de la fenêtre racine

canvas = tk.Canvas(racine, bg="red", height=HEIGHT, width=WIDTH)
canvas.grid(column=0, row=0)

color = "black"
largueur = WIDTH // 8

for j in range(8):
    for i in range(8):
        if (i+j)%2 == 0:
            color = "black"
        else:
            color = "white"
        canvas.create_rectangle((i * largueur, j * largueur),((i+1) * largueur, (j+1) * largueur), fill=color)





racine = tk.Tk()

racine.mainloop()
