import serial
from .microbit import MicroBit

class TerminalControl:
    baudRate = 115200
    def __init__(self,port,leftMicroBit,rightMicroBit):
        '''
        Sets up serial communication
        '''
        self.serial = serial.Serial()
        self.port = port
        self.serial.port = port
        self.serial.baudrate = TerminalControl.baudRate
        self.leftMicroBit = leftMicroBit
        self.rightMicroBit = rightMicroBit
        self.calibrate()

    def writeToConsole(self,string):
        '''
        Writes string to console
        '''
        byteString = string.encode()
        self.serial.write(bytes(byteString))

    def parseData(self,str_data):
        return eval(str_data)

    def update(self,data):
        left = data['l']
        right = data['r']
        self.leftMicroBit.update(left)
        self.rightMicroBit.update(right)

if __name__ == '__main__':
    control = TerminalControl("COM5",MicroBit(),MicroBit())
    control.serial.open()
    control.writeToConsole("Hello World")

    while (True):
        data_str = control.serial.readline().decode("utf-8")
        parsed_data = control.parseData(data_str)
        control.update(parsed_data)