import pygame,time

screen = pygame.display.set_mode((100,100))

image = pygame.image.load("explosion.hasgraphics.png")

white=[0,0,0]
j=2
Pixel_down = 100
for i in range(1,72):
    if i%10==0:
        Pixel_down = 100 * j
        j+=1
    Pixel_left = 100*i
    screen.fill(white)
    screen.blit( image, (0, 0), (Pixel_down, Pixel_left, 100, 100) )
    pygame.display.update()
    time.sleep(0.05)