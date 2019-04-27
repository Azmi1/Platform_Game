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

F = open("Save.py", "w+")
F.write("import Level_Builder as L")
F.write("\n")
F.write("import Second_Classes as SC")
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
F.write("\n")
F.write("def Save(screen):")
F.write("\n")
F.write("   B = {}")
F.write("\n")
F.write("   Enemy = {}")
F.write("\n")
F.write("   Trump_Wall = L.level(0, 0, 0, 40, 1680, black, False)")
F.write("\n")
F.write("   Done = L.level(0, 1480, 940, 200, 40, green, True)")
F.write("\n")
F.write("   Origin_Block = L.level(0, -1, 0, 1, 1, white, True)")
F.write("\n")
F.write("   E1 = L.level(0,40, 948, 100, 20, black, True)")
F.write("\n")
F.write("   BlockGroup.append(Done)")
F.write("\n")
F.write("   BlockGroup.append(E1)")
F.write("\n")
F.write("   BlockGroup.append(Origin_Block)")
F.write("\n")
F.write("   BlockGroup.append(Trump_Wall)")
F.write("\n")

Chose = "LoL"
Move = "Neutral"

running = True

white = [255, 255, 255]
blue = [0, 0, 255]
black = [0, 0, 0]
red = [255, 0, 0]

custom = [10,10,220, 52]
left = [10,918, 105, 52]
right = [125,918, 105, 52]

# For custom rectangles
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
Break_Point = False
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
            F.write("   B[" + str(st) + "] = L.level("+ str(PrevX1)+ ", " + str(x+(1680*Page)) + ", " + str(y) + ", " + str(width)+ ", " + str(height) + ", " + str(black)+ ", " + str(True) + ")")
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

while running == True:
    screen.fill(white)
    surf_1.fill(white)
    surf_2.fill(black)
    pygame.draw.rect(surf_2, white, custom)
    pygame.draw.rect(surf_2, white, left)
    pygame.draw.rect(surf_2, white, right)
    PS = myfont.render('Custom block', False, red)
    surf_2.blit(PS, (custom[0]+15,custom[1]+5))
    PS = myfont.render('<-----', False, red)
    surf_2.blit(PS, (left[0]+15,left[1]+5))
    PS = myfont.render('----->', False, red)
    surf_2.blit(PS, (right[0]+15,right[1]+5))
    #PS = myfont.render(str(x)+ " " + str(y), False, red)
    #surf_1.blit(PS, (10,20))
    print("Loop went away")
    print("Choice: " + Chose)
    if pygame.mouse.get_pressed()[0] == True and Break_Point == False:
        x, y = pygame.mouse.get_pos()
        Break_Point = True
        print("Checking for interactions")
        print(str(x)+ " " + str(y))
        if x >= custom[0] + 1680 and x <= custom[0] + custom[2] + 1680 and y >= custom[1] and y <= custom[1]+custom[3]:
            print("I interacted with custom")
            Chose = "Custom"
        elif x >= left[0] + 1680 and x <= left[0] + left[2] + 1680 and y >= left[1] and y <= left[1]+left[3]:
            print("I interacted with left")
            Move = "left"
            Page -= 1
        elif x >= right[0] + 1680 and x <= right[0] + 1680 + right[2] and y >= right[1] and y <= right[1] + right[3]:
            print("I interacted with right")
            Move = "right"
            Page+= 1
    
    if time.clock()-T2 > 1:
        T2 = time.clock()
        Break_Point = False
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
