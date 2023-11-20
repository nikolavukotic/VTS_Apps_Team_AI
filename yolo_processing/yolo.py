from ultralytics import YOLO
from PIL import Image as im
from yolo_processing.osoba import *

model = YOLO('yolo_processing/yolov8m-pose.pt')

def ocitajOsobu(frame):
    results = model(source=im.fromarray(frame)) 
    listaTacaka = results[0].keypoints.data.numpy()[0] # YOLO Pose modelu dajemo jedan frejm sa kojeg on čita tačke
    osoba = Osoba(listaTacaka)
    return osoba