import  pygame, Level_Builder, Second_Classes, random, time
import Options as OPS
import Classes as C
import Randomizer as rand

L = Level_Builder
SC = Second_Classes

# Defines colours
black = [0,0,0]
white = [255,255,255]
red = [255,0,0]
blue =[0,0,255]
green = [0,255,0]
magenta = [255,0,255]

# Loads in image
Block_Image = pygame.image.load("images/Block.jpg")

# Variables needed
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
L.Power_UpsGroup = []
L.El = []
L.El_1 = []
L.Star = {}
L.StarL = []
L.Cant_Enemy = False
L.T1 = time.clock()

def Load_level_1(screen, choice, P, Approval_SpecialDraw, Screen_Diff, ScreeX): #Creates the level
   L.Screen_DiffX = Screen_Diff[0]
   L.Screen_DiffY = Screen_Diff[1]
   if choice == "normal":
        E1 = level(20, 948, 100, 20, black)
        El = [E1]
        L.i = 0
        return El, L.i

   elif choice == "save":
        import Save
        L.El, L.EnemyGroup, PowerUpGroup = Save.Save(screen)
        L.i = 2
        return L.El, L.i, L.StarL, L.EnemyGroup, PowerUpGroup

   elif choice == "custom":
        if L.w == 0:
            Trump_Wall = level(screen, 0, 0-Screen_DiffX, 0-Screen_DiffY, 40, 1680, black, False, True, Block_Image)
            Origin_Block = level(screen, 0, -1-Screen_DiffX, 0-Screen_DiffY, 1, 1, white, True)
            L.Done = level(screen, 0, 1480-Screen_DiffX, 940-Screen_DiffY, 200, 40, green, True)
            E1 = level(screen, 0, OPS.width/2, 948-Screen_DiffY, 100, 20, black, True)
            L.El.append(L.Done)
            L.El.append(E1)
            L.El.append(Origin_Block)
            L.El.append(Trump_Wall)
            L.w = 1
            #for i in range(0, random.randint(2,12)):
            #    print("Haga: ", i)
            #    L.Star[i]=SC.Points(screen)
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
                E[L.st] = level(screen, PrevX1, L.x-ScreeX, L.y, width, height, black, True)
                L.El.append(E[L.st])
                L.st +=1
                L.j == 2
                L.id = 0
                if random.randint(0,100) < 20:
                    Double = {}
                    Double[L.st] = C.Power_Ups(rand.Randomize("Power_Ups"), random.randint(L.x, L.x1), L.y-33)
                    Double[L.st].Hitbox(screen)
                    L.Power_UpsGroup.append(Double[L.st])

        
        if pygame.mouse.get_pressed()[1] == True and L.Cant_Enemy == False: #Middle click to create enemies
            L.x1, L.y1 = pygame.mouse.get_pos()
            Enemy = {}
            Enemy[L.StEnemy] = SC.Enemy(L.x1, L.y1)
            Enemy[L.StEnemy].Hitbox(screen)
            L.EnemyGroup.append(Enemy[L.StEnemy])
            L.StEnemy += 1
            L.T1= time.clock()
            L.Cant_Enemy = True
        if time.clock() - L.T1 > 0.25:
            L.Cant_Enemy = False
        if len(L.El) > 1000:
            L.i = 0
            L.El.remove(L.Done)
        if L.j == 2:
            L.j == 0
        if L.x > 1480 and L.x < 1720 and L.y > 940 and L.y < 1020:
            L.i = 2
            L.El.remove(L.Done)
        return L.El, L.i, L.StarL, L.EnemyGroup, L.Power_UpsGroup
        

class level(SC.Block): # Blocks
    def __init__(self, screen, PrevX1, x, y, width, height, color, CanJumpReg, ImagePresent = 'False', Image = ''): # Puts everything needed for the class
        self.x = x
        self.y = y
        self.PrevX1 = PrevX1
        self.width = width
        self.imagePresent = ImagePresent
        self.image = Image
        self.height = height
        self.color = color
        self.CanCanJumpReg = CanJumpReg
        if ImagePresent == True: # If image is present it automaticly crops it and blit it over block
            screen.blit(self.image,(self.x, self.y),(0,0, self.width, self.height))
        self.rect = pygame.draw.rect(screen, black,[self.x, self.y, self.width, self.height])
        #self.cert = self.create(self.x, self.y, self.width, self.height, self.color, self.imagePresent, self.image).normalize()

    def draw(self, screen, PosX):
        pygame.draw.rect(screen, black,[self.x+PosX, self.y, self.width, self.height])
        if self.imagePresent == True: # If image is present it automaticly crops it and blit it over block
            screen.blit(self.image,(self.x+PosX, self.y),(0,0, self.width, self.height))


    def Special_draw(self,screen, PosX): # Draws the blocks in a special way... ;)
        self.cert = self.create(screen, self.x, self.y, self.width, self.height, self.color, self.imagePresent, self.image).normalize()
        pygame.draw.rect(screen, black,[self.x + PosX , self.y, self.width, self.height])

class star(object): # Old point system
    def __init__(self, screen):
        self.x = random.randint(10,1670)
        self.y = random.randint(10, 970)
        self.image = pygame.image.load("images/LoGo.png")
        self.rect = self.image.get_rect()
        self.cert = pygame.draw.rect(screen, black,[self.x, self.y, 26, 20])
    def draw(self,screen, P):
        self.x = self.x + P.x
        self.cert = pygame.draw.rect(screen, black,[self.x, self.y, 26, 20])
        screen.blit(self.image, (self.x, self.y))
