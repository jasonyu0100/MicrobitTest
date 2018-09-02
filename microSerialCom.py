import serial
from microbit import MicroBit
import urllib.request, urllib.parse
import json, time
import subprocess

class TerminalControl:
    baudRate = 115200
    sendRate = 50 #ms
    def __init__(self,port,leftMicroBit,rightMicroBit,serverURL):
        self.serial = serial.Serial()
        self.serverURL = serverURL
        self.port = port
        self.serial.port = port
        self.serial.baudrate = TerminalControl.baudRate
        self.leftMicroBit = leftMicroBit
        self.rightMicroBit = rightMicroBit

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
        self.leftMicroBit.update(left,TerminalControl.sendRate)
        self.rightMicroBit.update(right,TerminalControl.sendRate)

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

    def startServer(self):
        checkStartServer = input("Do you want to start server? (Y/N): ")
        while checkStartServer not in ['Y','N']:
            if checkStartServer == 'Y':
                subprocess.call('sudo node server_node.js',shell=True)
            elif checkStartServer == 'N':
                break
            else:
                checkStartServer = input("Do you want to start server? (Y/N): ")



if __name__ == '__main__':
    terminalControl = TerminalControl("COM5",MicroBit(),MicroBit(),"http://127.0.0.1:3000/")
    terminalControl.startServer()
    terminalControl.serial.open()
    terminalControl.writeToConsole("Hello World")
    self.sendDummyData(self)
    # terminalControl.updateLoop()