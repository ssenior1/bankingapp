import random

interval = random.randint(40, 100)
print("Number of events before abnormal events start will be: " + str(interval))

def getIntervalForAbnormalIssues():
    global interval
    return interval

def setNewIntervalForAbnormalIssues():
    global interval
    interval = random.randint(60, 2500)
