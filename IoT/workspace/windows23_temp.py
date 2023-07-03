import adafruit_dht
from datetime import datetime
from time import sleep
import requests
import json
from gpiozero import Motor


speed = 0.8

def upload(temp):
    url_temp = 'http://192.168.35.245:8000/api/temp/'
    # url_temp = 'http://172.30.1.111:8000/api/temp/'

    data_temp = {
        'value': temp,
        'date': datetime.now().isoformat()
    }

    try:
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url_temp, data = json.dumps(data_temp), headers = headers)

        if response.status_code == 201 :
            print('데이터 업로드 성공!\n')
        else:
            print('데이터 업로드 실패:', response.status_code)

    except requests.exceptions.RequestException as e:
        print('데이터 업로드 도중 오류 발생:', str(e))


def measure_temp():
    mydht22 = adafruit_dht.DHT22(17)
    motor = Motor(20, 21, 12)
    
    while True:
        try:
            temp_now = mydht22.temperature 
            print('현재 온도:', temp_now)

            # if temp_now >= 26:
            #     motor.backward(speed)
            #     sleep(3)
            #     motor.stop()
            #     print("창문을 닫았습니다.")
            #     window_status = 0
            #     return window_status

            upload(temp_now)
            sleep(2)

        except KeyboardInterrupt:
            break

        except RuntimeError as e:
            print('센서 통신 오류:', str(e))


measure_temp() 









