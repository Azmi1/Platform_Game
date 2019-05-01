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
   B[0] = L.level(1161, 237, 916, 924, 33, [0, 0, 0], True)
   BlockGroup.append(B[0])
   B[1] = L.level(1203, 751, 712, 452, 93, [0, 0, 0], True)
   BlockGroup.append(B[1])
   B[2] = L.level(505, 347, 727, 158, 65, [0, 0, 0], True)
   BlockGroup.append(B[2])
   Enemy[0] = SC.Enemy(881, 919)
   Enemy[0].Hitbox(screen) 
   EnemyGroup.append(Enemy[0])
   Enemy[1] = SC.Enemy(890, 711)
   Enemy[1].Hitbox(screen) 
   EnemyGroup.append(Enemy[1])
   Enemy[2] = SC.Enemy(397, 722)
   Enemy[2].Hitbox(screen) 
   EnemyGroup.append(Enemy[2])
   B[3] = L.level(1634, 1188, 863, 446, 66, [0, 0, 0], True)
   BlockGroup.append(B[3])
   B[4] = L.level(1537, 1175, 528, 362, 166, [0, 0, 0], True)
   BlockGroup.append(B[4])
   Enemy[3] = SC.Enemy(1283, 527)
   Enemy[3].Hitbox(screen) 
   EnemyGroup.append(Enemy[3])
   B[5] = L.level(1083, 743, 435, 340, 148, [0, 0, 0], True)
   BlockGroup.append(B[5])
   Enemy[4] = SC.Enemy(1022, 431)
   Enemy[4].Hitbox(screen) 
   EnemyGroup.append(Enemy[4])
   B[6] = L.level(308, 1724, 823, 264, 123, [0, 0, 0], True)
   BlockGroup.append(B[6])
   Enemy[5] = SC.Enemy(1853, 822)
   Enemy[5].Hitbox(screen) 
   EnemyGroup.append(Enemy[5])
   B[7] = L.level(926, 2003, 768, 603, 80, [0, 0, 0], True)
   BlockGroup.append(B[7])
   Enemy[6] = SC.Enemy(2322, 778)
   Enemy[6].Hitbox(screen) 
   EnemyGroup.append(Enemy[6])
   Enemy[7] = SC.Enemy(2211, 766)
   Enemy[7].Hitbox(screen) 
   EnemyGroup.append(Enemy[7])
   B[8] = L.level(1481, 2665, 710, 496, 125, [0, 0, 0], True)
   BlockGroup.append(B[8])
   Enemy[8] = SC.Enemy(2768, 709)
   Enemy[8].Hitbox(screen) 
   EnemyGroup.append(Enemy[8])
   Enemy[9] = SC.Enemy(2995, 711)
   Enemy[9].Hitbox(screen) 
   EnemyGroup.append(Enemy[9])
   return BlockGroup, EnemyGroup