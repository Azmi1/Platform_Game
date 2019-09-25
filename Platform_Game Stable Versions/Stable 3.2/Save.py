import Level_Builder as L
import Second_Classes as SC
import Options as OPS
import Classes as C
import os, pygame

black = [0,0,0]
white = [255,255,255]
red = [255,0,0]
blue =[0,0,255]
green = [0,255,0]
magenta = [255,0,255]

BlockGroup = []
EnemyGroup = []
PowerUpGroup = []
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
   Power_Up = {}
   Trump_Wall = L.level(0, 0-L.Screen_DiffX, 0-L.Screen_DiffY, 40, 1680, black, False)
   Origin_Block = L.level(0, 1-L.Screen_DiffX, 0-L.Screen_DiffY, 1, 1, white, True)
   E1 = L.level(0,OPS.width/2, 948-L.Screen_DiffY, 100, 20, black, True)
   BlockGroup.append(E1)
   BlockGroup.append(Origin_Block)
   BlockGroup.append(Trump_Wall)
   return BlockGroup, EnemyGroup, PowerUpGroup