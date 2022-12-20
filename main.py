import kandinsky as k
import turtle as t
from random import *
import time


def initialize():   #initialise l'écran
    k.fill_rect(0, 0, 320, 222, k.color(248, 252, 248)) #uniformise le fond d'écran en blanc
    t.penup()
    t.goto(-160, -111)  #va dans un coin pour se préparer à dessiner un cadre
    t.pendown()
    t.goto(-160, 111)
    t.goto(160, 111)
    t.goto(160, -111)
    t.goto(-160, -111)
    t.hideturtle()


def draw_borders():
    for i in range(10):
        x=randrange(0,321)
        y=randrange(0,223)
        while k.get_pixel(x,y)!=(0,0,0):
            x=randrange(0,321)
            y=randrange(0,223)
        print(x,y)


initialize()
draw_borders()