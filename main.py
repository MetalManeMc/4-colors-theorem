from turtle import *
from random import *

ht()
colormode(255)
speed(0)
setup(420,322)  #taille de la fenêtre
screensize(320,222,"white")   #taille de l'espace de dessein
def initialize():  # initialise l'écran
    tracer(0,0)
    penup()
    # dessine un cadre noir
    goto(-160, -111)
    pendown()
    goto(-160, 111)
    goto(160, 111)
    goto(160, -111)
    goto(-160, -111)
    update()

def draw_borders():
    tracer(0,0)
    for i in range(20):
        color("black")
        penup()
        # cherche un point noir d'où commencer le tracé
        x = randrange(-160, 161)
        y = randrange(-111, 112)
        #print(get_pixel(-160,-111))
        while get_pixel(x, y) == "white":
            x = randrange(-160, 161)
            y = randrange(-111, 112)
        #print(x, y, get_pixel(x, y))
        goto(x,y)
        # prend un angle apporprié à la position
        if x <= -150:
            setheading(0)
        elif x >= 150:
            setheading(180)
        elif y <= -101:
            setheading(90)
        elif y >= 101:
            setheading(270)
        else: setheading(randrange(-360,361))
        # modifie légèrement l'angle
        setheading(heading()+randrange(-3, 3))
        #print(t.position(), ttk(list(t.position())))
        forward(1)
        # teste si le pixel devant est noir. S'il ne l'est pas, avance.
        while get_pixel(position()[0],position()[1]) == "white":
            pendown()
            backward(1)
            forward(1)
            setheading(float(heading())+choice([3*random(), -3*random()]))
            penup()
            forward(1)
    update()

def get_pixel(x, y):

    # canvas use different coordinates
    y = -y

    canvas = getcanvas()
    ids = canvas.find_overlapping(x, y, x, y)

    if ids: # if list is not empty
        index = ids[-1]
        color = canvas.itemcget(index, "fill")
        if color != '':
            return color.lower()

    return "white" # default color 

initialize()
draw_borders()
input("a")

"""import kandinsky as k
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


def fill_region(L: int, l: int, col: tuple):
    k.set_pixel(L, l, col)
    for l1 in range(223):
        for L1 in range(321):
            if k.get_pixel(L1, l1) == (248, 252, 248):
                if k.get_pixel(L1-1, l1) == col or k.get_pixel(L1, l1-1) == col:
                    k.set_pixel(L1, l1, col)
    for l1 in range(223):
        l1 = 222-l1
        for L1 in range(321):
            L1 = 320-L1
            if k.get_pixel(L1, l1) == (248, 252, 248):
                if k.get_pixel(L1+1, l1) == col or k.get_pixel(L1, l1+1) == col:
                    k.set_pixel(L1, l1, col)


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
    for l in range(223):
        for L in range(321):
            if k.get_pixel(L, l) == (248, 252, 248):
                col = choice(collist)
                countries[(L, l)] = col
                fill_region(L, l, col)


def check_adjacent():
    for l in range(223):
        for L in range(321):
            if k.get_pixel(L, l) == (0, 0, 0):
                pix_colors = []
                pix_colors.append(k.get_pixel(L+1, l))
                pix_colors.append(k.get_pixel(L-1, l))
                pix_colors.append(k.get_pixel(L, l+1))
                pix_colors.append(k.get_pixel(L, l-1))
                pix_colors = [
                    color for color in pix_colors if color in collist]
                #print(L, l, pix_colors)
                end=False
                for color in pix_colors:
                    o_colors = [color for color in pix_colors]
                    o_colors.remove(color) #pix_colors mysteriously disappears here
                    #print(L, l, pix_colors, o_colors, color)
                    if color in o_colors:
                        print(l, L, pix_colors, color)
                        k.set_pixel(L+3, l, (150, 150, 150))
                        k.set_pixel(L-3, l, (150, 150, 150))
                        k.set_pixel(L, l+3, (150, 150, 150))
                        k.set_pixel(L, l-3, (150, 150, 150))
                        end=True
                    if end:break
                if end:break
            if end:break
        if end:break
        


initialize()
draw_borders()
fill_colors()
check_adjacent()
print(countries)
"""