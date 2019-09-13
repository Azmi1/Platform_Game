import pygame
import Classes as Cl
import Pysics as Py
import Renderer as R
import Options as OPS

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

class Power_Ups(object):
    def __init__(self, Mode, x, y):
        self.x = x
        self.y = y
        self.Mode = Mode
        self.Destruct = False
        if Mode == "Jumps":
            self.image = pygame.image.load("images\Power_Ups\DoubleJump_Boots.png").convert_alpha()
        elif Mode == "JumpBoost":
            self.image = pygame.image.load("images\Power_Ups\BoostJump_Boots.png").convert_alpha()
        elif Mode == "Speed":
            self.image = pygame.image.load("images\Power_Ups\Speed_Boots.png").convert_alpha()

    def Display(self, screen, Camera):
        self.x += Camera.x
        screen.blit(pygame.transform.smoothscale(self.image, (32, 32)), (self.x, self.y))

    def Hitbox(self, screen):
        self.certall = pygame.draw.rect(screen, red, [self.x, self.y, 25, 32])

    def Power_Up_Delivery(self, P, Group):
        if self.Mode == "Jumps" and OPS.Max_Jumps > P.Jumps:
            P.Jumps += 1
        elif self.Mode == "Speed" and OPS.Max_Speed > P.Speed:
            P.Speed = P.Speed + P.Speed/10
        elif self.Mode == "JumpBoost" and OPS.Max_JumpBoost > P.JumpHeight/5:
            P.JumpHeight = P.JumpHeight + P.JumpHeight/10
        self.Destruct = True

    def Self_Destruct(self, Group):
        if self.Destruct == True:
            Group.remove(self)
            del self
            Breaky = True
            return Breaky

class camera(object):
    def __init__(self, player):
        self.player = player
        self.x = 0
        self.y = 0

    def getpos(self):
        self.x = self.player.CameraX


class player(pygame.sprite.Sprite): #Defines player that you play
    def __init__(self, Approval_SpecialDraw): #Setups the player
        #pygame.sprite.Sprite.__init__(self)
        #Player.add(self)
        self.CameraX = 0 #Sets the world camera position
        self.x = 42 #Used mainly for the hitbox
        self.y = 900
        self.Jump = True # Defines if you can jump so you can't jump infinitely
        self.Jumping = False # Defines so that the gravity dosn't pull you down
        self.JumpHeight = 5
        self.Score = 0  
        self.Moving = False # Same as Jumping
        self.MoveY = 0
        self.MoveX = 0
        self.Speed = 3
        if Approval_SpecialDraw == True:
            self.CameraPosX = 42
        else:
            self.CameraPosX = 840 # Where on x line you spawn
        self.Orientation = "right" # Where the player looks at
        self.Life = 3
        self.ScoreY = 0
        self.Zaporedje = 0
        self.ID = 0
        # Power- Ups
        self.Jumps = 1
        self.VarJumps = 0

        # Key-Lag
        self.WLag = False

    def move(self, screen): # Defines player movement
        surface = screen
        key = pygame.key.get_pressed() # Registers key press
        if self.Jump == True: # Checks if you can jump
            if key[pygame.K_w] and self.WLag == False:
                self.WLag = True
                self.MoveY = -self.JumpHeight
                self.Moving = True
                self.Jumping = True
                self.VarJumps +=1
                if self.VarJumps >= self.Jumps:
                    self.Jump = False
            elif key[pygame.K_w] == False and self.WLag == True:
                self.WLag = False

        if self.MoveY < 0: # this check if the variable is smaller 0 if it is it starts smoothing to 0
                self.MoveY += 0.15
                self.Moving = True
        else:
                self.Moving = False
                self.Jumping = False
        if key[pygame.K_d]: # This moves player right
            if self.CameraX > -self.Speed and Py.CollHappened == False or CanSpeed == True and Py.CollHappened == False:
                self.CameraX -= 1
                self.Orientation = "right"
            self.Moving = False
            self.Zaporedje += 1
        elif key[pygame.K_a]: # This moves player left
            if self.CameraX < self.Speed and Py.CollHappened == False or CanSpeed == True and Py.CollHappened == False:
                self.CameraX += 1
                self.Orientation = "left"
            self.Moving = False
            self.Zaporedje -= 1
        else: # All this is for slowly stopping
            if self.CameraX > self.Speed+1.5:
                self.CameraX = self.Speed
            if self.CameraX < -self.Speed-0.5:
                self.CameraX = -self.Speed
            if self.CameraX > -0.1 and self.MoveX < 0.1 or Py.CollHappened == True:
                self.PrevX = self.CameraX
                self.CameraX = 0
            elif self.CameraX > 0:
                self.CameraX -= 0.1
            elif self.CameraX <= 0:
                self.CameraX += 0.1
        self.y += self.MoveY

    def Status(self):
        print("Jumps: "+ str(self.VarJumps))
        print("Jump-Lag: "+ str(self.WLag))

    def Camera(self, El, Approval_SpecialDraw): # Controls the camera
        key = pygame.key.get_pressed()
        print("Kje je kamera na x osi: " + str(self.CameraPosX))
        if El[2].x >= -4 and self.CameraPosX <= 823 and Approval_SpecialDraw == True: # Controls the start of the game
            Cl.Special_Draw = True
            if El[2].x > 0:
                self.CameraPosX = self.CameraX + 42
            elif El[2].x <= 0 and self.CameraPosX <= 824 and self.CameraX < 0 and key[pygame.K_d]:
                self.CameraPosX += 4
            elif El[2].x <= 0 and self.CameraPosX <= 832 and self.CameraX > 0 and key[pygame.K_a] and El[2].x > -622.5 and self.CameraPosX >= 40:
                self.CameraPosX += -4
        elif El[2].x <= - 622.5 or self.CameraPosX >= 824 or Approval_SpecialDraw == False: # Controls the rest the game
            Cl.Special_Draw = False
            print("Navadno rise kot ponavadi")
            if El[2].x > 0 and Approval_SpecialDraw == True:
                self.CameraPosX = self.CameraX + 42
            elif El[2].x <= 0 and self.CameraPosX <= 824 and self.CameraX < 0 and key[pygame.K_d]:
                self.CameraPosX += 4
            elif El[2].x <= 0 and self.CameraPosX <= 832 and self.CameraX > 0 and key[pygame.K_a] and El[2].x > -622.5 and self.CameraPosX >= 40:
                self.CameraPosX += -4
        elif El[2].x > 0 and Approval_SpecialDraw == True:
            self.CameraPosX = self.CameraX + 42
        elif El[2].x < 0 and self.CameraPosX <= 824 and self.CameraX < 0 and key[pygame.K_d] and Approval_SpecialDraw == True:
            self.CameraPosX += 4
        elif El[2].x < 0 and self.CameraPosX <= 832 and self.CameraX > 0 and key[pygame.K_a] and El[2].x > -622.5 and Approval_SpecialDraw == True:
            self.CameraPosX += -4
        self.x = self.CameraPosX

    def HitBox(self, screen): # Hitboxes for player
        self.certall = pygame.draw.rect(screen, black, [self.x, self.y, 25.44, 48])
        self.certtop = pygame.draw.rect(screen, red, [self.x, self.y, 25.44, 3])
        self.certLeft = pygame.draw.rect(screen, green, [self.x, self.y + 3, 3, 42])
        self.certIn = pygame.draw.rect(screen, magenta, [self.x + 3, self.y + 3, 19.44, 42])
        self.certRight = pygame.draw.rect(screen, green, [self.x + 22.44, self.y + 3, 3, 42])
        self.certbottom = pygame.draw.rect(screen, blue, [self.x, self.y + 45, 25.44, 3])
        HitBoxes = [self.certall, self.certtop, self.certLeft, self.certIn]
        return HitBoxes

    def Check_For_Life(self, screen, Character_Dead):
        if self.Life <= 0:
            Character_Dead = True
            return Character_Dead

    def Display_Life(self, screen, Character_Dead):
        PS = myfont.render('First player lives: ' + str(self.Life), False, red)
        screen.blit(PS,(10,10))

class player_two(pygame.sprite.Sprite): #Defines player that you play
    def __init__(self): #Setups the player
        #pygame.sprite.Sprite.__init__(self)
        #Player.add(self)
        self.x = 42 #Used mainly for the hitbox
        self.y = 900
        self.CameraX = 0 #Sets the world camera position
        self.Jump = True # Defines if you can jump so you can't jump infinitely
        self.Jumping = False # Defines so that the gravity dosn't pull you down
        self.Score = 0  
        self.Moving = False # Same as Jumping
        self.MoveY = 0
        self.MoveX = 0
        self.CameraPosX = self.CameraX + 75 # Where on x line you spawn
        self.Orientation = "right" # Where the player looks at
        self.Life = 3
        self.ScoreY = 25
        self.Zaporedje = 0
        self.ID = 1
        # Power- Ups
        self.DoubleJump = False
        self.VarJumps = 0
        
        # Key-Lag
        self.WLag = False

    def move(self, screen): # Defines player movement
        surface = screen
        key = pygame.key.get_pressed() # Registers key press
        dist = 1
        if self.Jump == True: # Checks if you can jump
            if key[pygame.K_w] and self.WLag == False:
                self.WLag = True
                self.MoveY = -5
                self.Moving = True
                self.Jumping = True
                self.VarJumps +=1
                if self.DoubleJump == False or self.VarJumps >= 2:
                    self.Jump = False
            else:
                self.WLag = False
        if self.MoveY < 0: # this check if the variable is smaller 0 if it is it starts smoothing to 0
                self.MoveY += 0.15
                self.Moving = True
        else:
                self.Moving = False
                self.Jumping = False
        if key[pygame.K_RIGHT]: # This moves player right
            if self.CameraX > -dist and Py.CollHappened == False or CanSpeed == True and Py.CollHappened == False:
                self.CameraX -= 1
                self.Orientation = "right"
            self.Moving = False
            self.Zaporedje += 1
        elif key[pygame.K_LEFT]: # This moves player left
            if self.CameraX < dist and Py.CollHappened == False or CanSpeed == True and Py.CollHappened == False:
                self.CameraX += 1
                self.Orientation = "left"
            self.Moving = False
            self.Zaporedje -= 1
        else: # All this is for slowly stopping
            if self.CameraX > dist + 0.5:
                self.CameraX = dist
            if self.CameraX < -dist-0.5:
                self.CameraX = -dist
            if self.CameraX > -0.1 and self.MoveX < 0.1 or Py.CollHappened == True:
                self.PrevX = self.CameraX
                self.CameraX = 0
            elif self.CameraX > 0:
                self.CameraX -= 0.1
            elif self.CameraX <= 0:
                self.CameraX += 0.1
        self.y += self.MoveY

    def Status(self):
        print("Jumps: "+ self.VarJumps)
        print("Jump-Lag: "+ self.WLag)

    def Camera(self, El): # Controls the camera
        key = pygame.key.get_pressed()
        print("Kje je kamera na x osi: " + str(self.CameraPosX))
        dist = 4
        if key[pygame.K_RIGHT]:
            self.CameraPosX += dist
        elif key[pygame.K_LEFT]:
            self.CameraPosX += -dist
        self.x = self.CameraPosX

    def HitBox(self, screen): # Hitboxes for player
        self.certall = pygame.draw.rect(screen, black, [self.x, self.y, 25.44, 48])
        self.certtop = pygame.draw.rect(screen, red, [self.x, self.y, 25.44, 3])
        self.certLeft = pygame.draw.rect(screen, green, [self.x, self.y + 3, 3, 42])
        self.certIn = pygame.draw.rect(screen, magenta, [self.x + 3, self.y + 3, 19.44, 42])
        self.certRight = pygame.draw.rect(screen, green, [self.x + 22.44, self.y + 3, 3, 42])
        self.certbottom = pygame.draw.rect(screen, blue, [self.x, self.y + 45, 25.44, 3])
        HitBoxes = [self.certall, self.certtop, self.certLeft, self.certIn]
        return HitBoxes

    def Check_For_Life(self, screen, Character_Dead):
        if self.Life <= 0:
            Character_Dead = True
            return Character_Dead

    def Display_Life(self, screen, Character_Dead):
        PS = myfont.render('Second player lives: ' + str(self.Life), False, red)
        screen.blit(PS,(10,20))


Special_Draw = True
black = [0, 0, 0]
white = [255, 255, 255]
red = [255, 0, 0]
blue = [0, 0, 255]
green = [0, 255, 0]
magenta = [255, 0, 255]

Player = pygame.sprite.Group()

CanSpeed = False

print(" ")
