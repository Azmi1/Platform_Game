import pygame, time, Enemy, Renderer

black = [0,0,0]
white = [255,255,255]
red = [255,0,0]
blue =[0,0,255]
green = [0,255,0]
magenta = [255,0,255]

BGroup = pygame.sprite.Group()

class enemy(pygame.sprite.Sprite):
    def __init__(Him):
        l=0
    def create(Him, screen, x, y, width, height, color):
        pygame.sprite.Sprite.__init__(Him)
        Him.y = y
        Him.x = x
        Him.width = width
        Him.height = height
        Him.rect = pygame.draw.rect(screen, color, [Him.x, Him.y, width,height])
        BGroup.add(Him)
        return Him.rect
