import time
from picamera import PiCamera
import numpy as np
import cv2

with PiCamera() as camera:
    camera.resolution = (640, 480)

    image = np.empty((480, 640, 3), dtype=np.uint8)
    
    while True:
        start = time.time()
        camera.capture(image, 'bgr', use_video_port=True)  # fps가 커짐 빨리짐
        cv2.imshow('frame', image)

        if cv2.waitKey(1) == 27: # esc 키 입력시 종료
            break

        end = time.time()
        fps = 1 / (end - start)
        print(f'fps: {fps:0.1f}')