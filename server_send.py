# import urllib.request, urllib.parse
# import json, time
# from microSerialCom import TerminalControl
# from microbit import MicroBit

# serverURL = "http://127.0.0.1:3000/receive_data"
# control = TerminalControl("COM5",MicroBit(),MicroBit())
# control.serial.open()
# prev_send = {}
# while True:
#     data_str = control.serial.readline().decode("utf-8")
#     parsed_data = control.parseData(data_str)
#     control.update(parsed_data)
#     data_send = {}
#     if control.leftMicroBit.btnA:
#         data_send["l"] = control.leftMicroBit.getXYZ()
#     elif control.rightMicroBit.btnA:
#         data_send["r"] = control.rightMicroBit.getXYZ()
#     if len(data_send) > 0 and prev_send != data_send:
#         data_enc = json.dumps(data_send)
#         data_enc = bytes(data_enc,"ascii")
#         urllib.request.urlopen(serverURL,data=data_enc)
#     prev_send = data_send

# Deprecated functionality now in micro serial com
