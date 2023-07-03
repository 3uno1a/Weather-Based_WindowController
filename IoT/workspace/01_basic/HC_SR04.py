# 초음파 센서
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False) #센서에 연결한 Trig와 Echo 핀의 핀 번호 설정
TRIG = 20
ECHO = 21
print("Distance measurement in progress")

#Trig와 Echo 핀의 출력/입력 설정
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

#Trig핀의 신호를 0으로 출력
GPIO.output(TRIG, False)
print("Waiting for sensor to settle")

time.sleep(2)

try:
    while 1:
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0:
            start = time.time()
        while GPIO.input(ECHO) == 1:
            stop = time.time()

        check_time = stop - start
        distance = check_time * 34300 / 2
        print("Distance : %.1f cm" % distance)
        time.sleep(0.4)

except KeyboardInterrupt:
    print("Measurement stoped by User")
    GPIO.cleanup()