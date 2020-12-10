import tkinter as tk

def boutton1(event):
    carreconfig(event)
    draw_pixel(event)
    destroy(event)


def draw_pixel(event):
    global x1, y1
    if event.x < l/2:
        color = 'blue'
    elif event.x >l/2:
        color = 'red'
    else:
        color = 'green'
    canvas.create_oval((event.x-25, event.y-25, event.x+25, event.y+25), outline='', fill=color)
    
    if x1 >=0 and y1 >=0:
        if (x1 < l/2 and event.x < l/2) or (x1 > l/2 and event.x > l/2):
            color_line = 'blue'
        else:
            color_line = 'red'
        canvas.create_line(x1, y1, event.x, event.y, fill = color_line)
        x1, y1 = -10, -10
    else:
        x1, y1 = event.x, event.y


def carreconfig(event):
    global remplit
    if remplit == True:
        canvas.itemconfig(carre, fill='black') 
        remplit = False
    else:
        canvas.itemconfig(carre, fill='white')
        remplit = True


def destroy(event):
    global cpt
    cpt += 1
    if cpt == 10:
        racine.destroy()


##################################### Variables #####################################

l = 500
larg = 25
x1,y1 = -10, -10
remplit = False
cpt = 0

##################################### Fenetre #####################################

racine = tk.Tk()
canvas = tk.Canvas(racine, width = l, height = l, bg = 'black')
canvas.grid()

ligne = canvas.create_line(l/2, 0, l/2, l, fill = 'white')
carre = canvas.create_rectangle((l/2)-larg, (l/2)-larg, (l/2)+larg, (l/2)+larg, outline = 'white', fill = 'black')
racine.bind("<Button-1>", boutton1)

racine.mainloop()