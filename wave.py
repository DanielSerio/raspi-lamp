import time

import board
import neopixel
import numpy as np

# LED Strip config
LED_COUNT = 12
LED_PIN = board.D7
LED_BRIGHTNESS = 0.75
LED_ORDER = neopixel.GRB

# COLORS
seafoam = (255, 0, 205)
skyblue = (198, 16, 249)
blue = (147, 15, 255)
bluenavy = (117, 2, 211)
bluepurple = (89, 64, 173)
COLORS = [blue, seafoam, skyblue, blue, bluenavy, bluepurple, blue]

strip = neopixel.Neopixel(LED_PIN, LED_COUNT, brightness = LED_BRIGHTNESS, pixel_order = LED_ORDER, auto_write = False)

def fade(color1, color2, percent):
    color1 = np.array(color1)
    color2 = np.array(color2)
    vector = color2-color1
    newcolor = (int((color1 + vector * percent)[0]), int((color1 + vector * percent)[1]), int((color1 + vector * percent)[2]))
    return newcolor

def cycle(wait):
  for c in range(len(COLORS)):
    for i in range(10):
      color1 = COLORS[c]
      if c == 5:
        color2 = blue
      else:
        try: 
          color2 = COLORS[c + 1]
        except IndexError:
          color2 = COLORS[0]

      percent = i * 0.1
      strip.fill(fade(color1, color2, percent))
      strip.show()
      time.sleep(wait)

while True:
  time.sleep(1)
  cycle(2)