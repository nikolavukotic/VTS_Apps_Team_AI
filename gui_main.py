import tkinter as tk
import gui_functions

root = tk.Tk()
root.title("VTSFIT")
root.iconbitmap("gui_images/gui_icon.ico")
root.state('zoomed')
root.bind("<Escape>", lambda event: gui_functions.close_window(root, event))
gui_functions.create_source_frame(root)

root.mainloop()