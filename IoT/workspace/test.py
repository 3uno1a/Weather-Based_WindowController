from gpiozero import Motor
from time import sleep

motor = Motor(20, 21, 16)
speed = 0.8


def open():
    print("창문 여는 중..")
    motor.backward(speed)    # 레일이 왼쪽으로 이동
    sleep(2)
    motor.stop()
    print("창문 열림")
    sleep(2)

 

def close():
    print("창문 닫는 중..")
    motor.forward(speed)
    sleep(2)
    motor.stop()
    print("창문 닫힘")
    sleep(2)

sleep(3)
close()
sleep(1)