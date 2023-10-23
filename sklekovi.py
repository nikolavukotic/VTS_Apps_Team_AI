import cv2
from osoba import *
from yolo import *
import math


def izracunajSklekovi(cap):
    while True:
        ret, frame = cap.read()  # Čitanje frejma sa kamere
        if not ret:
            break

        osoba = ocitajOsobu(frame) # Čitanje osobe sa frejma
        if(True):

            sredinaRameX = (osoba.desnoRame.x+osoba.levoRame.x)/2
            sredinaRameY = osoba.desnoRame.y
            sredinaKukX = (osoba.desniKuk.x+osoba.levoKuk.x)/2
            sredinaKukY = osoba.desniKuk.y
            sredinaKolenoX = (osoba.desnoKoleno.x+osoba.levoKoleno.x)/2
            sredinaKolenoY = osoba.desnoKoleno.y
            sredinaStopaloX = (osoba.levoStopalo.x+osoba.desnoStopalo.x)/2
            sredinaStopaloY = osoba.desnoStopalo.y

            cv2.line(frame, (int(osoba.nos.x),int(osoba.nos.y)), (int(sredinaRameX),int(sredinaRameY)), (0,0,0), 3)
            cv2.line(frame, (int(sredinaRameX),int(sredinaRameY)), (int(sredinaKukX),int(sredinaKukY)), (0,0,0), 3)
            cv2.line(frame, (int(sredinaKukX),int(sredinaKukY)), (int(sredinaKolenoX),int(sredinaKolenoY)), (0,0,0), 3)
            cv2.line(frame, (int(sredinaKolenoX),int(sredinaKolenoY)), (int(sredinaStopaloX),int(sredinaStopaloY)), (0,0,0), 3)
            
            cv2.line(frame, (int(osoba.levoRame.x),int(osoba.levoRame.y)), (int(osoba.desnoRame.x),int(osoba.desnoRame.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.leviKuk.x),int(osoba.leviKuk.y)), (int(osoba.desniKuk.x),int(osoba.desniKuk.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.desnoKoleno.x),int(osoba.desnoKoleno.y)), (int(osoba.desnoKoleno.x),int(osoba.desnoKoleno.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.desnoStopalo.x),int(osoba.desnoStopalo.y)), (int(osoba.levoStopalo.x),int(osoba.levoStopalo.y)), (0,0,0), 3)
           
            cv2.circle(frame, (int(osoba.nos.x),int(osoba.nos.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(sredinaRameX),int(sredinaRameY)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(sredinaKukX),int(sredinaKukY)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(sredinaKolenoX),int(sredinaKolenoY)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(sredinaStopaloX),int(sredinaStopaloY)), radius=5, color=(255, 0, 0), thickness=5)
             
         
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
        cv2.imshow('VTSAssistant',frame)
        
        if cv2.waitKey(1) & 0xFF == 27:  # Esc taster za prekid petlje
            break
    cv2.destroyAllWindows()
    