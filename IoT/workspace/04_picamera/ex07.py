from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()

camera.exposure_mode = 'beach'

sleep(5)

camera.capture('/home/pi/beach.jpg')
camera.stop_preview()

# EXPOSURE_MODES 값 목록
# off, auto, night, nightpreview, backlight, spotlight, sports, snow, beach, 
# verylong, fixedfps, antishake, fireworks
