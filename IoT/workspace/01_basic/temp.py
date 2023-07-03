import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)


try:
    while 1:
        time.sleep(0.1)  # 0.1초 딜레이
finally:
    GPIO.cleanup()