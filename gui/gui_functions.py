from gui.gui_config import Colors as c
from gui.gui_config import Padding as p
from gui.gui_config import Spacer as sp
from gui.gui_config import Text as t
from gui.gui_config import Styles as st
from yolo_processing.exercises import run_yolo

import tkinter as tk
import os
from PIL import Image, ImageTk
import cv2

selected_video = ''
selected_exercise = 0

global frame_counter
frame_counter = 0

def create_logo(frame, spacer_pady, columnspan):
    logo_label = tk.Label(frame, text="VTŠFIT", font=("Helvetica", 24, "bold"), background=c.background, foreground=c.accent)
    logo_label.grid(row=0, column=0, padx=10, pady=10, columnspan=columnspan)

    image = tk.PhotoImage(file="assets/gui_images/gui_line.png")
    image_label = tk.Label(frame, image=image, borderwidth=0, relief="flat")
    image_label.grid(row=1, column=0, columnspan=columnspan)
    
    spacer = tk.Label(frame, pady=spacer_pady, bg=c.background)
    spacer.grid(row=2, column=0, columnspan=columnspan)

#Soruce
def select_existing_video(selected_option, root, source_frame):
    global selected_video
    selected_video = 'assets/exercise_videos/existing_videos/' + selected_option.get()
    create_exercise_frame(root, source_frame)

def workout_live(selected_option, root, source_frame):
    pass

def record_new_video(root, source_frame):
    global selected_video
    selected_video = 'exercise_videos/new_videos/recorded_video.mp4'
    create_exercise_frame2(root, source_frame)

def get_existing_videos():
    folder_path = "assets/exercise_videos/existing_videos"
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

def create_source_frame(root):
    source_frame = tk.Frame(root, bg=c.background)
    source_frame.pack()
    source_frame.pack(fill=tk.BOTH, expand=True)
    create_logo(source_frame, sp.source, 1)

    options_list = get_existing_videos()
    selected_option = tk.StringVar(source_frame)
    selected_option.set("Izaberite video")
    option_menu = tk.OptionMenu(source_frame, selected_option, *options_list)

    option_menu.configure(**st.optionmenu)
    option_menu["menu"].configure(
        font=t.text,
        background=c.object,
        foreground=c.text,
        activebackground=c.object,
        activeforeground=c.accent,
        relief="solid",
    )
    option_menu.grid(row=3, column=0)

    spacer_two = tk.Label(source_frame, pady=sp.source_buttons, bg=c.background)
    spacer_two.grid(row=4, column=0)

    button_one_border = tk.Frame(source_frame, st.button_frame)
    button_one = tk.Button(button_one_border, text='Izaberi postojeći video', **st.source_button,
                        command=lambda: select_existing_video(selected_option, root, source_frame))
    button_one_border.grid(row=5, column=0, columnspan=1)
    button_one.grid(column=0, row=0)

    spacer_three = tk.Label(source_frame, pady=sp.source_buttons, bg=c.background)
    spacer_three.grid(row=6, column=0)

    button_two_border = tk.Frame(source_frame, st.button_frame)
    button_two = tk.Button(button_two_border, text='Vežbaj uživo', **st.source_button,
                        command=lambda: workout_live(selected_option, root, source_frame))
    button_two_border.grid(row=7, column=0, columnspan=1)
    button_two.grid(column=0, row=0)

    spacer_four = tk.Label(source_frame, pady=sp.source_buttons, bg=c.background)
    spacer_four.grid(row=8, column=0)

    button_three_border = tk.Frame(source_frame, st.button_frame)
    button_three = tk.Button(button_three_border, text='Snimi novi video', **st.source_button,
                            command=lambda: record_new_video(root, source_frame))
    button_three_border.grid(row=9, column=0, columnspan=1)
    button_three.grid(row=0, column=0)

#Exercise
def select_exercise(exercise, root, exercise_frame):
    global selected_exercise
    selected_exercise = exercise
    create_display_frame(root, exercise_frame)

def select_exercise2(exercise, root, exercise_frame):
    global selected_exercise
    selected_exercise = exercise
    create_record_frame(root, exercise_frame)

def create_exercise_frame(root, source_frame):
    source_frame.destroy()

    exercise_frame = tk.Frame(root, bg=c.background)
    exercise_frame.pack()
    exercise_frame.pack(fill=tk.BOTH, expand=True)
    create_logo(exercise_frame, sp.exercise, 5)

    exercises_frame = tk.Frame(exercise_frame, background=c.background)
    exercises_frame.grid(row=3, column=1, columnspan=3)
    exercise_images = []
    for i in range(1, 7):
        image_path = f"assets/gui_images/gui_exercises/gui_exercise_{i}.png"
        exercise_image = tk.PhotoImage(file=image_path)
        exercise_images.append(exercise_image)

    for i, exercise_image in enumerate(exercise_images):
        row = i // 3
        col = i % 3
        exercise_label = tk.Label(exercises_frame, image=exercise_image, border=0, relief='flat')
        exercise_label.image = exercise_image
        exercise_label.grid(row=row, column=col, padx=p.exercise, pady=p.exercise)
        exercise_label.bind("<Button-1>", lambda event, i=i: select_exercise(i, root, exercise_frame))  

def create_exercise_frame2(root, source_frame):
    source_frame.destroy()

    exercise_frame = tk.Frame(root, bg=c.background)
    exercise_frame.pack()
    exercise_frame.pack(fill=tk.BOTH, expand=True)
    create_logo(exercise_frame, sp.exercise, 5)

    exercises_frame = tk.Frame(exercise_frame, background=c.background)
    exercises_frame.grid(row=3, column=1, columnspan=3)
    exercise_images = []
    for i in range(1, 7):
        image_path = f"assets/gui_images/gui_exercises/gui_exercise_{i}.png"
        exercise_image = tk.PhotoImage(file=image_path)
        exercise_images.append(exercise_image)

    for i, exercise_image in enumerate(exercise_images):
        row = i // 3
        col = i % 3
        exercise_label = tk.Label(exercises_frame, image=exercise_image, border=0, relief='flat')
        exercise_label.image = exercise_image
        exercise_label.grid(row=row, column=col, padx=p.exercise, pady=p.exercise)
        exercise_label.bind("<Button-1>", lambda event, i=i: select_exercise2(i, root, exercise_frame))    

#Display

def create_display_frame(root, exercise_frame):
    exercise_frame.destroy()
    print(selected_video)


    display_frame = tk.Frame(root, bg=c.background)
    display_frame.pack()
    display_frame.pack(fill=tk.BOTH, expand=True)
    create_logo(display_frame, sp.display, 3)

    vertical_frame = tk.Frame(display_frame, background=c.background)
    vertical_frame.grid(row=3, column=1)

    default_image = tk.PhotoImage(file="assets/gui_images/strumf.png")
    vertical_label = tk.Label(vertical_frame, image=default_image, borderwidth=0, relief="flat")
    vertical_label.image = default_image
    vertical_label.grid(row=0, column=0)

    def update_display():
        global frame_counter

        cap = cv2.VideoCapture(selected_video)
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_counter)
        ret, frame = cap.read()
        if ret:
            run_yolo(frame, selected_exercise)
            cap.release()

            image = tk.PhotoImage(file="assets/temporary_images/display_frame.png")
            display_label = tk.Label(vertical_frame, image=image, borderwidth=0, relief="flat")
            display_label.image = image
            display_label.grid(row=0, column=0)

            frame_counter += 1
            root.after(1, update_display)
        else:
             print('End of the video')
             frame_counter = 0
             cap.release()

    play_button_border = tk.Frame(display_frame, st.button_frame)
    play_button = tk.Button(                       
                            play_button_border,
                            font = t.text,
                            background=c.object,
                            foreground= c.text,
                            activebackground= c.object,
                            activeforeground= c.accent,
                            highlightthickness= 2,
                            highlightbackground= c.accent,
                            highlightcolor="WHITE",
                            width=21,
                            height=1, 
                            border=0,
                            text='Play',
                            command=update_display                               
                            )
    play_button_border.grid(row=4,column=1, pady=10)
    play_button.grid(column=0, row=0)

#RECORD NEW VIDEO
def create_record_frame(root, exercise_frame):
    exercise_frame.destroy()

    preview_frame = tk.Frame(root, bg=c.background)
    preview_frame.pack()
    preview_frame.pack(fill=tk.BOTH, expand=True)
    create_logo(preview_frame, sp.display, 3)

    vertical_frame = tk.Frame(preview_frame, background=c.background)
    vertical_frame.grid(row=3, column=1)

    default_image = tk.PhotoImage(file="assets/gui_images/strumf.png")
    vertical_label = tk.Label(vertical_frame, image=default_image, borderwidth=0, relief="flat")
    vertical_label.image = default_image
    vertical_label.grid(row=0, column=0)
    
    frames = []
    global selected_video
    selected_video = 'assets/exercise_videos/new_videos/recorded_video.mp4'

    co = 0
    cap = cv2.VideoCapture(0)   
    def update_preview():
        nonlocal co
        nonlocal frames
        nonlocal root
        nonlocal preview_frame

        if (co < 100): #30 FRAMES * 10 SECONDS
            ret, frame = cap.read()
            frames.append(frame)

            frame = cv2.resize(frame, (410, 740))
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(frame_rgb)
            tk_image = ImageTk.PhotoImage(pil_image)
            
            preview_label = tk.Label(vertical_frame, image=tk_image, borderwidth=0, relief="flat")
            preview_label.config(image=tk_image)
            preview_label.image = tk_image
            preview_label.grid(row=0, column=0)
    
            co += 1 
            root.after(1, update_preview)
        else: 
            print('End of the video')
            co = 0
            cap.release()
            image = tk.PhotoImage(file="assets/gui_images/strumf.png")
            
            video_name = 'assets/exercise_videos/new_videos/recorded_video.mp4'
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(video_name, fourcc, 30, (420, 750))
        
            for f in frames:
                print('cat')
                resized_image = cv2.resize(f, (420, 750))
                out.write(resized_image)
            out.release()
            create_display_frame(root, preview_frame)

    play_button_border = tk.Frame(preview_frame, st.button_frame)
    play_button = tk.Button(                       
                            play_button_border,
                            font = t.text,
                            background=c.object,
                            foreground= c.text,
                            activebackground= c.object,
                            activeforeground= c.accent,
                            highlightthickness= 2,
                            highlightbackground= c.accent,
                            highlightcolor="WHITE",
                            width=21,
                            height=1, 
                            border=0,
                            text='Record',
                            command=update_preview                               
                            )
    play_button_border.grid(row=4,column=1, pady=10)
    play_button.grid(column=0, row=0)



#Other
def close_window(root, event):
    root.destroy()