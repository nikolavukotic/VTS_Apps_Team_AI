import tkinter as tk
from colors import ColorPalette as colors
import utils

# Create the main window
root = tk.Tk()
root.title("VTSFIT")
root.geometry("350x500")
root.resizable(width=False, height=False)

# Create the main frame
main_frame = tk.Frame(root, bg=colors.c1, pady=40)
main_frame.pack(fill=tk.BOTH, expand=True)
main_frame.columnconfigure(0, weight=1)

# Create a label for the larger text (logo)
logo_label = tk.Label(main_frame, text="VTSFIT", font=("Helvetica", 24), background=colors.c1, foreground=colors.c2)
logo_label.grid(row=0, column=0, padx=10, pady=10)

video = "videoSnimci/squatTrim.mp4"

# Button one

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
                            text='Čučanj',
                            command=lambda:utils.cucanjj(video)
                                    
                            )

button_one_border.grid(row=1, column=0, columnspan=1)
button_one.grid(column=0, row=0)

# Button Two

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
                            command=lambda:utils.letenje(video)
)

button_two_border.grid(row=2, column=0, columnspan=1)
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
                            text='temp',
                            command=lambda:utils.bicepsUspravnoStajanje(video)
                            )

button_three_border.grid(row=3, column=0, columnspan=1)
button_three.grid(column=0, row=0)

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
                            text='temp',
                            command=utils.trbusnjaci
)


button_four_boarder.grid(row=4, column=0, columnspan=1)
button_four.grid(column=0, row=0)

root.mainloop()