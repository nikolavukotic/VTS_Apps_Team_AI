import tkinter as tk
import cv2
from gui_config import ColorPalette as colors
import gui_functions as guif
import utils
from PIL import Image as im, ImageTk

#Root
root = tk.Tk()
root.title("VTSFIT")
root.iconbitmap("gui_images/gui_icon.ico")
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

##Main Frame
#main_frame = tk.Frame(root, bg=colors.c1, pady=40)
#main_frame.pack(fill=tk.BOTH, expand=True)
#main_frame.columnconfigure(0, weight=1)
##Logo
#logo_label = tk.Label(main_frame, text="VTSFIT", font=("Helvetica", 24), background=colors.c1, foreground=colors.c2)
#logo_label.grid(row=0, column=0, padx=10, pady=10)
##Izaberi video
#folder_path = "videoSnimci"
#options_list = utils.get_video_file_names(folder_path)
#
#selected_option = tk.StringVar(main_frame) 
#selected_option.set("Izaberite video")
#option_menu = tk.OptionMenu(main_frame, selected_option, *options_list)
#optionmenu_style = {
#    "font": ('Arial', 16, 'bold'),
#    "background": colors.c2,
#    "foreground": colors.c4,
#    "activebackground": colors.c3,
#    "activeforeground": colors.c4,
#    "highlightthickness": 2,
#    "highlightbackground": colors.c2,
#    "highlightcolor": "WHITE",
#    "width": 12,
#    "border": 0,
#}
#option_menu.configure(**optionmenu_style)
#option_menu["menu"].configure(
#                            font = ('Arial', 16, 'bold'),
#                            background=colors.c2,
#                            foreground= colors.c4,
#                            activebackground= colors.c3,
#                            activeforeground= colors.c4,
#                            relief = "solid"
#)
#option_menu.grid(row=1, column=0)
##temp
#image = im.open("strumf.png")
#photo = ImageTk.PhotoImage(image)
#image_label = tk.Label(main_frame, image=photo, bd=0)
#image_label.grid(row=1, column=1, rowspan=20)
#
##Option Frame   
#
option_frame = guif.create_source_frame(root)
#
#def get_video():
#    video = ''
#    video = 'videoSnimci/' + selected_option.get()
#    return str(video)

#video & excersise
v = guif.selected_video
e = guif.selected_exercise

# Update funkcija
br=0
def update():
        global br
        video = get_video()
        print(v)
        ex = utils.get_excersise_name(video)

        cap = cv2.VideoCapture(video)
        cap.set(cv2.CAP_PROP_POS_FRAMES, br)
        ret, frame = cap.read()
        if ret:
            frame_processed = utils.process_frame(frame,ex)

            new_image=utils.resize_frame(frame_processed)
            
            cap.release()

            updated_photo = ImageTk.PhotoImage(new_image)
            image_label.configure(image=updated_photo)
            image_label.image = updated_photo

            br=br+1
            root.after(1, update)
        else:
             print('frame not found')
             br = 0
             strumf=im.open('strumf.png')
             updated_photo = ImageTk.PhotoImage(strumf)
             image_label.configure(image=updated_photo)
             image_label.image = updated_photo

def update_loop_button():
    update()

def temp():
    pass


root.mainloop()