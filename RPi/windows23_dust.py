from gpiozero import MCP3008
from time import sleep
import requests
import json

# MCP3008 ADC 초기화
outdoor = MCP3008(channel=0)
indoor = MCP3008(channel=1)


while True:
    voltage_o = outdoor.value * (5 / 1024.0)   # 미세먼지 센서의 전압값
    voltage_i = indoor.value * (5 / 1024.0)

    out_dust = (0.172 * voltage_o - 0.09999) * 1000
    in_dust = (0.172 * voltage_i - 0.09999) * 1000

    # ADC 값을 기준으로 미세먼지 값을 계산하거나 처리하는 코드를 추가하세요.

    # 측정된 미세먼지 값을 출력
    print("실외 미세먼지: {}".format(out_dust))
    print("실내 미세먼지: {}".format(in_dust))

    sleep(2)