import cv2
import os
from tkinter import PhotoImage
from PIL import Image as im, ImageTk
import cucanj as squat
import kolena as knees
import letenje as flying
import sklekovi as pushups
import trbusnjaci as abss
import biceps as biceps
import deadlift as deadlift


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


def resize_frame(frame_processed):
    height, width, channels = frame_processed.shape
    
    if(width>height):
        desired_width = 720
        desired_height = 460
    else:
        desired_width = 460
        desired_height = 720
        
    new_image = cv2.resize(frame_processed, (desired_width, desired_height))
    new_image = im.fromarray(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
    new_image.save('gui_images/temp.png')
    
#biceps, Cucanj #kolena(Mrtvo), Letenje #sklekovi, trbusnjaci
def process_frame2(frame, exercise):
    exercises = [biceps.biceps_draw_yolo, squat.squat_draw_yolo, knees.knees_draw_yolo, flying.fly_draw_yolo, pushups.pushups_draw_yolo, abss.abs_draw_yolo ]
    processed_frame = exercises[exercise](frame)
    return processed_frame


def get_excersise_name(video):
    exw = video.split('/')
    ex = exw[-1]
    return ex



   






