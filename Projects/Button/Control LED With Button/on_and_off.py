from gpiozero import Button, LED
import time

button = Button(2)
led = LED(17)

while True:
        button.wait_for_press()
        print("THE BUTTON WAS PRESSED!")
        led.toggle()
        time.sleep(0.5)
