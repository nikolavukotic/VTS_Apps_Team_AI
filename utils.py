import cv2
from cucanj import *
from osoba import *
from yolo import *
from letenje import *
from biceps import *
from trbusnjaci import *
from sklekovi import *
from kolena import *
import os
import glob

# Other

def get_video_file_names(folder_path):

    video_extensions = ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm']
    video_files = []

    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if any(file.endswith(ext) for ext in video_extensions):
                    video_files.append(file)
    else:
        print("Folder does not exist or is not a directory.")

    return video_files


def cucanjj(video):

    cap = cv2.VideoCapture(video)

    izracunajCucanj(cap) # Izračunaj i prikaži čučanj


def letenje(video):

    cap = cv2.VideoCapture(video)

    izracunajLetenje(cap) # Izračunaj i prikaži letenje



def bicepsUspravnoStajanje(video):
    
    cap = cv2.VideoCapture(video)

    izracunajBiceps(cap) # Izračunaj i prikaži bicebs

def trbusnjaci(video):

    cap = cv2.VideoCapture(video)

    izracunajTrbusnjaci(cap) # Izračunaj i prikaži trbusanjci

def sklekovi(video):

    cap = cv2.VideoCapture(video)

    izracunajSklekovi(cap) # Izračunaj i prikaži sklekovi

def kolena(video):

    cap = cv2.VideoCapture(video)

    izracunajKolena(cap) # Izračunaj i prikaži kolena


