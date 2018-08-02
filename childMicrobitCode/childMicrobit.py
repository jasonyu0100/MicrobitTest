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

    def getData(self,data):
        return data