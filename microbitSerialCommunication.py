import serial
from microbit import MicroBit
from microbitActivities import ActivityControl
import urllib.request,urllib.parse
import json
import time

'''
Terminal control receives data from the microbit and sends it to the server 
It also sends its data to the activity monitor which sends its data to the server
'''

class TerminalControl:
    BAUDRATE = 115200
    SENDRATE = 50 #ms

    def __init__(self,port,leftMicroBit,rightMicroBit,serverURL):
        self.serial = serial.Serial()
        self.serverURL = serverURL
        self.port = port
        self.serial.port = port
        self.serial.baudrate = TerminalControl.BAUDRATE
        self.leftMicroBit = leftMicroBit
        self.rightMicroBit = rightMicroBit
        self.activityControl = ActivityControl(self.serverURL)

    def writeToConsole(self,string):
        byteString = string.encode()
        self.serial.write(bytes(byteString))

    def parseData(self,str_data):
        return eval(str_data)

    def calibrate(self):
        self.leftMicroBit.setXYZ(0,0,0)
        self.rightMicroBit.setXYZ(0,0,0)
        

    def update(self,data):
        left = data['l']
        right = data['r']
        self.leftMicroBit.update(left,TerminalControl.SENDRATE)
        self.rightMicroBit.update(right,TerminalControl.SENDRATE)

    def updateLoop(self):
        while (True):
            data_str = self.serial.readline().decode("utf-8")
            parsedData = self.parseData(data_str)
            self.update(parsedData)
            self.sendPOST(parsedData)

    def sendPOST(self,parsedData):
        postData = {"l":[],"r":[]}
        serverRequestURL = self.serverURL + 'receive_data'
        if "l" in parsedData:
            # leftData = parsedData["l"]
            # data_send["l"] = leftData
            postData["l"] = 'LEFT SENT'
        if "r" in parsedData:
            # leftData = parsedData["r"]
            # data_send["r"] = leftData
            postData["r"] = 'RIGHT SENT'
        jsonPost = json.dumps(postData)
        byteJsonPost = bytes(jsonPost,"ascii")
        urllib.request.urlopen(serverRequestURL,data=byteJsonPost)

    def sendDummyData(self):
        self.sendPOST({'r':'R Dummy','l':'L Dummy'})

if __name__ == '__main__':
    terminalControl = TerminalControl("COM5",MicroBit(TerminalControl.SENDRATE),MicroBit(TerminalControl.SENDRATE),"http://127.0.0.1:3000/")
    terminalControl.sendDummyData()

    # send actual data
    # terminalControl.serial.open()
    # terminalControl.writeToConsole("Sending actual data")
    # terminalControl.updateLoop()