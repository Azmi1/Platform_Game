import pygame, time, Classes, Renderer, level, Pysics, os, Level_Builder

C=Classes
L=level
LB=Level_Builder
Py=Pysics
R = Renderer

i = 1

pygame.display.init()

width = 1680
height = 980


black = [0,0,0] 
white = [255,255,255]
red = [255,0,0]
blue =[0,0,255]
green = [0,255,0]
magenta = [255,0,255]

screen = pygame.display.set_mode((width,height))

image = pygame.image.load("images/player.png").convert_alpha()
icon = pygame.image.load("images/player.ico").convert_alpha()
star = pygame.image.load("images/LoGo.png").convert_alpha()
Animation_Image = pygame.image.load("images/explosion.hasgraphics.png").convert_alpha()
#Background = pygame.image.load("images/background.jpg").convert_alpha()

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

R.E = []
R.Tracker= 1
R.Pixel_down = 0
R.Animation_left = 1
R.Animation_number = 0
Start_Animation = False
pygame.display.set_icon(icon)
pygame.display.set_caption('Platform game')
def Create_screen(width, height): #creates the screen
    screen = pygame.display.set_mode((width,height))
    return screen

def Build_screen(screen, P, RenderL):#Renders the scene
    R.EL = RenderL[0]
    StarL = RenderL[1]
    HitBoxes = RenderL[2]
    screen.fill(white)
    pygame.display.get_caption()
    R.E = L.Draw_level(screen, R.El, StarL, P)
    x = len(R.E)
    print ("Število kvadratov", x)
    #h = len(StarL)
    #if R.Start_Animation == True:
    #    R.Start_Animation = Score_animation(screen)
    Score = str(P.Score)
    PS = myfont.render(Score, False, red)
    screen.blit(PS, [840,0])
    #if h <= 1:
    #    PS = myfont.render('Bravo pobrali ste vse možne točke', False, red)
    #    screen.blit(PS, [650,490])
    #    pygame.display.update()
    #    time.sleep(2)
    #    pygame.quit()
    #P.HitBox(screen)
    if P.Orientation == "right":
        screen.blit(image, (P.CameraX + 22, P.y))
    if P.Orientation == "left":
        screen.blit(pygame.transform.flip(image, True, False), (P.CameraX + 22, P.y))
    pygame.display.update()

def Score_animation(screen):
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
