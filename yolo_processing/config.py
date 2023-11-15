import cv2
from yolo_processing.osoba import *
import math
import numpy as np 
from PIL import Image as im
from yolo_processing.yolo import *

class BicepsConfig:
    angleLeftShoulderLower = 0
    angleLeftShoulderUpper = 30
    
    angleRightSoulderLower = 0
    angleRightSoulderUpper = 30

    angleLeftElbowLower = 30
    angleLeftElbowUpper = 190

    angleRightElbowLower = 30
    angleRightElbowUpper = 190

    def check(osoba):
        x = 0
        if(osoba.desniKuk.visibility > 0.5 and osoba.desnoRame.visibility > 0.5 and osoba.desniLakat.visibility > 0.5 and osoba.desnaSaka.visibility > 0.5 and osoba.desnoStopalo.visibility > 0.5 or osoba.leviKuk.visibility > 0.5 and osoba.levoRame.visibility > 0.5 and osoba.leviLakat.visibility > 0.5 and osoba.levaSaka.visibility > 0.5 and osoba.levoStopalo.visibility > 0.5 ):
            x = 1
        else:
            x = 2
        
        return x
    
class SquatConfig:
    angleLeftKneeUpper = 85
    angleRightKneeUpper = 85
    

    def check(osoba):
        x = 0
        if(osoba.desniKuk.visibility > 0.5 and osoba.desnoStopalo.visibility > 0.5 and osoba.desnoKoleno.visibility > 0.5 or osoba.leviKuk.visibility > 0.5 and  osoba.levoStopalo.visibility > 0.5 and osoba.levoKoleno.visibility > 0.5 ):
            x = 1
        else:
            x = 2
        
        return x
    
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
    
class FlyConfig:
    angleLeftShoulderLower = 80
    angleLeftShoulderUpper = 100
    
    angleRightShoulderLower = 80
    angleRightShoulderUpper = 100

    angleRightElbowLower = 100
    angleRightElbowLower = 150

    angleLeftElbowLower = 100
    angleLeftElbowUpper = 150

    def check(osoba):
        x = 0
        if(osoba.desniKuk.visibility > 0.5 and osoba.desnoRame.visibility > 0.5 and osoba.desniLakat.visibility > 0.5 and osoba.desnaSaka.visibility > 0.5 or osoba.leviKuk.visibility > 0.5 and osoba.levoRame.visibility > 0.5 and osoba.leviLakat.visibility > 0.5 and osoba.levaSaka.visibility > 0.5):
            x = 1
        else:
            x = 2
        
        return x

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