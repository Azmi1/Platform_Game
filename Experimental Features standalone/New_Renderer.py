import pygame
import New_Renderer as NR

width = 1680
height = 980
screen = pygame.display.set_mode((width, height))

class Block(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, screen):
        pygame.draw.rect(screen,[255, 255, 255], [self.x-NR.PosX, self.y, self.width, self.height])

Block_1 = Block(640,140,100,100)
Block_2 = Block(2320,340,100,100)
Block_3 = Block(4000,540,100,100)
Block_4 = Block(5680,740,100,100)

BlockGroup = [Block_1, Block_2, Block_3, Block_4]

running = True

mode = 0

PosX = 0
PosY = 0

def Get_Screen(mode):
    NR.PosX = 1680*mode

while NR.running == True:
    screen.fill([0, 0, 0])
    key = pygame.key.get_pressed()
    if key[pygame.K_1]:
        NR.mode = 0
    if key[pygame.K_2]:
        NR.mode = 1
    if key[pygame.K_3]:
        NR.mode = 2
    if key[pygame.K_4]:
        NR.mode = 3
    Get_Screen(NR.mode)
    NR.mode+=1
    if NR.mode == 4:
        NR.mode = 0
    print(NR.PosX)
    for block in BlockGroup:
        if block.x + block.width >= NR.PosX and block.x <= NR.PosX+1680:
            block.draw(screen)
    print("Hello")
    pygame.display.update()
    for event in pygame.event.get():
            if event.type == pygame.QUIT: #For ending the loop
                pygame.quit()
                NR.running=False