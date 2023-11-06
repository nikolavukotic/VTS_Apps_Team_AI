from gui_config import ColorPalette as c
from gui_config import Size as s
import utils
import tkinter as tk
from tkinter import PhotoImage
import cv2


#globals
selected_video = ''
selected_exercise = 0
frame_counter = 0

#SOURCE
#Existing video
def select_existing_video(selected_option, root, source_frame):
    global selected_video
    selected_video = 'videoSnimci/' + selected_option.get()
    create_exercise_frame(root, source_frame)

#Live
def workout_live():
    pass

#Record new video
def record_new_video():
    pass 

def create_source_frame(root):

    source_frame = tk.Frame(root, bg=c.background)
    source_frame.pack()
    source_frame.pack(fill=tk.BOTH, expand=True)

    logo_label = tk.Label(source_frame, text="VTŠFIT", font=("Helvetica", 24, "bold"), background=c.background, foreground=c.accent)
    logo_label.grid(row=0, column=0, padx=10, pady=10)
    image = tk.PhotoImage(file="gui_images/gui_line.png")
    image_label = tk.Label(source_frame, image=image, borderwidth=0, relief="flat")
    image_label.grid(row=1, column=0)
    spacer_one = tk.Label(source_frame, pady=s.big, bg=c.background)
    spacer_one.grid(row=2, column=0)

    #options
    folder_path = "videoSnimci"
    options_list = utils.get_video_file_names(folder_path)
    
    selected_option = tk.StringVar(source_frame)
    selected_option.set("Izaberite video")
    option_menu = tk.OptionMenu(source_frame, selected_option, *options_list)
    optionmenu_style = {
        "font": ("Arial", s.font, "bold"),
        "background": c.object,
        "foreground": c.text,
        "activebackground": c.object,
        "activeforeground": c.accent,
        "highlightthickness": 5,
        "highlightbackground": c.accent,
        "highlightcolor": "WHITE",
        "width": 24,
        "border": 0,
    }
    option_menu.configure(**optionmenu_style)
    option_menu["menu"].configure(
        font=("Arial", s.font, "bold"),
        background=c.object,
        foreground=c.text,
        activebackground=c.object,
        activeforeground=c.accent,
        relief="solid",
    )
    option_menu.grid(row=3, column=0)

    #Spacer two 40 / 2 = 20
    spacer_two = tk.Label(source_frame, pady=s.small, bg=c.background)
    spacer_two.grid(row=4, column=0)

    #Button one
    button_one_border = tk.Frame(
                        source_frame, 
                        highlightbackground = c.accent,
                        highlightthickness = 5,
                        background=c.accent,
                        border=0
                        )
    button_one = tk.Button(                       
                                button_one_border,
                                font = ('Arial', s.font, 'bold'),
                                background=c.object,
                                foreground= c.text,
                                activebackground= c.object,
                                activeforeground= c.accent,
                                highlightthickness= 2,
                                highlightbackground= c.accent,
                                highlightcolor="WHITE",
                                width=23,
                                height=2, 
                                border=0,
                                text='Izaberi postojeći video',
                                command=lambda: select_existing_video(selected_option, root, source_frame)                               
                                )
    button_one_border.grid(row=5, column=0, columnspan=1)
    button_one.grid(column=0, row=0)

    #Spacer three 40 / 2 = 20
    spacer_three = tk.Label(source_frame, pady=s.small, bg=c.background)
    spacer_three.grid(row=6, column=0)

    #Button two
    button_two_border = tk.Frame(
                        source_frame, 
                        highlightbackground = c.accent,
                        highlightthickness = 5,
                        background=c.accent,
                        border=0
                        )
    button_two = tk.Button(                       
                                button_two_border,
                                font = ('Arial', s.font, 'bold'),
                                background=c.object,
                                foreground= c.text,
                                activebackground= c.object,
                                activeforeground= c.accent,
                                highlightthickness= 2,
                                highlightbackground= c.accent,
                                highlightcolor="WHITE",
                                width=23,
                                height=2, 
                                border=0,
                                text='Vežbaj uživo',
                                command=workout_live()   
    )
    button_two_border.grid(row=7, column=0, columnspan=1)
    button_two.grid(column=0, row=0)

    #Spacer four 40 / 2 = 20
    spacer_four = tk.Label(source_frame, pady=s.small, bg=c.background)
    spacer_four.grid(row=8, column=0)

    #Button three
    button_three_border = tk.Frame(
                        source_frame, 
                        highlightbackground = c.accent,
                        highlightthickness = 5,
                        background=c.accent,
                        border=0
                        )
    button_three = tk.Button(                       
                                button_three_border,
                                font = ('Arial', s.font, 'bold'),
                                background=c.object,
                                foreground= c.text,
                                activebackground= c.object,
                                activeforeground= c.accent,
                                highlightthickness= 2,
                                highlightbackground= c.accent,
                                highlightcolor="WHITE",
                                width=23,
                                height=2, 
                                border=0,
                                text='Snimi novi video',
                                command=record_new_video()   
                                )
    button_three_border.grid(row=9, column=0, columnspan=1)
    button_three.grid(row=0, column=0)


#EXERCISE

def select_exercise(exercise, root, exercise_frame):
    global selected_exercise
    selected_exercise = exercise
    create_display_frame(root, exercise_frame)

#def update_display123(vertical_label, root):
#    global frame_counter
#    global selected_video
#    global selected_exercise
#
#    temp1 = vertical_label
#    temp2 = root
#    print(type(vertical_label))
#    
#
#    cap = cv2.VideoCapture(selected_video)
#    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_counter)
#    ret, frame = cap.read()
#    if ret:
#        processed_frame = utils.process_frame2(frame, selected_exercise)
#        resized_frame=utils.resize_frame(processed_frame)
#
#        cap.release()
#        updated_display = tk.PhotoImage(resized_frame)
#        vertical_label.configure(image=updated_display)
#        vertical_label.image = updated_display
#        frame_counter = frame_counter + 1
#
#        root.after(1, lambda: update_display(temp1, temp2))
#    else:
#         print('End of the video')
#         frame_counter = 0
#         default_photo = tk.PhotoImage("gui_images/strumf.png")
#         vertical_label.configure(image=default_photo)
#         vertical_label.image = default_photo


def create_exercise_frame(root, source_frame):
    source_frame.destroy()

    exercise_frame = tk.Frame(root, bg=c.background)
    exercise_frame.pack()
    exercise_frame.pack(fill=tk.BOTH, expand=True)

    logo_label = tk.Label(exercise_frame, text="VTŠFIT", font=("Helvetica", 24, "bold"), background=c.background, foreground=c.accent)
    logo_label.grid(row=0, column=0, padx=10, pady=10, columnspan=5)
    image = tk.PhotoImage(file="gui_images/gui_line.png")
    image_label = tk.Label(exercise_frame, image=image, borderwidth=0, relief="flat")
    image_label.grid(row=1, column=0, columnspan=5)
    spacer_one = tk.Label(exercise_frame, pady=s.medium, bg=c.background)
    spacer_one.grid(row=2, column=0, columnspan=5)

    image_frame = tk.Frame(exercise_frame, background=c.background)
    image_frame.grid(row=3, column=1, columnspan=3)
    #biceps, Cucanj
    exercise_1 = tk.PhotoImage(file="gui_images/gui_exercises/gui_exercise_1.png")
    exercise_2 = tk.PhotoImage(file="gui_images/gui_exercises/gui_exercise_2.png")
    #kolena(Mrtvo), Letenje
    exercise_3 = tk.PhotoImage(file="gui_images/gui_exercises/gui_exercise_3.png")
    exercise_4 = tk.PhotoImage(file="gui_images/gui_exercises/gui_exercise_4.png")
    #sklekovi, trbusnjaci
    exercise_5 = tk.PhotoImage(file="gui_images/gui_exercises/gui_exercise_5.png")
    exercise_6 = tk.PhotoImage(file="gui_images/gui_exercises/gui_exercise_6.png")

    exercise_label_1 = tk.Label(image_frame, image=exercise_1, border=0, relief='flat')
    exercise_label_1.image = exercise_1
    exercise_label_1.grid(row=0, column=0, padx=s.padding, pady=s.padding)
    exercise_label_1.bind("<Button-1>", lambda event: select_exercise(0, root, exercise_frame))

    exercise_label_2 = tk.Label(image_frame, image=exercise_2, border=0, relief='flat')
    exercise_label_2.image = exercise_2
    exercise_label_2.grid(row=1, column=0, padx=s.padding, pady=s.padding)
    exercise_label_2.bind("<Button-1>", lambda event: select_exercise(1, root, exercise_frame))    

    exercise_label_3 = tk.Label(image_frame, image=exercise_3, border=0, relief='flat')
    exercise_label_3.image = exercise_3
    exercise_label_3.grid(row=0, column=1, padx=s.padding, pady=s.padding)
    exercise_label_3.bind("<Button-1>", lambda event: select_exercise(2, root, exercise_frame))

    exercise_label_4 = tk.Label(image_frame, image=exercise_4, border=0, relief='flat')
    exercise_label_4.image = exercise_4
    exercise_label_4.grid(row=1, column=1, padx=s.padding, pady=s.padding)    
    exercise_label_4.bind("<Button-1>", lambda event: select_exercise(3, root, exercise_frame))

    exercise_label_5 = tk.Label(image_frame, image=exercise_5, border=0, relief='flat')
    exercise_label_5.image = exercise_5
    exercise_label_5.grid(row=0, column=2, padx=s.padding, pady=s.padding)
    exercise_label_5.bind("<Button-1>", lambda event: select_exercise(4, root, exercise_frame))

    exercise_label_6 = tk.Label(image_frame, image=exercise_6, border=0, relief='flat')
    exercise_label_6.image = exercise_6
    exercise_label_6.grid(row=1, column=2, padx=s.padding, pady=s.padding)
    exercise_label_6.bind("<Button-1>", lambda event: select_exercise(5, root, exercise_frame))

def create_display_frame(root, exercise_frame):
    exercise_frame.destroy()

    display_frame = tk.Frame(root, bg=c.background)
    display_frame.pack()
    display_frame.pack(fill=tk.BOTH, expand=True)

    logo_label = tk.Label(display_frame, text="VTŠFIT", font=("Helvetica", 24, "bold"), background=c.background, foreground=c.accent)
    logo_label.grid(row=0, column=0, padx=10, pady=10, columnspan=3)
    image = tk.PhotoImage(file="gui_images/gui_line.png")
    vertical_label = tk.Label(display_frame, image=image, borderwidth=0, relief="flat")
    vertical_label.grid(row=1, column=0, columnspan=3)
    spacer_one = tk.Label(display_frame, pady=s.medium, bg=c.background)
    spacer_one.grid(row=2, column=0, columnspan=3)


    vertical_frame = tk.Frame(display_frame, background=c.background)
    vertical_frame.grid(row=3, column=1)

    image = tk.PhotoImage(file="gui_images/strumf.png")
    vertical_label = tk.Label(vertical_frame, image=image, borderwidth=0, relief="flat")
    vertical_label.image = image
    vertical_label.grid(row=0, column=0)

    #UPDATE GOES HERE

    def update_display():
        global frame_counter
        global selected_video
        global selected_exercise

        cap = cv2.VideoCapture(selected_video)
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_counter)
        ret, frame = cap.read()
        if ret:
            processed_frame = utils.process_frame2(frame, selected_exercise)

            utils.resize_frame(processed_frame)
            cap.release()

            image = tk.PhotoImage(file="gui_images/temp.png")
            cats_label = tk.Label(vertical_frame, image=image, borderwidth=0, relief="flat")
            cats_label.image = image
            cats_label.grid(row=0, column=0)

            frame_counter = frame_counter + 1

            root.after(1, update_display)
        else:
             print('End of the video')
             frame_counter = 0
             default_photo = tk.PhotoImage("gui_images/strumf.png")
             vertical_label.configure(image=default_photo)
             vertical_label.image = default_photo      
             cap.release()
    button = tk.Button(display_frame, text="Click Me", command=update_display)
    button.grid(row=4,column=1)

    #image = tk.PhotoImage(file="gui_images/temp.png")
    #vertical_label = tk.Label(display_frame, image=image, borderwidth=0, relief="flat")
    #vertical_label.image = image
    #vertical_label.grid(row=3, column=0)

    #image = tk.PhotoImage(file="gui_images/tempp.png")
    #vertical_label = tk.Label(display_frame, image=image, borderwidth=0, relief="flat")
    #vertical_label.image = image
    #vertical_label.grid(row=3, column=2)
    