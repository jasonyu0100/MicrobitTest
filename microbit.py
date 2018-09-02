class MicroBit:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def applyAcceleration(self,x,y,z,time):
        self.x += x*time
        self.y += y*time
        self.z += z*time

    def update(self,data,time):
        acceleration = data['acceleration']
        self.applyAcceleration(acceleration['X'],acceleration['Y'],acceleration['Z'],time)

    def setXYZ(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
