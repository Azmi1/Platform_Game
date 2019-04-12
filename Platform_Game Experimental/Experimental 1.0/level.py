import Second_Classes, level, pygame, time, random

SC = Second_Classes
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


def Draw_level(screen, El, StarL, P):
    x = len(El)
    z = len(StarL)
    print("Prisotne tocke: ",z-1)
    E = []
    #if StarL != []:
    #    for i in range(0,z-1):
    #        StarL[i].draw(screen, P).normalize()
    #        StarL.remove(StarL[i])
    #        StarL.append(StarL[i])
            #pygame.display.update(StarL[i].rect)
    for i in range(0,x):
        El[i].draw(screen, P)
        El[i].cert = El[i]
        E.append(El[i].rect)
        #pygame.display.update(El[i].rect)
    return E
