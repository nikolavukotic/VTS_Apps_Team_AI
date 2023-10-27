import tkinter as tk
import cv2
from colors import ColorPalette as colors
import utils
from tkinter import PhotoImage
from PIL import Image as im, ImageTk
import cucanj as squat_class
import kolena as knees_class
import letenje as fly_class
import sklekovi as push_ups_class
import trbusnjaci as abs_class
import biceps as biceps_class
import os
import numpy as np



root = tk.Tk()
root.title("VTSFIT")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
screen_resolution = str(screen_width) + 'x' + str(screen_height)
root.geometry(screen_resolution)
root.state('zoomed')
root.resizable(width=True, height=True)

def close_window(event):
    root.destroy()
    print("mrs")
root.bind("<Escape>", close_window)

main_frame = tk.Frame(root, bg=colors.c1, pady=40)
main_frame.pack(fill=tk.BOTH, expand=True)
main_frame.columnconfigure(0, weight=1)

logo_label = tk.Label(main_frame, text="VTSFIT", font=("Helvetica", 24), background=colors.c1, foreground=colors.c2)
logo_label.grid(row=0, column=0, padx=10, pady=10)

folder_path = "videoSnimci"
options_list = utils.get_video_file_names(folder_path)
selected_option = tk.StringVar(main_frame) 
selected_option.set("Izaberite video")
option_menu = tk.OptionMenu(main_frame, selected_option, *options_list)
optionmenu_style = {
    "font": ('Arial', 16, 'bold'),
    "background": colors.c2,
    "foreground": colors.c4,
    "activebackground": colors.c3,
    "activeforeground": colors.c4,
    "highlightthickness": 2,
    "highlightbackground": colors.c2,
    "highlightcolor": "WHITE",
    "width": 12,
    "border": 0,
}

option_menu.configure(**optionmenu_style)
option_menu["menu"].configure(
                            font = ('Arial', 16, 'bold'),
                            background=colors.c2,
                            foreground= colors.c4,
                            activebackground= colors.c3,
                            activeforeground= colors.c4,
                            relief = "solid"
)
option_menu.grid(row=1, column=0)

image = im.open("strumf.png")
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(main_frame, image=photo, bd=0)
image_label.grid(row=1, column=1, rowspan=20)

def get_video():
    video = ''
    video = 'videoSnimci/' + selected_option.get()
    return str(video)

br=0
x = 69

def update():
        global br
        global x
        video = get_video()

        exw = video.split('/')
        ex = exw[-1]
        cap = cv2.VideoCapture(video)
        cap.set(cv2.CAP_PROP_POS_FRAMES, br)
        ret, frame = cap.read()

        match ex:
            case 'squatTrim.mp4':
                sredjen = squat_class.squat_draw_yolo(frame)
            case 'abs.mp4':
                sredjen = abs_class.abs_draw_yolo(frame)
            case 'biceps.mp4':
                sredjen = biceps_class.biceps_draw_yolo(frame)
            case 'push-ups.mp4':
                sredjen = push_ups_class.pushups_draw_yolo(frame)
            case 'flying.mp4':
                sredjen = fly_class.fly_draw_yolo(frame)
            case 'knees.mp4':
                sredjen = knees_class.knees_draw_yolo(frame)

        height, width, channels = sredjen.shape
        if ret:
            if(width>height):
                desired_width = 700
                desired_height = 400
            else:
                desired_width = 460
                desired_height = 720
            new_image = cv2.resize(sredjen, (desired_width, desired_height))
            new_image = im.fromarray(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
        else:
            print('Error: Frame not found')
            x=96
        cap.release()
        
        updated_photo = ImageTk.PhotoImage(new_image)
        image_label.configure(image=updated_photo)
        image_label.image = updated_photo

        if(x == 69):
            br=br+1
            root.after(1, update)
            x=69

def update_noYOLO():
        global br
        global x
        video = get_video()

        cap = cv2.VideoCapture(video)
        cap.set(cv2.CAP_PROP_POS_FRAMES, br)
        ret, frame = cap.read()
        
        #sredjen = cucanj.squat_draw_yolo(frame)
        
        
        
        if ret:
            desired_width = 430
            desired_height = 760
            new_image = cv2.resize(frame, (desired_width, desired_height))
            new_image = im.fromarray(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
            print(type(new_image))
        else:
            print('Error: Frame not found')
            x=96
        cap.release()
        
        updated_image = new_image
        updated_photo = ImageTk.PhotoImage(updated_image)
        image_label.configure(image=updated_photo)
        image_label.image = updated_photo

        if(x == 69):
            br=br+1
            root.after(1, update_noYOLO)
            x=69

def update_loop_button():
    update()

def temp():
    pass

# Buttons
button_one_border = tk.Frame(
                        main_frame, 
                        highlightbackground = colors.c1,
                        highlightthickness = 10,
                        background=colors.c2,
                        border=2)

button_one = tk.Button(                       
                            button_one_border,
                            font = ('Arial', 16, 'bold'),
                            background=colors.c2,
                            foreground= colors.c4,
                            activebackground= colors.c3,
                            activeforeground= colors.c4,
                            highlightthickness= 2,
                            highlightbackground= colors.c2,
                            highlightcolor="WHITE",
                            width=13,
                            height=2, 
                            border=0,
                            text='Cucanj',
                            command=temp()                                
                            )

button_one_border.grid(row=2, column=0, columnspan=1)
button_one.grid(column=0, row=0)

button_two_border = tk.Frame(
                        main_frame, 
                        highlightbackground = colors.c1,
                        highlightthickness = 10,
                        background=colors.c2,
                        border=2)

button_two = tk.Button(                       
                            button_two_border,
                            font = ('Arial', 16, 'bold'),
                            background=colors.c1,
                            foreground= colors.c2,
                            activebackground= colors.c3,
                            activeforeground= colors.c4,
                            highlightthickness= 2,
                            highlightbackground= colors.c2,
                            highlightcolor="WHITE",
                            width=13,
                            height=2, 
                            border=0,
                            text='Letenje',
                            command=temp()   
)

button_two_border.grid(row=3, column=0, columnspan=1)
button_two.grid(column=0, row=0)

button_three_border = tk.Frame(
                        main_frame, 
                        highlightbackground = colors.c1,
                        highlightthickness = 10,
                        background=colors.c2,
                        border=2)

button_three = tk.Button(                       
                            button_three_border,
                            font = ('Arial', 16, 'bold'),
                            background=colors.c2,
                            foreground= colors.c4,
                            activebackground= colors.c3,
                            activeforeground= colors.c4,
                            highlightthickness= 2,
                            highlightbackground= colors.c2,
                            highlightcolor="WHITE",
                            width=13,
                            height=2, 
                            border=0,
                            text='Biceps',
                            command=temp()   
                            )

button_three_border.grid(row=4, column=0, columnspan=1)
button_three.grid(row=0, column=0)

button_four_boarder = tk.Frame(
                        main_frame, 
                        highlightbackground = colors.c1,
                        highlightthickness = 10,
                        background=colors.c2,
                        border=2)

button_four = tk.Button(                       
                            button_four_boarder,
                            font = ('Arial', 16, 'bold'),
                            background=colors.c1,
                            foreground= colors.c2,
                            activebackground= colors.c3,
                            activeforeground= colors.c4,
                            highlightthickness= 2,
                            highlightbackground= colors.c2,
                            highlightcolor="WHITE",
                            width=13,
                            height=2, 
                            border=0,
                            text='Trbusnjaci',
                            command=temp()   
)

button_four_boarder.grid(row=5, column=0, columnspan=1)
button_four.grid(column=0, row=0)

button_five_border = tk.Frame(
                        main_frame, 
                        highlightbackground = colors.c1,
                        highlightthickness = 10,
                        background=colors.c2,
                        border=2)

button_five = tk.Button(                       
                            button_five_border,
                            font = ('Arial', 16, 'bold'),
                            background=colors.c2,
                            foreground= colors.c4,
                            activebackground= colors.c3,
                            activeforeground= colors.c4,
                            highlightthickness= 2,
                            highlightbackground= colors.c2,
                            highlightcolor="WHITE",
                            width=13,
                            height=2, 
                            border=0,
                            text='Sklekovi',
                            command=temp()   
                            )

button_five_border.grid(row=6, column=0, columnspan=1)
button_five.grid(row=0, column=0)

button_six_boarder = tk.Frame(
                        main_frame, 
                        highlightbackground = colors.c1,
                        highlightthickness = 10,
                        background=colors.c2,
                        border=2)

button_six = tk.Button(                       
                            button_six_boarder,
                            font = ('Arial', 16, 'bold'),
                            background=colors.c1,
                            foreground= colors.c2,
                            activebackground= colors.c3,
                            activeforeground= colors.c4,
                            highlightthickness= 2,
                            highlightbackground= colors.c2,
                            highlightcolor="WHITE",
                            width=13,
                            height=2, 
                            border=0,
                            text='Kolena',
                            command=temp()   
)

button_six_boarder.grid(row=7, column=0, columnspan=1)
button_six.grid(column=0, row=0)

button = tk.Button(main_frame, text="Click Me", command=update_loop_button)
button.grid(row=7, column=2, columnspan=1)

print('mrsbrate')
root.mainloop()