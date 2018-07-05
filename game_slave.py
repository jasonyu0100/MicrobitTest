# Add your Python code here. E.g.
from microbit import *
import radio
radio.on()

while True:
    message = radio.receive()
    display.show(message)
    if message == image.HAPPY:
        radio.off()
        break
    if button_a.is_pressed():
        radio.send(0)
        sleep(400)
    elif button_b.is_pressed():
        radio.send(1)
        sleep(400)
    elif pin0.is_touched():
        radio.send(2)
    elif pin1.is_touched():
        radio.send(3)
