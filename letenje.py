import cv2
from osoba import *
from yolo import *


def fly_draw_yolo(frame):
    
        
            
        osoba = ocitajOsobu(frame) # Čitanje osobe sa frejma

        if((osoba.desniLakat.visibility > 0.5 and osoba.desnoRame.visibility > 0.5 and osoba.desniKuk.visibility > 0.5 and osoba.desnaSaka.visibility > 0.5) or 
          ( osoba.leviLakat.visibility > 0.5 and osoba.levoRame.visibility > 0.5 and osoba.leviKuk.visibility > 0.5 and osoba.levaSaka.visibility > 0.5) ):

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
            if(ugaoLevoRame > 80 and ugaoLevoRame < 100): 
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
            if(ugaoDesnoRame > 80 and ugaoDesnoRame < 100): 
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
            if(ugaoLeviLakat > 100 and ugaoLeviLakat < 150): 
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
            if(ugaoDesniLakat > 100 and ugaoDesniLakat < 150): 
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
        return frame
    