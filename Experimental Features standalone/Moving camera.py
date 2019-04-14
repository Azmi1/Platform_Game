import pygame

screen = pygame.display.set_mode((1280,1024))
world = pygame.display.set_mode((2580,1024))

running = True

camerax = 0

black = [0, 0, 0]
white = [255, 255, 255]

while running == True:
    world.fill(white)
    Rect1 = pygame.draw.rect(world, black, [100+camerax, 1000, 200,50])
    Rect2 = pygame.draw.rect(world, black, [1005+camerax, 500, 125, 60])
    Rect3 = pygame.draw.rect(world, black, [543+camerax, 234, 153,74])
    camerax -= 5
    print(camerax)
    pygame.display.update()
    for event in pygame.event.get():
            if event.type == pygame.QUIT: #For ending the loop
                pygame.quit()
                running = False