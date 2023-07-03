import picamera
from time import sleep

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.start_preview()

    for i in range(5):
        sleep(5)
        camera.capture(f'image_{i}.jpg')

    camera.stop_preview()