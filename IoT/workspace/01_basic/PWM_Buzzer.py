import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.OUT)

# 인스턴스 p, 주파수 100Hz
p = GPIO.PWM(21, 100)  # 100ms 주기

Frq = [262, 294, 330, 349, 392, 440, 493, 532]
speed = 0.5   # 음과 음 사이 연주시간 설정

p.start(10)  # PWM 시작 듀티사이클 10

try:
    while 1:
        for fr in Frq:
            p.ChangeFrequency(fr)  #주파수를 fr로 변경
            time.sleep(speed)     #speed 초만큼 딜레이 (0.5s)

except KeyboardInterrupt:  # 키보드 Ctrl+C 눌렀을때 예외발생
    p.stop()   # PWM을 종료
    GPIO.cleanup()