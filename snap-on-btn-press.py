import RPi.GPIO as GPIO

if __name__ == '__main__':
    GPIO.setwarnings(False)  # Ignore warning for now
    GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
    GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set pin 10 to be an input pin and set initial value to be pulled low (off)

    while True:
        if GPIO.input(10) == GPIO.HIGH:
            print("Shutter button was pressed, saving photo...")