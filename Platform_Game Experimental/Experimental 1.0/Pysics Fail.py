import pygame, time, Classes, Pysics, Renderer, level, Enemy

C = Classes
R = Renderer
L = level
EN = Enemy

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
red = [255,0,0]

def Collision(screen, Hitboxes, Ecert, E,i, P, RenderL):
    E1cert=Ecert[i]
    Him = E[i]
    Him.cert = E1cert
    print(pygame.sprite.groupcollide(C.Player, EN.BGroup, False, False))
    if pygame.sprite.groupcollide(C.Player, EN.BGroup, 0,0) == True:
        print("I am colliding")
        P.MoveX = 0
        P.MoveY = 0
        P.Moving = False
    else:
        print("Collision false")

def Gravity(self):
    self.y +=3

def Borders(self,screen):
    if self.y > 1080:
        PS = myfont.render('Padli ste v globine iz katerih se ni mogoče vrniti', False, red)
        screen.blit(PS, [525,490])
        pygame.display.update()
        time.sleep(3)
        pygame.quit()
    elif self.x > 1680:
        self.x = 0
    elif self.x < 0:
        self.x = 1680

