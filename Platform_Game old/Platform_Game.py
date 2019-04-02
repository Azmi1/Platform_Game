import pygame, time, Classes, Renderer, level, Platform_Game

C = Classes   #These 3 lines make a mudule 1 character long for ease of use
R = Renderer
L = level
PG = Platform_Game

i = 0

width = 1680
height = 980

red = [255,0,0]

updates = 0
t0 = time.clock()
Approval = True

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

white = [255,255,255]
screen = R.Create_screen(width,height) #Creates screen

def main():    
    Running = True 
    while Running == True: # Makes a game loop
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: #For ending the loop
                pygame.quit()
                running = False
        
        Moving = P.move(screen, P) #Function that makes playermove
        Moving = False
        R.Build_screen(screen, P, Moving) #Function that renders the scene
        PG.updates += 1
        print("Updatov: ",PG.updates)
        T2 = time.clock()
        T = T2-PG.t0
        print("Toliko casa minilo: ", T)
        if T > 10 and PG.Approval == True:
            PS = myfont.render('Updates per 10 seconds:', False, red)
            PG.updates = str(PG.updates)
            PS1 = myfont.render(PG.updates, False, red)
            screen.blit(PS, [650,490])
            screen.blit(PS1, [650,550])
            pygame.display.update()
            time.sleep(2)
            pygame.quit()

P = C.player() #Creates player object
screen.fill(white)
pygame.display.update()
main()
