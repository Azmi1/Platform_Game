import pygame, math
import Destructable_Blocks as DB
import random
import sys

random.seed()

screen = pygame.display.set_mode((1280,1280))

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
        self.cert = pygame.draw.rect(screen, [255,255,255],[self.x,self.y, self.width, self.height])

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

    def Destroy_Blocklings(self, Bullet):
        for Blockling in self.BlocklingsList:
            if Bullet.cert.colliderect(Blockling.cert):
                self.BlocklingsList.remove(Blockling)
                Bullet.Life = True


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
        self.cert = pygame.draw.rect(screen, self.color,[self.x,self.y, self.width, self.height])


    def draw(self, screen):
        pygame.draw.rect(screen, self.color,[self.x,self.y, self.width, self.height])

running = True

Block_1 = Block(0, 0, 1000, 500, 10000)

BlockList = [Block_1]
Aiming = False
BulletList = []
BulletL = {}
BulletC = 0
x = 0
y = 0
x1 = 0
y1 = 0
LineOffset = 75
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
    dy = DB.y1 - DB.y
    dx = DB.x1 - DB.x
    DB.angle = math.atan2(dy, dx)
    pygame.draw.line(screen, cyan, [DB.x, DB.y], [DB.x+DB.LineOffset*round(math.cos(DB.angle),2), DB.y+DB.LineOffset*round(math.sin(DB.angle),2)], 2)
    print("Shhh")

def Release(screen):
    print("Pew**(22/7)")
    if DB.x1 > DB.x:
        DB.OrientX = 1
    elif DB.x1 < DB.x:
        DB.OrientX = -1
    if DB.y1 > DB.y:
        DB.OrientY = -1
    elif DB.y1 < DB.y:
        DB.OrientY = 1
    if DB.x1-DB.x != 0:
        k = (DB.y1-DB.y)/(DB.x1-DB.x)
    else:
        k = 0
    DB.Aiming = False
    DB.BulletL[DB.BulletC] = Bullet(DB.angle, DB.OrientX, DB.OrientY, screen)
    DB.BulletList.append(DB.BulletL[DB.BulletC])
    DB.BulletC += 1


class Bullet(object):
    def __init__(self, angle, OrientX, OrientY, screen):
        self.x = DB.x
        self.y = DB.y
        self.n = DB.y
        self.Life = True
        self.speed = 10
        self.OrientX = OrientX
        self.OrientY = OrientY
        self.cos = round(math.cos(angle),2)
        self.sin = round(math.sin(angle),2)
        print("x: ", str(self.x))
        print("y: ", str(self.y))
        print("speed: ", str(abs(self.speed)))
        print("Orient: ", str(self.OrientX))
        self.cert = pygame.draw.rect(screen, black,[self.x,self.y, 10, 10])

    def move(self):
        self.x += self.speed*self.cos
        self.y += self.speed*self.sin
        #print("x: ", str(self.x))
        #print("y: ", str(self.y))
        #print("speed: ", str(self.speed))
        #print("Orient: ", str(self.OrientX))

    def hit(self, BlockGroup, BulletGroup):
        for i in range(0, len(BlockGroup)):
            if self.cert.colliderect(BlockGroup[i].cert):
                BlockGroup[i].Destroy_Blocklings(self)
                print("Destruction!")
                i += 1
                return i

    def display(self, screen):
        self.cert = pygame.draw.rect(screen, black,[self.x,self.y, 10, 10])

while running == True:
    screen.fill([128,128, 128])
    if BlockList != []:
        for Blocks in BlockList:
            Blocks.draw(screen)
    if pygame.mouse.get_pressed()[0] == True and DB.Aiming == False:
        Gun()
    elif pygame.mouse.get_pressed()[0] == True and DB.Aiming == True:
        Line(screen)
    elif pygame.mouse.get_pressed()[0] == False and DB.Aiming == True:
        Release(screen)
    if BulletList != []:
        for i in range(0, len(BulletList)):
            BulletList[i].move()
            BulletList[i].hit(BlockList, BulletList)
            if BulletList[i].Life == True:
                BulletList[i].display(screen)
            else:
                BulletList.remove(BulletList[i])
                break
    pygame.display.update()
    for event in pygame.event.get():
            if event.type == pygame.QUIT: #For ending the loop
                pygame.quit()
                running = False
                sys.exit()
