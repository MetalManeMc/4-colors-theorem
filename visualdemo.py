from PIL import Image, ImageDraw
from time import time
from random import randrange, random, choice
from time import sleep

img = Image.new("RGB", (320, 222), "blue")
imgname = "image_"+str(time())+".png"
draw = ImageDraw.Draw(img)
draw.rectangle((0, 0, 319, 221), "white", "black")
# img.save(imgname)


# img.putpixel((x, y), "color")
# img.getpixel(xy)

class Position():
    def __init__(self, x=0, y=0, heading: float = 0):
        self.x = x
        self.y = y
        self.coo = (x, y)
        self.heading = heading

    def goto(self, x, y):
        self.x = x
        self.y = y
        self.coo = (x, y)

    def setheading(self, heading):
        if heading < 0:
            heading += 360
        elif heading > 360:
            heading -= 360
        self.heading = heading

    def validate_next(self):
        NextPosition = Position(self.x, self.y, self.heading)
        NextPosition.forward()
        if NextPosition.get() == (255, 255, 255):
            if not (NextPosition.x > 310 or NextPosition.x < 10 or NextPosition.y > 212 or NextPosition.y < 10):
                if img.getpixel((NextPosition.x+1, NextPosition.y)) == (0, 0, 0) and img.getpixel((NextPosition.x, NextPosition.y+1)) == (0, 0, 0):
                    return False
                if img.getpixel((NextPosition.x-1, NextPosition.y)) == (0, 0, 0) and img.getpixel((NextPosition.x, NextPosition.y+1)) == (0, 0, 0):
                    return False
                if img.getpixel((NextPosition.x+1, NextPosition.y)) == (0, 0, 0) and img.getpixel((NextPosition.x, NextPosition.y-1)) == (0, 0, 0):
                    return False
                if img.getpixel((NextPosition.x-1, NextPosition.y)) == (0, 0, 0) and img.getpixel((NextPosition.x, NextPosition.y-1)) == (0, 0, 0):
                    return False
            return True
        return False

    def forward(self, l=1):
        for i in range(l):
            if self.heading > 292 or self.heading < 68:
                self.goto(self.x+1, self.y)
            elif self.heading > 112 and self.heading < 248:
                self.goto(self.x-1, self.y)
            if self.heading > 23 and self.heading < 157:
                self.goto(self.x, self.y+1)
            elif self.heading > 203 and self.heading < 337:
                self.goto(self.x, self.y-1)

    def place(self, col=(0, 0, 0)):
        try:
            img.putpixel(self.coo, col)
        except IndexError:
            print("place() failed at position " +
                  str(self.coo) + str(self.heading))

    def get(self):
        try:
            return img.getpixel(self.coo)
        except IndexError:
            print("get() failed at position " + str(self.coo))


pos = Position()


def draw_borders():
    for i in range(20):
        color = "black"
        # cherche un point noir d'où commencer le tracé
        x = randrange(0, 320)
        y = randrange(0, 222)
        while Position(x, y).get() == (255, 255, 255):
            x = randrange(0, 320)
            y = randrange(0, 222)
        pos.goto(x, y)
        # prend un angle apporprié à la position
        if x <= 10:
            pos.setheading(0)
        elif x >= 310:
            pos.setheading(180)
        elif y <= 10:
            pos.setheading(90)
        elif y >= 212:
            pos.setheading(270)
        else:
            pos.setheading(randrange(0, 360))
        # modifie "légèrement" l'angle
        pos.setheading(pos.heading+randrange(-30, 30))
        # print("Initiated line:", pos.x, pos.y, pos.get(), pos.heading)
        # teste si le pixel devant est noir. S'il ne l'est pas, avance.
        while pos.validate_next():
            #print(pos.x, pos.y, pos.get(), pos.heading)
            pos.forward(1)
            pos.place()
            pos.setheading(pos.heading+choice([10*random(), -10*random()]))
        pos.forward(1)
        pos.place()
        # print("Killed line:", pos.x, pos.y, pos.get())


draw_borders()
img.save(imgname)
