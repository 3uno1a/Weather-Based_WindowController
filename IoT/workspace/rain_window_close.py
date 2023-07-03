from time import sleep
import requests
import json
from gpiozero import Motor
from gpiozero import DigitalInputDevice

speed = 0.8
rain_status = 0

def get_window_state():
    # url_window = 'http://192.168.35.245:8000/api/window/'
    url_window = 'http://172.30.1.111:8000/api/window/'

    response = requests.get(url_window)
    if response.status_code == 200:
        data = response.json()
        print("API GET 요청 성공")
        # return data['results'][0]['windowstatus']
        data = data[0]['windowstatus']
        print(data)
        return data
    else:
        print("API GET 요청 실패:", response.status_code)
        return None

def measure_rain():
    global window_status
    # 빗물 검출되면 HIGH -> LOW
    if rain_sensor.value == 0 and window_status == 1:     # 비가 오는데 창문이 열려있으면 창문 닫음
        print("강우가 감지되었습니다.")
        motor.backward(speed)
        sleep(3)
        motor.stop()
        print("창문을 닫았습니다.")
        rain_status = 1
        window_status = 0
        return rain_status, window_status

    elif rain_sensor.value == 0 and window_status == 0:    # 비가 오는데 창문이 닫혀있으면
        print("강우가 감지되었습니다. 창문이 닫혀있습니다.")
        rain_status = 1
        return rain_status

    elif rain_sensor.value == 1: 
        print("강우가 감지되지 않았습니다.")
        rain_status = 0
        return rain_status


def main():
    global window_status
    try:
        while True:
            window_status = get_window_state()
            measure_rain()
            sleep(3)      # 5초 간격으로 감지

    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    rain_sensor = DigitalInputDevice(23)
    motor = Motor(20, 21, 12)
    main()

