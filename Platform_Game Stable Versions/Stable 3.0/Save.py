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
   B[0] = L.level(1236, 896-L.Screen_DiffX, 908-L.Screen_DiffY, 340, 11, [0, 0, 0], True)
   BlockGroup.append(B[0])
   B[1] = L.level(1611, 1381-L.Screen_DiffX, 911-L.Screen_DiffY, 230, 15, [0, 0, 0], True)
   BlockGroup.append(B[1])
   Enemy[0] = SC.Enemy(1405-L.Screen_DiffX, 908-L.Screen_DiffY)
   Enemy[0].Hitbox(screen) 
   EnemyGroup.append(Enemy[0])
   Enemy[1] = SC.Enemy(1163-L.Screen_DiffX, 902-L.Screen_DiffY)
   Enemy[1].Hitbox(screen) 
   EnemyGroup.append(Enemy[1])
   B[2] = L.level(264, 1705-L.Screen_DiffX, 910-L.Screen_DiffY, 239, 23, [0, 0, 0], True)
   BlockGroup.append(B[2])
   B[3] = L.level(785, 2048-L.Screen_DiffX, 913-L.Screen_DiffY, 417, 23, [0, 0, 0], True)
   BlockGroup.append(B[3])
   B[4] = L.level(1394, 2576-L.Screen_DiffX, 910-L.Screen_DiffY, 498, 52, [0, 0, 0], True)
   BlockGroup.append(B[4])
   Enemy[2] = SC.Enemy(1763-L.Screen_DiffX, 903-L.Screen_DiffY)
   Enemy[2].Hitbox(screen) 
   EnemyGroup.append(Enemy[2])
   Enemy[3] = SC.Enemy(2261-L.Screen_DiffX, 909-L.Screen_DiffY)
   Enemy[3].Hitbox(screen) 
   EnemyGroup.append(Enemy[3])
   Enemy[4] = SC.Enemy(2706-L.Screen_DiffX, 902-L.Screen_DiffY)
   Enemy[4].Hitbox(screen) 
   EnemyGroup.append(Enemy[4])
   return BlockGroup, EnemyGroup