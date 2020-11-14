import threading
import time
import tkinter as tk


def capture_after_10_secs():
    print("Will take a picture after 10 seconds")
    start_time = threading.Timer(10, capture)
    start_time.start()


def capture_after_15_secs():
    print("Will take a picture after 15 seconds")
    start_time = threading.Timer(15, capture)
    start_time.start()


def capture():
    print("Taking picture...")
    filename = "/home/pi/Pictures/image_" + str(int(time.time())) + ".jpg"
    print("Saved image as " + filename)


if __name__ == '__main__':
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()
    capture_btn = tk.Button(frame, text="Capture", height=10, width=30, command=capture)
    capture_btn.pack(side=tk.TOP)

    capture_after_10_secs_btn = tk.Button(frame, text="Capture after 10 secs", height=10, width=30,
                                          command=capture_after_10_secs)
    capture_after_10_secs_btn.pack(side=tk.TOP)

    capture_after_15_secs_btn = tk.Button(frame, text="Capture after 15 secs", height=10, width=30,
                                          command=capture_after_15_secs)
    capture_after_15_secs_btn.pack(side=tk.TOP)

    quit_btn = tk.Button(frame, text="QUIT", fg="red", height=10, width=30, command=quit)
    quit_btn.pack(side=tk.BOTTOM)

    root.mainloop()
