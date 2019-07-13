import level, pygame, Classes

L=level
Cl = Classes


# Defines colours
black = [0,0,0]
white = [255,255,255]
red = [255,0,0]
blue =[0,0,255]
green = [0,255,0]
magenta = [255,0,255]

# Variables used in the creation
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


def Draw_level(screen, El, StarL, P, EnemyGroup, Camera): # Draws the level
    x = len(El)
    y = len(EnemyGroup)
    z = len(StarL)
    print("Prisotne tocke: ",z)
    print("Prisotni stricki: ", y)
    E = []
    #if StarL != []:
    #    for i in range(0,z-1):
    #        if Cl.Special_Draw == False:
    #            StarL[i].draw(screen, StarL[i].x + P.CameraX)
    #        elif Cl.Special_Draw == True:
    #            StarL[i].Special_draw(screen)
    #        StarL.remove(StarL[i])
    #        StarL.append(StarL[i])
            #pygame.display.update(StarL[i].rect)
    for i in range(0,x): # Draws the blocks
        if Cl.Special_Draw == False:
            El[i].draw(screen, Camera)
        elif Cl.Special_Draw == True:
            El[i].Special_draw(screen)
        E.append(El[i].rect)
        #pygame.display.update(El[i].rect)
    if len(EnemyGroup) > 0: # Draws the enemies
        for j in range(0,y):
            EnemyGroup[j].Hitbox(screen)
            if Cl.Special_Draw == False:
                EnemyGroup[j].display(screen, Camera)
            elif Cl.Special_Draw == True:
                EnemyGroup[j].Special_Display(screen)
    return E
