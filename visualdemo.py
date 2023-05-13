"""Le module PIL (Pillow) permet de modifier une image."""
from time import time  # , sleep
from random import randrange, random, choice
from PIL import Image, ImageDraw

img = Image.new("RGB", (320, 222), "blue")
IMGNAME = "image_"+str(time())+".png"
draw = ImageDraw.Draw(img)
draw.rectangle((0, 0, 319, 221), "white", "black")
# img.save(IMGNAME)


# img.putpixel((coo_x, coo_y), "color")
# img.getpixel(coo_xy)

class Position():
    """
    Classe enregistrant la position et le comportement d'une sorte de mini-turtle.
    """

    def __init__(self, coo_x=0, coo_y=0, heading: float = 0):
        self.coo_x = coo_x
        self.coo_y = coo_y
        self.coo = (coo_x, coo_y)
        self.heading = heading

    def goto(self, coo_x, coo_y):
        """
        Déplace l'instance de Position() à une nouvelle coordinnée
        """
        self.coo_x = coo_x
        self.coo_y = coo_y
        self.coo = (coo_x, coo_y)

    def setheading(self, heading):
        """
        Règle l'angle par rapport à l'horizontal du mini-turtle
        """
        if heading < 0:
            heading += 360
        elif heading > 360:
            heading -= 360
        self.heading = heading

    def validate_next(self):
        """
        Teste si le position devant est valide pour le tracé des lignes
        """
        next_position = Position(self.coo_x, self.coo_y, self.heading)
        next_position.forward()
        if next_position.get() == (255, 255, 255):
            if not (next_position.coo_x > 310 or next_position.coo_x < 10
                    or next_position.coo_y > 212 or next_position.coo_y < 10):
                if (img.getpixel((next_position.coo_x+1, next_position.coo_y)) == (0, 0, 0) and
                        img.getpixel((next_position.coo_x, next_position.coo_y+1)) == (0, 0, 0)):
                    return False
                if (img.getpixel((next_position.coo_x-1, next_position.coo_y)) == (0, 0, 0) and
                        img.getpixel((next_position.coo_x, next_position.coo_y+1)) == (0, 0, 0)):
                    return False
                if (img.getpixel((next_position.coo_x+1, next_position.coo_y)) == (0, 0, 0) and
                        img.getpixel((next_position.coo_x, next_position.coo_y-1)) == (0, 0, 0)):
                    return False
                if (img.getpixel((next_position.coo_x-1, next_position.coo_y)) == (0, 0, 0) and
                        img.getpixel((next_position.coo_x, next_position.coo_y-1)) == (0, 0, 0)):
                    return False
            return True
        return False

    def forward(self, dist=1):
        """
        Déplace l'instance vers la position devant en fonction de l'angle
        """
        for _ in range(dist):
            if self.heading > 292 or self.heading < 68:
                self.goto(self.coo_x+1, self.coo_y)
            elif self.heading > 112 and self.heading < 248:
                self.goto(self.coo_x-1, self.coo_y)
            if self.heading > 23 and self.heading < 157:
                self.goto(self.coo_x, self.coo_y+1)
            elif self.heading > 203 and self.heading < 337:
                self.goto(self.coo_x, self.coo_y-1)

    def place(self, col=(0, 0, 0)):
        """
        Place un pixel d'une couleur donnée dur l'image, aux coordonnées du turtule
        """
        try:
            img.putpixel(self.coo, col)
        except IndexError:
            print("place() failed at position " +
                  str(self.coo) + str(self.heading))

    def get(self):
        """
        Retourne la couleur du pixel à la position de l'instance
        """
        try:
            return img.getpixel(self.coo)
        except IndexError:
            print("get() failed at position " + str(self.coo))


def has_border(coo_x, coo_y, col):
    """
    Détecte si le point de coordonnées (coo_x; coo_y) touche un pixel de couleur col
    """
    if img.getpixel((coo_x, coo_y)) != (255, 255, 255):
        return False
    if img.getpixel((coo_x+1, coo_y)) == col:
        return True
    if img.getpixel((coo_x-1, coo_y)) == col:
        return True
    if img.getpixel((coo_x, coo_y+1)) == col:
        return True
    if img.getpixel((coo_x, coo_y-1)) == col:
        return True
    return False


pos = Position()


def draw_borders():
    """
    Dessine les frontières des régions
    """
    for _ in range(20):
        # cherche un point noir d'où commencer le tracé
        coo_x = randrange(0, 320)
        coo_y = randrange(0, 222)
        while Position(coo_x, coo_y).get() == (255, 255, 255):
            coo_x = randrange(0, 320)
            coo_y = randrange(0, 222)
        pos.goto(coo_x, coo_y)
        # prend un angle apporprié à la position
        if coo_x <= 10:
            pos.setheading(0)
        elif coo_x >= 310:
            pos.setheading(180)
        elif coo_y <= 10:
            pos.setheading(90)
        elif coo_y >= 212:
            pos.setheading(270)
        else:
            pos.setheading(randrange(0, 360))
        # modifie "légèrement" l'angle
        pos.setheading(pos.heading+randrange(-30, 30))
        # print("Initiated line:", pos.coo_x, pos.coo_y, pos.get(), pos.heading)
        # teste si le pixel devant est noir. S'il ne l'est pas, avance.
        while pos.validate_next():
            # print(pos.coo_x, pos.coo_y, pos.get(), pos.heading)
            pos.forward(1)
            pos.place()
            pos.setheading(pos.heading+choice([10*random(), -10*random()]))
        pos.forward(1)
        pos.place()
        # print("Killed line:", pos.coo_x, pos.coo_y, pos.get())


def fill_controller():
    """
    Remplie chaque zone d'une conleur aléatoire
    """
    i = -1
    for coo_y in range(1, 222):
        for coo_x in range(1, 320):
            if img.getpixel((coo_x, coo_y)) == (255, 255, 255):
                i += 1
                col = (0+10*i, 0+10*i, 255-10*i)
                useful = True
                print("Started coloring in", col, "at", coo_x, coo_y)
                img.putpixel((coo_x, coo_y), col)
                while useful:
                    useful = False
                    for fill_y in range(1, 221):
                        for fill_x in range(1, 319):
                            if has_border(fill_x, fill_y, col):
                                img.putpixel((fill_x, fill_y), col)
                                useful = True
                                #print('filled', fill_x, fill_y)
                img.save(IMGNAME)


draw_borders()
fill_controller()
img.save(IMGNAME)
