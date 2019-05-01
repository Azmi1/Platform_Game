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
   BlockGroup.append(E1)
   BlockGroup.append(Origin_Block)
   BlockGroup.append(Trump_Wall)
   B[0] = L.level(1134, 553, 180, 581, 153, [0, 0, 0], True)
   BlockGroup.append(B[0])
   B[1] = L.level(1478, 1054, 350, 424, 132, [0, 0, 40], True)
   BlockGroup.append(B[1])
   B[2] = L.level(1511, 1190, 164, 321, 130, [0, 60, 40], True)
   BlockGroup.append(B[2])
   B[3] = L.level(1183, 503, 256, 680, 230, [0, 85, 255], True)
   BlockGroup.append(B[3])
   B[4] = L.level(1160, 690, 470, 470, 221, [0, 255, 255], True)
   BlockGroup.append(B[4])
   B[5] = L.level(1438, 1138, 630, 300, 132, [0, 255, 145], True)
   BlockGroup.append(B[5])
   return BlockGroup, EnemyGroup