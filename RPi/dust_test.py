import RPi.GPIO as GPIO
import spidev
from datetime import datetime
from time import sleep
import requests
import json

outdoor_channel = 0
indoor_channel = 1

spi = spidev.SpiDev()
spi.open(0, 0)   # 통신 시작
spi.max_speed_hz = 100000   # 통신 속도

LED_o = 13
LED_i = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_o, GPIO.OUT)
GPIO.setup(LED_i, GPIO.OUT)


def readadc(adcnum):
    if adcnum < 0 or adcnum > 7:    
        return -1
    
    r = spi.xfer2([1, 8 + adcnum <<4, 0])   # 요청 및 값 리턴
    data = ((r[1] & 3) << 8) + r[2]    # 10 비트 해석
    return data


def read_outdoor():
    GPIO.output(LED_o, GPIO.LOW)
    sleep(0.00028)
    value_o = readadc(outdoor_channel)
    sleep(0.00004)
    GPIO.output(LED_o, GPIO.HIGH)
    sleep(0.00968)
    voltage = value_o * (3.3 / 1024.0)
    outdoor_dust = abs((0.17 * voltage - 0.1) * 1000)
    print("outdoor ultrafinedust value: %d" % outdoor_dust)
    return outdoor_dust

def read_indoor():
    GPIO.output(LED_o, GPIO.LOW)
    sleep(0.00028)
    value_i = readadc(indoor_channel)
    sleep(0.00004)
    GPIO.output(LED_o, GPIO.HIGH)
    sleep(0.00968)
    voltage = value_i * (3.3 / 1024.0)
    indoor_dust = abs((0.17 * voltage - 0.1) * 1000)
    print("indoor ultrafinedust value: %d" % indoor_dust)
    return indoor_dust


def post_dust(outdoor_dust, indoor_dust):
    url_out = 'http://172.30.1.111:8000/api/out_ultrafinedust/'
    url_in = 'http://172.30.1.111:8000/api/in_ultrafinedust/'

    data_out = {
        'value': outdoor_dust,
        'date': datetime.now().isoformat()
    }

    data_in = {
        'value': indoor_dust,
        'date': datetime.now().isoformat()
    }

    headers = {'Content-Type': 'application/json'}
    response_o = requests.post(url_out, data=json.dumps(data_out), headers=headers)
    response_i = requests.post(url_in, data=json.dumps(data_in), headers=headers)

    if response_o.status_code == 201 and response_i.status_code == 201:
        print("API POST 요청 성공")
    else:
        print("API POST 요청 실패")


try:
    while True:
        outdoor_dust = read_outdoor()
        indoor_dust = read_indoor()
        post_dust(outdoor_dust, indoor_dust)
        print("---------------------------------")
        sleep(2)
except Exception as e:
    print(e)

finally:
    spi.close()
    GPIO.cleanup()