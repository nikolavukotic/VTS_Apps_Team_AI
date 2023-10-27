import cv2
from osoba import *
from yolo import *


def abs_draw_yolo(frame):
   

        osoba = ocitajOsobu(frame) # Čitanje osobe sa frejma
        if(True):

            cv2.line(frame, (int(osoba.desnoRame.x),int(osoba.desnoRame.y)), (int(osoba.desniKuk.x),int(osoba.desniKuk.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.desniKuk.x),int(osoba.desniKuk.y)), (int(osoba.desnoKoleno.x),int(osoba.desnoKoleno.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.desnoKoleno.x),int(osoba.desnoKoleno.y)), (int(osoba.desnoStopalo.x),int(osoba.desnoStopalo.y)), (0,0,0), 3)
            
            cv2.circle(frame, (int(osoba.desniKuk.x),int(osoba.desniKuk.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.desnoRame.x),int(osoba.desnoRame.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.desnoKoleno.x),int(osoba.desnoKoleno.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.desnoStopalo.x),int(osoba.desnoStopalo.y)), radius=5, color=(255, 0, 0), thickness=5)
              
            cv2.line(frame, (int(osoba.levoRame.x),int(osoba.levoRame.y)), (int(osoba.leviKuk.x),int(osoba.leviKuk.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.leviKuk.x),int(osoba.leviKuk.y)), (int(osoba.levoKoleno.x),int(osoba.levoKoleno.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.levoKoleno.x),int(osoba.levoKoleno.y)), (int(osoba.levoStopalo.x),int(osoba.levoStopalo.y)), (0,0,0), 3)
            
            cv2.circle(frame, (int(osoba.leviKuk.x),int(osoba.leviKuk.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.levoRame.x),int(osoba.levoRame.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.levoKoleno.x),int(osoba.levoKoleno.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.levoStopalo.x),int(osoba.levoStopalo.y)), radius=5, color=(255, 0, 0), thickness=5)
            
            r=0
            g=0
            ugaoLevaStrana = int(osoba.izracunajUgao(osoba.levoStopalo,osoba.leviKuk,osoba.levoRame))
            if(ugaoLevaStrana > 170 and ugaoLevaStrana < 90): 
                g=255 
            else: 
                r=255
            cv2.putText(frame,
                        text = str(ugaoLevaStrana),
                        org = (int(osoba.levoRame.x)+20, int(osoba.levoRame.y)+20),
                        fontFace = cv2.FONT_HERSHEY_DUPLEX,
                        fontScale = 1.0,
                        color = (0, g, r),
                        thickness = 3)
            
            r=0
            g=0
            ugaoDesnaStrana = int(osoba.izracunajUgao(osoba.desnoStopalo,osoba.desniKuk,osoba.desnoRame))
            if(ugaoDesnaStrana > 180 and ugaoDesnaStrana < 90): 
                g=255 
            else: 
                r=255
            cv2.putText(frame,
                        text = str(ugaoDesnaStrana),
                        org = (int(osoba.desnoRame.x)-100, int(osoba.desnoRame.y)+20),
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
    