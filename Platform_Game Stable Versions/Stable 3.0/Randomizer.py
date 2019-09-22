import Randomizer as rando
import Options as OPS
import random as rand
rand.seed()

First_Run = True

def Randomize(mode):
    if mode == "Power_Ups":
        if rando.First_Run == True:
            rando.Power_Ups_List = []
            for i in range(0, OPS.Max_Jumps_Rarity):
                rando.Power_Ups_List.append("Jumps")
            for i in range(0, OPS.Max_JumpBoost_Rarity):
                rando.Power_Ups_List.append("JumpBoost")
            for i in range(0, OPS.Max_Speed_Rarity):
                rando.Power_Ups_List.append("Speed")
            rando.First_Run = False
        print("Skupna vsota: ",OPS.Max_JumpBoost_Rarity + OPS.Max_Jumps_Rarity + OPS.Max_Speed_Rarity)
        print("V listu: ", len(rando.Power_Ups_List))
        rand.shuffle(rando.Power_Ups_List)
        return rando.Power_Ups_List[rand.randint(0,len(rando.Power_Ups_List))]