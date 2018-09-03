import math
from microbit import MicroBit
import urllib.request,urllib.parse

'''
All of these monitors review data and check for a certain activity 
ie clapping monitor would count the amount of claps made within a period of time
The activity control would send data to the server to be used 
'''

class ActivityControl:
    def __init__(self,serverURL):
        self.serverURL = serverURL
        self.runningMonitor = RunningMonitor()
        self.punchingMonitor = PunchingMonitor()
        self.clappingMonitor = ClappingMonitor()

    def sendPOST(self,postData):
        serverRequestURL = self.serverURL + 'receive_data'
        jsonPost = json.dumps(postData)
        byteJsonPost = bytes(jsonPost,"ascii")
        urllib.request.urlopen(serverRequestURL,data=byteJsonPost)

    def postLoop(self):
        while (True):
            postData = {'CLAP':0,'RUN':0,'PUNCHING':0}
            postData['CLAP'] = self.clappingMonitor.clapCount
            postData['RUN'] = self.runningMonitor.stepCount
            postData['PUNCHING'] = self.punchingMonitor.punchCount
            self.sendPOST(postData)
  
class RunningMonitor:
    def __init__(self):
        self.stepCount = 0
        pass

    def checkStep(self):
        pass

class PunchingMonitor:
    def __init__(self):
        self.punchCount = 0

    def checkPunch(self):
        pass

class ClappingMonitor:
    THRESHOLD = 10
    def __init__(self):
        self.clapped = False
        self.clapCount = 0
    
    def checkClap(self,rightMicroBit,leftMicroBit):
        xDist = abs(rightMicroBit.x - leftMicroBit.x)
        yDist = abs(rightMicroBit.y - leftMicroBit.y)
        zDist = abs(rightMicroBit.z - leftMicroBit.z)
        totalDistance = math.sqrt(xDist ** 2 + yDist ** 2 + zDist ** 2)
        if totalDistance <= self.THRESHOLD and self.clapped==False:
            self.clapped=True
            self.clapCount += 1
        elif totalDistance > self.THRESHOLD and self.clapped==True:
            self.clapped=False