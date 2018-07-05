# Add your Python code here. E.g.
from microbit import *
import radio
radio.on()
image = Image("90000:"
              "00000:"
              "00000:"
              "00000:"
              "00001")
col = 0
row = 0
while True:
    message = radio.receive()
    if button_a.is_pressed() or message == 0:
        image.set_pixel(col,row,0)
        if col != 0:
            col -= 1
        sleep(400)
        image.set_pixel(col,row,9)
    elif button_b.is_pressed() or message == 1:
        image.set_pixel(col,row,0)
        if col != 4:
            col += 1
        sleep(400)
        image.set_pixel(col,row,9)
    elif pin0.is_touched() or message == 2:
        image.set_pixel(col,row,0)
        if row != 0:
            row -= 1
        sleep(400)
        image.set_pixel(col,row,9)
    elif pin1.is_touched() or message == 3:
        image.set_pixel(col,row,0)
        if row != 4:
            row += 1
        sleep(400)
        image.set_pixel(col,row,9)
    if row == 4 and col == 4:
        radio.send(image.HAPPY)
        display.show(image.HAPPY)
        break
    radio.send(image)
    display.show(image)
        
