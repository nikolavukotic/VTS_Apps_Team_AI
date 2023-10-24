import tkinter as tk
import cv2

from colors import ColorPalette as colors
import utils

root = tk.Tk()
root.title("VTSFIT")
root.geometry("450x750")
root.resizable(width=True, height=True)

main_frame = tk.Frame(root, bg=colors.c1, pady=40)
main_frame.pack(fill=tk.BOTH, expand=True)
main_frame.columnconfigure(0, weight=1)

logo_label = tk.Label(main_frame, text="VTSFIT", font=("Helvetica", 24), background=colors.c1, foreground=colors.c2)
logo_label.grid(row=0, column=0, padx=10, pady=10)

folder_path = 'C:/Users/Korisnik/Desktop/Projekti/Py PROJEKAT/videoSnimci'
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

submit_button = tk.Button(root, text='Submit', command=get_video()) 
submit_button.pack() 

# Button commands
def command_one():
    video = get_video()
    utils.empty_function_1(video)

def command_two():
    video = get_video()
    utils.empty_function_2(video)

def command_three():
    video = get_video()
    utils.empty_function_3(video)

def command_four():
    video = get_video()
    utils.empty_function_4(video)

def command_five():
    video = get_video()
    utils.empty_function_5(video)

def command_six():
    video = get_video()
    utils.empty_function_6(video)

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

root.mainloop()