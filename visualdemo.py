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
                col = (0+5*i, 0+5*i, 255-5*i)
                useful = True
                print("Started coloring in", col, "at", coo_x, coo_y)
                img.putpixel((coo_x, coo_y), col)
                while useful:
                    useful = False
                    for fill_y in range(2-coo_y, 221):
                        for fill_x in range(1, 319):
                            if has_border(fill_x, fill_y, col):
                                img.putpixel((fill_x, fill_y), col)
                                useful = True
                                #print('filled', fill_x, fill_y)
                #img.save(IMGNAME)


COULEURS = {}
LIAISONS = []


def create_graph():
    """
    Crée un graphe à partr de l'image
    """
    i = 0
    for coo_y in range(1, 221):
        for coo_x in range(1, 319):
            if img.getpixel((coo_x, coo_y)) == (0, 0, 0):
                adj_colors = []
                nextcords = [(coo_x+1, coo_y), (coo_x-1, coo_y),
                             (coo_x, coo_y+1), (coo_x, coo_y-1)]
                for nextcord in nextcords:
                    nextcol = img.getpixel(nextcord)
                    adj_colors.append(str(nextcol))
                    if nextcol != (0, 0, 0) and nextcol not in adj_colors:
                        if str(nextcol) not in [k for k in COULEURS]:
                            i += 1
                            COULEURS[str(nextcol)] = str(i)
                for ind1 in range(4):
                    for ind2 in range(4):
                        if ind1 != ind2:
                            if (adj_colors[ind1] != adj_colors[ind2] and adj_colors[ind1] !=
                                    "(0, 0, 0)" and adj_colors[ind2] != "(0, 0, 0)"):
                                liaison = (
                                    COULEURS[adj_colors[ind1]], COULEURS[adj_colors[ind2]])
                                if liaison not in LIAISONS:
                                    LIAISONS.append(liaison)


def color_graph(vertices, edges):
    """
    Colorie le graphe
    """
    colors = [(255, 0, 0), (255, 255, 0), (0, 0, 255), (0, 255, 0)]
    vertex_colors = {}
    for vertex in vertices:
        vertex_colors[vertex] = None
    for vertex in vertices:
        used_colors = set()
        for neighbor in get_neighbors(vertex, edges):
            if vertex_colors[neighbor] is not None:
                used_colors.add(vertex_colors[neighbor])
        for color in colors:
            if color not in used_colors:
                vertex_colors[vertex] = color
                break
    return vertex_colors


def get_neighbors(vertex, edges):
    """
    Cherche les sommets connectés à un sommet du graphe
    """
    neighbors = set()
    for edge in edges:
        if vertex == edge[0]:
            neighbors.add(edge[1])
        elif vertex == edge[1]:
            neighbors.add(edge[0])
    return neighbors


def refill_map(graph):
    """
    Recolorie la carte en 4 couleurs
    """
    data = list(img.getdata())
    for i, pixel in enumerate(data):
        if pixel != (0, 0, 0):
            data[i] = graph[COULEURS[str(pixel)]]
    img.putdata(data)


draw_borders()
fill_controller()
#img = Image.open("image_1683988825.3462548.png")
create_graph()
# print(LIAISONS)
graphe = color_graph(list(COULEURS.values()), LIAISONS)
# print(list(img.getdata()))
refill_map(graphe)

img.save(IMGNAME)
