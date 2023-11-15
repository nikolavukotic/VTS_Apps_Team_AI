import tkinter as tk
from PIL import Image, ImageTk
import cv2

from testing import test_functions
from yolo_processing.exercises import run_yolo

#To run a test:
#   1. Add "from testing.test_main import run_test" at the top for main.py
#   2. Call the function run_test() in main.py
#   3. Delete run_gui() in main.py

frame_counter = 0
selected_video = 'assets/exercise_videos/existing_videos/cucanj.mov'
selected_exercise = 0

def run_test():
    root = tk.Tk()
    root.title("VTSFIT TEST")
    root.iconbitmap("assets/gui_images/gui_icon.ico")
    root.state('zoomed')

    button = tk.Button(root, text="Test function 1!", command=lambda: test_functions.test_function_1())
    button.pack()

    image = tk.PhotoImage(file="assets/temporary_images/display_frame.png")
    display_label = tk.Label(root, image=image, borderwidth=0, relief="flat")
    display_label.image = image
    display_label.pack()

    def update():
        print("This update loop is used for testing!")
        global frame_counter
        global selected_video
        global selected_exercise

        cap = cv2.VideoCapture(selected_video)
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_counter)
        ret, frame = cap.read()
        if ret:
            run_yolo(frame, selected_exercise)
            #Your functions goes here!
            test_functions.test_function_2()

            cap.release()
            image = tk.PhotoImage(file="assets/temporary_images/display_frame.png")
            display_label.config(image=image)
            display_label.image = image
            display_label.pack()

            frame_counter += 1
            root.after(1, update)
        else:
            print('End of the video')
            frame_counter = 0
            cap.release() 

    play_button = tk.Button(root, text="PLAY!", command=lambda: update())
    play_button.pack()    

    root.mainloop()

if __name__ == "__main__":
    run_test()