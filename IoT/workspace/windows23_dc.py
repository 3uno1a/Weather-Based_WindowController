from gpiozero import Motor
from time import sleep
import requests
import json

motor = Motor(20, 21, 16)
speed = 0.8

WINDOW_OPEN = True
WINDOW_CLOSED = False


def upload(window_status):
    # url_rain = 'http://192.168.35.245:8000/api/window/'
    url_window = 'http://172.30.1.111:8000/api/window/'

    data_window = {
        'windowstatus': window_status,
    }

    try:
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url_window, data=json.dumps(data_window), headers=headers)

        if response.status_code == 201:
            print('창문 상태 업로드 성공!\n')
        else:
            print('칭문 상태 업로드 실패:', response.status_code)

    except requests.exceptions.RequestException as e:
        print('데이터 업로드 도중 오류 발생:', str(e))


def open():
    print("창문 여는 중..")
    motor.forward(speed)    # 레일이 왼쪽으로 이동
    sleep(2)
    motor.stop()
    print("창문 열림")
    sleep(2)
    return WINDOW_OPEN
 

def close():
    print("창문 닫는 중..")
    motor.backward(speed)
    sleep(2)
    motor.stop()
    print("창문 닫힘")
    sleep(2)
    return WINDOW_CLOSED


def window_control():
    window_status = WINDOW_CLOSED

    try:
        while True:
            if window_status == WINDOW_CLOSED:
                window_status = open()
            else:
                window_status = close()

            upload(window_status)
            sleep(5)

    except KeyboardInterrupt:
        pass

window_control()




'''
backward()일때 레일이 오른쪽으로 이동 / forward가 왼쪽으로 이동
motor.forward() 호출하면 forward 핀이 HIGH, backward가 LOW
motor.backward() 호출하면 forward 핀이 LOW, backward 핀이 HIGH
'''