import time
from picamera import PiCamera


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
    the_camera.rotation = 0
    the_camera.hflip = False
    the_camera.vflip = False
    the_camera.crop = (0.0, 0.0, 1.0, 1.0)
    the_camera.resolution = (2000, 1500)
    # you may need to increase gpu_mem in /boot/config.txt to achieve full resolution with the Camera Module v2.


if __name__ == '__main__':
    the_camera = PiCamera()
    setup_camera(the_camera)
    filename = "/home/pi/Pictures/image_" + str(int(time.time())) + ".jpg"
    the_camera.capture(filename)
    print("Saved image as " + filename)