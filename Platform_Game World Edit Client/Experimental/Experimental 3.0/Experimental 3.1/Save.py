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
   B[0] = L.level(1661, 40-L.Screen_DiffX, 954-L.Screen_DiffY, 1621, 17, [0, 0, 0], True)
   BlockGroup.append(B[0])
   Power_Up[1] = C.Power_Ups('Speed', 920, 917)
   PowerUpGroup.append(Power_Up[1])
   Power_Up[2] = C.Power_Ups('Speed', 978, 904)
   PowerUpGroup.append(Power_Up[2])
   Power_Up[3] = C.Power_Ups('Speed', 1047, 908)
   PowerUpGroup.append(Power_Up[3])
   Power_Up[4] = C.Power_Ups('Jumps', 1088, 899)
   PowerUpGroup.append(Power_Up[4])
   Power_Up[5] = C.Power_Ups('Jumps', 1154, 904)
   PowerUpGroup.append(Power_Up[5])
   Power_Up[6] = C.Power_Ups('Jumps', 1229, 909)
   PowerUpGroup.append(Power_Up[6])
   Power_Up[7] = C.Power_Ups('JumpBoost', 1266, 904)
   PowerUpGroup.append(Power_Up[7])
   Power_Up[8] = C.Power_Ups('JumpBoost', 1336, 910)
   PowerUpGroup.append(Power_Up[8])
   Power_Up[9] = C.Power_Ups('JumpBoost', 1393, 911)
   PowerUpGroup.append(Power_Up[9])
   B[10] = L.level(1655, 1684-L.Screen_DiffX, 951-L.Screen_DiffY, 1651, 16, [0, 0, 0], True)
   BlockGroup.append(B[10])
   return BlockGroup, EnemyGroup, PowerUpGroup