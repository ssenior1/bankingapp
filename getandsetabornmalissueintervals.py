import random

interval = random.randint(60, 2500)

def getIntervalForAbnormalIssues():
    global interval
    return interval

def setNewIntervalForAbnormalIssues():
    global interval
    interval = random.randint(60, 2500)
    print("Number of events before abnormal events start will be: " + interval)
