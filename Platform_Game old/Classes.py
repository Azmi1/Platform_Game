import pygame, time, Classes, Renderer, level

R=Renderer
L=level

black = [0,0,0]
white = [255,255,255]
red = [255,0,0]
blue =[0,0,255]
green = [0,255,0]
magenta = [255,0,255]

ASprites = pygame.sprite.Group()

class player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x= 20
        self.y= 900
        self.image= pygame.image.load("player.png")
        self.rect = self.image.get_rect()
        self.Jump = True
        self.Score = 0

    def move(self, screen, P):
        surface=screen
        Moving = True
        key = pygame.key.get_pressed()
        dist = 3
        if key[pygame.K_UP]:
            self.y -= dist
        if self.Jump == True:
            self.Jump = False
            if key[pygame.K_w] and key [pygame.K_d]:
                i = 0
                k = 0
                for i in range(0,50):
                    self.y -= 4
                    self.x +=3
                    R.Build_screen(screen, self, Moving)
                time.sleep(0.0)
                x=0
                for x in range(0,10):
                    self.x += 3
                    R.Build_screen(screen, self, Moving)
            elif key[pygame.K_w] and key[pygame.K_a]:
                i = 0
                for i in range(0,50):
                    self.y -= 4
                    self.x -= 3
                    R.Build_screen(screen, self, Moving)
                time.sleep(0.0)
                x=0
                for x in range(0,10):
                    self.x -= 3
                    R.Build_screen(screen, self, Moving)
            elif key[pygame.K_w]:
                i = 0
                for i in range (0,50):
                    screen.fill(white)
                    self.y -= 4
                    R.Build_screen(screen, self, Moving)
        if key[pygame.K_d]: 
            self.x += dist 
        elif key[pygame.K_a]: 
            self.x -= dist
        
    
    def HitBox(self, screen):
        self.certall = pygame.draw.rect(screen, black,[self.x, self.y, 48,48])
        self.certtop = pygame.draw.rect(screen, red,[self.x, self.y, 48,3])
        self.certLeft = pygame.draw.rect(screen, green, [self.x, self.y+3, 3,42])
        self.certIn = pygame.draw.rect(screen, magenta, [self.x+3, self.y+3, 42,42])
        self.certRight = pygame.draw.rect(screen, green, [self.x+45, self.y+3, 3,42])
        self.certbottom = pygame.draw.rect(screen, blue, [self.x, self.y+45, 48,3])
        HitBoxes = [self.certall,self.certtop,self.certLeft,self.certIn,self.certRight,self.certbottom]
        return HitBoxes
