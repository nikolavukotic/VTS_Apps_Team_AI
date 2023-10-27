import cv2
import os
from tkinter import PhotoImage
from PIL import Image as im, ImageTk
import cucanj as squat_class
import kolena as knees_class
import letenje as fly_class
import sklekovi as push_ups_class
import trbusnjaci as abs_class
import biceps as biceps_class


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
        desired_width = 700
        desired_height = 400
    else:
        desired_width = 460
        desired_height = 720
        
    new_image = cv2.resize(frame_processed, (desired_width, desired_height))
    new_image = im.fromarray(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))

    return new_image

def process_frame(frame,ex):
     match ex:
            case 'squatTrim.mp4':
                frame_processed = squat_class.squat_draw_yolo(frame)
                return frame_processed
            case 'abs.mp4':
                frame_processed = abs_class.abs_draw_yolo(frame)
                return frame_processed
            case 'biceps.mp4':
                frame_processed = biceps_class.biceps_draw_yolo(frame)
                return frame_processed
            case 'push-ups.mp4':
                frame_processed = push_ups_class.pushups_draw_yolo(frame)
                return frame_processed
            case 'flying.mp4':
                frame_processed = fly_class.fly_draw_yolo(frame)
                return frame_processed
            case 'knees.mp4':
                frame_processed = knees_class.knees_draw_yolo(frame)
                return frame_processed
    
def get_excersise_name(video):
    exw = video.split('/')
    ex = exw[-1]
    return ex



   






