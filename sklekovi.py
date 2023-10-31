import cv2
from osoba import *
from yolo import *
import math


def pushups_draw_yolo(frame):
    

        osoba = ocitajOsobu(frame) # Čitanje osobe sa frejma
        if(True):

            cv2.line(frame, (int(osoba.levoStopalo.x),int(osoba.levoStopalo.y)), (int(osoba.levoKoleno.x),int(osoba.levoKoleno.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.levoKoleno.x),int(osoba.levoKoleno.x)), (int(osoba.leviKuk.x),int(osoba.leviKuk.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.leviKuk.x),int(osoba.leviKuk.x)), (int(osoba.levoRame.x),int(osoba.levoRame.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.levoRame.x),int(osoba.levoRame.y)), (int(osoba.leviLakat.x),int(osoba.leviLakat.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.levaSaka.x),int(osoba.levaSaka.y)), (int(osoba.leviLakat.x),int(osoba.leviLakat.y)), (0,0,0), 3)
            
            cv2.line(frame, (int(osoba.desnoStopalo.x),int(osoba.desnoStopalo.y)), (int(osoba.desnoKoleno.x),int(osoba.desnoKoleno.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.desnoKoleno.x),int(osoba.desnoKoleno.x)), (int(osoba.desniKuk.x),int(osoba.desniKuk.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.desniKuk.x),int(osoba.desniKuk.x)), (int(osoba.desnoRame.x),int(osoba.desnoRame.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.desnoRame.x),int(osoba.desnoRame.y)), (int(osoba.desniLakat.x),int(osoba.desniLakat.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.desnaSaka.x),int(osoba.desnaSaka.y)), (int(osoba.desniLakat.x),int(osoba.desniLakat.y)), (0,0,0), 3)
            
            cv2.circle(frame, (int(osoba.levaSaka.x),int(osoba.levaSaka.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.desnaSaka.x),int(osoba.desnaSaka.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.levoRame.x),int(osoba.levoRame.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.desnoRame.x),int(osoba.desnoRame.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.leviKuk.x),int(osoba.leviKuk.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.desniKuk.x),int(osoba.desniKuk.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.levoKoleno.x),int(osoba.levoKoleno.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.desnoKoleno.x),int(osoba.desnoKoleno.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.levoStopalo.x),int(osoba.levoStopalo.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.desnoStopalo.x),int(osoba.desnoStopalo.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.leviLakat.x),int(osoba.leviLakat.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.desniLakat.x),int(osoba.desniLakat.y)), radius=5, color=(255, 0, 0), thickness=5)

            
             
         
            r=0
            g=0
            ugaoLeviRuka = int(osoba.izracunajUgao(osoba.levaSaka,osoba.leviLakat,osoba.levoRame))
            if(ugaoLeviRuka > 185 and ugaoLeviRuka < 85): 
                g=255 
            else: 
                r=255
            cv2.putText(frame,
                        text = str(ugaoLeviRuka),
                        org = (int(osoba.levoRame.x)+20, int(osoba.levoRame.y)+20),
                        fontFace = cv2.FONT_HERSHEY_DUPLEX,
                        fontScale = 1.0,
                        color = (0, g, r),
                        thickness = 3)
            
            r=0
            g=0
            ugaoDesniRuka = int(osoba.izracunajUgao(osoba.desnaSaka,osoba.desniLakat,osoba.desnoRame))
            if(ugaoDesniRuka > 185 and ugaoDesniRuka < 85): 
                g=255 
            else: 
                r=255
            cv2.putText(frame,
                        text = str(ugaoDesniRuka),
                        org = (int(osoba.desnoRame.x)-100, int(osoba.desnoRame.y)+20),
                        fontFace = cv2.FONT_HERSHEY_DUPLEX,
                        fontScale = 1.0,
                        color = (0, g, r),
                        thickness = 3)
            r=0
            g=0
            ugaoTeloLevo = int(osoba.izracunajUgao(osoba.levoRame,osoba.leviKuk,osoba.levoKoleno))
            if(ugaoTeloLevo > 175 and ugaoTeloLevo < 185): 
                g=255 
            else: 
                r=255
            cv2.putText(frame,
                        text = str(ugaoTeloLevo),
                        org = (int(osoba.leviKuk.x)-100, int(osoba.leviKuk.y)+20),
                        fontFace = cv2.FONT_HERSHEY_DUPLEX,
                        fontScale = 1.0,
                        color = (0, g, r),
                        thickness = 3)
            r=0
            g=0
            ugaoTeloDesno = int(osoba.izracunajUgao(osoba.desnoRame,osoba.desniKuk,osoba.desnoKoleno))
            if(ugaoTeloLevo > 175 and ugaoTeloDesno < 185): 
                g=255 
            else: 
                r=255
            cv2.putText(frame,
                        text = str(ugaoTeloDesno),
                        org = (int(osoba.desniKuk.x)-100, int(osoba.desniKuk.y)+20),
                        fontFace = cv2.FONT_HERSHEY_DUPLEX,
                        fontScale = 1.0,
                        color = (0, g, r),
                        thickness = 3)
        else:
            cv2.putText(frame,
                        text = str("budite sigurni da ste lepo zauzeli polozaj"),
                        org = (0,200),
                        fontFace = cv2.FONT_HERSHEY_DUPLEX,
                        fontScale = 1.0,
                        color = (0, 0, 255),
                        thickness = 3)
        return frame
    