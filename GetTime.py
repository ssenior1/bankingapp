import datetime
from datetime import timedelta
import time

counter = 0
start_time = time.time() - timedelta(days=28).total_seconds()

def getTime():
    global counter
    createdAtTime = start_time + (counter * 60)
    counter += 1


    return createdAtTime
