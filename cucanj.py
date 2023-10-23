import cv2
from osoba import *
from yolo import *
proba1=65

def izracunajCucanj(cap):
    proba2=100
    while True:
        ret, frame = cap.read()  # Čitanje frejma sa kamere
        if not ret:
            break

        osoba = ocitajOsobu(frame) # Čitanje osobe sa frejma

        cv2.line(frame, (int(osoba.levoKoleno.x),int(osoba.levoKoleno.y)), (int(osoba.levoStopalo.x),int(osoba.levoStopalo.y)), (0,0,0), 3)
        cv2.line(frame, (int(osoba.levoKoleno.x),int(osoba.levoKoleno.y)), (int(osoba.leviKuk.x),int(osoba.leviKuk.y)), (0,0,0), 3)
        cv2.circle(frame, (int(osoba.levoKoleno.x),int(osoba.levoKoleno.y)), radius=5, color=(255, 0, 0), thickness=5)
        cv2.circle(frame, (int(osoba.levoStopalo.x),int(osoba.levoStopalo.y)), radius=5, color=(255, 0, 0), thickness=5)
        cv2.circle(frame, (int(osoba.leviKuk.x),int(osoba.leviKuk.y)), radius=5, color=(255, 0, 0), thickness=5)
        
        cv2.line(frame, (int(osoba.desnoKoleno.x),int(osoba.desnoKoleno.y)), (int(osoba.desnoStopalo.x),int(osoba.desnoStopalo.y)), (0,0,0), 3)
        cv2.line(frame, (int(osoba.desnoKoleno.x),int(osoba.desnoKoleno.y)), (int(osoba.desniKuk.x),int(osoba.desniKuk.y)), (0,0,0), 3)
        cv2.circle(frame, (int(osoba.desnoKoleno.x),int(osoba.desnoKoleno.y)), radius=5, color=(255, 0, 0), thickness=5)
        cv2.circle(frame, (int(osoba.desnoStopalo.x),int(osoba.desnoStopalo.y)), radius=5, color=(255, 0, 0), thickness=5)
        cv2.circle(frame, (int(osoba.desniKuk.x),int(osoba.desniKuk.y)), radius=5, color=(255, 0, 0), thickness=5)

        r=0
        g=0
        ugaoLevoKoleno = int(osoba.izracunajUgao(osoba.levoStopalo,osoba.levoKoleno,osoba.leviKuk))
        if(ugaoLevoKoleno > 85): 
            g=255 
        else: 
            r=255
        cv2.putText(frame,
                    text = str(ugaoLevoKoleno),
                    org = (int(osoba.levoKoleno.x)+20, int(osoba.levoKoleno.y)+20),
                    fontFace = cv2.FONT_HERSHEY_DUPLEX,
                    fontScale = 1.0,
                    color = (0, g, r),
                    thickness = 3)
        
        r=0
        g=0
        ugaoDesnoKoleno = int(osoba.izracunajUgao(osoba.desnoStopalo,osoba.desnoKoleno,osoba.desniKuk))
        if(ugaoDesnoKoleno > 85): 
            g=255 
        else: 
            r=255
        cv2.putText(frame,
                    text = str(ugaoDesnoKoleno),
                    org = (int(osoba.desnoKoleno.x)-100, int(osoba.desnoKoleno.y)+20),
                    fontFace = cv2.FONT_HERSHEY_DUPLEX,
                    fontScale = 1.0,
                    color = (0, g, r),
                    thickness = 3)
        
        cv2.imshow('VTSAssistant',frame)
        
        if cv2.waitKey(1) & 0xFF == 27:  # Esc taster za prekid petlje
            break
    cv2.destroyAllWindows()
    