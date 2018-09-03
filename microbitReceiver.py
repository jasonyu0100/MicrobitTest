from microbit import *

uart.init(baudrate=115200, bits=8, parity=None, stop=1)
while True:
    lControl = {"gesture":accelerometer.current_gesture(),
    "tilt":(accelerometer.get_x(),accelerometer.get_y(),accelerometer.get_z()),
    "buttons":(button_a.ispressed(),button_b.ispressed()),
    "pins":(pin0.is_touched(),pin1.is_touched(),pin2.is_touched()),
    "acceleration":{"x":accelerometer.get_x(),"y":accelerometer.get_y(),"z":accelerometer.get_z()}}
    sensors = {"l":lControl}
    uart.write(bytes(str(sensors)+"\n","utf-8"))
    sleep(50)
