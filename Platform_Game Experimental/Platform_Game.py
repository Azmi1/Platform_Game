import pygame, time, Classes, Renderer, level, Pysics, Platform_Game, Level_Builder


# These 4 lines make a mudule 1 character long for ease of use
PG = Platform_Game
C = Classes   
R = Renderer
L = level
LB=Level_Builder
Py = Pysics

# Creates screen
width = 1680
height = 980
screen = R.Create_screen(width,height)

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
updates = 0
t0 = time.clock()
Approval = False
Gravity = True

#Load all outside images
image= pygame.image.load("images/player.png").convert_alpha()
icon= pygame.image.load("images/player.ico").convert_alpha()
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
            R.El, PG.i, StarL = LB.Load_level_1(screen, "custom", P)
            print ("Level loading/creating")
        HitBoxes = P.HitBox(screen)
        if PrviZagon == 0:
            PG.RenderL.append(R.El)
            PG.RenderL.append(StarL)
            PG.RenderL.append(HitBoxes)
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
                pygame.quit()
                PG.Running = False

#Prepares all essentials for game loop
P = C.player()
screen.fill(white)
pygame.display.update()
Running = True

#Calls the game loop
main()
