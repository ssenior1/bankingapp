import sendevents as se
import sendmeasurements as sm
import random
import time
import _thread

# api endpoint
EVENT_SEND_URL = "https://api.truesight.bmc.com/v1/events"
HEADERS = {'Content-Type': 'application/json'}

def CreateAbnormalErrorSet(userName, apiToken):
    numberOfConsistentErrors = random.randint(100, 300)
    avgNumberOfErrorsPerMinute = random.randint(10, 50)
    numberOfEventsSent = 0
    abnormalErrorSetInterval = random.uniform(1,3)
    timeofLastAbnormalError = time.time()

    while numberOfEventsSent <= numberOfConsistentErrors:

        overallErrorClass = random.randint(1, 4)
        elementInErrorClassArray = random.randint(0, 4)

        if time.time() >= (timeofLastAbnormalError + abnormalErrorSetInterval):
            timeofLastAbnormalError = time.time()
            abnormalErrorSetInterval = random.uniform(1,3)
            eventDict = se.postEvent(userName, apiToken, overallErrorClass, elementInErrorClassArray)
            numberOfEventsSent += 1

            sm.sendMeasurements(userName, apiToken, eventDict, avgNumberOfErrorsPerMinute)

    _thread.exit()