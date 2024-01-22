import cv2
from yolo_processing.osoba import *
from yolo_processing.yolo import ocitajOsobu
from yolo_processing.config import *

message = ""
erHandler = 0



def biceps_draw_yolo(frame):
        global message
        global erHandler
        osoba = ocitajOsobu(frame) # Čitanje osobe sa frejma
        pro = BicepsConfig.check(osoba)
        if(pro == 3):
            both = True
        else:
            both = False
        
        if(pro == 1 or both):
            message = "nastavite..."
            erHandler = 0
            
            cv2.line(frame, (int(osoba.desnaSaka.x),int(osoba.desnaSaka.y)), (int(osoba.desniLakat.x),int(osoba.desniLakat.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.desniLakat.x),int(osoba.desniLakat.y)), (int(osoba.desnoRame.x),int(osoba.desnoRame.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.desnoRame.x),int(osoba.desnoRame.y)), (int(osoba.desniKuk.x),int(osoba.desniKuk.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.desniKuk.x),int(osoba.desniKuk.y)), (int(osoba.desnoStopalo.x),int(osoba.desnoStopalo.y)), (0,0,0), 3)
        
            cv2.circle(frame, (int(osoba.desniKuk.x),int(osoba.desniKuk.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.desnoRame.x),int(osoba.desnoRame.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.desniLakat.x),int(osoba.desniLakat.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.desnaSaka.x),int(osoba.desnaSaka.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.desnoStopalo.x),int(osoba.desnoStopalo.y)), radius=5, color=(255, 0, 0), thickness=5)
            
            r=0
            g=0
            b=0
            ugaoDesnoRame = int(osoba.izracunajUgao(osoba.desniKuk,osoba.desnoRame,osoba.desniLakat))
            if(ugaoDesnoRame > BicepsConfig.angleRightShoulderLower and ugaoDesnoRame < BicepsConfig.angleRightShoulderUpper): 
                g=0
                b=255
                if(ugaoDesnoRame < BicepsConfig.angleRightShoulderLimitGreen):
                    g=255
                    b=0
            else: 
                r=255
            cv2.putText(frame,
                        text = str(ugaoDesnoRame),
                        org = (int(osoba.desnoRame.x)-100, int(osoba.desnoRame.y)+20),
                        fontFace = cv2.FONT_HERSHEY_DUPLEX,
                        fontScale = 1.0,
                        color = (b, g, r),
                        thickness = 3)
            r=0
            g=0
            b=0
            ugaoDesniLakat = int(osoba.izracunajUgao(osoba.desnoRame,osoba.desniLakat,osoba.desnaSaka))
            if(ugaoDesniLakat > BicepsConfig.angleRightElbowLower and ugaoDesniLakat < BicepsConfig.angleRightElbowUpper): 
                g=0
                b=255
                if(ugaoDesniLakat <= BicepsConfig.angleRightElbowLimitGreen):
                    g=255
                    b=0
            else: 
                r=255
            cv2.putText(frame,
                        text = str(ugaoDesniLakat),
                        org = (int(osoba.desniLakat.x)-100, int(osoba.desniLakat.y)+20),
                        fontFace = cv2.FONT_HERSHEY_DUPLEX,
                        fontScale = 1.0,
                        color = (b, g, r),
                        thickness = 3)

        if(pro == 2 or both):
            message = "nastavite..."
            erHandler = 0
            
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
            b=0
            ugaoLevoRame = int(osoba.izracunajUgao(osoba.leviKuk,osoba.levoRame,osoba.leviLakat))
            if(ugaoLevoRame > BicepsConfig.angleLeftShoulderLower and ugaoLevoRame < BicepsConfig.angleLeftShoulderUpper): 
                g=0
                b=255
                if(ugaoLevoRame < BicepsConfig.angleLeftShoulderLimitGreen):
                    g=255
                    b=0
            else: 
                r=255
            cv2.putText(frame,
                        text = str(ugaoLevoRame),
                        org = (int(osoba.levoRame.x)+20, int(osoba.levoRame.y)+20),
                        fontFace = cv2.FONT_HERSHEY_DUPLEX,
                        fontScale = 1.0,
                        color = (b, g, r),
                        thickness = 3)
            r=0
            g=0
            b=0    
            ugaoLeviLakat = int(osoba.izracunajUgao(osoba.levoRame,osoba.leviLakat,osoba.levaSaka))
            if(ugaoLeviLakat > BicepsConfig.angleLeftElbowLower and ugaoLeviLakat < BicepsConfig.angleLeftElbowUpper): 
                g=0
                b=255
                if(ugaoLeviLakat <= BicepsConfig.angleLeftElbowLimitGreen):
                    g=255
                    b=0
            else: 
                r=255
            cv2.putText(frame,
                        text = str(ugaoLeviLakat),
                        org = (int(osoba.leviLakat.x)+20, int(osoba.leviLakat.y)+20),
                        fontFace = cv2.FONT_HERSHEY_DUPLEX,
                        fontScale = 1.0,
                        color = (b, g, r),
                        thickness = 3)
        if(pro == 0):
           message = "budite sigurni da ste lepo zauzeli polozaj, neki delovi tela nisu vidljivi"
           erHandler = 1

        return frame

def squat_draw_yolo(frame):
    global message
    global erHandler

    osoba = ocitajOsobu(frame) # Čitanje osobe sa frejma
    pro = SquatConfig.check(osoba)
    if(pro == 3):
        both = True
    else:
        both = False
    if(pro == 1 or both):
        message = "nastavite..."
        erHandler = 0

        cv2.line(frame, (int(osoba.desnoKoleno.x),int(osoba.desnoKoleno.y)), (int(osoba.desnoStopalo.x),int(osoba.desnoStopalo.y)), (0,0,0), 3)
        cv2.line(frame, (int(osoba.desnoKoleno.x),int(osoba.desnoKoleno.y)), (int(osoba.desniKuk.x),int(osoba.desniKuk.y)), (0,0,0), 3)
        cv2.circle(frame, (int(osoba.desnoKoleno.x),int(osoba.desnoKoleno.y)), radius=5, color=(255, 0, 0), thickness=5)
        cv2.circle(frame, (int(osoba.desnoStopalo.x),int(osoba.desnoStopalo.y)), radius=5, color=(255, 0, 0), thickness=5)
        cv2.circle(frame, (int(osoba.desniKuk.x),int(osoba.desniKuk.y)), radius=5, color=(255, 0, 0), thickness=5)

        r=0 
        g=0
        b=0
        ugaoDesnoKoleno = int(osoba.izracunajUgao(osoba.desnoStopalo,osoba.desnoKoleno,osoba.desniKuk))
        if(ugaoDesnoKoleno > SquatConfig.angleKneeLimitBlue):
            b=255
            g=0
        elif(ugaoDesnoKoleno > SquatConfig.angleKneeLimitGreen):
            g=255
            b=0
        else: 
            r=255
        cv2.putText(frame,
                    text = str(ugaoDesnoKoleno),
                    org = (int(osoba.desnoKoleno.x)-200, int(osoba.desnoKoleno.y)+20),
                    fontFace = cv2.FONT_HERSHEY_DUPLEX,
                    fontScale = 1.3,
                    color = (b, g, r),
                    thickness = 3)

    if(pro == 2 or both):
        message = "nastavite..."
        erHandler = 0

        cv2.line(frame, (int(osoba.levoKoleno.x),int(osoba.levoKoleno.y)), (int(osoba.levoStopalo.x),int(osoba.levoStopalo.y)), (0,0,0), 3)
        cv2.line(frame, (int(osoba.levoKoleno.x),int(osoba.levoKoleno.y)), (int(osoba.leviKuk.x),int(osoba.leviKuk.y)), (0,0,0), 3)
        cv2.circle(frame, (int(osoba.levoKoleno.x),int(osoba.levoKoleno.y)), radius=5, color=(255, 0, 0), thickness=5)
        cv2.circle(frame, (int(osoba.levoStopalo.x),int(osoba.levoStopalo.y)), radius=5, color=(255, 0, 0), thickness=5)
        cv2.circle(frame, (int(osoba.leviKuk.x),int(osoba.leviKuk.y)), radius=5, color=(255, 0, 0), thickness=5)

        r=0
        g=0
        b=0
        ugaoLevoKoleno = int(osoba.izracunajUgao(osoba.levoStopalo,osoba.levoKoleno,osoba.leviKuk))
        if(ugaoLevoKoleno > SquatConfig.angleKneeLimitBlue):
            b=255
            g=0
        elif(ugaoLevoKoleno > SquatConfig.angleKneeLimitGreen):
            g=255
            b=0
        else: 
            r=255
        cv2.putText(frame,
                    text = str(ugaoLevoKoleno),
                    org = (int(osoba.levoKoleno.x)+20, int(osoba.levoKoleno.y)+20),
                    fontFace = cv2.FONT_HERSHEY_DUPLEX,
                    fontScale = 1.3,
                    color = (b, g, r),
                    thickness = 3) 
    
    if(pro == 3):
        message = "budite sigurni da ste lepo zauzeli polozaj, neki delovi tela nisu vidljivi"
        erHandler = 1

    return frame

def deadLift_draw_yolo(frame):
    global message
    global erHandler
    osoba = ocitajOsobu(frame) # Čitanje osobe sa frejma
    pro = DeadLiftConfig.check(osoba)
    if(pro == 3):
        both = True
    else:
        both = False
        
    if(pro == 1 or both):
            message = "nastavite..."
            erHandler = 0
           
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
            
            r=0
            g=0
            b=0
            ugaoDesnoKoleno = int(osoba.izracunajUgao(osoba.desniKuk,osoba.desnoKoleno,osoba.desnoStopalo))
            if(ugaoDesnoKoleno > DeadLiftConfig.angleRightKneeLower and ugaoDesnoKoleno < DeadLiftConfig.angleRightKneeUpper): 
                g=0
                b=255
                if(DeadLiftConfig.angleRightKneeLimitGreenL<= ugaoDesnoKoleno and ugaoDesnoKoleno<= DeadLiftConfig.angleRightKneeLimitGreenU):
                    g=255
                    b=0
            else: 
                r=255
            cv2.putText(frame,
                        text = str(ugaoDesnoKoleno),
                        org = (int(osoba.desnoKoleno.x)-100, int(osoba.desnoKoleno.y)+20),
                        fontFace = cv2.FONT_HERSHEY_DUPLEX,
                        fontScale = 1.0,
                        color = (b, g, r),
                        thickness = 3)
            r=0
            g=0
            b=0
            ugaoDesniKuk = int(osoba.izracunajUgao(osoba.desnoRame,osoba.desniKuk,osoba.desnoKoleno))
            if(ugaoDesniKuk > DeadLiftConfig.angleRightHipLower and ugaoDesniKuk < DeadLiftConfig.angleRightHipUpper): 
                g=0
                b=255
                if(DeadLiftConfig.angleRightHipLimitGreenL <= ugaoDesniKuk and ugaoDesniKuk <= DeadLiftConfig.angleRightHipLimitGreenU):
                    g=255
                    b=0
            else: 
                r=255
            cv2.putText(frame,
                        text = str(ugaoDesniKuk),
                        org = (int(osoba.desniKuk.x)-100, int(osoba.desniKuk.y)+20),
                        fontFace = cv2.FONT_HERSHEY_DUPLEX,
                        fontScale = 1.0,
                        color = (b, g, r),
                        thickness = 3)
    
    if(pro == 2 or both):
            message = "nastavite..."
            erHandler = 0
            
            cv2.line(frame, (int(osoba.levoStopalo.x),int(osoba.levoStopalo.y)), (int(osoba.levoKoleno.x),int(osoba.levoKoleno.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.levoKoleno.x),int(osoba.levoKoleno.y)), (int(osoba.leviKuk.x),int(osoba.leviKuk.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.leviKuk.x),int(osoba.leviKuk.y)), (int(osoba.levoRame.x),int(osoba.levoRame.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.levoRame.x),int(osoba.levoRame.y)), (int(osoba.leviLakat.x),int(osoba.leviLakat.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.leviLakat.x),int(osoba.leviLakat.y)), (int(osoba.levaSaka.x),int(osoba.levaSaka.y)), (0,0,0), 3)

            cv2.circle(frame, (int(osoba.levoKoleno.x),int(osoba.levoKoleno.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.levoStopalo.x),int(osoba.levoStopalo.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.leviKuk.x),int(osoba.leviKuk.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.levoRame.x),int(osoba.levoRame.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.leviLakat.x),int(osoba.leviLakat.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.levaSaka.x),int(osoba.levaSaka.y)), radius=5, color=(255, 0, 0), thickness=5)

            r=0
            g=0
            b=0
            ugaoLevoKoleno = int(osoba.izracunajUgao(osoba.leviKuk,osoba.levoKoleno,osoba.levoStopalo))
            if(ugaoLevoKoleno > DeadLiftConfig.angleLeftKneeLower and ugaoLevoKoleno < DeadLiftConfig.angleLeftKneeUpper): 
                g=0
                b=255
                if(DeadLiftConfig.angleLeftKneeLimitGreenL<= ugaoLevoKoleno and ugaoLevoKoleno<= DeadLiftConfig.angleLeftKneeLimitGreenU):
                    g=255
                    b=0
            else: 
                r=255
            cv2.putText(frame,
                        text = str(ugaoLevoKoleno),
                        org = (int(osoba.levoKoleno.x)-100, int(osoba.levoKoleno.y)+20),
                        fontFace = cv2.FONT_HERSHEY_DUPLEX,
                        fontScale = 1.0,
                        color = (b, g, r),
                        thickness = 3)
            r=0
            g=0
            b=0
            ugaoLeviKuk = int(osoba.izracunajUgao(osoba.levoRame,osoba.leviKuk,osoba.levoKoleno))
            if(ugaoLeviKuk > DeadLiftConfig.angleLeftHipLower and ugaoLeviKuk < DeadLiftConfig.angleLeftHipUpper): 
                g=0
                b=255
                if(DeadLiftConfig.angleLeftHipLimitGreenL <= ugaoLeviKuk and ugaoLeviKuk <= DeadLiftConfig.angleLeftHipLimitGreenU):
                    g=255
                    b=0
            else: 
                r=255
            cv2.putText(frame,
                        text = str(ugaoLeviKuk),
                        org = (int(osoba.leviKuk.x)-100, int(osoba.leviKuk.y)+20),
                        fontFace = cv2.FONT_HERSHEY_DUPLEX,
                        fontScale = 1.0,
                        color = (b, g, r),
                        thickness = 3)

           
          
    if(pro == 0):
        message = "budite sigurni da ste lepo zauzeli polozaj, neki delovi tela nisu vidljivi"
        erHandler = 1

    
    return frame

def fly_draw_yolo(frame):
        global message
        global erHandler

        osoba = ocitajOsobu(frame) # Čitanje osobe sa frejma
        pro = FlyConfig.check(osoba)
        if(pro == 3):
            both = True
        else:
            both = False
        
        if(pro == 1 or both):
            message = "nastavite..."
            erHandler = 0

            cv2.line(frame, (int(osoba.desniKuk.x),int(osoba.desniKuk.y)), (int(osoba.desnoRame.x),int(osoba.desnoRame.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.desnoRame.x),int(osoba.desnoRame.y)), (int(osoba.desniLakat.x),int(osoba.desniLakat.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.desniLakat.x),int(osoba.desniLakat.y)), (int(osoba.desnaSaka.x),int(osoba.desnaSaka.y)), (0,0,0), 3)
        
            cv2.circle(frame, (int(osoba.desniKuk.x),int(osoba.desniKuk.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.desnoRame.x),int(osoba.desnoRame.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.desniLakat.x),int(osoba.desniLakat.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.desnaSaka.x),int(osoba.desnaSaka.y)), radius=5, color=(255, 0, 0), thickness=5)
            
            r=0
            g=0
            b=0
            ugaoDesnoRame = int(osoba.izracunajUgao(osoba.desniKuk,osoba.desnoRame,osoba.desniLakat))
            if(ugaoDesnoRame > FlyConfig.angleRightShoulderLower and ugaoDesnoRame < FlyConfig.angleRightShoulderUpper): 
                g=0
                b=255
            if(ugaoDesnoRame >= FlyConfig.angleRightShoulderLimitGreenL and ugaoDesnoRame <= FlyConfig.angleRightShoulderLimitGreenU):
                    g=255
                    b=0
            else: 
                r=255
            cv2.putText(frame,
                        text = str(ugaoDesnoRame),
                        org = (int(osoba.desnoRame.x)-100, int(osoba.desnoRame.y)+20),
                        fontFace = cv2.FONT_HERSHEY_DUPLEX,
                        fontScale = 1.0,
                        color = (b, g, r),
                        thickness = 3)
            r=0
            g=0
            b=0
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
                        color = (b, g, r),
                        thickness = 3)
            
        if(pro == 2 or both):
            message = "nastavite..."
            erHandler = 0
            cv2.line(frame, (int(osoba.leviKuk.x),int(osoba.leviKuk.y)), (int(osoba.levoRame.x),int(osoba.levoRame.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.levoRame.x),int(osoba.levoRame.y)), (int(osoba.leviLakat.x),int(osoba.leviLakat.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.leviLakat.x),int(osoba.leviLakat.y)), (int(osoba.levaSaka.x),int(osoba.levaSaka.y)), (0,0,0), 3)
        
            cv2.circle(frame, (int(osoba.leviKuk.x),int(osoba.leviKuk.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.desnoRame.x),int(osoba.levoRame.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.leviLakat.x),int(osoba.leviLakat.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.levaSaka.x),int(osoba.levaSaka.y)), radius=5, color=(255, 0, 0), thickness=5)
        
            r=0
            g=0
            b=0
            ugaoLevoRame = int(osoba.izracunajUgao(osoba.leviKuk,osoba.levoRame,osoba.leviLakat))
            if(ugaoLevoRame > FlyConfig.angleLeftShoulderLower and ugaoLevoRame < FlyConfig.angleRightShoulderUpper): 
                g=0
                b=255
            if(ugaoLevoRame >= FlyConfig.angleLeftShoulderLimitGreenL and ugaoLevoRame <= FlyConfig.angleLeftShoulderLimitGreenU): 
                    g=255
                    b=0
            else: 
                r=255
            cv2.putText(frame,
                        text = str(ugaoLevoRame),
                        org = (int(osoba.levoRame.x)+20, int(osoba.levoRame.y)+20),
                        fontFace = cv2.FONT_HERSHEY_DUPLEX,
                        fontScale = 1.0,
                        color = (b, g, r),
                        thickness = 3)
            
           
            r=0
            g=0
            b=0
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
                        color = (b, g, r),
                        thickness = 3)
        
        if(pro == 0):
           message = "budite sigurni da ste lepo zauzeli polozaj, neki delovi tela nisu vidljivi"
           erHandler = 1


        return frame

def pushups_draw_yolo(frame):
    global message
    global erHandler

    osoba = ocitajOsobu(frame) # Čitanje osobe sa frejma
    pro = PushUpsConfig.check(osoba)
    if(pro == 3):
        both = True
    else:
        both = False
        
    if(pro == 1 or both):
        message = "nastavite..."
        erHandler = 0
            
        cv2.line(frame, (int(osoba.desnaSaka.x),int(osoba.desnaSaka.y)), (int(osoba.desniLakat.x),int(osoba.desniLakat.y)), (0,0,0), 3)
        cv2.line(frame, (int(osoba.desniLakat.x),int(osoba.desniLakat.y)), (int(osoba.desnoRame.x),int(osoba.desnoRame.y)), (0,0,0), 3)
        cv2.line(frame, (int(osoba.desnoRame.x),int(osoba.desnoRame.y)), (int(osoba.desniKuk.x),int(osoba.desniKuk.y)), (0,0,0), 3)
        cv2.line(frame, (int(osoba.desniKuk.x),int(osoba.desniKuk.y)), (int(osoba.desnoKoleno.x),int(osoba.desnoKoleno.y)), (0,0,0), 3)
        cv2.line(frame, (int(osoba.desnoKoleno.x),int(osoba.desnoKoleno.y)), (int(osoba.desnoStopalo.x),int(osoba.desnoStopalo.y)), (0,0,0), 3)
        
        cv2.circle(frame, (int(osoba.desniKuk.x),int(osoba.desniKuk.y)), radius=5, color=(255, 0, 0), thickness=5)
        cv2.circle(frame, (int(osoba.desnoRame.x),int(osoba.desnoRame.y)), radius=5, color=(255, 0, 0), thickness=5)
        cv2.circle(frame, (int(osoba.desniLakat.x),int(osoba.desniLakat.y)), radius=5, color=(255, 0, 0), thickness=5)
        cv2.circle(frame, (int(osoba.desnaSaka.x),int(osoba.desnaSaka.y)), radius=5, color=(255, 0, 0), thickness=5)
        cv2.circle(frame, (int(osoba.desnoStopalo.x),int(osoba.desnoStopalo.y)), radius=5, color=(255, 0, 0), thickness=5)
        cv2.circle(frame, (int(osoba.desnoKoleno.x),int(osoba.desnoKoleno.y)), radius=5, color=(255, 0, 0), thickness=5)
            
        r=0
        g=0
        b=0
        ugaoDesniLakat = int(osoba.izracunajUgao(osoba.desnoRame,osoba.desniLakat,osoba.desnaSaka))
        if(ugaoDesniLakat > PushUpsConfig.angleRightElbowLower and ugaoDesniLakat < PushUpsConfig.angleRightElbowUpper): 
            g=0
            b=255
            if(PushUpsConfig.angleRightElbowLimitGreenL<=ugaoDesniLakat and ugaoDesniLakat <= PushUpsConfig.angleRightElbowLimitGreenU):
                g=255
                b=0
        else: 
            r=255
        cv2.putText(frame,
                    text = str(ugaoDesniLakat),
                    org = (int(osoba.desniLakat.x)-100, int(osoba.desniLakat.y)-40),
                    fontFace = cv2.FONT_HERSHEY_DUPLEX,
                    fontScale = 1.0,
                    color = (b, g, r),
                    thickness = 3)
        r=0
        g=0
        b=0
        ugaoDesniTeloKuk = int(osoba.izracunajUgao(osoba.desnoRame,osoba.desniKuk,osoba.desnoKoleno))
        if(ugaoDesniTeloKuk > PushUpsConfig.angleRightBodyLower and ugaoDesniTeloKuk < PushUpsConfig.angleRightBodyUpper): 
            g=0
            b=255
            if(True):
                g=255
                b=0
        else: 
            r=255
        cv2.putText(frame,
                    text = str(ugaoDesniTeloKuk),
                    org = (int(osoba.desniKuk.x)-90, int(osoba.desniKuk.y)-40),
                    fontFace = cv2.FONT_HERSHEY_DUPLEX,
                    fontScale = 1.0,
                    color = (b, g, r),
                    thickness = 3)
        r=0
        g=0
        b=0
        ugaoDesniTeloKoleno = int(osoba.izracunajUgao(osoba.desniKuk,osoba.desnoKoleno,osoba.desnoStopalo))
        if(ugaoDesniTeloKoleno > PushUpsConfig.angleRightBodyLower and ugaoDesniTeloKoleno < PushUpsConfig.angleRightBodyUpper): 
            g=0
            b=255
            if(True):
                g=255
                b=0
        else: 
            r=255
        cv2.putText(frame,
                    text = str(ugaoDesniTeloKoleno),
                    org = (int(osoba.desnoKoleno.x)-90, int(osoba.desnoKoleno.y)-40),
                    fontFace = cv2.FONT_HERSHEY_DUPLEX,
                    fontScale = 1.0,
                    color = (b, g, r),
                    thickness = 3)
        

    if(pro == 2 or both):
        message = "nastavite..."
        erHandler = 0
            
        cv2.line(frame, (int(osoba.levaSaka.x),int(osoba.levaSaka.y)), (int(osoba.leviLakat.x),int(osoba.leviLakat.y)), (0,0,0), 3)
        cv2.line(frame, (int(osoba.leviLakat.x),int(osoba.leviLakat.y)), (int(osoba.levoRame.x),int(osoba.levoRame.y)), (0,0,0), 3)
        cv2.line(frame, (int(osoba.levoRame.x),int(osoba.levoRame.y)), (int(osoba.leviKuk.x),int(osoba.leviKuk.y)), (0,0,0), 3)
        cv2.line(frame, (int(osoba.leviKuk.x),int(osoba.leviKuk.y)), (int(osoba.levoKoleno.x),int(osoba.levoKoleno.y)), (0,0,0), 3)
        cv2.line(frame, (int(osoba.levoKoleno.x),int(osoba.levoKoleno.y)), (int(osoba.levoStopalo.x),int(osoba.levoStopalo.y)), (0,0,0), 3)
        
        cv2.circle(frame, (int(osoba.leviKuk.x),int(osoba.leviKuk.y)), radius=5, color=(255, 0, 0), thickness=5)
        cv2.circle(frame, (int(osoba.levoRame.x),int(osoba.levoRame.y)), radius=5, color=(255, 0, 0), thickness=5)
        cv2.circle(frame, (int(osoba.leviLakat.x),int(osoba.leviLakat.y)), radius=5, color=(255, 0, 0), thickness=5)
        cv2.circle(frame, (int(osoba.levaSaka.x),int(osoba.levaSaka.y)), radius=5, color=(255, 0, 0), thickness=5)
        cv2.circle(frame, (int(osoba.levoStopalo.x),int(osoba.levoStopalo.y)), radius=5, color=(255, 0, 0), thickness=5)
        cv2.circle(frame, (int(osoba.levoKoleno.x),int(osoba.levoKoleno.y)), radius=5, color=(255, 0, 0), thickness=5)
            
        r=0
        g=0
        b=0
        ugaoLeviLakat = int(osoba.izracunajUgao(osoba.levoRame,osoba.leviLakat,osoba.levaSaka))
        if(ugaoLeviLakat > PushUpsConfig.angleLeftElbowLower and ugaoLeviLakat < PushUpsConfig.angleLeftElbowUpper): 
            g=0
            b=255
            if(PushUpsConfig.angleLeftElbowLimitGreenL<=ugaoLeviLakat and ugaoLeviLakat <= PushUpsConfig.angleLeftElbowLimitGreenU):
                g=255
                b=0
        else: 
            r=255
        cv2.putText(frame,
                    text = str(ugaoLeviLakat),
                    org = (int(osoba.leviLakat.x)-100, int(osoba.leviLakat.y)-30),
                    fontFace = cv2.FONT_HERSHEY_DUPLEX,
                    fontScale = 1.0,
                    color = (b, g, r),
                    thickness = 3)
        r=0
        g=0
        b=0
        ugaoLeviTeloKuk = int(osoba.izracunajUgao(osoba.levoRame,osoba.leviKuk,osoba.levoKoleno))
        if(ugaoLeviTeloKuk > PushUpsConfig.angleLeftBodyLower and ugaoLeviTeloKuk < PushUpsConfig.angleLeftBodyUpper): 
            g=0
            b=255
            if(True):
                g=255
                b=0
        else: 
            r=255
        cv2.putText(frame,
                    text = str(ugaoLeviTeloKuk),
                    org = (int(osoba.leviKuk.x)-120, int(osoba.leviKuk.y)-40),
                    fontFace = cv2.FONT_HERSHEY_DUPLEX,
                    fontScale = 1.0,
                    color = (b, g, r),
                    thickness = 3)
        r=0
        g=0
        b=0
        ugaoLeviTeloKoleno = int(osoba.izracunajUgao(osoba.leviKuk,osoba.levoKoleno,osoba.levoStopalo))
        if(ugaoLeviTeloKoleno > PushUpsConfig.angleLeftBodyLower and ugaoLeviTeloKoleno < PushUpsConfig.angleLeftBodyUpper): 
            g=0
            b=255
            if(True):
                g=255
                b=0
        else: 
            r=255
        cv2.putText(frame,
                    text = str(ugaoLeviTeloKoleno),
                    org = (int(osoba.levoKoleno.x)-100, int(osoba.levoKoleno.y)-40),
                    fontFace = cv2.FONT_HERSHEY_DUPLEX,
                    fontScale = 1.0,
                    color = (b, g, r),
                    thickness = 3)
    if(pro == 0):
        message = "budite sigurni da ste lepo zauzeli polozaj, neki delovi tela nisu vidljivi"
        erHandler = 1

    return frame

def abs_draw_yolo(frame):
    global message
    global erHandler
    osoba = ocitajOsobu(frame) # Čitanje osobe sa frejma
    pro = AbsConfig.check(osoba)
    if(pro == 3):
        both = True
    else:
        both = False
        
    if(pro == 1 or both):
            global message
            message = "nastavite..."
            global erHandler
            erHandler = 0
           
            cv2.line(frame, (int(osoba.desnoStopalo.x),int(osoba.desnoStopalo.y)), (int(osoba.desnoKoleno.x),int(osoba.desnoKoleno.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.desnoKoleno.x),int(osoba.desnoKoleno.y)), (int(osoba.desniKuk.x),int(osoba.desniKuk.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.desniKuk.x),int(osoba.desniKuk.y)), (int(osoba.desnoRame.x),int(osoba.desnoRame.y)), (0,0,0), 3)
            
            cv2.circle(frame, (int(osoba.desnoKoleno.x),int(osoba.desnoKoleno.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.desnoStopalo.x),int(osoba.desnoStopalo.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.desniKuk.x),int(osoba.desniKuk.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.desnoRame.x),int(osoba.desnoRame.y)), radius=5, color=(255, 0, 0), thickness=5)
           
            r=0
            g=0
            b=0
            ugaoDesnoKoleno = int(osoba.izracunajUgao(osoba.desniKuk,osoba.desnoKoleno,osoba.desnoStopalo))
            if(ugaoDesnoKoleno > AbsConfig.angleRightKneeLower and ugaoDesnoKoleno < AbsConfig.angleRightKneeUpper): 
                g=0
                b=255
                if(AbsConfig.angleRightBodyLimitGreenL<= ugaoDesnoKoleno and ugaoDesnoKoleno <= AbsConfig.angleRightBodyLimitGreenU):
                    g=255
                    b=0
            else: 
                r=255
            cv2.putText(frame,
                        text = str(ugaoDesnoKoleno),
                        org = (int(osoba.desnoKoleno.x)-100, int(osoba.desnoKoleno.y)+20),
                        fontFace = cv2.FONT_HERSHEY_DUPLEX,
                        fontScale = 1.0,
                        color = (b, g, r),
                        thickness = 3)
            r=0
            g=0
            b=0
            ugaoDesniKuk = int(osoba.izracunajUgao(osoba.desnoRame,osoba.desniKuk,osoba.desnoKoleno))
            if(ugaoDesniKuk > AbsConfig.angleRightBodyLower and ugaoDesniKuk < AbsConfig.angleRightBodyUpper): 
                g=0
                b=255
                if(AbsConfig.angleRightBodyLimitGreenL <= ugaoDesniKuk and ugaoDesniKuk <= AbsConfig.angleRightBodyLimitGreenU):
                    g=255
                    b=0
            else: 
                r=255
            cv2.putText(frame,
                        text = str(ugaoDesniKuk),
                        org = (int(osoba.desniKuk.x)-100, int(osoba.desniKuk.y)+20),
                        fontFace = cv2.FONT_HERSHEY_DUPLEX,
                        fontScale = 1.0,
                        color = (b, g, r),
                        thickness = 3)
    
    if(pro == 2 or both):
            message = "nastavite..."
            erHandler = 0

            cv2.line(frame, (int(osoba.levoStopalo.x),int(osoba.levoStopalo.y)), (int(osoba.levoKoleno.x),int(osoba.levoKoleno.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.levoKoleno.x),int(osoba.levoKoleno.y)), (int(osoba.leviKuk.x),int(osoba.leviKuk.y)), (0,0,0), 3)
            cv2.line(frame, (int(osoba.leviKuk.x),int(osoba.leviKuk.y)), (int(osoba.levoRame.x),int(osoba.levoRame.y)), (0,0,0), 3)
           
            cv2.circle(frame, (int(osoba.levoKoleno.x),int(osoba.levoKoleno.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.levoStopalo.x),int(osoba.levoStopalo.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.leviKuk.x),int(osoba.leviKuk.y)), radius=5, color=(255, 0, 0), thickness=5)
            cv2.circle(frame, (int(osoba.levoRame.x),int(osoba.levoRame.y)), radius=5, color=(255, 0, 0), thickness=5)
           
            r=0
            g=0
            b=0
            ugaoLevoKoleno = int(osoba.izracunajUgao(osoba.leviKuk,osoba.levoKoleno,osoba.levoStopalo))
            if(ugaoLevoKoleno > AbsConfig.angleLeftKneeLower and ugaoLevoKoleno < AbsConfig.angleLeftKneeUpper): 
                g=0
                b=255
                if(AbsConfig.angleLeftKneeLimitGreenL<= ugaoLevoKoleno and ugaoLevoKoleno<= AbsConfig.angleLeftKneeLimitGreenU):
                    g=255
                    b=0
            else: 
                r=255
            cv2.putText(frame,
                        text = str(ugaoLevoKoleno),
                        org = (int(osoba.levoKoleno.x)-100, int(osoba.levoKoleno.y)+20),
                        fontFace = cv2.FONT_HERSHEY_DUPLEX,
                        fontScale = 1.0,
                        color = (b, g, r),
                        thickness = 3)
            r=0
            g=0
            b=0
            ugaoLeviKuk = int(osoba.izracunajUgao(osoba.levoRame,osoba.leviKuk,osoba.levoKoleno))
            if(ugaoLeviKuk > AbsConfig.angleLeftBodyLower and ugaoLeviKuk < AbsConfig.angleLeftBodyUpper): 
                g=0
                b=255
                if(AbsConfig.angleLeftBodyLimitGreenL <= ugaoLeviKuk and ugaoLeviKuk <= AbsConfig.angleLeftBodyLimitGreenU):
                    g=255
                    b=0
            else: 
                r=255
            cv2.putText(frame,
                        text = str(ugaoLeviKuk),
                        org = (int(osoba.leviKuk.x)-100, int(osoba.leviKuk.y)+20),
                        fontFace = cv2.FONT_HERSHEY_DUPLEX,
                        fontScale = 1.0,
                        color = (b, g, r),
                        thickness = 3)

           
          
    if(pro == 0):
        message = "budite sigurni da ste lepo zauzeli polozaj, neki delovi tela nisu vidljivi"
        erHandler = 1

    
    return frame
       
    
exerciseList = [squat_draw_yolo,deadLift_draw_yolo, pushups_draw_yolo, abs_draw_yolo,biceps_draw_yolo , fly_draw_yolo]

#0 squat
#1 deadLift
#2 pushups
#3 abs
#4 biceps
#5 fly

def run_yolo(frame, exercise):

    processed_frame = exerciseList[exercise](frame)
    print(exercise)

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