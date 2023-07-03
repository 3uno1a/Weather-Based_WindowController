from gpiozero import Servo
from time import sleep

servo = Servo(12, min_pulse_width=0.0004, max_pulse_width=0.0024) # 0 ~ 180

while True:
    servo.value = 0
    print("mid")
    sleep(0.5)
    servo.value = -1
    print("min")
    sleep(1)
    servo.value = 0
    print("mid")
    sleep(0.5)
    servo.value = 1
    print("max")
    sleep(1)
