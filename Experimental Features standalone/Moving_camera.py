import pygame, Moving_camera

MC = Moving_camera

screen = pygame.display.set_mode((1280,1024))
world = pygame.display.set_mode((2580,1024))

running = True

camerax = 0
cameraY = 0

black = [0, 0, 0]
white = [255, 255, 255]

def move():
    key = pygame.key.get_pressed() # Registers key press
    dist = 3
    if key[pygame.K_w]:
        MC.cameraY -= 5
    elif key[pygame.K_s]:
        MC.cameraY += 5
    elif key[pygame.K_a]:
        MC.camerax -= 5
    elif key[pygame.K_d]:
        MC.camerax += 5

while running == True:
    world.fill(white)
    move()
    Rect1 = pygame.draw.rect(world, black, [100+camerax, 1000+cameraY, 200,50])
    Rect2 = pygame.draw.rect(world, black, [1005+camerax, 500+cameraY, 125, 60])
    Rect3 = pygame.draw.rect(world, black, [543+camerax, 234+cameraY, 153,74])
    print(camerax)
    pygame.display.update()
    for event in pygame.event.get():
            if event.type == pygame.QUIT: #For ending the loop
                pygame.quit()
                running = False