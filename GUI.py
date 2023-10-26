import tkinter as tk
import cv2
from colors import ColorPalette as colors
import utils
from tkinter import PhotoImage
from PIL import Image as im, ImageTk
import cucanj
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

def get_video():
    video = ''
    video = 'videoSnimci/' + selected_option.get()
    print(video)
    return str(video)

# Button commands
def command_one():
    utils.cucanj(get_video())

def command_two():
    utils.letenje(get_video())

def command_three():
    utils.biceps(get_video())

def command_four():
    utils.trbusnjaci(get_video())

def command_five():
    utils.sklekovi(get_video())

def command_six():
    utils.kolena(get_video())

#image = PhotoImage(file="strumf.png")
#image_label = tk.Label(main_frame, image=image)
#image_label.grid(row=1, column=1, columnspan=7)
image = im.open("strumf.png")
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=photo)
image_label.pack()



def frame_generator(video,frame_number):
   
   cap = cv2.VideoCapture(video)
   cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
   ret, frame = cap.read()  # Čitanje frejma sa kamere
   print(frame)
   if ret:
    cv2.imwrite('strumf.png', frame)
    print('27th frame saved as cat.png')
   else:
    print('Error: Frame not found')

   cap.release()
   return frame
          
def mrs(temp):
    video_path = 'videoSnimci\squatTrim1.mp4'

# Initialize the video capture object
    cap = cv2.VideoCapture(video_path)

# Get the frame at the 27th position (0-based index)
    frame_number = temp

# Set the frame position
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

# Read the frame
    ret, frame = cap.read()

# Check if the frame was read successfully
    if ret:
    # Save the frame as "cat.png"
        cv2.imwrite('strumf.png', frame)
        print('27th frame saved as cat.png')
    else:
        print('Error: Frame not found')

# Release the video capture object
    cap.release()
   

br = 1
def update_image():
    video="videoSnimci/squadtime1.mp4"
    global br
    print("test 1")
    frame = frame_generator(video,br)

    
    
    #cucanj.test(frame)

    # Load the updated image (you can replace this with your method to generate the new image)
    updated_image = im.open("strumf.png")  # Replace with your method to update the image
    updated_photo = ImageTk.PhotoImage(updated_image)

    # Update the label with the new image
    image_label.configure(image=updated_photo)
    image_label.image = updated_photo

    print("test 2")
    print(br)
    mrs(br)
    br=br+1

    root.after(1, update_image)
    


def temp_one():
    update_image();

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
                            command=command_one                                   
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
                            command=command_two
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
                            command=command_three
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
                            command=command_four
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
                            command=command_five
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
                            command=command_six
)

button_six_boarder.grid(row=7, column=0, columnspan=1)
button_six.grid(column=0, row=0)

button = tk.Button(main_frame, text="Click Me", command=temp_one)
button.grid(row=7, column=2, columnspan=1)


root.mainloop()