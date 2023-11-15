import cv2
from yolo_processing.osoba import *
from yolo_processing.yolo import ocitajOsobu
from yolo_processing.config import *

#prba

def biceps_draw_yolo(frame):
        
        osoba = ocitajOsobu(frame) # Čitanje osobe sa frejma
        pro = BicepsConfig.check(osoba)
        if(pro == 1):

            cv2.line(frame, (int(osoba.desnaSaka.x),int(osoba.desnaSaka.y)), (int(osoba.desniLakat.x),int(osoba.desniLakat.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.desniLakat.x),int(osoba.desniLakat.y)), (int(osoba.desnoRame.x),int(osoba.desnoRame.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.desnoRame.x),int(osoba.desnoRame.y)), (int(osoba.desniKuk.x),int(osoba.desniKuk.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.desniKuk.x),int(osoba.desniKuk.y)), (int(osoba.desnoStopalo.x),int(osoba.desnoStopalo.y)), (0,0,0), 3)
        
            cv2.circle(frame, (int(osoba.desniKuk.x),int(osoba.desniKuk.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.desnoRame.x),int(osoba.desnoRame.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.desniLakat.x),int(osoba.desniLakat.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.desnaSaka.x),int(osoba.desnaSaka.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.desnoStopalo.x),int(osoba.desnoStopalo.y)), radius=5, color=(255, 0, 0), thickness=5)
            
            cv2.line(frame, (int(osoba.levaSaka.x),int(osoba.levaSaka.y)), (int(osoba.leviLakat.x),int(osoba.leviLakat.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.leviLakat.x),int(osoba.leviLakat.y)), (int(osoba.levoRame.x),int(osoba.levoRame.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.levoRame.x),int(osoba.levoRame.y)), (int(osoba.leviKuk.x),int(osoba.leviKuk.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.leviKuk.x),int(osoba.leviKuk.y)), (int(osoba.levoStopalo.x),int(osoba.levoStopalo.y)), (0,0,0), 3)
        
            cv2.circle(frame, (int(osoba.leviKuk.x),int(osoba.leviKuk.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.levoRame.x),int(osoba.levoRame.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.leviLakat.x),int(osoba.leviLakat.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.levaSaka.x),int(osoba.levaSaka.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.levoStopalo.x),int(osoba.levoStopalo.y)), radius=5, color=(255, 0, 0), thickness=5)
            
            r=0
            g=0
            ugaoLevoRame = int(osoba.izracunajUgao(osoba.leviKuk,osoba.levoRame,osoba.leviLakat))
            if(ugaoLevoRame > BicepsConfig.angleLeftShoulderLower and ugaoLevoRame < BicepsConfig.angleLeftShoulderUpper): 
                g=255 
            else: 
                r=255
            cv2.putText(frame,
                        text = str(ugaoLevoRame),
                        org = (int(osoba.levoRame.x)+20, int(osoba.levoRame.y)+20),
                        fontFace = cv2.FONT_HERSHEY_DUPLEX,
                        fontScale = 1.0,
                        color = (0, g, r),
                        thickness = 3)
            
            r=0
            g=0
            ugaoDesnoRame = int(osoba.izracunajUgao(osoba.desniKuk,osoba.desnoRame,osoba.desniLakat))
            if(ugaoDesnoRame > BicepsConfig.angleRightSoulderLower and ugaoDesnoRame < BicepsConfig.angleRightSoulderUpper): 
                g=255 
            else: 
                r=255
            cv2.putText(frame,
                        text = str(ugaoDesnoRame),
                        org = (int(osoba.desnoRame.x)-100, int(osoba.desnoRame.y)+20),
                        fontFace = cv2.FONT_HERSHEY_DUPLEX,
                        fontScale = 1.0,
                        color = (0, g, r),
                        thickness = 3)
            
            ugaoLeviLakat = int(osoba.izracunajUgao(osoba.levoRame,osoba.leviLakat,osoba.levaSaka))
            if(ugaoLeviLakat > BicepsConfig.angleLeftElbowLower and ugaoLeviLakat < BicepsConfig.angleLeftElbowUpper): 
                g=255 
            else: 
                r=255
            cv2.putText(frame,
                        text = str(ugaoLeviLakat),
                        org = (int(osoba.leviLakat.x)+20, int(osoba.leviLakat.y)+20),
                        fontFace = cv2.FONT_HERSHEY_DUPLEX,
                        fontScale = 1.0,
                        color = (0, g, r),
                        thickness = 3)
            
            r=0
            g=0

            ugaoDesniLakat = int(osoba.izracunajUgao(osoba.desnoRame,osoba.desniLakat,osoba.desnaSaka))
            if(ugaoDesniLakat > BicepsConfig.angleRightElbowLower and ugaoDesniLakat < BicepsConfig.angleRightElbowUpper): 
                g=255 
            else: 
                r=255
            cv2.putText(frame,
                        text = str(ugaoDesniLakat),
                        org = (int(osoba.desniLakat.x)-100, int(osoba.desniLakat.y)+20),
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
        if(pro == 2):
            errorMessage = 'neke tacke nisu vidljive na yolu, popravite polozaj'

        return frame

def squat_draw_yolo(frame):
    
    osoba = ocitajOsobu(frame) # Čitanje osobe sa frejma
    pro = SquatConfig.check(osoba)
    if(pro == 1):

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
            if(ugaoLevoKoleno > SquatConfig.angleLeftKneeUpper): 
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
            if(ugaoDesnoKoleno > SquatConfig.angleRightKneeUpper): 
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
    else:
        cv2.putText(frame,
            text = str("budite sigurni da ste lepo zauzeli polozaj"),
            org = (0,0),
            fontFace = cv2.FONT_HERSHEY_DUPLEX,
            fontScale = 1.0,
            color = (0, 0, 255),
            thickness = 3)
    
    if(pro == 2):
            errorMessage = 'neke tacke nisu vidljive na yolu, popravite polozaj'

    return frame

def deadLift_draw_yolo(frame):
    
    osoba = ocitajOsobu(frame) # Čitanje osobe sa frejma
    pro = DeadLiftConfig.check(osoba)
    if(pro == 1):

            cv2.line(frame, (int(osoba.levoStopalo.x),int(osoba.levoStopalo.y)), (int(osoba.levoKoleno.x),int(osoba.levoKoleno.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.levoKoleno.x),int(osoba.levoKoleno.y)), (int(osoba.leviKuk.x),int(osoba.leviKuk.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.leviKuk.x),int(osoba.leviKuk.y)), (int(osoba.levoRame.x),int(osoba.levoRame.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.levoRame.x),int(osoba.levoRame.y)), (int(osoba.leviLakat.x),int(osoba.leviLakat.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.leviLakat.x),int(osoba.leviLakat.y)), (int(osoba.levaSaka.x),int(osoba.levaSaka.y)), (0,0,0), 3)
            
            cv2.line(frame, (int(osoba.desnoStopalo.x),int(osoba.desnoStopalo.y)), (int(osoba.desnoKoleno.x),int(osoba.desnoKoleno.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.desnoKoleno.x),int(osoba.desnoKoleno.y)), (int(osoba.desniKuk.x),int(osoba.desniKuk.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.desniKuk.x),int(osoba.desniKuk.y)), (int(osoba.desnoRame.x),int(osoba.desnoRame.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.desnoRame.x),int(osoba.desnoRame.y)), (int(osoba.desniLakat.x),int(osoba.desniLakat.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.desniLakat.x),int(osoba.desniLakat.y)), (int(osoba.desnaSaka.x),int(osoba.desnaSaka.y)), (0,0,0), 3)
           
            cv2.circle(frame, (int(osoba.desnoKoleno.x),int(osoba.desnoKoleno.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.desnoStopalo.x),int(osoba.desnoStopalo.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.desniKuk.x),int(osoba.desniKuk.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.desnoRame.x),int(osoba.desnoRame.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.desniLakat.x),int(osoba.desniLakat.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.desnaSaka.x),int(osoba.desnaSaka.y)), radius=5, color=(255, 0, 0), thickness=5)
            
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

def knees_draw_yolo(frame):
    
        osoba = ocitajOsobu(frame) # Čitanje osobe sa frejma
        pro = KneesConfig.check(osoba)
        if(pro == 1):

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
            ugaoLevaStranaKuk = int(osoba.izracunajUgao(osoba.levoRame,osoba.leviKuk,osoba.levoKoleno))
            if(ugaoLevaStranaKuk > 85 and ugaoLevaStranaKuk < 185): 
                g=255 
            else: 
                r=255
            cv2.putText(frame,
                        text = str(ugaoLevaStranaKuk),
                        org = (int(osoba.levoRame.x)+20, int(osoba.levoRame.y)+20),
                        fontFace = cv2.FONT_HERSHEY_DUPLEX,
                        fontScale = 1.0,
                        color = (0, g, r),
                        thickness = 3)
            
            r=0
            g=0
            ugaoDesnaStranaKuk = int(osoba.izracunajUgao(osoba.desnoRame,osoba.desniKuk,osoba.desnoKoleno))
            if(ugaoDesnaStranaKuk > 85 and ugaoDesnaStranaKuk < 185): 
                g=255 
            else: 
                r=255
            cv2.putText(frame,
                        text = str(ugaoDesnaStranaKuk),
                        org = (int(osoba.desnoRame.x)-100, int(osoba.desnoRame.y)+20),
                        fontFace = cv2.FONT_HERSHEY_DUPLEX,
                        fontScale = 1.0,
                        color = (0, g, r),
                        thickness = 3)
            r=0
            g=0
            ugaoDesnaStranaKoleno = int(osoba.izracunajUgao(osoba.desniKuk,osoba.desnoKoleno,osoba.desnoStopalo))
            if(ugaoDesnaStranaKoleno > 80 and ugaoDesnaStranaKoleno < 100): 
                g=255 
            else: 
                r=255
            cv2.putText(frame,
                        text = str(ugaoDesnaStranaKoleno),
                        org = (int(osoba.desnoKoleno.x)-100, int(osoba.desnoKoleno.y)+20),
                        fontFace = cv2.FONT_HERSHEY_DUPLEX,
                        fontScale = 1.0,
                        color = (0, g, r),
                        thickness = 3)
            r=0
            g=0
            ugaoLevaStranaKoleno = int(osoba.izracunajUgao(osoba.leviKuk,osoba.levoKoleno,osoba.levoStopalo))
            if(ugaoLevaStranaKoleno > 80 and ugaoLevaStranaKoleno < 100): 
                g=255 
            else: 
                r=255
            cv2.putText(frame,
                        text = str(ugaoLevaStranaKoleno),
                        org = (int(osoba.levoKoleno.x)-100, int(osoba.levoKoleno.y)+20),
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
        if(pro == 2):
            errorMessage = 'neke tacke nisu vidljive na yolu, popravite polozaj'

        return frame

def fly_draw_yolo(frame):
    
        
            
        osoba = ocitajOsobu(frame) # Čitanje osobe sa frejma
        pro = FlyConfig.check(osoba)

        if(pro == 1):

            cv2.line(frame, (int(osoba.desniKuk.x),int(osoba.desniKuk.y)), (int(osoba.desnoRame.x),int(osoba.desnoRame.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.desnoRame.x),int(osoba.desnoRame.y)), (int(osoba.desniLakat.x),int(osoba.desniLakat.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.desniLakat.x),int(osoba.desniLakat.y)), (int(osoba.desnaSaka.x),int(osoba.desnaSaka.y)), (0,0,0), 3)
        
            cv2.circle(frame, (int(osoba.desniKuk.x),int(osoba.desniKuk.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.desnoRame.x),int(osoba.desnoRame.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.desniLakat.x),int(osoba.desniLakat.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.desnaSaka.x),int(osoba.desnaSaka.y)), radius=5, color=(255, 0, 0), thickness=5)
        
            cv2.line(frame, (int(osoba.leviKuk.x),int(osoba.leviKuk.y)), (int(osoba.levoRame.x),int(osoba.levoRame.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.levoRame.x),int(osoba.levoRame.y)), (int(osoba.leviLakat.x),int(osoba.leviLakat.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.leviLakat.x),int(osoba.leviLakat.y)), (int(osoba.levaSaka.x),int(osoba.levaSaka.y)), (0,0,0), 3)
        
            cv2.circle(frame, (int(osoba.leviKuk.x),int(osoba.leviKuk.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.desnoRame.x),int(osoba.levoRame.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.leviLakat.x),int(osoba.leviLakat.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.levaSaka.x),int(osoba.levaSaka.y)), radius=5, color=(255, 0, 0), thickness=5)
        
            r=0
            g=0
            ugaoLevoRame = int(osoba.izracunajUgao(osoba.leviKuk,osoba.levoRame,osoba.leviLakat))
            if(ugaoLevoRame > FlyConfig.angleLeftShoulderLower and ugaoLevoRame < FlyConfig.angleRightShoulderUpper): 
                g=255 
            else: 
                r=255
            cv2.putText(frame,
                        text = str(ugaoLevoRame),
                        org = (int(osoba.levoRame.x)+20, int(osoba.levoRame.y)+20),
                        fontFace = cv2.FONT_HERSHEY_DUPLEX,
                        fontScale = 1.0,
                        color = (0, g, r),
                        thickness = 3)
            
            r=0
            g=0
            ugaoDesnoRame = int(osoba.izracunajUgao(osoba.desniKuk,osoba.desnoRame,osoba.desniLakat))
            if(ugaoDesnoRame > FlyConfig.angleRightShoulderLower and ugaoDesnoRame < FlyConfig.angleRightShoulderUpper): 
                g=255 
            else: 
                r=255
            cv2.putText(frame,
                        text = str(ugaoDesnoRame),
                        org = (int(osoba.desnoRame.x)-100, int(osoba.desnoRame.y)+20),
                        fontFace = cv2.FONT_HERSHEY_DUPLEX,
                        fontScale = 1.0,
                        color = (0, g, r),
                        thickness = 3)
            
            ugaoLeviLakat = int(osoba.izracunajUgao(osoba.levoRame,osoba.leviLakat,osoba.levaSaka))
            if(ugaoLeviLakat > FlyConfig.angleLeftElbowLower and ugaoLeviLakat < FlyConfig.angleLeftElbowUpper): 
                g=255 
            else: 
                r=255
            cv2.putText(frame,
                        text = str(ugaoLeviLakat),
                        org = (int(osoba.leviLakat.x)+20, int(osoba.leviLakat.y)+20),
                        fontFace = cv2.FONT_HERSHEY_DUPLEX,
                        fontScale = 1.0,
                        color = (0, g, r),
                        thickness = 3)
            
            r=0
            g=0

            ugaoDesniLakat = int(osoba.izracunajUgao(osoba.desnoRame,osoba.desniLakat,osoba.desnaSaka))
            if(ugaoDesniLakat > FlyConfig.angleRightElbowLower  and ugaoDesniLakat < FlyConfig.angleLeftElbowUpper): 
                g=255 
            else: 
                r=255
            cv2.putText(frame,
                        text = str(ugaoDesniLakat),
                        org = (int(osoba.desniLakat.x)-100, int(osoba.desniLakat.y)+20),
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
        if(pro == 2):
            errorMessage = 'neke tacke nisu vidljive na yolu, popravite polozaj'

        return frame
    
def pushups_draw_yolo(frame):
    

        osoba = ocitajOsobu(frame) # Čitanje osobe sa frejma
        pro = PushUpsConfig.check(osoba)
        if(pro == 1):

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
            if(ugaoLeviRuka > PushUpsConfig.angleLeftElbowLower and ugaoLeviRuka <  PushUpsConfig.angleLeftElbowUpper): 
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
            if(ugaoDesniRuka >  PushUpsConfig.angleRightElbowLower and ugaoDesniRuka < PushUpsConfig.angleRightElbowUpper): 
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
            if(ugaoTeloLevo > PushUpsConfig.angleLeftBodyLower and ugaoTeloLevo < PushUpsConfig.angleLeftBodyUpper): 
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
            if(ugaoTeloLevo > PushUpsConfig.angleRightBodyLower and ugaoTeloDesno < PushUpsConfig.angleRightBodyUpper): 
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
        if(pro == 2):
            errorMessage = 'neke tacke nisu vidljive na yolu, popravite polozaj'

        
        return frame

def abs_draw_yolo(frame):
   
   

        osoba = ocitajOsobu(frame) # Čitanje osobe sa frejma
        pro = AbsConfig.check(osoba)
        if(pro == 1):

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
            if(ugaoLevaStrana > 100 and ugaoLevaStrana < 150): 
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
            if(ugaoDesnaStrana > 100 and ugaoDesnaStrana < 150): 
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
    
exerciseList = [squat_draw_yolo, biceps_draw_yolo, pushups_draw_yolo, abs_draw_yolo, deadLift_draw_yolo, fly_draw_yolo, knees_draw_yolo ]

#0 squat
#1 biceps
#2 pushups
#3 abs
#4 deadlift
#5 fly
#6 knees

def run_yolo(frame, exercise):

    processed_frame = exerciseList[exercise](frame)

    height, width, channels = processed_frame.shape
    if(width>height):
        desired_width = 750
        desired_height = 420
    else:
        desired_width = 420
        desired_height = 750
        
    new_image = cv2.resize(processed_frame, (desired_width, desired_height))
    new_image = im.fromarray(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
    new_image.save('assets/temporary_images/display_frame.png')