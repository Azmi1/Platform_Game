import pygame, time, Second_Classes, Renderer, random

black = [0,0,0]
white = [255,255,255]
red = [255,0,0]
blue =[0,0,255]
green = [0,255,0]
magenta = [255,0,255]
transparent = [0,0,0,128]

BGroup = pygame.sprite.Group()

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
