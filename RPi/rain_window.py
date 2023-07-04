from time import sleep
import requests
import json
from gpiozero import Motor
from gpiozero import DigitalInputDevice

speed = 0.8
rain_status = 0
window_status = 0

def upload():
    url_rain = 'http://172.30.1.111:8000/api/rain/'
    url_window = 'http://172.30.1.111:8000/api/window/'

    data_rain = {
        'rainstatus': rain_status,
    }

    data_window = {
        'windowstatus': window_status,
    }

    try:
        headers = {'Content-Type': 'application/json'}
        response_rain = requests.post(url_rain, data=json.dumps(data_rain), headers=headers)
        response_window = requests.post(url_window, data=json.dumps(data_window), headers=headers)

        if response_rain.status_code == 201 and response_window.status_code == 201:
            print('강우 & 창문 상태 업로드 성공!\n')
        else:
            print('강우 상태 업로드 실패:', response_rain.status_code, response_window.status_code)

    except requests.exceptions.RequestException as e:
        print('데이터 업로드 도중 오류 발생:', str(e))


def measure_rain():
    global window_status
    # 빗물 검출되면 HIGH -> LOW
    if rain_sensor.value == 0 and window_status == 1:     # 비가 오는데 창문이 열려있으면 창문 닫음
        print("강우가 감지되었습니다.")
        motor.backward(speed)
        sleep(2)
        motor.stop()
        print("창문을 닫았습니다.")
        rain_status = 1
        window_status = 0
        return rain_status, window_status

    elif rain_sensor.value == 0 and window_status == 0:    # 비가 오는데 창문이 닫혀있으면
        print("강우가 감지되었습니다.")
        rain_status = 1
        return rain_status

    elif rain_sensor.value == 1: 
        print("강우가 감지되지 않았습니다.")
        rain_status = 0
        return rain_status


def main():
    try:
        while True:
            measure_rain()
            sleep(5)      # 5초 간격으로 감지

    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    rain_sensor = DigitalInputDevice(23)
    motor = Motor(20, 21, 12)
    main()

