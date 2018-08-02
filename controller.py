# Add your Python code here. E.g.
from microbit import *
import radio

radio.on()
radio.config(channel=5)
while True:
    sensors = {"gesture":accelerometer.current_gesture(),
    "tilt":(accelerometer.get_x(),accelerometer.get_y(),accelerometer.get_z())
    "buttons":(button_a.ispressed(),button_b.ispressed())
    "pins":(pin0.is_touched(),pin1.is_touched(),pin2.is_touched())
    radio.send(str(sensors))
    
