# 카메라 동영상에서 얼굴을 검출/ 영상에서 몸 검출
# 검출된 영역에 사각형 박스 그리기
# cv2.imshow()로 출력하기

import cv2
from harrdetect import HarrDetect

# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('./data/vtest.avi')

# cascade = HarrDetect('haarcascade_frontalface_default.xml')
cascade = HarrDetect('haarcascade_fullbody.xml')

while True:
    retval, frame = cap.read()  # 프레임 캡쳐
    if not retval: break

    object_list = cascade.detect(frame, minSize = (40, 40))
    if len(object_list) > 0:
        cascade.draw_rect(frame, object_list, thickness = 1)

    cv2.imshow('frame', frame)

    key = cv2.waitKey(40)
    if key == 27: break # ESC 누르면 루프 탈출

if cap.isOpened():
    cap.release()

cv2.destroyAllWindows()














