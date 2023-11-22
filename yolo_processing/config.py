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
    
    angleLeftElbowLower = 40
    angleLeftElbowUpper = 180

    angleLeftElbowLimitGreen = 160

    angleRightShoulderLower = 0
    angleRightShoulderUpper = 40

    angleRightShoulderLimitGreen = 35

    angleRightElbowLower = 40
    angleRightElbowUpper = 180

    angleRightElbowLimitGreen = 160

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
    angleKneeLimitBlue = 95
    angleKneeLimitGreen = 80
    

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
        if(rightVisibility==leftVisibility): #or (abs((rightVisibility-leftVisibility)))<0.1):
            s=3
            

        
        
        
        return s           
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
#done    
class PushUpsConfig:
    angleLeftElbowLower = 80
    angleLeftElbowUpper = 160
    
    angleRightElbowLower = 80
    angleRightElbowUpper = 160

    angleLeftElbowLimitGreenL = 95
    angleLeftElbowLimitGreenU = 155

    angleRightElbowLimitGreenL = 95
    angleRightElbowLimitGreenU = 155

    angleLeftBodyLower = 155
    angleLeftBodyUpper = 185
    
    angleRightBodyLower = 155
    angleRightBodyUpper = 185

    def check(osoba):
        s = 0
        rightVisibility = round((osoba.desniKuk.visibility + osoba.desnoRame.visibility + osoba.desniLakat.visibility + osoba.desnaSaka.visibility + osoba.desnoStopalo.visibility + osoba.desnoKoleno.visibility )/6,2)
        leftVisibility = round((osoba.leviKuk.visibility + osoba.levoRame.visibility + osoba.leviLakat.visibility + osoba.levaSaka.visibility + osoba.levoStopalo.visibility + osoba.levoKoleno.visibility)/6,2)
        
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
class AbsConfig:
    angleLeftBodyLower = 60
    angleLeftBodyUpper = 140
    
    angleLeftBodyLimitGreenL = 65
    angleLeftBodyLimitGreenU = 135

    angleRightBodyLower = 60
    angleRightBodyUpper = 140

    angleRightBodyLimitGreenL = 65
    angleRightBodyLimitGreenU = 135

    angleRightKneeLower = 170
    angleRightKneeUpper = 190

    angleRightKneeLimitGreenL = 175
    angleRightKneeLimitGreenU = 185

    angleLeftKneeLower = 170
    angleLeftKneeUpper = 190

    angleLeftKneeLimitGreenL = 175
    angleLeftKneeLimitGreenU = 185

    def check(osoba):
        s = 0
        rightVisibility = round((osoba.desniKuk.visibility + osoba.desnoRame.visibility + osoba.desnoStopalo.visibility + osoba.desnoKoleno.visibility )/4,2)
        leftVisibility = round((osoba.leviKuk.visibility + osoba.levoRame.visibility + osoba.levoStopalo.visibility + osoba.levoKoleno.visibility)/4,2)
        
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
class DeadLiftConfig:
    
    angleLeftKneeLower = 80
    angleLeftKneeUpper = 180

    angleLeftKneeLimitGreenL = 90
    angleLeftKneeLimitGreenU = 170

    angleLeftHipLower = 140 
    angleLeftHipUpper = 185

    angleLeftHipLimitGreenL = 70
    angleLeftHipLimitGreenU = 175

    angleRightKneeLower = 80
    angleRightKneeUpper = 180

    angleRightKneeLimitGreenL = 90
    angleRightKneeLimitGreenU = 170

    angleRightHipLower = 140 
    angleRightHipUpper = 185

    angleRightHipLimituGreenL = 70
    angleRightHipLimituGreenU = 175

    def check(osoba):
        s = 0
        rightVisibility = round((osoba.desniKuk.visibility + osoba.desnoRame.visibility + osoba.desniLakat.visibility + osoba.desnaSaka.visibility + osoba.desnoStopalo.visibility + osoba.desnoKoleno.visibility )/6,2)
        leftVisibility = round((osoba.leviKuk.visibility + osoba.levoRame.visibility + osoba.leviLakat.visibility + osoba.levaSaka.visibility + osoba.levoStopalo.visibility + osoba.levoKoleno.visibility)/6,2)
        
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


    