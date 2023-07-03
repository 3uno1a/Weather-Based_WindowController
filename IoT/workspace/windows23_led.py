import time
import board
# import neopixel
from rpi_ws281x import *

# pixels = neopixel.NeoPixel(board.D18, 60, brightness = 1)

LED_COUNT = 60
LED_PIN = 12
LED_BRIGHTNESS = 65
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
strip.begin()

color = Color(0, 255, 0)

for i in range(LED_COUNT):
    strip.setPixelColor(i, color)

strip.show()

time.sleep(10)

for i in range(LED_COUNT):
    strip.setPixelColor(i, Color(0, 0, 0))

strip.show()