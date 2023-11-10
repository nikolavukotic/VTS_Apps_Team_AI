import cv2
import os
from PIL import Image as im, ImageTk
from exercises import exercizeList
import numpy as np
import time

def get_video_file_names():
    folder_path = "exercise_videos/existing_videos/"
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

def resize_frame(frame_processed):
    height, width, channels = frame_processed.shape
    
    if(width>height):
        desired_width = 750
        desired_height = 420
    else:
        desired_width = 420
        desired_height = 750
        
    new_image = cv2.resize(frame_processed, (desired_width, desired_height))
    new_image = im.fromarray(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
    new_image.save('gui_images/display_frame.png')

def process_frame(frame, exercise):
    processed_frame = exercizeList[exercise](frame)
    return processed_frame

#TODO
def process_and_resize_frame(frame, exercise):

    processed_frame = exercizeList[exercise](frame)

    height, width, channels = processed_frame.shape
    if(width>height):
        desired_width = 750
        desired_height = 420
    else:
        desired_width = 420
        desired_height = 750
        
    new_image = cv2.resize(processed_frame, (desired_width, desired_height))
    new_image = im.fromarray(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
    new_image.save('gui_images/display_frame.png')    
    

   






