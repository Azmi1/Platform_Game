import pygame, time, Classes, Renderer, level

R = Renderer
L = level

black = [0, 0, 0]
white = [255, 255, 255]
red = [255, 0, 0]
blue = [0, 0, 255]
green = [0, 255, 0]
magenta = [255, 0, 255]

Player = pygame.sprite.Group()

CanSpeed = False

class player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        Player.add(self)
        self.x = 20
        self.y = 900
        self.image = pygame.image.load("images/player.png")
        self.rect = self.image.get_rect()
        self.Jump = True
        self.Jumping = False
        self.Score = 0
        self.Moving = False
        self.MoveY = 0
        self.MoveX = 0

    def move(self, screen, P, RenderL):
        surface = screen
        key = pygame.key.get_pressed()
        dist = 3
        if key[pygame.K_UP]:
            self.MoveY = -3
        if self.Jump == True:
            if key[pygame.K_w]:
                self.MoveY = -5
                self.Moving = True
                self.Jumping = True
                self.Jump = False
        if self.MoveY < 0:
                self.MoveY += 0.15
                self.Moving = True
        else:
                self.Moving = False
                self.Jumping = False
        if key[pygame.K_d]:
            if self.MoveX < 3 or CanSpeed == True:
                self.MoveX += 1
            self.Moving = False
        elif key[pygame.K_a]:
            if self.MoveX > -3:
                self.MoveX += -1
            self.Moving = False
        else:
            if self.MoveX > -0.1 and self.MoveX < 0.1:
                self.MoveX = 0
            elif self.MoveX > 0:
                self.MoveX -= 0.1
            elif self.MoveX <= 0:
                self.MoveX += 0.1
        self.x += self.MoveX
        self.y += self.MoveY

    def HitBox(self, screen):
        self.certall = pygame.draw.rect(screen, black, [self.x, self.y, 48, 48])
        self.certtop = pygame.draw.rect(screen, red, [self.x, self.y, 48, 3])
        self.certLeft = pygame.draw.rect(screen, green, [self.x, self.y + 3, 3, 42])
        self.certIn = pygame.draw.rect(screen, magenta, [self.x + 3, self.y + 3, 42, 42])
        self.certRight = pygame.draw.rect(screen, green, [self.x + 45, self.y + 3, 3, 42])
        self.certbottom = pygame.draw.rect(screen, blue, [self.x, self.y + 45, 48, 3])
        HitBoxes = [self.certall, self.certtop, self.certLeft, self.certIn, self.certRight, self.certbottom]
        return HitBoxes
