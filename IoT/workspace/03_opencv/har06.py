import cv2
from cv2.data import haarcascades
from os import path
from video import Video

xml = path.join(haarcascades, 'haarcascade_frontalface_default.xml')
cascade = cv2.CascadeClassifier(xml)

FACE_WIDTH = 200

def detect_face(frame):
    object_list = cascade.detect(frame)

    if len(object_list) > 0:
        cascade.draw_rect(frame, object_list, thickness = 1)
        x, y, w, h = object_list[0]  # 첫 번째 얼굴

        # 얼굴 부분 검출(정사각형으로 영역 지정)
        width = max(w, h)
        x = x +w//2 - width//2
        y = y + h//2 - width//2
        face_image = frame[y:y+width, x:x + width].copy()

        # 좌측 상단 출력
        face_image = Video.resize_frame(face_image, FACE_WIDTH,
                                        FACE_WIDTH)
        frame[0:FACE_WIDTH, 0:FACE_WIDTH] = face_image[:]

        return frame
    
    
with Video(0) as v:
    for image in v:
        detect_face(image)
        # 보여주기
        if not Video.show(image): break