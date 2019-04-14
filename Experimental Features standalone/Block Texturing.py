import pygame

screen = pygame.display.set_mode((1240,1240))

Block_Image = pygame.image.load("Images/Block.jpg")

class Block(object):
    def __init__(self, x, y, width, height, Image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = Image

    def draw(self, screen):
        screen.blit(self.image,(self.x, self.y),(0,0, self.width, self.height))

running = True

Block_1 = Block(100, 100, 1000, 200, Block_Image)

while running == True:
    Block_1.draw(screen)
    pygame.display.update()
    for event in pygame.event.get():
            if event.type == pygame.QUIT: #For ending the loop
                pygame.quit()
                running = False
