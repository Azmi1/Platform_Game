import pygame
import time
import sys
import Classes as C
import Renderer as R
import level as L
import Pysics as Py
import Platform_Game as PG
import Level_Builder as LB

# Creates screen
width = 1680
height = 980
screen = pygame.display.set_mode((width, height))

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

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
Approval = False
Gravity = True
Character_Dead = False

#Load all outside images
image = pygame.image.load("images/player.png").convert_alpha()
icon = pygame.image.load("images/player.ico").convert_alpha()
star = pygame.image.load("images/LoGo.png").convert_alpha()
Animation_Image = pygame.image.load("images/explosion.hasgraphics.png").convert_alpha()
#Background = pygame.image.load("images/background.jpg").convert_alpha()

#Main game loop
def main(): 
    while Running == True:  # Makes a game loop
        PG.Character_Dead = P.Check_For_Life(screen, Character_Dead)
        if Character_Dead == True:
            PG.Close_Game()
        RenderL = PG.RenderL
        for i in range(0, len(PG.PlayerGroup)):
            PG.PlayerGroup[i].move(screen)  # Function that makes player move
            if PG.PlayerGroup[i].Moving == True and PG.PlayerGroup[i].Jumping == True: # Cheks if the gravity will work
                print("I am moving")
            elif PG.PlayerGroup[i].Moving == False and PG.PlayerGroup[i].Jumping == False and PG.Gravity == True: # Cheks if the gravity will work
                print("I am wrong")
                Py.Gravity(PG.PlayerGroup[i])
            Py.Borders(PlayerGroup[i], screen) # Used if players goes under screen
            PG.HitBox = PG.PlayerGroup[i].HitBox(screen)
        if PG.i == 1:
            R.El, PG.i, StarL, L.EnemyGroup = LB.Load_level_1(screen, "custom", P)
            print ("Level loading/creating")
        if PrviZagon == 0:
            PG.RenderL.append(R.El)
            PG.RenderL.append(StarL)
            PG.RenderL.append(L.EnemyGroup)
        #h = len(StarL)
        #i = 0
        #for i in range(0,h-1):
        #    if P.certall.colliderect(StarL[i].cert):
        #        P.Score +=1
        #        print("Tvoj Score:", P.Score)
        #        R.Start_Animation = True
        #        StarL.remove(StarL[i])
        i=0
        j = 0
        x = len(R.E)
        for i in range(0,x): # Checks for any collision with blocks
            for j in range(0,len(PG.PlayerGroup)):
                if PG.PlayerGroup[j].certall.colliderect(R.E[i]):
                    Py.Collision(screen, R.E, R.El, i, PG.PlayerGroup[j], RenderL)
        j = 0
        i = 0
        if L.EnemyGroup != []: # Checks for any collisions with enemies
            for j in range(0, len(L.EnemyGroup)):
                if L.EnemyGroup != []:
                    for i in range(0, len(PG.PlayerGroup)):
                        if PG.PlayerGroup[i].certall.colliderect(L.EnemyGroup[j-1].CertAll):
                            Py.Collision_Enemy(screen, PG.PlayerGroup[i], L.EnemyGroup[j-1], L.EnemyGroup, R.El)
                            if j != 0:
                                j-=1                    
        RenderL = PG.RenderL
        R.Build_screen(screen, PG.PlayerGroup, RenderL, PG.Character_Dead) #Function that renders the scene
        PG.updates += 1
        print("Update: ", updates)
        T2 = time.clock()
        T = T2-PG.t0
        print("Toliko casa minilo: ", T)
        if T > 10 and PG.Approval == True: # System to measure how much loops happened in 10 seconds 
            PS = myfont.render('Updates per 10 seconds:', False, red)
            PG.updates = str(PG.updates)
            PS1 = myfont.render(PG.updates, False, red)
            screen.fill(white)
            screen.blit(PS, [650,490])
            screen.blit(PS1, [650,550])
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #For ending the loop
                PG.Close_Game()
#Prepares all essentials for game loop
P = C.player()
P_2 = C.player_two()
PlayerGroup = [P,P_2]
screen.fill(white)
pygame.display.update()

# Closses the loop
def Close_Game():
    PG.Running = False
    pygame.quit()
    print("I closed")
    sys.exit(0)

#Calls the game loop
main()
