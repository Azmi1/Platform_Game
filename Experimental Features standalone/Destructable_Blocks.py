import pygame
import Destructable_Blocks as DB
import random

random.seed()

screen = pygame.display.set_mode((1280,1280))

Block_Image = pygame.image.load("Images/Block.jpg")

black = [0, 0, 0]
white = [255, 255, 255]
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
cyan = [0, 255, 255]
ColorList = [black, white, red, green, blue, cyan]
ColN = 0

DB.Xi = 0
DB.Yi = 0
DB.Cycle = 0

class Block(object):
    def __init__(self, x, y, width, height, accuracy):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.OGaccuracy = accuracy
        self.accuracy = accuracy*accuracy
        self.Blockling = {}
        self.BlocklingsList = []
        self.Blaster()
        self.DrawMode = "Seperate"

    def Blaster(self):
        DB.Xi = 0
        DB.Yi = 0
        DB.Cycle = 0
        for i in range(0, self.accuracy):
            Bheight = self.height/self.OGaccuracy
            x = self.x + (self.width/self.OGaccuracy)*DB.Xi
            y = self.y + (Bheight)*DB.Yi
            DB.Cycle += 1
            if DB.Cycle >= self.OGaccuracy:
                DB.Cycle = 0
                DB.Yi += 1
                DB.Xi = -1
            self.Blockling[i] = Blocklings(x, y, self.width/self.OGaccuracy, Bheight)
            self.BlocklingsList.append(self.Blockling[i])
            DB.Xi += 1

    def draw(self, screen):
        if self.DrawMode == "Combined":
            pygame.draw.rect(screen, [255,255,255],[self.x,self.y, self.width, self.height])
        elif self.DrawMode == "Seperate":
            for i in range(0, len(self.BlocklingsList)):
                self.BlocklingsList[i].draw(screen)

class Blocklings(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = ColorList[DB.ColN]
        DB.ColN += 1
        if DB.ColN == 6:
            DB.ColN = 0


    def draw(self, screen):
        pygame.draw.rect(screen, self.color,[self.x,self.y, self.width, self.height])

running = True

Block_1 = Block(0, 0, 1000, 500, 100)

Aiming = False
BulletList = []
BulletL = {}
BulletC = 0
x = 0
y = 0
x1 = 0
y1 = 0
LineOffset = 1000
OrientX = 0
OrientY = 0

def Gun():
    DB.x, DB.y = pygame.mouse.get_pos()
    DB.Aiming = True
    print("Gun")

def Line(screen):
    DB.x1, DB.y1 = pygame.mouse.get_pos()
    if DB.x1 > DB.x + DB.LineOffset:
        DB.x1 = DB.x + DB.LineOffset
        Orient = 1
    elif DB.x1 < DB.x - DB.LineOffset:
        DB.x1 = DB.x - DB.LineOffset
        Orient = -1
    if DB.y1 > DB.y + DB.LineOffset:
        DB.y1 = DB.y + DB.LineOffset
    elif DB.y1 < DB.y - DB.LineOffset:
        DB.y1 = DB.y - DB.LineOffset
    pygame.draw.line(screen, cyan, [DB.x, DB.y], [DB.x1, DB.y1], 2)
    print("Shhh")

def Release():
    print("Pew**(22/7)")
    k = (DB.y1-DB.y)/(DB.x1-DB.x)
    if DB.x1 > DB.x:
        DB.OrientX = 1
    elif DB.x1 < DB.x:
        DB.OrientX = -1
    if DB.y1 > DB.y:
        DB.OrientY = -1
    elif DB.y1 < DB.y:
        DB.OrientY = 1
    DB.Aiming = False
    DB.BulletL[DB.BulletC] = Bullet(k, DB.OrientX, DB.OrientY)
    DB.BulletList.append(DB.BulletL[DB.BulletC])
    DB.BulletC += 1


class Bullet(object):
    def __init__(self, k, OrientX, OrientY):
        self.x = DB.x
        self.y = DB.y
        self.n = DB.y
        self.k = k
        self.speed = 10* OrientX
        self.MoveY = -1*(((self.k*self.x +self.n))-((self.k*(self.x+self.speed) +self.n)))
        self.OrientX = OrientX
        self.OrientY = OrientY
        print("x: ", str(self.x))
        print("y: ", str(self.y))
        print("MoveY: ", str(self.MoveY))
        print("speed: ", str(self.speed))
        print("Orient: ", str(self.OrientX))

    def move(self):
        self.x += self.speed
        self.y += self.MoveY
        print("x: ", str(self.x))
        print("y: ", str(self.y))
        print("MoveY: ", str(self.MoveY))
        print("speed: ", str(self.speed))
        print("Orient: ", str(self.OrientX))

    def display(self, screen):
        pygame.draw.rect(screen, black,[self.x,self.y, 10, 10])

while running == True:
    screen.fill([128,128, 128])
    Block_1.draw(screen)
    if pygame.mouse.get_pressed()[0] == True and DB.Aiming == False:
        Gun()
    elif pygame.mouse.get_pressed()[0] == True and DB.Aiming == True:
        Line(screen)
    elif pygame.mouse.get_pressed()[0] == False and DB.Aiming == True:
        Release()
    if BulletList != []:
        for i in range(0, len(BulletList)):
            BulletList[i].move()
            BulletList[i].display(screen)
    pygame.display.update()
    for event in pygame.event.get():
            if event.type == pygame.QUIT: #For ending the loop
                pygame.quit()
                running = False
