import threading
import time
import tkinter as tk
from picamera import PiCamera


the_camera = PiCamera()
base_filename = "/home/pi/Pictures/image_"


def setup_camera(the_camera):
    the_camera.brightness = 50
    the_camera.sharpness = 0
    the_camera.contrast = 0
    the_camera.saturation = 0
    the_camera.iso = 0
    the_camera.exposure_compensation = 0
    the_camera.exposure_mode = 'auto'
    the_camera.meter_mode = 'average'
    the_camera.awb_mode = 'auto'
    the_camera.rotation = 270
    the_camera.hflip = False
    the_camera.vflip = False
    the_camera.crop = (0.0, 0.0, 1.0, 1.0)
    the_camera.resolution = (640, 480)
    the_camera.image_denoise = False
    the_camera.exif_tags['IFD0.Copyright'] = 'Copyright (c) 2020 NFS Industries'
    the_camera.exif_tags['IFD0.Model'] = 'NatanCam Model 1'
    # you may need to increase gpu_mem in /boot/config.txt to achieve full resolution with the Camera Module v2.


def start_preview(the_camera):
    the_camera.resolution = (500, 280)
    # Set up the preview. Here we're using the return value of start_preview
    # but you can specify these values as arguments to start_preview too
    preview = the_camera.start_preview()
    preview.fullscreen = False
    preview.window = (0, 180, 500, 280)
    preview.alpha = 255 


def capture_after_10_secs():
    print("Will take a picture after 10 seconds")
    start_time = threading.Timer(10, capture)
    start_time.start()


def capture_after_15_secs():
    print("Will take a picture after 15 seconds")
    start_time = threading.Timer(15, capture)
    start_time.start()


def capture():
    the_camera.stop_preview()
    the_camera.resolution = (4056, 3040)
    print("Taking picture...")
    filename = base_filename + str(int(time.time())) + ".jpg"
    the_camera.capture(filename)
    print("Saved image as " + filename)
    start_preview(the_camera)


if __name__ == '__main__':
    setup_camera(the_camera)
    root = tk.Tk()
    root.geometry("750x100+0+0")
    frame = tk.Frame(root)
    frame.pack()
    capture_btn = tk.Button(frame, text="Capture", height=5, width=20, command=capture)
    capture_btn.pack(side=tk.LEFT)

    capture_after_10_secs_btn = tk.Button(frame, text="Capture after 10 secs", height=5, width=20,
                                          command=capture_after_10_secs)
    capture_after_10_secs_btn.pack(side=tk.LEFT)

    capture_after_15_secs_btn = tk.Button(frame, text="Capture after 15 secs", height=5, width=20,
                                          command=capture_after_15_secs)
    capture_after_15_secs_btn.pack(side=tk.LEFT)

    quit_btn = tk.Button(frame, text="QUIT", fg="red", height=5, width=20, command=quit)
    quit_btn.pack(side=tk.LEFT)
    
    start_preview(the_camera)

    root.mainloop()
