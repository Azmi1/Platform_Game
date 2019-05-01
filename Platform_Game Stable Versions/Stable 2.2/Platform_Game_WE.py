import pygame, time
import Platform_Game_WE as PGW
import Second_Classes as SC
import sys, Tab

width = 1920
height = 980

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

screen = pygame.display.set_mode((width, height))
surf_1 = screen.subsurface(0,0,1680,980)
surf_2 = screen.subsurface(1680, 0, 240, 980)

F = open("Save.py", "w+")
F.write("import Level_Builder as L")
F.write("\n")
F.write("import Second_Classes as SC")
F.write("\n")
F.write("import os, pygame")
F.write("\n")
F.write("\n")
F.write("black = [0,0,0]")
F.write("\n")
F.write("white = [255,255,255]")
F.write("\n")
F.write("red = [255,0,0]")
F.write("\n")
F.write("blue =[0,0,255]")
F.write("\n")
F.write("green = [0,255,0]")
F.write("\n")
F.write("magenta = [255,0,255]")
F.write("\n")
F.write("\n")
F.write("BlockGroup = []")
F.write("\n")
F.write("EnemyGroup = []")
F.write("\n")
F.write("picture = {}")
F.write("\n")
F.write("Pictures = []")
F.write("\n")
F.write("st = 0")
F.write("\n")
F.write("\n")
F.write("entries = os.listdir('images/block_textures')")
F.write("\n")
F.write("for entry in entries:")
F.write("\n")
F.write("   picture[st] = pygame.image.load("+ "'"'images/block_textures/'"'"+"+entry).convert_alpha()")
F.write("\n")
F.write("   Pictures.append(picture[st])")
F.write("\n")
F.write("   st+=1")
F.write("\n")
F.write("def Save(screen):")
F.write("\n")
F.write("   B = {}")
F.write("\n")
F.write("   Enemy = {}")
F.write("\n")
F.write("   Trump_Wall = L.level(0, 0, 0, 40, 1680, black, False)")
F.write("\n")
F.write("   Origin_Block = L.level(0, -1, 0, 1, 1, white, True)")
F.write("\n")
F.write("   E1 = L.level(0,40, 948, 100, 20, black, True)")
F.write("\n")
F.write("   BlockGroup.append(E1)")
F.write("\n")
F.write("   BlockGroup.append(Origin_Block)")
F.write("\n")
F.write("   BlockGroup.append(Trump_Wall)")
F.write("\n")

Chose = "Normal"
Move = "Neutral"

running = True

R = 0
G = 0
B = 0

white = [255, 255, 255]
blue = [0, 0, 255]
black = [0, 0, 0]
red = [255, 0, 0]

custom = [10,10,220, 52]
left = [10,918, 105, 52]
right = [125,918, 105, 52]

# For custom rectangles
Image = False
Id = 0
st = 0
x = 0
y = 0
j = 1
Page = 0
BlockGroup = []
EnemyGroup = []
T1 = time.clock()
T2 = time.clock()
T3 = time.clock()
Break_Point = False
Break_Point_Fast = False
Cant_Enemy = False
StEnemy = 0

def Custom():
    print("Custom Loop went away")
    x, y = pygame.mouse.get_pos()
    if not(x >= 1680):
        if pygame.mouse.get_pressed()[0] == True: #Left Click and drag to draw
            if PGW.Id == 0:
                PGW.x, PGW.y = pygame.mouse.get_pos()
                print (PGW.x)
                print (PGW.y)
                PGW.j = 1
                PGW.Id = 1
        if pygame.mouse.get_pressed()[2] == True: #Left Click and drag to draw
            if PGW.Id == 1:
                B = {}
                x1, y1 = pygame.mouse.get_pos()
                if PGW.x > x1:
                    Tx =PGW.x
                    PGW.x = x1
                    x1 = Tx
                if PGW.y > y1:
                    Ty =PGW.y
                    PGW.y = y1
                    y1 = Ty
                print (x1)
                print (y1)
                PrevX1 = x1
                width = x1 - PGW.x
                height = y1 - PGW.y
                x = PGW.x
                y = PGW.y
                if PGW.Image == False:
                    B[st] = level(PrevX1, x, y, width, height, [Tab.R, Tab.G, Tab.B], True)
                    F.write("   B[" + str(st) + "] = L.level("+ str(PrevX1)+ ", " + str(x+(1680*Page)) + ", " + str(y) + ", " + str(width)+ ", " + str(height) + ", [" + str(Tab.R) + ", " + str(Tab.G) + ", " + str(Tab.B) + "], " + str(True) + ")")
                    F.write("\n")
                elif PGW.Image == True:
                    B[st] = level(PrevX1, x, y, width, height, black, True, True, Tab.Pictures[Tab.Picture_ID])
                    F.write("   B[" + str(st) + "] = L.level("+ str(PrevX1)+ ", " + str(x+(1680*Page)) + ", " + str(y) + ", " + str(width)+ ", " + str(height) + ", " + str(black)+ ", " + str(True) + ", " + str(True) + ", " + "Pictures[" + str(Tab.Picture_ID) + "]" + ")")
                    F.write("\n")
                BlockGroup.append(B[PGW.st])
                F.write("   BlockGroup.append(B[" + str(PGW.st) + "])")
                F.write("\n")
                PGW.st +=1
                PGW.j == 2
                PGW.Id = 0
        if pygame.mouse.get_pressed()[1] == True and PGW.Cant_Enemy == False:
            PGW.x1, PGW.y1 = pygame.mouse.get_pos()
            Enemy = {}
            Enemy[PGW.StEnemy] = SC.Enemy(PGW.x1, PGW.y1)
            F.write("   Enemy[" + str(PGW.StEnemy) + "] = SC.Enemy(" + str(PGW.x1+(1680*Page)) + ", "+ str(PGW.y1) + ")")
            F.write("\n")
            Enemy[PGW.StEnemy].Hitbox(screen)
            F.write("   Enemy[" + str(PGW.StEnemy) + "].Hitbox(screen) ")
            F.write("\n")
            PGW.EnemyGroup.append(Enemy[PGW.StEnemy])
            F.write("   EnemyGroup.append(Enemy[" + str(PGW.StEnemy) + "])")
            F.write("\n")
            PGW.StEnemy += 1
            PGW.T1= time.clock()
            PGW.Cant_Enemy = True
    if time.clock() - PGW.T1 > 0.25:
        PGW.Cant_Enemy = False
class level(SC.Block): # Blocks
    def __init__(self, PrevX1, x, y, width, height, color, CanJumpReg, ImagePresent = 'False', Image = ''): # Puts everything needed for the class
        self.x = x
        self.y = y
        self.PrevX1 = PrevX1
        self.width = width
        self.imagePresent = ImagePresent
        self.image = Image
        self.height = height
        self.color = color
        self.CanCanJumpReg = CanJumpReg
    def draw(self,screen, P): # Draws the blocks
        self.cert = self.create(screen, self.x + P.CameraX, self.y, self.width, self.height, self.color, self.imagePresent, self.image).normalize()
    def Special_draw(self,screen): # Draws the blocks in a special way... ;)
        self.cert = self.create(screen, self.x, self.y, self.width, self.height, self.color, self.imagePresent, self.image).normalize()

Trump_Wall = level(0, 0, 0, 40, 1680, black, False)
Origin_Block = level(0, -1, 0, 1, 1, white, True)
Starting_Block = level(0,40, 948, 100, 20, black, True)
BlockGroup.append(Trump_Wall)
BlockGroup.append(Origin_Block)
BlockGroup.append(Starting_Block)

while running == True:
    screen.fill(white)
    surf_1.fill(white)
    surf_2.fill(black)
    Tab.State(Chose, surf_1, surf_2)
    #PS = myfont.render(str(x)+ " " + str(y), False, red)
    #surf_1.blit(PS, (10,20))
    print("Loop went away")
    print("Choice: " + Chose)
    if time.clock()-T2 > 1:
        T2 = time.clock()
        Break_Point = False
    if time.clock()-T3 > 0.38:
        T3 = time.clock()
        Break_Point_Fast = False
    if Chose == "Custom":
        Custom()
    if Move == "right":
        Move = "Neutral"
        if BlockGroup != []:
            for i in range(0, len(BlockGroup)):
                BlockGroup[i].x -= 1680
        if EnemyGroup != []:
            for i in range(0, len(EnemyGroup)):
                EnemyGroup[i].x -= 1680
    if Move == "left":
        Move = "Neutral"
        if BlockGroup != []:
            for i in range(0, len(BlockGroup)):
                BlockGroup[i].x += 1680
        if EnemyGroup != []:
            for i in range(0, len(EnemyGroup)):
                EnemyGroup[i].x += 1680
    if BlockGroup != []:
        for i in range(0, len(BlockGroup)):
            BlockGroup[i].Special_draw(surf_1)
    if EnemyGroup != []:
        for i in range(0, len(EnemyGroup)):
            EnemyGroup[i].Special_Display(surf_1)
    pygame.display.update()
    for event in pygame.event.get():
            if event.type == pygame.QUIT: #For ending the loop
                F.write("   return BlockGroup, EnemyGroup")
                PGW.running = False
                F.close()
                pygame.quit()
                print("I closed")
                sys.exit(0)
