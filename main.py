import kandinsky as k
import turtle as t
from random import *
import time


def ktt(coo: list):
    coo[0] -= 160
    coo[1] = -coo[1]-111
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
    for i in range(10):
        x = randrange(0, 321)
        y = randrange(0, 223)
        while k.get_pixel(x, y) != (0, 0, 0):
            x = randrange(0, 321)
            y = randrange(0, 223)
        print(x, y)
        t.goto(ktt([x, y]))


initialize()
draw_borders()
