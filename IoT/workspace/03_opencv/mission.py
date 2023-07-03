import cv2
from datetime import datetime

start = datetime.now()
fname = start.strftime('./data/%Y%m%d_%H%M.mp4')  # str format time

cap = cv2.VideoCapture(0) # 0번 카메라

frame_size = (640, 480)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out1 = cv2.VideoWriter(fname, fourcc, 20.0, frame_size)

while True:
    retval, frame = cap.read() # 프레임 캡처
    if not retval: break

    now = datetime.now()
    timestamp = now.strftime('REC. %Y-%m-%d %H:%M:%S')

    cv2.putText(frame, timestamp, (10, 30),
                 cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, 
                 (0, 0, 0), 1, cv2.LINE_AA)

    out1.write(frame)

    cv2.imshow('mission', frame)

    key = cv2.waitKey(25)
    if key == 27: break # ESC


cap.release()
out1.release()

cv2.destroyAllWindows()
