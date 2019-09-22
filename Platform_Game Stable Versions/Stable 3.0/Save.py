import Level_Builder as L
import Second_Classes as SC
import Options as OPS
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
   Trump_Wall = L.level(0, 0-L.Screen_DiffX, 0-L.Screen_DiffY, 40, 1680, black, False)
   Origin_Block = L.level(0, 1-L.Screen_DiffX, 0-L.Screen_DiffY, 1, 1, white, True)
   E1 = L.level(0,OPS.width/2, 948-L.Screen_DiffY, 100, 20, black, True)
   BlockGroup.append(E1)
   BlockGroup.append(Origin_Block)
   BlockGroup.append(Trump_Wall)
   B[0] = L.level(1544, 921-L.Screen_DiffX, 866-L.Screen_DiffY, 623, 53, [0, 0, 0], True, True, Pictures[0])
   BlockGroup.append(B[0])
   B[1] = L.level(1641, 1573-L.Screen_DiffX, 830-L.Screen_DiffY, 68, 12, [0, 0, 0], True, True, Pictures[0])
   BlockGroup.append(B[1])
   B[2] = L.level(460, 1692-L.Screen_DiffX, 848-L.Screen_DiffY, 448, 24, [0, 0, 0], True, True, Pictures[0])
   BlockGroup.append(B[2])
   B[3] = L.level(1158, 2183-L.Screen_DiffX, 783-L.Screen_DiffY, 655, 13, [0, 0, 0], True, True, Pictures[0])
   BlockGroup.append(B[3])
   B[4] = L.level(1499, 2852-L.Screen_DiffX, 818-L.Screen_DiffY, 327, 40, [0, 0, 0], True, True, Pictures[0])
   BlockGroup.append(B[4])
   B[5] = L.level(1504, 2850-L.Screen_DiffX, 345-L.Screen_DiffY, 334, 329, [0, 0, 0], True, True, Pictures[0])
   BlockGroup.append(B[5])
   B[6] = L.level(646, 1958-L.Screen_DiffX, 275-L.Screen_DiffY, 368, 228, [0, 0, 0], True, True, Pictures[0])
   BlockGroup.append(B[6])
   return BlockGroup, EnemyGroup