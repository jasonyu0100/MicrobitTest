import urllib.request
from .microSerialCom import TerminalControl

serverURL = "127.0.0.1:3000"
control = TerminalControl("COM5",MicroBit(),MicroBit())
control.serial.open()
while True:
    data_str = control.serial.readline().decode("utf-8")
    parsed_data = control.parseData(data_str)
    control.update(parsed_data)
    data_send = {}
    if control.leftMicroBit.btnA:
        data_send["l"] = control.leftMicroBit.getXYZ()
    elif control.rightMicroBit.btnA:
        data_send["r"] = control.rightMicroBit.getXYZ()
    urllib.request(serverURL,data=data_send)
