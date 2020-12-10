import tkinter as tk


def draw_pixel(event):
    if event.x < l/2:
        color = 'blue'
    elif event.x >l/2:
        color = 'red'
    else:
        color = 'green'
    canvas.create_oval((event.x-25, event.y-25, event.x+25, event.y+25), outline='', fill=color)


##################################### Variables #####################################

l = 500

##################################### Fenetre #####################################

racine = tk.Tk()
canvas = tk.Canvas(racine, width = l, height = l, bg = 'black')
canvas.grid(column = 1, row = 0)
ligne = canvas.create_line(l/2, 0, l/2, l, fill = 'white')

racine.bind("<Button-1>", draw_pixel)

racine.mainloop()