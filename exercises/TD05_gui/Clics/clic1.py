import tkinter as tk


def draw_pixel(event):
    canvas.create_rectangle((event.x, event.y)*2, outline='', fill='red')


##################################### Variables #####################################

l = 500

##################################### Fenetre #####################################

racine = tk.Tk()
canvas = tk.Canvas(racine, width = l, height = l, bg = 'black')
canvas.grid(column = 1, row = 0)

racine.bind("<Button-1>", draw_pixel)

racine.mainloop()