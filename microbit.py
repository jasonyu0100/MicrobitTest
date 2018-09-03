class MicroBit:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.vx = 0
        self.vy = 0
        self.vz = 0
        self.acc = {'X':0,'Y':0,'Z':0}

    def applyAcceleration(self,x,y,z,time):
        self.vx += x*time
        self.vy += y*time
        self.vz += z*time
        self.x += vx*time
        self.y += vy*time
        self.z += vz*time

    def update(self,data,time):
        self.acc = data['acceleration']
        self.applyAcceleration(self.acc['X'],self.acc['Y'],self.acc['Z'],time)

    def setXYZ(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z


