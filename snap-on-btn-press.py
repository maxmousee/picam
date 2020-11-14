import time
import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep


def setup_gpio():
    GPIO.setwarnings(False)  # Ignore warning for now
    GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
    GPIO.setup(10, GPIO.IN,
               pull_up_down=GPIO.PUD_DOWN)  # Set pin 10 to be an input pin and set initial value to be pulled low (off)


def setup_camera():
    camera.brightness = 50
    camera.sharpness = 0
    camera.contrast = 0
    camera.saturation = 0
    camera.iso = 0
    camera.exposure_compensation = 0
    camera.exposure_mode = 'auto'
    camera.meter_mode = 'average'
    camera.awb_mode = 'auto'
    camera.rotation = 0
    camera.hflip = False
    camera.vflip = False
    camera.crop = (0.0, 0.0, 1.0, 1.0)
    camera.resolution = (4056, 3040)
    # you may need to increase gpu_mem in /boot/config.txt to achieve full resolution with the Camera Module v2.


if __name__ == '__main__':
    setup_gpio()
    setup_camera()

    while True:
        if GPIO.input(10) == GPIO.HIGH:
            print("Shutter button was pressed, saving photo...")
            filename = "image_" + str(int(time.time())) + ".jpg"
            camera.capture("/home/pi/Pictures/" + filename)
            sleep(1)