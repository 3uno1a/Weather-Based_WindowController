from gpiozero import Button
from signal import pause

def say_hello():
    print("Hello!")

def say_goodbye():
    print("Goodbye!")


button = Button(26)

button.when_pressed = say_hello     # 버튼 누를 때
button.when_released = say_goodbye  # 버튼 뗄 떄

pause()