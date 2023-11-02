import cv2
from osoba import *
import yolo
import math
import numpy as np 
from PIL import Image as im

class ColorPalette:
    c1 = '#020f12'
    c2 = '#05d7ff'
    c3 = '#65e7ff'
    c4 = 'BLACK'
    c5 = 'WHITE'

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