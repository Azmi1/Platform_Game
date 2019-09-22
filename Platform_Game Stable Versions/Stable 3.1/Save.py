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
   B[0] = L.level(1320, 912-L.Screen_DiffX, 863-L.Screen_DiffY, 408, 43, [0, 0, 0], True)
   BlockGroup.append(B[0])
   B[1] = L.level(768, 159-L.Screen_DiffX, 794-L.Screen_DiffY, 609, 105, [0, 0, 0], True)
   BlockGroup.append(B[1])
   B[2] = L.level(1076, 728-L.Screen_DiffX, 696-L.Screen_DiffY, 348, 14, [45, 15, 60], True)
   BlockGroup.append(B[2])
   B[3] = L.level(1116, 490-L.Screen_DiffX, 406-L.Screen_DiffY, 626, 117, [45, 15, 60], True)
   BlockGroup.append(B[3])
   B[4] = L.level(1629, 1162-L.Screen_DiffX, 693-L.Screen_DiffY, 467, 80, [0, 0, 0], True, True, Pictures[0])
   BlockGroup.append(B[4])
   B[5] = L.level(744, 1705-L.Screen_DiffX, 710-L.Screen_DiffY, 719, 136, [0, 0, 0], True, True, Pictures[0])
   BlockGroup.append(B[5])
   B[6] = L.level(1670, 2739-L.Screen_DiffX, 439-L.Screen_DiffY, 611, 292, [0, 0, 0], True, True, Pictures[0])
   BlockGroup.append(B[6])
   Enemy[0] = SC.Enemy(1990-L.Screen_DiffX, 710-L.Screen_DiffY)
   Enemy[0].Hitbox(screen) 
   EnemyGroup.append(Enemy[0])
   Enemy[1] = SC.Enemy(2304-L.Screen_DiffX, 710-L.Screen_DiffY)
   Enemy[1].Hitbox(screen) 
   EnemyGroup.append(Enemy[1])
   Enemy[2] = SC.Enemy(2897-L.Screen_DiffX, 439-L.Screen_DiffY)
   Enemy[2].Hitbox(screen) 
   EnemyGroup.append(Enemy[2])
   Power_Up[7] = C.Power_Ups('Jumps', 1790, 63)
   PowerUpGroup.append(Power_Up[7])
   Power_Up[8] = C.Power_Ups('Jumps', 919, 841)
   PowerUpGroup.append(Power_Up[8])
   Power_Up[9] = C.Power_Ups('Jumps', 1003, 817)
   PowerUpGroup.append(Power_Up[9])
   Power_Up[10] = C.Power_Ups('JumpBoost', 1785, 206)
   PowerUpGroup.append(Power_Up[10])
   Power_Up[11] = C.Power_Ups('JumpBoost', 1167, 650)
   PowerUpGroup.append(Power_Up[11])
   Power_Up[12] = C.Power_Ups('JumpBoost', 1296, 651)
   PowerUpGroup.append(Power_Up[12])
   Power_Up[13] = C.Power_Ups('JumpBoost', 1405, 659)
   PowerUpGroup.append(Power_Up[13])
   return BlockGroup, EnemyGroup, PowerUpGroup