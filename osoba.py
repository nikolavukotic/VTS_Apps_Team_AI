from ultralytics import YOLO
import cv2
import math
import numpy as np 
from PIL import Image as im 

class TackaNaTelu:
    def __init__(self, tacka: list[float]):
        self.x = tacka[0]
        self.y = tacka[1]
        self.visibility = tacka[2]
class Osoba:
    def __init__(self, listaTacaka: list[list[float]]):
        self.nos = TackaNaTelu(listaTacaka[0])
        self.levoOko = TackaNaTelu(listaTacaka[1])
        self.desnoOko = TackaNaTelu(listaTacaka[2])
        self.levoUvo = TackaNaTelu(listaTacaka[3])
        self.desnoUvo = TackaNaTelu(listaTacaka[4])
        self.levoRame = TackaNaTelu(listaTacaka[5])
        self.desnoRame = TackaNaTelu(listaTacaka[6])
        self.leviLakat = TackaNaTelu(listaTacaka[7])
        self.desniLakat = TackaNaTelu(listaTacaka[8])
        self.levaSaka = TackaNaTelu(listaTacaka[9])
        self.desnaSaka = TackaNaTelu(listaTacaka[10])
        self.leviKuk = TackaNaTelu(listaTacaka[11])
        self.desniKuk = TackaNaTelu(listaTacaka[12])
        self.levoKoleno = TackaNaTelu(listaTacaka[13])
        self.desnoKoleno = TackaNaTelu(listaTacaka[14])
        self.levoStopalo = TackaNaTelu(listaTacaka[15])
        self.desnoStopalo = TackaNaTelu(listaTacaka[16])
    def izracunajUgao(self, t1, t2, t3) -> float:
        minimalnaVidljivostTacke = 0.5
        if(t1.visibility > minimalnaVidljivostTacke and
           t2.visibility > minimalnaVidljivostTacke and
           t3.visibility > minimalnaVidljivostTacke):
            vektorA = [(t1.x - t2.x), (t1.y - t2.y)]
            vektorB = [(t3.x - t2.x), (t3.y - t2.y)]

            skalarniProizvod = vektorA[0] * vektorB[0] + vektorA[1] * vektorB[1]
            moduoVektora = math.sqrt(vektorA[0] ** 2 + vektorA[1] ** 2) * math.sqrt(vektorB[0] ** 2 + vektorB[1] ** 2)

            cosUgao = skalarniProizvod / moduoVektora
            ugao = math.degrees(math.acos(cosUgao))
            return ugao
        else:
            return 0