import random

interval = random.randint(200, 6000)
print("Number of events before abnormal events start will be: " + str(interval))

def getIntervalForAbnormalIssues():
    global interval
    return interval

def setNewIntervalForAbnormalIssues():
    global interval
    interval = random.randint(200, 6000)
