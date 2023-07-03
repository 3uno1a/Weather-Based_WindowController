from gpiozero import PWMLED
from signal import pause

led = PWMLED(20)


led.pulse()

# pause()
input('종료하려면 엔터를 누르세요')
