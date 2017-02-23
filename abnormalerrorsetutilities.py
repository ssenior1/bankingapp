import sendevents as se
import sendmeasurements as sm
import random
import time
import _thread

# api endpoint
EVENT_SEND_URL = "https://api.truesight.bmc.com/v1/events"
HEADERS = {'Content-Type': 'application/json'}

def CreateAbnormalErrorSet(userName, apiToken, createError):
    numberOfConsistentErrors = random.randint(500, 1000)
    numberOfEventsSent = 0
    abnormalErrorSetInterval = random.uniform(0.25,0.75)
    timeofLastAbnormalError = time.time()

    while numberOfEventsSent <= numberOfConsistentErrors:

        if time.time() >= (timeofLastAbnormalError + abnormalErrorSetInterval):
            timeofLastAbnormalError = time.time()
            abnormalErrorSetInterval = random.uniform(0.25,0.75)
            eventDict = se.postEvent(userName, apiToken, createError)
            numberOfEventsSent += 1

            sm.sendMeasurements(userName, apiToken, eventDict)

    _thread.exit()