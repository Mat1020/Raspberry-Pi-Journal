from gpiozero import RGBLED 
import time

rgb_led = RGBLED(22, 17, 27)

for r in range(2):
    for g in range(2):
        for b in range(2):
            rgb_led.color = (r, g, b)
            time.sleep(0.50)

time.sleep(0.25)
rgb_led.off()
