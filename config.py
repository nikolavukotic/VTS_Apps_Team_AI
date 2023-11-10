import cv2
from osoba import *
import math
import numpy as np 
from PIL import Image as im
from yolo import *

#GUI CONFIG
class Colors:
    background = "#1c1c22"
    object = "#2a2a34"
    accent = "#0e74bb"
    text = "WHITE"

class Spacer:
    source = 100
    source_buttons = 0
    exercise = 40
    display = 20

class Text:
    font = "Arial"
    size = 25
    format = "bold"
    text = [font, size, format]

class Padding:
    source = 0
    source_buttons = 0
    exercise = 10
    display = 0

class Styles:
    source_button = {
        "font": Text.text,
        "background": Colors.object,
        "foreground": Colors.text,
        "activebackground": Colors.object,
        "activeforeground": Colors.accent,
        "highlightthickness": 2,
        "highlightbackground": Colors.accent,
        "highlightcolor": "WHITE",
        "width": 23,
        "height": 2,
        "border": 0,
    }
    button_frame = {
        "highlightbackground": Colors.accent,
        "highlightthickness": 5,
        "background": Colors.accent,
        "border": 0,
    }
    optionmenu = {
        "font": Text.text,
        "background": Colors.object,
        "foreground": Colors.text,
        "activebackground": Colors.object,
        "activeforeground": Colors.accent,
        "highlightthickness": 5,
        "highlightbackground": Colors.accent,
        "highlightcolor": "WHITE",
        "width": 24,
        "border": 0,
    }



#EXSERCISE CONFIG



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