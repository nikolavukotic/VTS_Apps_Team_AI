import cv2
import os
import glob
from osoba import *
from yolo import *
from cucanj import *
from letenje import *
from biceps import *
from trbusnjaci import *
from sklekovi import *
from kolena import *

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



   






