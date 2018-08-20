from microbit import *
import radio
radio.on()
uart.init(baudrate=115200, bits=8, parity=None, stop=1)
while True:
    radio.config(channel=5)
    lControl = eval(radio.receive())
    radio.config(channel=10)
    rControl = eval(radio.receive())
    sensors = {"l":lControl,"r":rControl}
    uart.write(bytes(str(sensors)+"\n"))
