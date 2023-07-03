import RPi.GPIO as GPIO
import time

count = 0
button_pin = 26

# 버튼의 callback 함수
def button_callback(channel):
    global count
    count += 1
    print(count, "Button pushed!")

# GPIO 핀의 번호 모드 설정
GPIO.setmode(GPIO.BCM)

# 버튼 핀의 IN/OUT 설정, PULL UP 설정
GPIO.setup(button_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Event 방식으로 핀의 FALLING 신호를 감지하면 button_callback 함수를 실행
GPIO.add_event_detect(button_pin, GPIO.FALLING, 
                      callback = button_callback,
                      bouncetime = 200)  # bounce time 주면 계속 눌러도 하나씩 증가
# 한번 누를 때 여러번 눌러지는게 사라짐

try:
    while 1:
        time.sleep(0.1)  # 0.1초 딜레이

finally:
    GPIO.cleanup()


