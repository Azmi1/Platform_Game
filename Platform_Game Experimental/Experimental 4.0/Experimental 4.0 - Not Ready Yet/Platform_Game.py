import pygame
import time
import sys
import Classes as C
import Renderer as R
import level as L
import Pysics as Py
import Platform_Game as PG
import Level_Builder as LB
import Options as OPS

# Creates screen
width = 1680
height = 980
screen = pygame.display.set_mode((OPS.width, OPS.height))


pygame.font.init()
myfont = pygame.font.SysFont('Times New Roman', 30)

# Colours:
black = [0,0,0] 
white = [255,255,255]
red = [255,0,0]
blue =[0,0,255]
green = [0,255,0]
magenta = [255,0,255]

#Variables for who knows what:
i = 1
PrviZagon = 0
RenderL=[]
Running = True
updates = 0
t0 = time.clock()
tFPS = time.clock()
Approval = OPS.Approval_FPS
Gravity = OPS.Gravity
Character_Dead = False
PlayerTwoJoined = False
Approval_SpecialDraw = OPS.Approval_SpecialDraw
Screen_DiffX = 0
Screen_DiffY = 0
Screen_Diff = []
PG.FPS = []
ScreenX = 0
#Load all outside images
image = pygame.image.load("images/player.png").convert_alpha()
icon = pygame.image.load("images/player.ico").convert_alpha()
star = pygame.image.load("images/LoGo.png").convert_alpha()
Animation_Image = pygame.image.load("images/explosion.hasgraphics.png").convert_alpha()
#Background = pygame.image.load("images/background.jpg").convert_alpha()

def Set_Up():
    if OPS.width != 1680:
        PG.Screen_DiffX = 1680 - OPS.width
        P.CameraPosX = OPS.width/2
    if OPS.height!= 980:
        PG.Screen_DiffY = 980 - OPS.height
        P.y -= PG.Screen_DiffY
    PG.Screen_Diff.append(PG.Screen_DiffX)
    PG.Screen_Diff.append(PG.Screen_DiffY)
    main()

def Get_Screen():
    MoveX = PlayerGroup[0].MoveX
    PG.ScreenX += MoveX

#Main game loop
def main(): 
    while Running == True:  # Makes a game loop
        if PG.PlayerTwoJoined == False:
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT] or key[pygame.K_UP] or key[pygame.K_RIGHT] or key[pygame.K_DOWN]:
                P_2 = C.player_two()
                PlayerGroup.append(P_2)
                PG.PlayerTwoJoined = True
        PG.Character_Dead = P.Check_For_Life(screen, Character_Dead)
        if Character_Dead == True:
            PG.Close_Game()
        RenderL = PG.RenderL
        for i in range(0, len(PG.PlayerGroup)):
            PG.PlayerGroup[i].Status()
            PG.PlayerGroup[i].move(screen)  # Function that makes player move
            if PG.PlayerGroup[i].Moving == True and PG.PlayerGroup[i].Jumping == True: # Cheks if the gravity will work
                print("I am moving")
            elif PG.PlayerGroup[i].Moving == False and PG.PlayerGroup[i].Jumping == False and PG.Gravity == True: # Cheks if the gravity will work
                print("I am wrong")
                Py.Gravity(PG.PlayerGroup[i])
            Py.Borders(PlayerGroup[i], screen) # Used if players goes under screen
            PG.HitBox = PG.PlayerGroup[i].HitBox(screen)
        if PG.i == 1:
            R.El, PG.i, StarL, L.EnemyGroup, LB.Power_UpsGroup = LB.Load_level_1(screen, OPS.Mode, P, Approval_SpecialDraw, PG.Screen_Diff, R.ScreeX)
            print ("Level loading/creating")
            if LB.Power_UpsGroup != []:
                for i in range(0, len(LB.Power_UpsGroup)):
                    LB.Power_UpsGroup[i].Hitbox(screen)
        #PG.ScreenX = PG.Get_Screen()
        ScreenXY = [PG.ScreenX]
        if PG.PrviZagon == 0:
            PG.RenderL.append(R.El)
            PG.RenderL.append(StarL)
            PG.RenderL.append(L.EnemyGroup)
            PG.RenderL.append(LB.Power_UpsGroup)
            PS = myfont.render('FPS:', False, red)
            PS1 = myfont.render('Null', False, red)
            PG.FPS = []
            FPS.append(PS)
            FPS.append(PS1)
        #h = len(StarL)
        #i = 0
        #for i in range(0,h-1):
        #    if P.certall.colliderect(StarL[i].cert):
        #        P.Score +=1
        #        print("Tvoj Score:", P.Score)
        #        R.Start_Animation = True
        #        StarL.remove(StarL[i])
        if PG.PrviZagon == 0:
            PG.PrviZagon = 1
        i=0
        j = 0
        x = len(R.E)
        for i in range(0,x):  # Checks for any collision with blocks
            for j in range(0,len(PG.PlayerGroup)):
                if PG.PlayerGroup[j].certall.colliderect(R.E[i]):
                    Py.Collision(screen, R.E, R.El, i, PG.PlayerGroup[j], RenderL)
        j = 0
        i = 0
        if L.EnemyGroup != []:  # Checks for any collisions with enemies
            for j in range(0, len(L.EnemyGroup)):
                if L.EnemyGroup != []:
                    i = 0
                    print("Stevilo kvadratov: " + str(len(L.EnemyGroup)))
                    for i in range(0, len(PG.PlayerGroup)):
                        if not(j < 0) and not(j > len(L.EnemyGroup)) and not(i < 0) and not(i > len(PlayerGroup)) and PG.PlayerGroup[i].certall.colliderect(L.EnemyGroup[j-1].CertAll):
                            Py.Collision_Enemy(screen, PG.PlayerGroup[i], L.EnemyGroup[j-1], L.EnemyGroup, R.El)
                            if j == len(L.EnemyGroup):
                                break                
        if LB.Power_UpsGroup != []:
            for j in range(0, len(LB.Power_UpsGroup)):
                for i in range(0, len(PG.PlayerGroup)):
                   Py.Collision_Power_Ups(PG.PlayerGroup[i], LB.Power_UpsGroup[j], LB.Power_UpsGroup) 
            Breaky = False
            for j in range (0, len(LB.Power_UpsGroup)):
                Breaky = LB.Power_UpsGroup[j].Self_Destruct(LB.Power_UpsGroup)
                if Breaky == True:
                    break
        RenderL = PG.RenderL
        PG.updates += 1
        print("Update: ", updates)
        T2 = time.clock()
        PG.TFPS = T2 - PG.tFPS
        T = T2-PG.t0
        print("Toliko casa minilo: ", T)
        print("TFPS: ", PG.TFPS)
        if PG.TFPS > 1 and PG.Approval == True:  # System to measure how much loops happened in 10 seconds
            PS = myfont.render('FPS:', False, red)
            PS1 = myfont.render(str(PG.updates), False, red)
            PG.updates = 0
            PG.FPS = []
            PG.tFPS = time.clock()
            PG.TFPS = 0
            FPS.append(PS)
            FPS.append(PS1)
        R.Build_screen(screen, PG.PlayerGroup, RenderL, PG.Character_Dead, Approval_SpecialDraw, PG.FPS)  # Function that renders the scene
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #For ending the loop
                PG.Close_Game()
#Prepares all essentials for game loop
P = C.player(Approval_SpecialDraw)
Camera = C.camera(P)
PlayerGroup = [P]
screen.fill(white)
pygame.display.update()

# Closses the loop
def Close_Game():
    PG.Running = False
    pygame.quit()
    print("I closed")
    sys.exit(0)

#Calls the game loop
Set_Up()
