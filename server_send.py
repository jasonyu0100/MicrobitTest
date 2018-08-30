import urllib.request, urllib.parse
from microSerialCom import TerminalControl
from microbit import MicroBit

serverURL = "127.0.0.1:3000/receive_data"
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
    data_send = urllib.parse.urlencode(data_send)
    data_send = data.encode("ascii")
    urllib.request(serverURL,data=data_send)
