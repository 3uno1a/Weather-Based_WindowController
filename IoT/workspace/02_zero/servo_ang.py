from gpiozero import AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory
# jittering 방지
from time import sleep
from signal import pause

factory = PiGPIOFactory(host = 'localhost')

servo = AngularServo(12, 
    min_angle=0, max_angle=180, 
    min_pulse_width=0.00054, 
    max_pulse_width=0.0024,
    pin_factory= factory)


servo.angle = 120
pause()
