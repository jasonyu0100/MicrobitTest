import serial

class TerminalControl:
    baudRate = 115200
    def __init__(self,port,microbits):
        '''
        Sets up serial communication
        '''
        self.serial = serial.Serial()
        self.port = port
        self.serial.port = port
        self.serial.baudrate = TerminalControl.baudRate
        self.microbits = microbits
        self.calibrate()

    def writeToConsole(self,string):
        '''
        Writes string to console
        '''
        byteString = string.encode()q
        self.serial.write(bytes(byteString))

    def calibrate(self):
        '''
        Resets origin point of microbit
        '''
        x,y,z = 0,0,0
        for microbit in self.microbits:
            microbit.setXYZ(x,y,z)
        pass

    def getDistance(self,microbitData1,microbitData2):
        pass


    def clappingFunction(self):
        '''
        Get histories of microbits and calcualte claps from there
        '''
        return

    def getData(self,microbitData):
        return microbitData

if __name__ == '__main__':
    control = TerminalControl("COM5",[])
    control.serial.open()
    control.writeToConsole("Hello World")
    byteString = serial.readline()
    print(byteString)

    

        
