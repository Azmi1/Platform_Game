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

#Load all outside images
image = pygame.image.load("images/player.png").convert_alpha()
icon = pygame.image.load("images/player.ico").convert_alpha()
star = pygame.image.load("images/LoGo.png").convert_alpha()
Animation_Image = pygame.image.load("images/explosion.hasgraphics.png").convert_alpha()
#Background = pygame.image.load("images/background.jpg").convert_alpha()

#Main game loop
def main(): 
    while Running == True:  # Makes a game loop
        RenderL = PG.RenderL
        P.move(screen, P)  # Function that makes player move
        if P.Moving == True and P.Jumping == True:
            print("I am moving")
        elif P.Moving == False and P.Jumping == False and PG.Gravity == True:
            print("I am wrong")
            Py.Gravity(P)
        if PG.i == 1:
            R.El, PG.i, StarL, L.EnemyGroup = LB.Load_level_1(screen, "custom", P)
            print ("Level loading/creating")
        HitBoxes = P.HitBox(screen)
        if PrviZagon == 0:
            PG.RenderL.append(R.El)
            PG.RenderL.append(StarL)
            PG.RenderL.append(HitBoxes)
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
        x = len(R.E)
        for i in range(0,x):
            if P.certall.colliderect(R.E[i]):
                Py.Collision(screen, HitBoxes, R.E, R.El, i, P, RenderL)
        if L.EnemyGroup != []:
            for i in range(0, len(L.EnemyGroup)):
                if P.certall.colliderect(L.EnemyGroup[i].CertAll):
                    Py.Collision_Enemy(screen, P, L.EnemyGroup[i], L.EnemyGroup)
        Py.Borders(P, screen)
        RenderL = PG.RenderL
        R.Build_screen(screen, P, RenderL) #Function that renders the scene
        PG.updates += 1
        print("Update: ", updates)
        T2 = time.clock()
        T = T2-PG.t0
        print("Toliko casa minilo: ", T)
        if T > 10 and PG.Approval == True:
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
screen.fill(white)
pygame.display.update()

def Close_Game():
    PG.Running = False
    pygame.quit()
    print("I closed")
    sys.exit()

#Calls the game loop
main()
