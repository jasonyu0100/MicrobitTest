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
        byteString = string.encode()
        self.serial.write(bytes(byteString))

    def calibrate(self):
        '''
        Resets origin point of microbit
        '''
        x,y,z = 0,0,0
        for microbit in self.microbits:
            microbit.setXYZ(x,y,z)
        pass

if __name__ == '__main__':
    control = TerminalControl("COM5",[])
    control.serial.open()
    control.writeToConsole("Hello World")

    while (True):
    if (control.serial.inWaiting()>0): #if incoming bytes are waiting to be read from the serial input buffer
        data_str = ser.read(ser.inWaiting()).decode('ascii') #read the bytes and convert from binary array to ASCII
        print(data_str, end='') #print the incoming string without putting a new-line ('\n') automatically after every print()
    #Put the rest of your code you want here

'''
class ReadLine:
    def __init__(self, s):
        self.buf = bytearray()
        self.s = s
    
    def readline(self):
        i = self.buf.find(b"\n")
        if i >= 0:
            r = self.buf[:i+1]
            self.buf = self.buf[i+1:]
            return r
        while True:
            i = max(1, min(2048, self.s.in_waiting))
            data = self.s.read(i)
            i = data.find(b"\n")
            if i >= 0:
                r = self.buf + data[:i+1]
                self.buf[0:] = data[i+1:]
                return r
            else:
                self.buf.extend(data)
'''
        
