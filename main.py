"""
===================== PLUS UTILISE, VOIR visualdemo.py ====================
"""


from turtle import *
from random import *
from time import time

ht()
colormode(255)
speed(0)
setup(420, 322)  # taille de la fenêtre
screensize(320, 222, "white")  # taille de l'espace de dessein


def initialize():  # initialise l'écran
    tracer(0, 0)
    penup()
    # dessine un cadre noir
    goto(-160, -111)
    pendown()
    goto(-160, 111)
    goto(160, 111)
    goto(160, -111)
    goto(-160, -111)
    update()


def get_pixel(x, y):

    # canvas use different coordinates than turtle
    y = -y
    # get access to tkinter.Canvas
    canvas = getcanvas()
    # find IDs of all objects in rectangle (x, y, x, y)
    ids = canvas.find_overlapping(x, y, x, y)
    # if found objects
    if ids:
        # get ID of last object (top most)
        index = ids[-1]
        # get its color
        color = canvas.itemcget(index, "fill")
        # if it has color then return it
        if color:
            return color
    # if there was no object then return "white" - background color in turtle
    return "white"  # default color


def draw_borders():
    tracer(0, 0)
    for i in range(20):
        color("black")
        penup()
        # cherche un point noir d'où commencer le tracé
        x = randrange(-160, 161)
        y = randrange(-111, 112)
        # print(get_pixel(-160,-111))
        while get_pixel(x, y) == "white":
            x = randrange(-160, 161)
            y = randrange(-111, 112)
        #print(x, y, get_pixel(x, y))
        goto(x, y)
        # prend un angle apporprié à la position
        if x <= -150:
            setheading(0)
        elif x >= 150:
            setheading(180)
        elif y <= -101:
            setheading(90)
        elif y >= 101:
            setheading(270)
        else:
            setheading(randrange(-360, 361))
        # modifie légèrement l'angle
        setheading(heading()+randrange(-3, 3))
        #print(t.position(), ttk(list(t.position())))
        forward(1)
        # teste si le pixel devant est noir. S'il ne l'est pas, avance.
        while get_pixel(position()[0], position()[1]) == "white":
            pendown()
            #set_pixel(x, y)
            backward(1)
            forward(1)
            setheading(float(heading())+choice([3*random(), -3*random()]))
            penup()
            forward(1)
    update()


def fill_controller():
    pensize(1)
    color("blue")
    i = 0
    for y in range(-111, 111):
        y = -y
        for x in range(-160, 160):
            if get_pixel(x, y) == "white" and not has_border(x, y):
                goto(x, y)
                #print("fill start")
                tracer(1, -1)
                if get_pixel(x, y+1) != "white":
                    color(get_pixel(x, y+1))
                    bruteforce_fill()
                    #print('copied color from y+1')
                elif get_pixel(x, y-1) != "white":
                    color(get_pixel(x, y-1))
                    bruteforce_fill()
                    #print('copied color from y-1')
                elif get_pixel(x+1, y) != "white":
                    color(get_pixel(x+1, y))
                    bruteforce_fill()
                    #print('copied color from x+1')
                elif get_pixel(x-1, y) != "white":
                    color(get_pixel(x-1, y))
                    bruteforce_fill()
                    #print('copied color from y-1')
                else:
                    print("not copied")
                    color((i*10, i*10, 255-i*10))
                    bruteforce_fill()
                    i += 1
                update()


def bruteforce_fill():
    pendown()
    while True:
        x = position()[0]
        y = position()[1]
        if get_pixel(x, y+1) == "white" and not has_border(x, y+1):
            goto(x, y+1)
            # print("up")
        elif get_pixel(x-1, y) == "white" and not has_border(x-1, y):
            goto(x-1, y)
            # print("left")
        elif get_pixel(x, y-1) == "white" and not has_border(x, y-1):
            goto(x, y-1)
            # print("down")
        elif get_pixel(x+1, y) == "white" and not has_border(x+1, y):
            goto(x+1, y)
            # print("right")
        else:
            penup()
            return


"""
def follow_borders():
    fillcolor("red")
    tracer(1)
    for y in range(-111, 111):
        y = -y
        for x in range(-160, 160):
            speed(1)
            color("blue")
            if get_pixel(x, y) == "white":
                origin = (x, y)
                penup()
                goto(x, y)
                begin_fill()
                find_adjacent(True)
                c = 0
                while position() != origin:
                    find_adjacent()
                    pendown()
                    c += 1
                    if c > 1000:
                        return
                end_fill()


def find_adjacent(first=False):
    x = position()[0]
    y = position()[1]
    if get_pixel(x-1, y) == "black":
        if get_pixel(x, y+1) == "white":
            if has_border(x-1, x+1):
                goto(x-1, y+1)
                return
        if has_border(x, y+1):
            goto(x, y+1)
            return
    if get_pixel(x, y-1) == "black":
        print("down_pixel detectes")
        if get_pixel(x-1, y) == "white":
            if has_border(x-1, y-1):
                print("wall jump")
                goto(x-1, y-1)
                return
        if has_border(x-1, y):
            print("wall slide")
            goto(x-1, y)
            return
    if get_pixel(x+1, y) == "black":
        if get_pixel(x, y-1) == "white":
            if has_border(x+1, y-1):
                goto(x+1, y-1)
                return
        if has_border(x, y-1):
            goto(x, y-1)
            return
    if get_pixel(x, y+1) == "black":
        if get_pixel(x+1, y) == "white":
            if has_border(x+1, y+1):
                goto(x+1, y+1)
                return
        if has_border(x+1, y):
            goto(x+1, y)
            return

"""


def has_border(x, y):
    if get_pixel(x, y) == "black":
        return False
    if get_pixel(x+1, y) == "black":
        return True
    if get_pixel(x-1, y) == "black":
        return True
    if get_pixel(x, y+1) == "black":
        return True
    if get_pixel(x, y-1) == "black":
        return True
    return False


def exit_handler():
    name = 'debug_'+str(time())
    Screen().getcanvas().postscript(file=name+'.eps', width=420, height=322)
    #EpsImagePlugin.gs_windows_binary =  r'C:\Program Files (x86)\gs\gs10.01.1'
    # Image.open(name+'.eps').save(name+'jpg')


initialize()
draw_borders()
fill_controller()
# follow_borders()
input("a")
exit_handler()
