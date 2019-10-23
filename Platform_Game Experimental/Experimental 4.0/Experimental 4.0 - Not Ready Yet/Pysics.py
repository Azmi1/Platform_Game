import pygame, datetime, time

currentTime = str(datetime.datetime.now())
currentTime = currentTime.replace(':', '_')

F = open("logs/Collision log latest.txt", "w+") 
Log = open("logs/Collision with enemy latest.txt", "w+")

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
red = [255,0,0]

CollHappened = False

def Collision(screen, Ecert, E,i, P, RenderL): # Checks where the collision happened
    E1cert=Ecert[i]
    Him = E[i]
    Him.cert = E1cert
    if P.certIn.colliderect(Him.cert): # Checks if the collision happened with inner hitbox
        P.y -= 3
        P.HBY -= 3
        F.write("Collision with inner block")
        F.write("\n")
        P.Moving = True
    elif P.certtop.colliderect(Him.cert) and not(P.certLeft.colliderect(Him.cert)) and not(P.certRight.colliderect(Him.cert)): # Checks if the collision happened with top hitbox
        P.y=Him.y+Him.height+2
        P.MoveY = 0
        F.write("Collision with top side")
        F.write("\n")
    elif P.certtop.colliderect(Him.cert) and P.certLeft.colliderect(Him.cert) or P.certbottom.colliderect(Him.cert) and P.certLeft.colliderect(Him.cert) or P.certbottom.colliderect(Him.cert) and P.certLeft.colliderect(Him.cert) and P.certtop.colliderect(Him.cert) or P.certLeft.colliderect(Him.cert): # Checks if the collision happened with left hitbox
        if Him.CanCanJumpReg == True:
            P.Jump = True
            P.VarJumps = 0
            P.WLag = False
        P.CameraX = - 0.2
        P.HBX -= 0.2
        F.write("Collision with left side")
        F.write("\n")
    elif P.certtop.colliderect(Him.cert) and P.certRight.colliderect(Him.cert) or P.certbottom.colliderect(Him.cert) and P.certRight.colliderect(Him.cert) or P.certtop.colliderect(Him.cert) and P.certRight.colliderect(Him.cert) and P.certbottom.colliderect(Him.cert) or P.certRight.colliderect(Him.cert): # Checks if the collision happened with right hitbox
        if Him.CanCanJumpReg == True:
            P.Jump = True
            P.VarJumps = 0
            P.WLag = False
        P.CameraX= + 0.2
        P.HBX += 0.2
        F.write("Collision with right side")
        F.write("\n")
    elif P.certbottom.colliderect(Him.cert): # Checks if the collision happened with bottom hitbox
        if Him.CanCanJumpReg == True:
            P.Jump = True
            P.VarJumps = 0
            P.WLag = False
        P.y=Him.y-48
        P.HBY = Him.y - 48
        P.MoveY = 0
        F.write("Collision with bottom side")
        F.write("\n")
    else:
        print("Collision false")
        Py.CollHappened = False

def Collision_Enemy(screen, P, Him, EnemyGroup, E): # Checks if collision happened with enemy
    if P.certbottom.colliderect(Him.CertTop) and not(P.certRight.colliderect(Him.CertTop)) and not(P.certLeft.colliderect(Him.CertTop)): # This checks if the player collided with enemies's top side and deletes it
        EnemyGroup.remove(Him)
        P.Score += 1
        del Him
    elif P.certtop.colliderect(Him.CertBottom) and P.certLeft.colliderect(Him.CertBottom) or P.certbottom.colliderect(Him.CertBottom) and P.certLeft.colliderect(Him.CertBottom) or P.certbottom.colliderect(Him.CertBottom) and P.certLeft.colliderect(Him.CertBottom) and P.certtop.colliderect(Him.CertBottom) or P.certLeft.colliderect(Him.CertBottom): # Checks if the collision happened with left hitbox
        P.CameraPosX = 42
        P.Life -= 1
        while E[2].x < 0:
            Log.write("LOL")
            for i in range(0, len(E)):
                Log.write("LeL")
                E[i].x += 1
            Log.write("\n")
        F.write("Collision with left side")
        F.write("\n")
    elif P.certtop.colliderect(Him.CertBottom) and P.certRight.colliderect(Him.CertBottom) or P.certbottom.colliderect(Him.CertBottom) and P.certRight.colliderect(Him.CertBottom) or P.certtop.colliderect(Him.CertBottom) and P.certRight.colliderect(Him.CertBottom) and P.certbottom.colliderect(Him.CertBottom) or P.certRight.colliderect(Him.CertBottom): # Checks if the collision happened with left hitbox
        P.CameraPosX = 42
        P.Life -= 1
        while E[2].x < -1:
            Log.write("LOL")
            for i in range(0, len(E)):
                Log.write("LeL")
                E[i].x += 1
            Log.write("Stevilo kvadratov: " + str(len(E)))
            Log.write("\n")
        F.write("Collision with right side")
        F.write("\n")
    elif P.certtop.colliderect(Him.CertBottom):
        P.MoveY = 0
        P.y=Him.y+Him.height+2

def Collision_Power_Ups(P, It, PowerUpsGroup):
    if P.certall.colliderect(It.certall):
        It.Power_Up_Delivery(P, PowerUpsGroup)

def Gravity(self): # The magic of gravity happens here
    self.y += 3
    self.HBY += 3

def Borders(self,screen): # Looks if the 
    if self.y > 1080:
        PS = myfont.render('You have fallen in too the depths of the floor', False, red)
        screen.blit(PS, [525,490])
        pygame.display.update()
        time.sleep(3)
        self.Life = 0
    elif self.x > 1680:
        self.x = 0
    elif self.x < 0:
        self.x = 1680

