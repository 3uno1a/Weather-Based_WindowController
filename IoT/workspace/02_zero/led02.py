from gpiozero import LED
from signal import pause
from time import sleep

red = LED(20)

print(red.value)
red.value = 1
print(red.value)
sleep(5)

red.value = 0
print(red.value)
sleep(5)


# red.blink()  # 스레드로 동작(기본) --> 데몬 스레드
# # 메인 스레드가 종료될 때 같이 종료

# # pause()
# sleep(10)  # 깜빡이다가 10초 후에 종료

# red.blink(on_time = 0.5, off_time = 0.5)
# sleep(5)

# red.blink(on_time = 0.2, off_time = 1)
# sleep(5)


