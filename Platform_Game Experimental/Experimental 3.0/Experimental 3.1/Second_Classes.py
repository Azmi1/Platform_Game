import pygame, random

# Defines colours
black = [0,0,0]
white = [255,255,255]
red = [255,0,0]
blue =[0,0,255]
green = [0,255,0]
magenta = [255,0,255]
transparent = [0,0,0,128]

BGroup = pygame.sprite.Group()

class Enemy(object): # Defines enemy
    def __init__(self, x, y): # Prepares class for what it comes after
        self.x = x
        self.y = y - 48
        self.width = 48
        self.height = 48
        self.image = pygame.image.load("images/player.png").convert_alpha()

    def Hitbox(self, screen): # Sets up the hitbox 
        self.CertAll = pygame.draw.rect(screen, magenta, [self.x, self.y, 48, 48])
        self.CertBottom = pygame.draw.rect(screen, blue, [self.x, self.y + 1, 48, 47])
        self.CertTop = pygame.draw.rect(screen, red, [self.x, self.y, 48, 1])
        Hitbox = [self.CertBottom, self.CertTop, self.CertAll]
        return Hitbox

    def Special_Display(self, screen): # It displays image in a special way... :<3
        screen.blit(self.image,(self.x, self.y))

    def display(self, screen, P): # It displays image
        self.x += P.CameraX
        screen.blit(self.image,(self.x, self.y))

class Points(object): # Legacy system for points
    def __init__(self, screen):
        self.x = random.randint(10,1670)
        self.y = random.randint(10, 970)
        self.image = pygame.image.load("images/LoGo.png").convert_alpha()
        self.cert = pygame.draw.rect(screen, white,[self.x, self.y, 26, 20])

    def draw(self, screen, x):
        self.x = x
        self.cert = pygame.draw.rect(screen, white,[self.x, self.y, 26, 20])
        self.rect = self.image.get_rect()
        screen.blit(self.image,(self.x, self.y))
        return self.rect

    def Special_draw(self, screen):
        screen.blit(self.image,(self.x, self.y))

class Block(pygame.sprite.Sprite): # Blocks
    def __init__(self):
        l=0

    def create(self, screen, x, y, width, height, color,ImagePresent = 'False', Image = ''): # Displays Blocks
        pygame.sprite.Sprite.__init__(self)
        self.y = y
        self.x = x
        self.width = width
        self.height = height
        self.image = Image
        self.rect = pygame.draw.rect(screen, color, [self.x, self.y, width,height])
        if ImagePresent == True: # If image is present it automaticly crops it and blit it over block
            screen.blit(self.image,(self.x, self.y),(0,0, self.width, self.height))
        BGroup.add(self)
        return self.rect

print("Second_Classes loaded")
