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
        self.serial.write(bytes(string))

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


class MicroBit:
    def __init__(self):
        '''
        XYZ is located at user's chest
        '''
        self.x = 0
        self.y = 0
        self.z = 0

    def applyAcceleration(self,x,y,z,time):
        '''
        Finds acceleration of all values at a given time and updates values
        '''
        self.x += x*time
        self.y += y*time
        self.z += z*time

    def setXYZ(self,x,y,z):
        '''
        Sets XYZ directly through values
        '''
        self.x = x
        self.y = y
        self.z = z

        

control = TerminalControl("COM5",[])
control.writeToConsole("Hello World")

    

        
