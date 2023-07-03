from picamera import PiCamera
from time import sleep

camera = PiCamera()


# 180도 회전
# camera.rotation = 180
print(camera.resolution)  # default 해상도

camera.start_preview()  # 미리보기 화면 시작
# camera.start_preview(alpha = 200)  # 투명도 설정, 값의 범위 : 0~255

sleep(10)

camera.stop_preview()  # 미리보기 화면 정지