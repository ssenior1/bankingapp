import random

interval = random.randint(60, 2500)

def getIntervalForAbnormalIssues():
    global interval
    return interval

def setNewIntervalForAbnormalIssues():
    global interval
    interval = random.randint(60, 2500)
