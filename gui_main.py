import tkinter as tk

from gui_config import ColorPalette as colors
import gui_functions as guif



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
option_frame = guif.create_source_frame(root)

root.mainloop()