import pygame, random

black = [0,0,0]
white = [255,255,255]
red = [255,0,0]
blue =[0,0,255]
green = [0,255,0]
magenta = [255,0,255]
transparent = [0,0,0,128]

BGroup = pygame.sprite.Group()

class Enemy(object):
    def __init__(self, Him):
        self.x = Him.x + (random.randint(Him.x, Him.PrevX1) - Him.x)
        self.y = Him.y - 48
        self.image = pygame.image.load("images/player.png").convert_alpha()

    def Hitbox(self, screen):
        self.CertAll = pygame.draw.rect(screen, magenta, [self.x, self.y, 48, 48])
        self.CertBottom = pygame.draw.rect(screen, blue, [self.x, self.y + 1, 48, 47])
        self.CertTop = pygame.draw.rect(screen, red, [self.x, self.y, 48, 1])
        Hitbox = [self.CertBottom, self.CertTop, self.CertAll]
        return Hitbox

    def display(self,screen):
        screen.blit(self.image,(self.x, self.y))

class Points(object):
    def __init__(self):
        l=0
        self.x = random.randint(10,1670)
        self.y = random.randint(10, 970)
        self.image = pygame.image.load("images/LoGo.png").convert_alpha()

    def draw(self, screen, P):
        self.y = self.y
        self.x = self.x + P.CameraX
        self.cert = pygame.draw.rect(screen, white,[self.x, self.y, 26, 20])
        self.rect = self.image.get_rect()
        return self.rect

class Block(pygame.sprite.Sprite):
    def __init__(self):
        l=0

    def create(self, screen, x, y, width, height, color,ImagePresent = 'False', Image = ''):
        pygame.sprite.Sprite.__init__(self)
        self.y = y
        self.x = x
        self.width = width
        self.height = height
        self.image = Image
        self.rect = pygame.draw.rect(screen, color, [self.x, self.y, width,height])
        if ImagePresent == True:
            screen.blit(self.image,(self.x, self.y),(0,0, self.width, self.height))
        BGroup.add(self)
        return self.rect

print("Second_Classes loaded")
