from gpiozero import Button
from signal import pause

count = 0

def say_hello():
    global count
    count += 1
    print(count, "Hello!")

button = Button(26)

button.when_pressed = say_hello

pause()