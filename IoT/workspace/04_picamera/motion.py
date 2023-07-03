from picamera import PiCamera
from gpiozero import MotionSensor
from datetime import datetime
from video_util import convert
from signal import pause
from iot_server.mjpeg.upload import upload, notify_intrusion

camera = PiCamera()
camera.framerate = 24
fname = None

def start_record():
    global fname
    start = datetime.now()
    fname = start.strftime('%Y%m%d_%H%M%S')
    camera.start_recording(fname + '.h264')
    print('start recording...', fname)
    notify_intrusion()

def stop_record():
    camera.stop_recording()
    
    src = fname + '.h264'
    dst = fname +'.mp4'
    convert(src, dst)
    print('stop recording')
    
    # 녹화 파일을 iot 서버에 업로드
    result = upload(dst)
    if result:
        print('업로드 성공:', dst)
    else:
        print('업로드 실패:', dst)


pir = MotionSensor(21)
pir.when_motion = start_record
pir.when_no_motion = stop_record

camera.start_preview()
pause()