import Level_Builder as L
import Second_Classes as SC

black = [0,0,0]
white = [255,255,255]
red = [255,0,0]
blue =[0,0,255]
green = [0,255,0]
magenta = [255,0,255]

BlockGroup = []
EnemyGroup = []

def Save(screen):
   B = {}
   Enemy = {}
   Trump_Wall = L.level(0, 0, 0, 40, 1680, black, False)
   Done = L.level(0, 1480, 940, 200, 40, green, True)
   Origin_Block = L.level(0, -1, 0, 1, 1, white, True)
   E1 = L.level(0,40, 948, 100, 20, black, True)
   BlockGroup.append(Done)
   BlockGroup.append(E1)
   BlockGroup.append(Origin_Block)
   BlockGroup.append(Trump_Wall)
   B[0] = L.level(816, 500, 165, 316, 153, [0, 0, 0], True)
   BlockGroup.append(B[0])
   B[1] = L.level(1490, 161, 905, 1329, 35, [0, 0, 0], True)
   BlockGroup.append(B[1])
   B[2] = L.level(1297, 1106, 488, 191, 91, [0, 0, 0], True)
   BlockGroup.append(B[2])
   B[3] = L.level(608, 1844, 892, 444, 67, [0, 0, 0], True)
   BlockGroup.append(B[3])
   B[4] = L.level(930, 2220, 330, 390, 335, [0, 0, 0], True)
   BlockGroup.append(B[4])
   B[5] = L.level(1403, 2700, 771, 383, 151, [0, 0, 0], True)
   BlockGroup.append(B[5])
   B[6] = L.level(1437, 3445, 827, 1352, 85, [0, 0, 0], True)
   BlockGroup.append(B[6])
   B[7] = L.level(1112, 4082, 508, 390, 199, [0, 0, 0], True)
   BlockGroup.append(B[7])
   Enemy[0] = SC.Enemy(3503, 826)
   Enemy[0].Hitbox(screen) 
   EnemyGroup.append(Enemy[0])
   Enemy[1] = SC.Enemy(3664, 836)
   Enemy[1].Hitbox(screen) 
   EnemyGroup.append(Enemy[1])
   Enemy[2] = SC.Enemy(3873, 839)
   Enemy[2].Hitbox(screen) 
   EnemyGroup.append(Enemy[2])
   Enemy[3] = SC.Enemy(4018, 834)
   Enemy[3].Hitbox(screen) 
   EnemyGroup.append(Enemy[3])
   Enemy[4] = SC.Enemy(4165, 828)
   Enemy[4].Hitbox(screen) 
   EnemyGroup.append(Enemy[4])
   return BlockGroup, EnemyGroup