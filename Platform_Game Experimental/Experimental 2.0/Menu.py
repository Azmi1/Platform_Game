import pygame

# Defines colours
white = [255, 255, 255]
red = [255, 0, 0]
black = [0, 0, 0]

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

screen = pygame.display.set_mode((840,480))

screen.fill(white)

Running = True
 
Him = pygame.draw.rect(screen, black, [50, 50, 225, 50])
PS = myfont.render('Start the game', False, white)
screen.blit(PS, [55,50])

pygame.display.update()

while Running == True: # Main loop for menu
    print("Working...")
    if pygame.mouse.get_pressed()[0] == True:
        x, y = pygame.mouse.get_pos()
        if x > 50 and x < 275 and y > 50 and y < 100:
            import Platform_Game
    for event in pygame.event.get():
            if event.type == pygame.QUIT: #For ending the loop
                pygame.quit()
                Running = False
