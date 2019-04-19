import pygame, time, Classes, Renderer, level, Pysics, os, Level_Builder, datetime, Platform_Game

PG = Platform_Game
C=Classes
L=level
LB=Level_Builder
Py=Pysics
R = Renderer

i = 1

pygame.display.init()

width = 1680
height = 980

currentTime = str(datetime.datetime.now())
currentTime = currentTime.replace(':', '_')

F = open("logs/Origin block position log "+ currentTime + ".txt", "w+")

# Defines colours
black = [0,0,0] 
white = [255,255,255]
red = [255,0,0]
blue =[0,0,255]
green = [0,255,0]
magenta = [255,0,255]

screen = pygame.display.set_mode((width,height))

PlayerImage = pygame.image.load("images/PlayerAni.png").convert_alpha()
image = pygame.image.load("images/player.png").convert_alpha()
icon = pygame.image.load("images/player.ico").convert_alpha()
star = pygame.image.load("images/LoGo.png").convert_alpha()
Animation_Image = pygame.image.load("images/explosion.hasgraphics.png").convert_alpha()
#Background = pygame.image.load("images/Block.jpg").convert_alpha()

#Player animation sheet
PlayerAni_ = {}
PlayerAniList = []
PlayerAni_Down = 0
for i in range(0, 7): # Automaticly saves the settings for the player animation
    for j in range(0,8):
        PlayerAni_[i] = [25.44 * j, PlayerAni_Down, 25.44, 48]
        PlayerAniList.append(PlayerAni_[i])
    PlayerAni_Down += 48
    j = 0


myfont = pygame.font.SysFont('Comic Sans MS', 30)
ID = 1
R.E = []
Zaporedje = 0
MejaZaporedja = len(PlayerAniList)
R.Tracker= 1
R.Pixel_down = 0
R.Animation_left = 1
R.Animation_number = 0
Start_Animation = False
pygame.display.set_icon(icon)
pygame.display.set_caption('Platform game')

def Build_screen(screen, P, RenderL, Character_Dead):#Renders the scene
    R.EL = RenderL[0]
    StarL = RenderL[1]
    HitBoxes = RenderL[2]
    EnemyGroup = RenderL[3]
    screen.fill(white)
    #screen.blit(R.Background,(0,0))
    pygame.display.get_caption()
    R.E = L.Draw_level(screen, R.El, StarL, P, EnemyGroup) # Draws level
    x = len(R.E)
    y = len(EnemyGroup)
    print ("Število kvadratov v prvi listi:", x)
    print ("Število kvadratov v drugi listi:", y)
    #h = len(StarL)
    #for i in range(0,h):
    #    screen.blit(StarL[i].image,(StarL[i].x, StarL[i].y))
    #if R.Start_Animation == True:
    #    R.Start_Animation = Score_animation(screen)
    Score = str(P.Score)
    PS = myfont.render(Score, False, red)
    screen.blit(PS, [840,0]) # Displays score
    #if h <= 1:
    #    PS = myfont.render('Bravo pobrali ste vse možne točke', False, red)
    #    screen.blit(PS, [650,490])
    #    pygame.display.update()
    #    time.sleep(2)
    #    pygame.quit()
    #P.HitBox(screen)
    F.write(str(LB.El[2].x))
    F.write("\n")
    P.Camera(LB.El)
    PG.Character_Dead = P.Check_For_Life(screen, Character_Dead)
    if P.Orientation == "right": # Display player if his orientation is to the right
        if R.Zaporedje > R.MejaZaporedja-1: # Restarts the animation
            R.Zaporedje = 0
        screen.blit(PlayerImage, (P.CameraPosX, P.y),(PlayerAniList[R.Zaporedje])) # Displays player and crops it
    if P.Orientation == "left": # Display player if his orientation is to the left
        if R.Zaporedje < 0: # Restarts the animation
            R.Zaporedje = R.MejaZaporedja - 1
        screen.blit(pygame.transform.flip(PlayerImage, True, False), (P.CameraPosX, P.y),(PlayerAniList[R.Zaporedje])) # Displays player, flips and crops it
    pygame.display.update()

def Score_animation(screen): # Legacy system for displaying the score
    while R.Animation_number < 72:
           if R.Animation_number%8==0:
                R.Pixel_down = 100 * R.Tracker
                R.Tracker+=1
                R.Animation_left = 1
           Pixel_left = 100*R.Animation_left
           screen.blit( Animation_Image, (800, -25), (Pixel_left, R.Pixel_down, 100, 100) )
           time.sleep(0.01)
           R.Animation_left+=1
           R.Animation_number += 1
           print("Animation number: ",R.Animation_number)
           break
    if R.Animation_number >= 72:
        Start_Animation = False
        R.Tracker= 1
        R.Pixel_down = 0
        R.Animation_left = 1
        R.Animation_number = 0
    else:
        Start_Animation = True
    return Start_Animation
