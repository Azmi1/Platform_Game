import pygame, time, Classes, Pysics, Renderer, level

C = Classes
R = Renderer
L = level

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
red = [255,0,0]

def Collision(screen, Hitboxes, Ecert,self, E,i, P, Moving):
    E1cert=Ecert[i]
    Him = E[i]
    Him.cert = E1cert
    if self.certIn.colliderect(Him.cert):
        P.y+=4
        R.Build_screen(screen, P, Moving)
    elif self.certtop.colliderect(Him.cert) and self.certRight.colliderect(Him.cert) or self.certbottom.colliderect(Him.cert) and self.certRight.colliderect(Him.cert) or self.certbottom.colliderect(Him.cert) and self.certRight.colliderect(Him.cert) and self.certtop.colliderect(Him.cert) or self.certRight.colliderect(Him.cert):
        self.x=Him.x-48
        P.Jump = True
    elif self.certtop.colliderect(Him.cert) and self.certLeft.colliderect(Him.cert) or self.certbottom.colliderect(Him.cert) and self.certLeft.colliderect(Him.cert) or self.certbottom.colliderect(Him.cert) and self.certLeft.colliderect(Him.cert) and self.certtop.colliderect(Him.cert) or self.certLeft.colliderect(Him.cert):
        self.x=Him.x+Him.width
        P.Jump = True
    elif self.certtop.colliderect(Him.cert):
        self.y=Him.y+Him.height
        P.Jump = True
    elif self.certbottom.colliderect(Him.cert):
        self.y=Him.y-47
        P.Jump = True
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

