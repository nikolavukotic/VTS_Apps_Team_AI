from ultralytics import YOLO
import cv2
from cucanj import *
from osoba import *
from yolo import *

video = "videoSnimci/squatTrim.mp4"

cap = cv2.VideoCapture(video)

izracunajCucanj(cap) # Izračunaj i prikaži čučanj

        


