import cv2
from cucanj import *
from osoba import *
from yolo import *

def show_webcam(mirror=False):
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        if mirror: 
            img = cv2.flip(img, 1)
        cv2.imshow('my webcam', img)
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
    cv2.destroyAllWindows()

def cucanj(video):

    cap = cv2.VideoCapture(video)

    izracunajCucanj(cap) # Izračunaj i prikaži čučanj


def letenje():
    pass


def empty_function_3():
    pass

def empty_function_4():
    pass



