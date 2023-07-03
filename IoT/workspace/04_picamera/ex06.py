from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()

camera.awb_mode = 'sunlight'

sleep(5)

camera.capture('/home/pi/sunlight.jpg')
camera.stop_preview()

# AWB_MODES 값 목록
# off, auto, sunlight, cloudy, shade, tungsten, fluorescent, incandescent, 
# flash, horizon
