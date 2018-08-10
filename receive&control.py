# Add your Python code here. E.g.
from microbit import *
import radio

radio.on()
uart.init(baudrate=115200, bits=8, parity=None, stop=1)
while True:
    radio.config(channel=5)
    lControl = {"gesture":accelerometer.current_gesture(),
    "tilt":(accelerometer.get_x(),accelerometer.get_y(),accelerometer.get_z()),
    "buttons":(button_a.is_pressed(),button_b.is_pressed()),
    "pins":(pin0.is_touched(),pin1.is_touched(),pin2.is_touched())}
    #radio.config(channel=10)
    #rControl = eval(radio.receive())
    sensors = {"l":lControl}#,"r":rControl}
    uart.write(bytes(str(sensors)+"\n","utf-8"))
    sleep(10000)
