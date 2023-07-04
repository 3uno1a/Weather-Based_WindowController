import time
import requests
import json
from gpiozero import DigitalInputDevice

RAIN_SENSOR_PIN = 23


def upload(rain_status):
    # url_rain = 'http://192.168.35.245:8000/api/rain/'
    url_rain = 'http://172.30.1.111:8000/api/rain/'

    data_rain = {
        'rainstatus': rain_status,
    }

    try:
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url_rain, data=json.dumps(data_rain), headers=headers)

        if response.status_code == 201:
            print('강우 상태 업로드 성공!\n')
        else:
            print('강우 상태 업로드 실패:', response.status_code)

    except requests.exceptions.RequestException as e:
        print('데이터 업로드 도중 오류 발생:', str(e))


def measure_rainfall():
    if rain_sensor.value == 0:  # 빗물 검출되면 HIGH -> LOW
        print("강우가 감지되었습니다.")
        upload(True)
    else:
        print("강우가 감지되지 않았습니다.")
        upload(False)


def main():
    try:
        while True:
            measure_rainfall()
            time.sleep(10)      # 10초 간격으로 감지

    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    rain_sensor = DigitalInputDevice(RAIN_SENSOR_PIN)
    main()



'''
아날로그 출력 핀은 물이 얼마나 많이 묻었냐를 확인
디지털 출력 핀은 일정량 이상 물이 묻었냐 안 묻었냐를 판단 (비가 온다/안 온다)
디지털 핀의 감도 조절은 가변 저항(파란 상자)으로 조절 가능 - 불이 켜졌다 꺼졌다

물을 떨어뜨리면 DO 출력이 낮아지고 스위치 표시등(DO LED)이 켜짐 / 물을 닦아내면 DO LED가 꺼짐
'''