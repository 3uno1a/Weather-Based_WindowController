import RPi.GPIO as GPIO

#서보모터를 PWM으로 제어할 핀 번호 설정
SERVO_PIN = 14

# GPIO핀의 번호 모드 설정
GPIO.setmode(GPIO.BCM)

# 서보핀의 출력 설정
GPIO.setup(SERVO_PIN, GPIO.OUT)

# PWM 인스턴스 servo 생성, 주파수 50으로 설정
servo = GPIO.PWM(SERVO_PIN,50)

# PWM 듀티비 0 으로 시작
servo.start(0)

try:
    while True:
        d = float(input("각도를 입력하세요: "))
        duty = (10/180) * d + 2.5
        servo.ChangeDutyCycle(duty) 
        
finally:
    servo.stop()
    GPIO.cleanup()




