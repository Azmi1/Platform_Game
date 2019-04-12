import pygame, time, Classes, Pysics, Renderer, level, datetime

C = Classes
R = Renderer
L = level
Py = Pysics

currentTime = str(datetime.datetime.now())
currentTime = currentTime.replace(':', '_')

F = open("logs/Collision log "+ currentTime + ".txt", "w+") 

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
        F.write("Collision with inner block")
        F.write("\n")
        P.Moving = True
    elif P.certtop.colliderect(Him.cert) and P.certLeft.colliderect(Him.cert) or P.certbottom.colliderect(Him.cert) and P.certLeft.colliderect(Him.cert) or P.certbottom.colliderect(Him.cert) and P.certLeft.colliderect(Him.cert) and P.certtop.colliderect(Him.cert) or P.certLeft.colliderect(Him.cert):
        P.Jump = True
        P.CameraX = - 0.2
        F.write("Collision with left side")
        F.write("\n")
    elif P.certtop.colliderect(Him.cert) and P.certRight.colliderect(Him.cert) or P.certbottom.colliderect(Him.cert) and P.certRight.colliderect(Him.cert) or P.certtop.colliderect(Him.cert) and P.certRight.colliderect(Him.cert) and P.certbottom.colliderect(Him.cert) or P.certRight.colliderect(Him.cert):
        P.CameraX= + 0.2
        P.Jump = True
        F.write("Collision with right side")
        F.write("\n")
    elif P.certtop.colliderect(Him.cert):
        P.y=Him.y+Him.height
        P.Jump = True
        P.MoveY = 0
        F.write("Collision with top side")
        F.write("\n")
    elif P.certbottom.colliderect(Him.cert):
        P.y=Him.y-48
        P.Jump = True
        P.MoveY = 0
        F.write("Collision with bottom side")
        F.write("\n")
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

