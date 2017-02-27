import random

interval = random.randint(20, 40)

def getIntervalForAbnormalIssues():
    global interval
    return interval

def setNewIntervalForAbnormalIssues():
    global interval
    interval = random.randint(20, 40)
