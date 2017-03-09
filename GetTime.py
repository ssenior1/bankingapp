import datetime
from datetime import timedelta
import time
import random

counter = 0
start_time = time.time() - timedelta(days=350).total_seconds()

def getTime():
    global counter
    createdAtTime = start_time + (counter * 60)
    counter += 1


    return createdAtTime
