import math, json
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
            self.clappingMonitor.checkClap()
            self.runningMonitor.checkStep()
            self.punchingMonitor.checkPunch()
            postData['CLAP'] = self.clappingMonitor.clapCount
            postData['RUN'] = self.runningMonitor.stepCount
            postData['PUNCHING'] = self.punchingMonitor.punchCount
            self.sendPOST(postData)
  
class RunningMonitor:
    def __init__(self):
        self.stepCount = 0
        pass
    
    def checkStep():
        pass

class PunchingMonitor:
    THRESHOLD = 0.5
    def __init__(self,rightMicroBit,leftMicroBit):
        self.punchCount = 0
        self.prev_acc_r = rightMicrobit.acc["x"] + rightMicrobit.acc["y"]
        self.prev_acc_l = leftMicrobit.acc["x"] + leftMicrobit.acc["y"]
        self.prev_z_l = leftMicrobit.z
        self.prev_z_r = rightMicrobit.z
        self.curr_acc_r = 0 
        self.curr_acc_l = 0

    def checkPunch(self,rightMicroBit,leftMicroBit):
        self.curr_acc_r = rightMicrobit.acc["x"] + rightMicrobit.acc["y"]
        self.curr_acc_l = leftMicrobit.acc["x"] + leftMicrobit.acc["y"]
        if self.curr_acc_l < -1*PunchingMonitor.THRESHOLD and self.prev_acc_l > PunchingMonitor.THRESHOLD and self.prev_z_l - leftMicrobit.z > PunchingMonitor.THRESHOLD:
            self.punchCount += 1
        if self.curr_acc_r < -1*PunchingMonitor.THRESHOLD and self.prev_acc_r > PunchingMonitor.THRESHOLD and self.prev_z_r - rightMicrobit.z > PunchingMonitor.THRESHOLD:
            self.punchCount += 1
        self.prev_acc_r = rightMicrobit.acc["x"] + rightMicrobit.acc["y"]
        self.prev_acc_l = leftMicrobit.acc["x"] + leftMicrobit.acc["y"]
        self.prev_z_l = leftMicrobit.z
        self.prev_z_r = rightMicrobit.z

class ClappingMonitor:
    THRESHOLD = 10
    def __init__(self):
        self.clapped = False
        self.clapCount = 0
    
    def checkClap(self,rightMicroBit,leftMicroBit):
        xDist = abs(rightMicroBit.pos['X'] - leftMicroBit.pos['X'])
        yDist = abs(rightMicroBit.pos['Y'] - leftMicroBit.pos['Y'])
        zDist = abs(rightMicroBit.pos['Z'] - leftMicroBit.pos['Z'])
        totalDistance = math.sqrt(xDist ** 2 + yDist ** 2 + zDist ** 2)
        if totalDistance <= self.THRESHOLD and self.clapped==False:
            self.clapped=True
            self.clapCount += 1
        elif totalDistance > self.THRESHOLD and self.clapped==True:
            self.clapped=False
