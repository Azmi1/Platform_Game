import pygame, time, Classes, Pysics, Renderer, level

C = Classes
R = Renderer
L = level
Py = Pysics

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
red = [255,0,0]

CollHappened = False

def Collision(screen, Hitboxes, Ecert, E,i, P, RenderL):
    E1cert=Ecert[i]
    Him = E[i]
    Him.cert = E1cert
    if P.certIn.colliderect(Him.cert):
        P.y-=3
        P.Moving = True
    elif P.certtop.colliderect(Him.cert) and P.certRight.colliderect(Him.cert) or P.certbottom.colliderect(Him.cert) and P.certRight.colliderect(Him.cert) or P.certtop.colliderect(Him.cert) and P.certRight.colliderect(Him.cert) and P.certbottom.colliderect(Him.cert) or P.certRight.colliderect(Him.cert):
        P.x=Him.x-48
        P.Jump = True
        P.MoveX = 0
        Py.CollHappened = True
    elif P.certtop.colliderect(Him.cert) and P.certLeft.colliderect(Him.cert) or P.certbottom.colliderect(Him.cert) and P.certLeft.colliderect(Him.cert) or P.certbottom.colliderect(Him.cert) and P.certLeft.colliderect(Him.cert) and P.certtop.colliderect(Him.cert) or P.certLeft.colliderect(Him.cert):
        P.x=Him.x+Him.width
        P.Jump = True
        P.MoveX = 0
        Py.CollHappened = True
    elif P.certtop.colliderect(Him.cert):
        P.y=Him.y+Him.height
        P.Jump = True
        P.MoveY = 0
        Py.CollHappened = True
    elif P.certbottom.colliderect(Him.cert):
        P.y=Him.y-49
        P.Jump = True
        P.MoveY = 0
    else:
        print("Collision false")
        Py.CollHappened = False

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

