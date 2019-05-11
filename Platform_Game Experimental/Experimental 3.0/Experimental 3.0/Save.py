import Level_Builder as L
import Second_Classes as SC
import os, pygame

black = [0,0,0]
white = [255,255,255]
red = [255,0,0]
blue =[0,0,255]
green = [0,255,0]
magenta = [255,0,255]

BlockGroup = []
EnemyGroup = []
picture = {}
Pictures = []
st = 0

entries = os.listdir('images/block_textures')
for entry in entries:
   picture[st] = pygame.image.load('images/block_textures/'+entry).convert_alpha()
   Pictures.append(picture[st])
   st+=1
def Save(screen):
   B = {}
   Enemy = {}
   Trump_Wall = L.level(0, 0, 0, 40, 1680, black, False)
   Origin_Block = L.level(0, -1, 0, 1, 1, white, True)
   E1 = L.level(0,40, 948, 100, 20, black, True)
   E2 = L.level(0,800, 948, 100, 20, black, True)
   BlockGroup.append(E1)
   BlockGroup.append(E2)
   BlockGroup.append(Origin_Block)
   BlockGroup.append(Trump_Wall)
   return BlockGroup, EnemyGroup