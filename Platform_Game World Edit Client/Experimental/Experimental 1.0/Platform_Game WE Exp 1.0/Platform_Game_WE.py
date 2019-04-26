import pygame, time
import Platform_Game_WE as PGW
import Second_Classes as SC
import sys

width = 1920
height = 980

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

screen = pygame.display.set_mode((width, height))
surf_1 = screen.subsurface(0,0,1680,980)
surf_2 = screen.subsurface(1680, 0, 240, 980)

F = open("Save_1.py", "w+")

Chose = "LoL"

running = True

white = [255, 255, 255]
blue = [0, 0, 255]
black = [0, 0, 0]
red = [255, 0, 0]

custom = [10,10,220, 52]


# For custom rectangles
Id = 0
st = 0
x = 0
y = 0
j = 1
BlockGroup = []
EnemyGroup = []
T1 = time.clock()
Cant_Enemy = False
StEnemy = 0

def Custom():
    print("Custom Loop went away")
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
            B[st] = level(PrevX1, x, y, width, height, black, True)
            F.write("level("+ str(PrevX1)+ ", " + str(x) + ", " + str(y) + ", " + str(width)+ ", " + str(height) + ", " + str(black)+ ", " + str(True) + ")")
            F.write("\n")
            BlockGroup.append(B[PGW.st])
            PGW.st +=1
            PGW.j == 2
            PGW.Id = 0
    if pygame.mouse.get_pressed()[1] == True and PGW.Cant_Enemy == False:
        PGW.x1, PGW.y1 = pygame.mouse.get_pos()
        Enemy = {}
        Enemy[PGW.StEnemy] = SC.Enemy(PGW.x1, PGW.y1)
        F.write("SC.Enemy(" + str(PGW.x1) + ", "+ str(PGW.y1) + ")")
        F.write("\n")
        Enemy[PGW.StEnemy].Hitbox(screen)
        PGW.EnemyGroup.append(Enemy[PGW.StEnemy])
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

while running == True:
    screen.fill(white)
    surf_1.fill(white)
    surf_2.fill(black)
    pygame.draw.rect(surf_2, white, custom)
    PS = myfont.render('Custom block', False, red)
    surf_2.blit(PS, (25,15))
    print("Loop went away")
    if pygame.mouse.get_pressed()[0] == True:
        x, y = pygame.mouse.get_pos()
        print("Checking for interactions")
        if x >= custom[0] + 1680 and x <= custom[2] + 1680 and y >= custom[1] and y <= custom[3]:
            print("I interacted with custom")
            Chose = "Custom"
    if Chose == "Custom":
        Custom()
    if BlockGroup != []:
        for i in range(0, len(BlockGroup)):
            BlockGroup[i].Special_draw(surf_1)
    if EnemyGroup != []:
        for i in range(0, len(EnemyGroup)):
            EnemyGroup[i].Special_Display(surf_1)
    pygame.display.update()
    for event in pygame.event.get():
            if event.type == pygame.QUIT: #For ending the loop
                PGW.running = False
                F.close()
                pygame.quit()
                print("I closed")
                sys.exit(0)