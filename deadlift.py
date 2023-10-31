import cv2
from osoba import *
import yolo
import math
import numpy as np 
from PIL import Image as im

def deadLift_draw_yolo(frame):
    
    osoba = yolo.ocitajOsobu(frame) # Čitanje osobe sa frejma

    if(osoba.levoKoleno.visibility > 0.5 and osoba.desnoKoleno.visibility > 0.5):

            cv2.line(frame, (int(osoba.levoStopalo.x),int(osoba.levoStopalo.y)), (int(osoba.levoKoleno.x),int(osoba.levoKoleno.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.levoKoleno.x),int(osoba.levoKoleno.y)), (int(osoba.leviKuk.x),int(osoba.leviKuk.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.leviKuk.x),int(osoba.leviKuk.y)), (int(osoba.levoRame.x),int(osoba.levoRame.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.levoRame.x),int(osoba.levoRame.y)), (int(osoba.leviLakat.x),int(osoba.leviLakat.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.leviLakat.x),int(osoba.leviLakat.y)), (int(osoba.levaSaka.x),int(osoba.levaSaka.y)), (0,0,0), 3)
            
            #cv2.line(frame, (int(osoba.desnoStopalo.x),int(osoba.desnoStopalo.y)), (int(osoba.desnoKoleno.x),int(osoba.desnoKoleno.y)), (0,0,0), 3)
            #cv2.line(frame, (int(osoba.desnoKoleno.x),int(osoba.desnoKoleno.y)), (int(osoba.desniKuk.x),int(osoba.desniKuk.y)), (0,0,0), 3)
            #cv2.line(frame, (int(osoba.desniKuk.x),int(osoba.desniKuk.y)), (int(osoba.desnoRame.x),int(osoba.desnoRame.y)), (0,0,0), 3)
            #cv2.line(frame, (int(osoba.desnoRame.x),int(osoba.desnoRame.y)), (int(osoba.desniLakat.x),int(osoba.desniLakat.y)), (0,0,0), 3)
            #cv2.line(frame, (int(osoba.desniLakat.x),int(osoba.desniLakat.y)), (int(osoba.desnaSaka.x),int(osoba.desnaSaka.y)), (0,0,0), 3)
           
            #cv2.circle(frame, (int(osoba.desnoKoleno.x),int(osoba.desnoKoleno.y)), radius=5, color=(255, 0, 0), thickness=5)
            #cv2.circle(frame, (int(osoba.desnoStopalo.x),int(osoba.desnoStopalo.y)), radius=5, color=(255, 0, 0), thickness=5)
            #cv2.circle(frame, (int(osoba.desniKuk.x),int(osoba.desniKuk.y)), radius=5, color=(255, 0, 0), thickness=5)
            #cv2.circle(frame, (int(osoba.desnoRame.x),int(osoba.desnoRame.y)), radius=5, color=(255, 0, 0), thickness=5)
            #cv2.circle(frame, (int(osoba.desniLakat.x),int(osoba.desniLakat.y)), radius=5, color=(255, 0, 0), thickness=5)
            #cv2.circle(frame, (int(osoba.desnaSaka.x),int(osoba.desnaSaka.y)), radius=5, color=(255, 0, 0), thickness=5)
            
            cv2.circle(frame, (int(osoba.levoKoleno.x),int(osoba.levoKoleno.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.levoStopalo.x),int(osoba.levoStopalo.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.leviKuk.x),int(osoba.leviKuk.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.levoRame.x),int(osoba.levoRame.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.leviLakat.x),int(osoba.leviLakat.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.levaSaka.x),int(osoba.levaSaka.y)), radius=5, color=(255, 0, 0), thickness=5)


            ##da se dodaju ifovi za ovu vezbu i iscrtavanje uglova
          
    else:
        cv2.putText(frame,
            text = str("budite sigurni da ste lepo zauzeli polozaj"),
            org = (0,0),
            fontFace = cv2.FONT_HERSHEY_DUPLEX,
            fontScale = 1.0,
            color = (0, 0, 255),
            thickness = 3)
    
    return frame #vraca nacrtani fejm
