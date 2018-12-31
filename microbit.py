class MicroBit:
	time = 50
    def __init__(self,time):
    	self.time = time
    	self.pos = {'X':0,'Y':0,'Z':0}
    	self.vel = {'X':0,'Y':0,'Z':0}
        self.acc = {'X':0,'Y':0,'Z':0}

    def updateVelocity(self):
        self.vel['X'] += self.acc['X'] * self.time
        self.vel['Y'] += self.acc['Y'] * self.time
        self.vel['Z'] += self.acc['Z'] * self.time

    def updatePosition(self):
        self.pos['X'] += self.vel['X'] * self.time
        self.pos['Y'] += self.vel['Y'] * self.time
        self.pos['Z'] += self.vel['Z'] * self.time

    def update(self,data):
        self.acc = data['acceleration']
        self.updateVelocity()
        self.updatePosition()

    def setXYZ(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z


