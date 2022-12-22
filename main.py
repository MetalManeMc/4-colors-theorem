import kandinsky as k
import turtle as t
from random import *
import time

collist = [k.color(255, 0, 0), k.color(0, 255, 0),
           k.color(0, 0, 255), k.color(255, 255, 0)]
countries = {}


def ktt(coo: list):
    coo[0] -= 160
    coo[1] = -coo[1]+111
    return coo


def ttk(coo: list):
    coo[0] += 160
    coo[1] = -coo[1]+111
    return coo


def initialize():  # initialise l'écran
    # uniformise le fond d'écran en blanc
    k.fill_rect(0, 0, 320, 222, k.color(248, 252, 248))
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
    for i in range(20):

        t.penup()
        # cherche un point noir d'où commencer le tracé
        x = randrange(0, 321)
        y = randrange(0, 223)
        while k.get_pixel(x, y) != (0, 0, 0):
            x = randrange(0, 321)
            y = randrange(0, 223)
        #print(x, y, ktt([x, y]))
        t.goto(ktt([x, y]))
        # prend un angle apporprié à la position
        if x <= 10:
            t.setheading(0)
        elif x >= 310:
            t.setheading(180)
        elif y <= 10:
            t.setheading(270)
        elif y >= 112:

            t.setheading(90)
        # modifie légèrement l'angle
        t.setheading(t.heading()+randrange(-3, 3))
        #print(t.position(), ttk(list(t.position())))
        t.forward(1)
        t.color("blue")
        # teste si le pixel devant est noir. S'il ne l'est pas, avance.
        while k.get_pixel(int(ttk(list(t.position()))[0]), int(ttk(list(t.position()))[1])) != (0, 0, 0):
            t.pendown()
            t.backward(1)
            t.forward(1)
            t.setheading(float(t.heading())+choice([random(), -random()]))
            t.penup()
            t.forward(1)
        # transforme tout le bleu en noir
        for L in range(321):
            for l in range(223):
                if k.get_pixel(L, l) == (0, 0, 248):
                    k.set_pixel(L, l, (0, 0, 0))


def fill_colors():
    for L in range(320):
        for l in range(222):
            if k.get_pixel(L, l) == (248, 252, 248):
                col = choice(collist)
                countries[(L, l)] = col
                k.set_pixel(L, l, col)
                for L1 in range(320):
                    for l1 in range(222):
                        if k.get_pixel(L1, l1) == (248, 252, 248):
                            if k.get_pixel(L1-1, l1)==col:
                                k.set_pixel(L1,l1,col)
                            elif k.get_pixel(L1, l1-1)==col:
                                k.set_pixel(L1,l1,col)


initialize()
draw_borders()
fill_colors()
