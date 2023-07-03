from gpiozero import MotionSensor
from time import sleep
from datetime import datetime
import cv2
from iot_server.mjpeg.upload import upload
from video_util import convert_cv


cap = cv2.VideoCapture(0)   # picamera 없는 상태에서는 0번
# 1번 카메라 (picamera 꽂혀있는 상태에서 usb cam)
frame_size = (640, 480)
fourcc = cv2.VideoWriter_fourcc('X', '2', '6', '4')  # mp4 코덱을 사용하려면
# fourcc = cv2.VideoWriter_fourcc(*'mp4')

recording = False   # 녹화 여부 판단 
recorder = None
fname = None

def start_record():
    global recorder, recording, fname
    start = datetime.now()
    fname = start.strftime('./data/%Y%m%d_%H%M.mp4')
    recorder = cv2.VideoWriter(fname + '.mp4', fourcc, 20.0, frame_size)   # 녹화 시작
    recording = True              # 녹화중임을 표시
    print(fname, 'start recording..')

def stop_record():
    global recorder, recording
    recording = False        # 녹화 중이 아님을 표시
    sleep(0.1)  # 세그멘테이션 오류 방지
    recorder.release()
    recorder = None
    print('stop recording')

    src = fname + '._mp4'
    dst = fname + '.mp4'
    convert_cv(src, dst)

    # 녹화 파일을 iot 서버에 업로드
    result = upload(dst)
    if result:
        print('업로드 성공:', dst)
    else:
        print('업로드 실패:', dst)

pir = MotionSensor(21)
pir.when_motion = start_record
pir.when_no_motion = stop_record

while True:
    if not recording:   # 동작 미 감지시 -> 녹화 X
        sleep(0.1)     # 대기
        continue

    # 동작 감지시 녹화
    retval, frame = cap.read()
    if not retval: break

    now = datetime.now()
    timestamp = now.strftime('REC. %Y-%m-%d %H:%M:%S')    # 현재 날짜 시간 

    cv2.putText(frame, timestamp, (10, 30),   
                 cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, 
                 (0, 0, 0), 1, cv2.LINE_AA)      # 현재 날짜와 시간을 프레임에 텍스트로 표시

    recorder.write(frame)

    cv2.waitKey(40)    # 키 이벤트 처리

cap.release()        # 카메라 리소스 해제
recorder.release()    # 녹화된 동영상 리소스 해제

cv2.destroyAllWindows()     # 모든 창을 닫아
