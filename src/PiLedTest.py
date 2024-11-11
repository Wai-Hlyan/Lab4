import RPi.GPIO as GPIO
from time import sleep, time

# Initialize GPIO settings
def init():
    GPIO.setmode(GPIO.BCM)  # Choose BCM mode
    GPIO.setwarnings(False)
    GPIO.setup(22, GPIO.IN)  # Set GPIO 22 as input for the slide switch
    GPIO.setup(24, GPIO.OUT) # Set GPIO 18 as output for the LED

# Read the slide switch position
def read_slide_switch():
    return GPIO.input(22)

# Main control function
def control_led():
    init()
    try:
        while True:
            switch_position = read_slide_switch()

            if switch_position == 0:  # Switch in left position
                # Blink at 5 Hz continuously
                frequency = 5
                period = 1 / frequency
                GPIO.output(24, GPIO.HIGH)
                sleep(period / 2)
                GPIO.output(24, GPIO.LOW)
                sleep(period / 2)

            else:  # Switch in right position
                # Blink at 10 Hz for 5 seconds, then turn off
                end_time = time() + 5
                while time() < end_time and read_slide_switch() == 1:
                    frequency = 10
                    period = 1 / frequency
                    GPIO.output(24, GPIO.HIGH)
                    sleep(period / 2)
                    GPIO.output(24, GPIO.LOW)
                    sleep(period / 2)
                
                # Ensure LED is off after 5 seconds
                GPIO.output(24, GPIO.LOW)
                sleep(1)  # Short delay to prevent bouncing

    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

# Run the LED control function
control_led()
