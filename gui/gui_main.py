import tkinter as tk
from gui import gui_functions

def run_gui():
    root = tk.Tk()
    root.title("VTSFIT")
    root.iconbitmap("assets/gui_images/gui_icon.ico")
    root.state('zoomed')
    root.bind("<Escape>", lambda event: gui_functions.close_window(root, event))
    gui_functions.create_source_frame(root)

    root.mainloop()

if __name__ == "__main__":
    run_gui()
