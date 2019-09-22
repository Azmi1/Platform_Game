import pygame, os, Tab
import Platform_Game_WE as PGW

pygame.font.init()
myfontsmaller = pygame.font.SysFont('Comic Sans MS', 20)
myfont = pygame.font.SysFont('Comic Sans MS', 30)
myfontbigger = pygame.font.SysFont('Comic Sans MS', 45)
myfontbiggest = pygame.font.SysFont('Comic Sans MS', 75)
pygame.display.set_mode((10,10))

white = [255, 255, 255]
blue = [0, 0, 255]
black = [0, 0, 0]
red = [255, 0, 0]
R = 0
G = 0
B = 0


custom = [10,10,220, 52]
left = [10,918, 105, 52]
right = [125,918, 105, 52]
checkbox_up = [10,10, 52, 52]
writebox_up = [72, 10, 160, 52]
ImageBox_1 = [10, 72, 72, 72]
ImageCheck_1 = [92, 72, 72, 72]
ImageBox_2 = [10, 154, 72, 72]
ImageCheck_2 = [92, 154, 72, 72]
ImageBox_3 = [10, 236, 72, 72]
ImageCheck_3 = [92, 236, 72, 72]
ImageBox_left = [10, 318, 72, 36]
ImageBox_right = [92, 318, 72, 36]

ColourBox = [10, 318, 72, 72]
RBox = [10, 72, 54, 54]
RValueBox = [74, 72, 78, 54]
R1X = [162, 72, 16, 54]
R5X = [188, 72, 16, 54]
R10X = [214, 72, 16, 54]
GBox = [10, 154, 54, 54]
GValueBox = [74, 154, 78, 54]
G1X = [162, 154, 16, 54]
G5X = [188, 154, 16, 54]
G10X = [214, 154, 16, 54]
BBox = [10, 236, 54, 54]
BValueBox = [74, 236, 78, 54]
B1X = [162, 236, 16, 54]
B5X = [188, 236, 16, 54]
B10X = [214, 236, 16, 54]
CalcBox = [92, 318, 72, 72]


checkbox_1 = False
checkbox_1Presed = False
ImageCheckBox_1 = True
ImageCheckBox_2 = False
ImageCheckBox_3 = False

CalcValue = "+"
CalcValue_Pressed = False
Picture_ID = 0
picture = {}
Pictures = []
st = 0
Page = 0
entries = os.listdir('images/block_textures')
for entry in entries:
    picture[st] = pygame.image.load("images/block_textures/"+entry).convert_alpha()
    Pictures.append(picture[st])

def State(state, surf_1, surf_2):
    if state == "Normal":
        pygame.draw.rect(surf_2, white, custom)
        pygame.draw.rect(surf_2, white, left)
        pygame.draw.rect(surf_2, white, right)
        PS = myfont.render('Custom block', False, red)
        surf_2.blit(PS, (custom[0]+15,custom[1]+5))
        PS = myfont.render('<-----', False, red)
        surf_2.blit(PS, (left[0]+15,left[1]+5))
        PS = myfont.render('----->', False, red)
        surf_2.blit(PS, (right[0]+15,right[1]+5))
        if pygame.mouse.get_pressed()[0] == True and PGW.Break_Point == False:
            x, y = pygame.mouse.get_pos()
            PGW.Break_Point = True
            print("Checking for interactions")
            print(str(x)+ " " + str(y))
            if x >= custom[0] + 1680 and x <= custom[0] + custom[2] + 1680 and y >= custom[1] and y <= custom[1]+custom[3]:
                print("I interacted with custom")
                PGW.Chose = "Custom"
            elif x >= left[0] + 1680 and x <= left[0] + left[2] + 1680 and y >= left[1] and y <= left[1]+left[3]:
                print("I interacted with left")
                PGW.Move = "left"
                PGW.Page -= 1
            elif x >= right[0] + 1680 and x <= right[0] + 1680 + right[2] and y >= right[1] and y <= right[1] + right[3]:
                print("I interacted with right")
                PGW.Move = "right"
                PGW.Page+= 1
    elif state == "Custom":
        pygame.draw.rect(surf_2, white, checkbox_up)
        pygame.draw.rect(surf_2, white, writebox_up)
        PS = myfont.render('Image', False, red)
        surf_2.blit(PS, (writebox_up[0]+15,writebox_up[1]+5))
        if Tab.checkbox_1 == True:
            pygame.draw.rect(surf_2, blue, [checkbox_up[0]+5, checkbox_up[1]+5, 42, 42])
            pygame.draw.rect(surf_2, white, ImageBox_1)
            pygame.draw.rect(surf_2, white, ImageCheck_1)
            if Tab.ImageCheckBox_1 == True:
                    pygame.draw.rect(surf_2, blue, [ImageCheck_1[0]+5, ImageCheck_1[1]+5, 62, 62])
            if Tab.Page != 0:
                pygame.draw.rect(surf_2, white, ImageBox_left)
                PS = myfont.render('<----', False, red)
                surf_2.blit(PS, (ImageBox_left[0]+5,ImageBox_left[1]-5))
            if len(Pictures) > 3+3*Tab.Page:
                pygame.draw.rect(surf_2, white, ImageBox_right)
                PS = myfont.render('---->', False, red)
                surf_2.blit(PS, (ImageBox_right[0]+5,ImageBox_right[1]-5))
            surf_2.blit(pygame.transform.scale(Tab.Pictures[0+3*Tab.Page], (72, 72)), (10, 72))
            if len(Tab.Pictures) >= 2+3*Tab.Page:
                pygame.draw.rect(surf_2, white, ImageBox_2)
                pygame.draw.rect(surf_2, white, ImageCheck_2)
                surf_2.blit(pygame.transform.scale(Tab.Pictures[1+3*Tab.Page], (72, 72)),(10, 154))
                if Tab.ImageCheckBox_2 == True:
                    pygame.draw.rect(surf_2, blue, [ImageCheck_2[0]+5, ImageCheck_2[1]+5, 62, 62])
            if len(Tab.Pictures) >= 3+3*Tab.Page:
                pygame.draw.rect(surf_2, white, ImageBox_3)
                pygame.draw.rect(surf_2, white, ImageCheck_3)
                surf_2.blit(pygame.transform.scale(Tab.Pictures[2+3*Tab.Page], (72, 72)),(10, 236))
                if Tab.ImageCheckBox_3 == True:
                    pygame.draw.rect(surf_2, blue, [ImageCheck_3[0]+5, ImageCheck_3[1]+5, 62, 62])
        elif Tab.checkbox_1 == False:
            pygame.draw.rect(surf_2, white, RBox)
            PS = myfontbigger.render('R:', False, red)
            surf_2.blit(PS, (RBox[0]+5,RBox[1]-5))
            pygame.draw.rect(surf_2, white, RValueBox)
            PS = myfontbigger.render(str(Tab.R), False, red)
            surf_2.blit(PS, (RValueBox[0]+3,RValueBox[1]-5))
            pygame.draw.rect(surf_2, white, R1X)
            PS = myfontsmaller.render(Tab.CalcValue, False, red)
            surf_2.blit(PS, (R1X[0]+3,R1X[1]-10))
            PS = myfontsmaller.render('1', False, red)
            surf_2.blit(PS, (R1X[0]+3,R1X[1]+15))
            pygame.draw.rect(surf_2, white, R5X)
            PS = myfontsmaller.render(Tab.CalcValue, False, red)
            surf_2.blit(PS, (R5X[0]+3,R5X[1]-10))
            PS = myfontsmaller.render('5', False, red)
            surf_2.blit(PS, (R5X[0]+3,R5X[1]+15))
            pygame.draw.rect(surf_2, white, R10X)
            PS = myfontsmaller.render(Tab.CalcValue, False, red)
            surf_2.blit(PS, (R10X[0]+3,R10X[1]-10))
            PS = myfontsmaller.render('1', False, red)
            surf_2.blit(PS, (R10X[0]+3,R10X[1]+8))
            PS = myfontsmaller.render('0', False, red)
            surf_2.blit(PS, (R10X[0]+3,R10X[1]+27))
            pygame.draw.rect(surf_2, white, GBox)
            PS = myfontbigger.render('G:', False, red)
            surf_2.blit(PS, (GBox[0]+5,GBox[1]-5))
            pygame.draw.rect(surf_2, white, GValueBox)
            PS = myfontbigger.render(str(Tab.G), False, red)
            surf_2.blit(PS, (GValueBox[0]+3,GValueBox[1]-5))
            pygame.draw.rect(surf_2, white, G1X)
            PS = myfontsmaller.render(Tab.CalcValue, False, red)
            surf_2.blit(PS, (G1X[0]+3,G1X[1]-10))
            PS = myfontsmaller.render('1', False, red)
            surf_2.blit(PS, (G1X[0]+3,G1X[1]+15))
            pygame.draw.rect(surf_2, white, G5X)
            PS = myfontsmaller.render(Tab.CalcValue, False, red)
            surf_2.blit(PS, (G5X[0]+3,G5X[1]-10))
            PS = myfontsmaller.render('5', False, red)
            surf_2.blit(PS, (G5X[0]+3,G5X[1]+15))
            pygame.draw.rect(surf_2, white, G10X)
            PS = myfontsmaller.render(Tab.CalcValue, False, red)
            surf_2.blit(PS, (G10X[0]+3,G10X[1]-10))
            PS = myfontsmaller.render('1', False, red)
            surf_2.blit(PS, (G10X[0]+3,G10X[1]+8))
            PS = myfontsmaller.render('0', False, red)
            surf_2.blit(PS, (G10X[0]+3,G10X[1]+27))
            pygame.draw.rect(surf_2, white, BBox)
            PS = myfontbigger.render('B:', False, red)
            surf_2.blit(PS, (BBox[0]+5,BBox[1]-5))
            pygame.draw.rect(surf_2, white, BValueBox)
            PS = myfontbigger.render(str(Tab.B), False, red)
            surf_2.blit(PS, (BValueBox[0]+3,BValueBox[1]-5))
            pygame.draw.rect(surf_2, white, B1X)
            PS = myfontsmaller.render(Tab.CalcValue, False, red)
            surf_2.blit(PS, (B1X[0]+3,B1X[1]-10))
            PS = myfontsmaller.render('1', False, red)
            surf_2.blit(PS, (B1X[0]+3,B1X[1]+15))
            pygame.draw.rect(surf_2, white, B5X)
            PS = myfontsmaller.render(Tab.CalcValue, False, red)
            surf_2.blit(PS, (B5X[0]+3,B5X[1]-10))
            PS = myfontsmaller.render('5', False, red)
            surf_2.blit(PS, (B5X[0]+3,B5X[1]+15))
            pygame.draw.rect(surf_2, white, B10X)
            PS = myfontsmaller.render(Tab.CalcValue, False, red)
            surf_2.blit(PS, (B10X[0]+3,B10X[1]-10))
            PS = myfontsmaller.render('1', False, red)
            surf_2.blit(PS, (B10X[0]+3,B10X[1]+8))
            PS = myfontsmaller.render('0', False, red)
            surf_2.blit(PS, (B10X[0]+3,B10X[1]+27))
            pygame.draw.rect(surf_2, [Tab.R, Tab.G, Tab.B], ColourBox)
            pygame.draw.rect(surf_2, white, CalcBox)
            PS = myfontbiggest.render('+', False, red)
            surf_2.blit(PS, (CalcBox[0]+1,CalcBox[1]-40))
            PS = myfontbiggest.render('/', False, red)
            surf_2.blit(PS, (CalcBox[0]+15,CalcBox[1]-15))
            PS = myfontbiggest.render('-', False, red)
            surf_2.blit(PS, (CalcBox[0]+35,CalcBox[1]-10))
        pygame.draw.rect(surf_2, white, left)
        pygame.draw.rect(surf_2, white, right)
        PS = myfont.render('<------', False, red)
        surf_2.blit(PS, (left[0]+15,left[1]+5))
        PS = myfont.render('------>', False, red)
        surf_2.blit(PS, (right[0]+15,right[1]+5))
        if pygame.mouse.get_pressed()[0] == True and PGW.Break_Point == False:
            x, y = pygame.mouse.get_pos()
            Tab.checkbox_1Presed = False
            Tab.CalcValue_Pressed = False
            print("Checking for interactions")
            print(str(x)+ " " + str(y))
            if x >= left[0] + 1680 and x <= left[0] + left[2] + 1680 and y >= left[1] and y <= left[1]+left[3]:
                print("I interacted with left")
                PGW.Move = "left"
                PGW.Page -= 1
                PGW.Break_Point = True
            elif x >= right[0] + 1680 and x <= right[0] + 1680 + right[2] and y >= right[1] and y <= right[1] + right[3]:
                print("I interacted with right")
                PGW.Move = "right"
                PGW.Page+= 1
                PGW.Break_Point = True
            elif x >= checkbox_up[0] + 1680 and x <= checkbox_up[0] + 1680 + checkbox_up[2] and y >= checkbox_up[1] and y <= checkbox_up[1] + checkbox_up[3]:
                print("I interacted with checkbox_up")
                PGW.Break_Point = True
                if Tab.checkbox_1 == False and Tab.checkbox_1Presed == False:
                    Tab.checkbox_1 = True
                    PGW.Image = True
                    Tab.checkbox_1Presed = True
                if Tab.checkbox_1 == True and Tab.checkbox_1Presed == False:
                    Tab.checkbox_1 = False
                    PGW.Image = False
                    Tab.checkbox_1Presed = True
            elif x >= ImageBox_right[0] + 1680 and x <= ImageBox_right[0] + 1680 + ImageBox_right[2] and y >= ImageBox_right[1] and y <= ImageBox_right[1] + ImageBox_right[3] and len(Pictures) > 3+3*Tab.Page:
                Tab.Page += 1
                PGW.Break_Point = True
            elif x >= ImageBox_left[0] + 1680 and x <= ImageBox_left[0] + 1680 + ImageBox_left[2] and y >= ImageBox_left[1] and y <= ImageBox_left[1] + ImageBox_left[3] and Tab.Page != 0:
                Tab.Page -= 1
                PGW.Break_Point = True
            elif x >= ImageCheck_1[0] + 1680 and x <= ImageCheck_1[0] + 1680 + ImageCheck_1[2] and y >= ImageCheck_1[1] and y <= ImageCheck_1[1] + ImageCheck_1[3] and Tab.ImageCheckBox_1 != True:
                Tab.ImageCheckBox_1 = True
                Tab.ImageCheckBox_2 = False
                Tab.ImageCheckBox_3 = False
                Tab.Picture_ID = 0+3*Tab.Page
                PGW.Break_Point = True
            elif x >= ImageCheck_2[0] + 1680 and x <= ImageCheck_2[0] + 1680 + ImageCheck_2[2] and y >= ImageCheck_2[1] and y <= ImageCheck_2[1] + ImageCheck_2[3] and Tab.ImageCheckBox_2 != True:
                Tab.ImageCheckBox_1 = False
                Tab.ImageCheckBox_2 = True
                Tab.ImageCheckBox_3 = False
                Tab.Picture_ID = 1+3*Tab.Page
                PGW.Break_Point = True
            elif x >= ImageCheck_3[0] + 1680 and x <= ImageCheck_3[0] + 1680 + ImageCheck_3[2] and y >= ImageCheck_3[1] and y <= ImageCheck_3[1] + ImageCheck_3[3] and Tab.ImageCheckBox_3 != True:
                Tab.ImageCheckBox_1 = False
                Tab.ImageCheckBox_2 = False
                Tab.ImageCheckBox_3 = True
                Tab.Picture_ID = 2+3*Tab.Page
                PGW.Break_Point = True
            elif x >= CalcBox[0] + 1680 and x <= CalcBox[0] + 1680 + CalcBox[2] and y >= CalcBox[1] and y <= CalcBox[1] + CalcBox[3]:
                if Tab.CalcValue == "+" and Tab.CalcValue_Pressed == False:
                    Tab.CalcValue = "-"
                    Tab.CalcValue_Pressed = True
                if Tab.CalcValue == "-" and Tab.CalcValue_Pressed == False:
                    Tab.CalcValue = "+"
                    Tab.CalcValue_Pressed = True
                PGW.Break_Point = True
        if pygame.mouse.get_pressed()[0] == True and PGW.Break_Point_Fast == False:
            x, y = pygame.mouse.get_pos()
            if x >= R1X[0] + 1680 and x <= R1X[0] + 1680 + R1X[2] and y >= R1X[1] and y <= R1X[1] + R1X[3]:
                if Tab.CalcValue == "+" and Tab.R < 255:
                    Tab.R +=1
                elif Tab.CalcValue == "-" and Tab.R > 0:
                    Tab.R -=1
                PGW.Break_Point_Fast = True
            elif x >= R5X[0] + 1680 and x <= R5X[0] + 1680 + R5X[2] and y >= R5X[1] and y <= R5X[1] + R5X[3]:
                if Tab.CalcValue == "+" and Tab.R < 251:
                    Tab.R +=5
                elif Tab.CalcValue == "-" and Tab.R > 4:
                    Tab.R -=5
                PGW.Break_Point_Fast = True
            elif x >= R10X[0] + 1680 and x <= R10X[0] + 1680 + R10X[2] and y >= R10X[1] and y <= R10X[1] + R10X[3]:
                if Tab.CalcValue == "+" and Tab.R < 246:
                    Tab.R +=10
                elif Tab.CalcValue == "-" and Tab.R > 9:
                    Tab.R -=10
                PGW.Break_Point_Fast = True
            elif x >= G1X[0] + 1680 and x <= G1X[0] + 1680 + G1X[2] and y >= G1X[1] and y <= G1X[1] + G1X[3]:
                if Tab.CalcValue == "+" and Tab.G < 255:
                    Tab.G +=1
                elif Tab.CalcValue == "-" and Tab.G > 0:
                    Tab.G -=1
                PGW.Break_Point_Fast = True
            elif x >= G5X[0] + 1680 and x <= G5X[0] + 1680 + G5X[2] and y >= G5X[1] and y <= G5X[1] + G5X[3]:
                if Tab.CalcValue == "+" and Tab.G < 251:
                    Tab.G +=5
                elif Tab.CalcValue == "-" and Tab.G > 4:
                    Tab.G -=5
                PGW.Break_Point_Fast = True
            elif x >= G10X[0] + 1680 and x <= G10X[0] + 1680 + G10X[2] and y >= G10X[1] and y <= G10X[1] + G10X[3]:
                if Tab.CalcValue == "+" and Tab.G < 246:
                    Tab.G +=10
                elif Tab.CalcValue == "-" and Tab.G > 9:
                    Tab.G -=10
                PGW.Break_Point_Fast = True
            elif x >= B1X[0] + 1680 and x <= B1X[0] + 1680 + B1X[2] and y >= B1X[1] and y <= B1X[1] + B1X[3]:
                if Tab.CalcValue == "+" and Tab.B < 255:
                    Tab.B +=1
                elif Tab.CalcValue == "-" and Tab.B > 0:
                    Tab.B -=1
                PGW.Break_Point_Fast = True
            elif x >= B5X[0] + 1680 and x <= B5X[0] + 1680 + B5X[2] and y >= B5X[1] and y <= B5X[1] + B5X[3]:
                if Tab.CalcValue == "+" and Tab.B < 251:
                    Tab.B +=5
                elif Tab.CalcValue == "-" and Tab.B > 4:
                    Tab.B -=5
                PGW.Break_Point_Fast = True
            elif x >= B10X[0] + 1680 and x <= B10X[0] + 1680 + B10X[2] and y >= B10X[1] and y <= B10X[1] + B10X[3]:
                if Tab.CalcValue == "+" and Tab.B < 246:
                    Tab.B +=10
                elif Tab.CalcValue == "-" and Tab.B > 9:
                    Tab.B -=10
                PGW.Break_Point_Fast = True