import kandinsky as k
import turtle as t
from random import *
import time

colors = [(0, 0, 248)]


def ktt(coo: list): #kandinsky to turtle
    coo[0] -= 160
    coo[1] = -coo[1]+111
    return coo


def ttk(coo: list): #turtle to kandinsky
    coo[0] += 160
    coo[1] = -coo[1]+111
    return coo


def initialize():  # initialise l'écran
    # uniformise le fond d'écran en blanc
    k.fill_rect(0, 0, 320, 222, k.color(248, 252, 248))
    t.speed(10)
    t.penup()
    # dessine un cadre noir
    t.goto(-160, -111)
    t.pendown()
    t.goto(-160, 111)
    t.goto(160, 111)
    t.goto(160, -111)
    t.goto(-160, -111)
    t.hideturtle()

def draw_borders():
    t.speed(10)
    for i in range(50):
        t.penup()
        # cherche un pixel d'où commencer le tracé
        x = randrange(0, 321)
        y = randrange(0, 223)
        while k.get_pixel(x, y) != (0, 0, 0):
            x = randrange(0, 321)
            y = randrange(0, 223)
        t.goto(ktt([x, y]))
        # prend un angle approprié à la position
        if x <=160:
            t.setheading(270)
        elif x >160:
            t.setheading(90)
        if y <=111:
            t.setheading(0)
        elif y >111:
            t.setheading(180)
        # modifie l'angle
        t.setheading(t.heading()+randrange(-10, 10))
        t.forward(1)
        t.color("blue")
        # Si le pixel est blanc, avance.
        while k.get_pixel(int(ttk(list(t.position()))[0]), int(ttk(list(t.position()))[1])) != (0, 0, 0):
            t.forward(1)
            t.right(randrange(-40, 40))
        # transforme tout le bleu en noir
        for L in range(321):
            for l in range(223):
                if k.get_pixel(L, l) == (0, 0, 248):
                    k.set_pixel(L, l, (0, 0, 0))


def fill_colors():
    collist=[color(255,0,0), color(0,255,0), color(0,0,255), color(255,255,0)]

initialize()
draw_borders()
fill_colors()