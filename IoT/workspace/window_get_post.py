from gpiozero import Motor
from time import sleep
import requests
import json

motor = Motor(20, 21, 12)
speed = 0.8

window_state = 0

def get_window_state():
    # url_window = 'http://192.168.35.245:8000/api/window/'
    url_window = 'http://172.30.1.111:8000/api/window/'

    response = requests.get(url_window)
    if response.status_code == 200:
        data = response.json()
        print("API GET 요청 성공")
        # return data['results'][0]['windowstatus']
        return data[0]['windowstatus']
    else:
        print("API GET 요청 실패:", response.status_code)
        return None

def post_window_state(state):
    # url_window = 'http://192.168.35.245:8000/api/window/'
    url_window = 'http://172.30.1.111:8000/api/window/'
    data_window = {
        'windowstatus': state,
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url_window, data=json.dumps(data_window), headers=headers)
    if response.status_code == 201:
        print("API POST 요청 성공")
    else:
        print("API POST 요청 실패")

def control_window():
    global window_state

    while True:
        api_state = get_window_state()

        if api_state is not None:
            if api_state and not window_state:  # API 상태가 True이고 창문 상태가 False인 경우
                motor.forward(speed)  # 창문 열기 동작
                sleep(2)
                motor.stop()
                print("창문 열림")
                window_state = 1  # 창문 상태 업데이트

            elif not api_state and window_state:  # API 상태가 False이고 창문 상태가 True인 경우
                motor.backward(speed)  # 창문 닫기 동작
                sleep(2)
                motor.stop()
                print("창문 닫힘")
                window_state = 0  # 창문 상태 업데이트
        else:
            # API 요청 실패 시 추가 처리 필요
            pass

        post_window_state(window_state)  
        sleep(1)

if __name__ == "__main__":
    control_window()
