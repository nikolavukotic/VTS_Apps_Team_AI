import cv2
from yolo_processing.osoba import *
import math
import numpy as np 
from PIL import Image as im
from yolo_processing.yolo import *

#done
class BicepsConfig:
    angleLeftShoulderLower = 0
    angleLeftShoulderUpper = 40

    angleLeftShoulderLimitGreen = 35
    
    angleLeftElbowLower = 30
    angleLeftElbowUpper = 190

    angleLeftElbowLimitGreen = 180

    angleRightSoulderLower = 0
    angleRightSoulderUpper = 40

    angleRightShoulderLimitGreen = 35

    angleRightElbowLower = 30
    angleRightElbowUpper = 190

    angleRightElbowLimitGreen = 180

    def check(osoba):
        s = 0
        rightVisibility = round((osoba.desniKuk.visibility + osoba.desnoRame.visibility + osoba.desniLakat.visibility + osoba.desnaSaka.visibility + osoba.desnoStopalo.visibility)/5,2)
        leftVisibility = round((osoba.leviKuk.visibility + osoba.levoRame.visibility + osoba.leviLakat.visibility + osoba.levaSaka.visibility + osoba.levoStopalo.visibility)/5,2)
        
        print('desno')
        print(rightVisibility)
        print('levo')
        print(leftVisibility)

        if(rightVisibility>leftVisibility):
            s = 1
        elif(leftVisibility>rightVisibility):
            s= 2
        elif(rightVisibility==leftVisibility):
            s=3
            

        
        
        
        return s
#done    
class SquatConfig:
    angleLeftKneeLimitBlue = 95
    angleRightKneeLimitGreen = 80
    

    def check(osoba):
        s = 0
        rightVisibility = round((osoba.desniKuk.visibility + osoba.desnoStopalo.visibility+osoba.desnoKoleno.visibility)/3,2)
        leftVisibility = round((osoba.leviKuk.visibility + osoba.levoStopalo.visibility+osoba.levoKoleno.visibility)/3,2)
        
        print('desno')
        print(rightVisibility)
        print('levo')
        print(leftVisibility)

        if(rightVisibility>leftVisibility):
            s = 1
        if(leftVisibility>rightVisibility):
            s= 2
        if(rightVisibility==leftVisibility or (abs((rightVisibility-leftVisibility)))<0.05):
            s=3
            

        
        
        
        return s  
                
class KneesConfig:
    angleLeftHipBoneLower = 85
    angleLeftHipBoneUpper = 185
    
    angleRightHipBoneLower = 85
    angleRightHipBoneUpper = 185

    angleRightKneesLower = 80
    angleRightKneesLower = 100

    angleLeftKneesLower = 80
    angleLeftKneesLower = 100

    def check(osoba):
        x = 0
        if(osoba.desniKuk.visibility > 0.5 and osoba.desnoRame.visibility > 0.5 and osoba.desnoStopalo.visibility > 0.5 and osoba.desnoKoleno.visibility > 0.5 or osoba.leviKuk.visibility > 0.5 and osoba.levoRame.visibility > 0.5 and osoba.levoStopalo.visibility > 0.5 and osoba.levoKoleno.visibility > 0.5):
            x = 1
        else:
            x = 2
        
        return x
   #done 
#done
class FlyConfig:
    angleLeftShoulderLower = 18
    angleLeftShoulderUpper = 100

    angleLeftShoulderLimitGreenL = 20
    angleLeftShoulderLimitGreenU = 85
    
    angleLeftElbowLower = 100
    angleLeftElbowUpper = 150

    angleRightShoulderLower = 18
    angleRightShoulderUpper = 100

    angleRightShoulderLimitGreenL = 20
    angleRightShoulderLimitGreenU = 85

    angleRightElbowLower = 100
    angleRightElbowUpper = 150

    def check(osoba):
        s = 0
        rightVisibility = round((osoba.desniKuk.visibility + osoba.desnoRame.visibility + osoba.desniLakat.visibility + osoba.desnaSaka.visibility)/4,2)
        leftVisibility = round((osoba.leviKuk.visibility + osoba.levoRame.visibility + osoba.leviLakat.visibility + osoba.levaSaka.visibility)/4,2)
        
        print('desno')
        print(rightVisibility)
        print('levo')
        print(leftVisibility)

        if(rightVisibility>leftVisibility):
            s = 1
        if(leftVisibility>rightVisibility):
            s= 2
        if(rightVisibility==leftVisibility or (abs((rightVisibility-leftVisibility)))<0.05):
            s=3
            
        return s
      
class PushUpsConfig:
    angleLeftElbowLower = 85
    angleLeftElbowUpper = 185
    
    angleRightElbowLower = 85
    angleRightElbowUpper = 185

    angleLeftBodyLower = 170
    angleLeftBodyUpper = 190
    
    angleRightBodyLower = 170
    angleRightBodyUpper = 190

    def check(osoba):
        x = 0
        if(osoba.desniKuk.visibility > 0.5 and osoba.desnoRame.visibility > 0.5 and osoba.desniLakat.visibility > 0.5 and osoba.desnaSaka.visibility > 0.5 and osoba.desnoKoleno.visibility > 0.5 and osoba.desnoStopalo.visibility > 0.5 or osoba.leviKuk.visibility > 0.5 and osoba.levoRame.visibility > 0.5 and osoba.leviLakat.visibility > 0.5 and osoba.levaSaka.visibility > 0.5 and osoba.levoKoleno.visibility > 0.5 and osoba.levoStopalo.visibility > 0.5):
            x = 1
        else:
            x = 2
        
        return x

class AbsConfig:
    angleLeftBodyLower = 100
    angleLeftBodyUpper = 150
    
    angleRightBodyLower = 100
    angleRightBodyUpper = 150

    def check(osoba):
        x = 0
        if(osoba.desniKuk.visibility > 0.5 and osoba.desnoRame.visibility > 0.5 and osoba.desnoKoleno.visibility > 0.5 and osoba.desnoStopalo.visibility > 0.5 or osoba.leviKuk.visibility > 0.5 and osoba.levoRame.visibility > 0.5 and osoba.levoKoleno.visibility > 0.5 and osoba.levoStopalo.visibility > 0.5):
            x = 1
        else:
            x = 2
        
        return x

class DeadLiftConfig:
    #angleLeftElbowLower = 85
    #angleLeftElbowUpper = 185
    
    #angleRightElbowLower = 85
    #angleRightElbowUpper = 185

    #angleLeftBodyLower = 170
    #angleLeftBodyUpper = 190
    
    #angleRightBodyLower = 170
    #angleRightBodyUpper = 190

    def check(osoba):
        x = 0
        if(osoba.desniKuk.visibility > 0.5 and osoba.desnoRame.visibility > 0.5 and osoba.desniLakat.visibility > 0.5 and osoba.desnaSaka.visibility > 0.5 and osoba.desnoKoleno.visibility > 0.5 and osoba.desnoStopalo.visibility > 0.5 or osoba.leviKuk.visibility > 0.5 and osoba.levoRame.visibility > 0.5 and osoba.leviLakat.visibility > 0.5 and osoba.levaSaka.visibility > 0.5 and osoba.levoKoleno.visibility > 0.5 and osoba.levoStopalo.visibility > 0.5):
            x = 1
        else:
            x = 1
        
        return x