import Enemy, level, pygame, time, random

EN = Enemy
L=level



black = [0,0,0]
white = [255,255,255]
red = [255,0,0]
blue =[0,0,255]
green = [0,255,0]
magenta = [255,0,255]

L.x = 0
L.x1 = 0
L.y = 0
L.y1 = 0
L.j = 0
L.st = 2
L.i = 1
L.id = 0
L.w = 0
L.El = []


def Draw_level(screen, El, StarL):
    x = len(El)
    z = len(StarL)
    print("Prisotne tocke: ",z-1)
    E = []
    for i in range(0,x):
        El[i].draw(screen)
        El[i].cert = El[i]
        E.append(El[i].rect)
        #pygame.display.update(El[i].rect)
    if StarL != []:
        for i in range(0,z-1):
            StarL[i].draw(screen)
            #pygame.display.update(L.StarL[i].rect)
    return E
