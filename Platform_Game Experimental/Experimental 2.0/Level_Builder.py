import  pygame, Level_Builder, Second_Classes, random

L = Level_Builder
SC = Second_Classes

black = [0,0,0]
white = [255,255,255]
red = [255,0,0]
blue =[0,0,255]
green = [0,255,0]
magenta = [255,0,255]

Block_Image = pygame.image.load("images/Block.jpg")

L.x = 0
L.x1 = 0
L.y = 0
L.y1 = 0
L.j = 0
L.st = 2
L.StEnemy = 0
L.i = 1
L.id = 0
L.w = 0
L.EnemyGroup = []
L.El = []
L.El_1 = []
L.Star = {}
L.StarL = []

def Load_level_1(screen, choice, P): #Creates the level
    if choice == "normal":
        E1 = level(20, 948, 100, 20, black)
        El = [E1]
        L.i = 0
        return El, L.i
    elif choice == "custom":
        if L.w == 0:
            Trump_Wall = level(0, 0, 0, 40, 1680, black, False, True, Block_Image)
            Origin_Block = level(0, -1, 0, 1, 1, white, True)
            L.Done = level(0, 1480, 940, 200, 40, green, True)
            E1 = level(0,40, 948, 100, 20, black, True)
            L.El.append(L.Done)
            L.El.append(E1)
            L.El.append(Origin_Block)
            L.El.append(Trump_Wall)
            L.w = 1
            Done.cert = Done.draw(screen, P)
            #for i in range(0, random.randint(2,12)):
            #    print("Haga: ", i)
            #    L.Star[i]=SC.Points()
            #    L.StarL.append(L.Star[i])
        if pygame.mouse.get_pressed()[0] == True: #Left Click and drag to draw
            if L.id == 0:
                L.x, L.y = pygame.mouse.get_pos()
                print (L.x)
                print (L.y)
                L.j = 1
                L.id = 1
        if pygame.mouse.get_pressed()[2] == True: #Left Click and drag to draw
            if L.id == 1:
                E = {}
                Enemy = {}
                L.x1, L.y1 = pygame.mouse.get_pos()
                if L.x > L.x1:
                    Tx =L.x
                    L.x = L.x1
                    L.x1 = Tx
                if L.y > L.y1:
                    Ty =L.y
                    L.y = L.y1
                    L.y1 = Ty
                print (L.x1)
                print (L.y1)
                PrevX1 = L.x1
                width = L.x1 - L.x
                height = L.y1 - L.y
                E[L.st] = level(PrevX1, L.x, L.y, width, height, black, True)
                RandProc = random.randint(1,100)
                if RandProc > 75:
                    Enemy[L.StEnemy] = SC.Enemy(E[L.st])
                    Enemy[L.StEnemy].Hitbox(screen)
                    L.EnemyGroup.append(Enemy[L.StEnemy])
                if len(L.El) < 1000:
                    L.El.append(E[L.st])
                L.st +=1
                L.j == 2
                L.id = 0
        
        if len(L.El) > 1000:
            L.i = 0
            L.El.remove(L.Done)
        if L.j == 2:
            L.j == 0
        if L.x > 1480 and L.x < 1720 and L.y > 940 and L.y < 1020:
            L.i = 2
            L.El.remove(L.Done)
        return L.El, L.i, L.StarL, L.EnemyGroup

class level(SC.Block):
    def __init__(self, PrevX1, x, y, width, height, color, CanJumpReg, ImagePresent = 'False', Image = ''):
        self.x = x
        self.y = y
        self.PrevX1 = PrevX1
        self.width = width
        self.imagePresent = ImagePresent
        self.image = Image
        self.height = height
        self.color = color
        self.CanCanJumpReg = CanJumpReg
    def draw(self,screen, P):
        self.cert = self.create(screen, self.x + P.CameraX, self.y, self.width, self.height, self.color, self.imagePresent, self.image).normalize()
    def Special_draw(self,screen):
        self.cert = self.create(screen, self.x, self.y, self.width, self.height, self.color, self.imagePresent, self.image).normalize()

class star(object):
    def __init__(self, screen):
        self.x = random.randint(10,1670)
        self.y = random.randint(10, 970)
        self.image = pygame.image.load("images/LoGo.png")
        self.rect = self.image.get_rect()
        self.cert = pygame.draw.rect(screen, black,[self.x, self.y, 26, 20])
    def draw(self,screen, P):
        self.x = self.x + P.CameraX
        self.cert = pygame.draw.rect(screen, black,[self.x, self.y, 26, 20])
        screen.blit(self.image, (self.x, self.y))