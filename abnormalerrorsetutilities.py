import sendevents as se
import sendmeasurements as sm
import random
import time
import _thread
import GetTime
# api endpoint
EVENT_SEND_URL = "https://api.truesight.bmc.com/v1/events"
HEADERS = {'Content-Type': 'application/json'}

def CreateAbnormalErrorSet(userName, apiToken):
    minutesOfConsistentErrors = random.randint(30, 90)

    overallErrorClass = random.randint(1, 4)
    elementInErrorClassArray = random.randint(0, 4)

    for i in range(minutesOfConsistentErrors):

        createdAt = GetTime.getTime()
        avgNumberOfErrorsPerMinute = random.randint(20, 60)

        for j in range(avgNumberOfErrorsPerMinute):
            eventDict = se.postEvent(userName, apiToken, overallErrorClass, elementInErrorClassArray, createdAt)

        sm.sendMeasurements(userName, apiToken, eventDict, avgNumberOfErrorsPerMinute, createdAt)



    # while numberOfEventsSent <= minutesOfConsistentErrors:
    #
    #
    #
    #     timeofLastAbnormalError = time.time()
    #     abnormalErrorSetInterval = random.uniform(1,3)
    #     numberOfEventsSent += 1


        # if time.time() >= (timeofLastAbnormalError + abnormalErrorSetInterval):
        #     createdAt = GetTime.getTime()
        #     timeofLastAbnormalError = time.time()
        #     abnormalErrorSetInterval = random.uniform(1,3)
        #     eventDict = se.postEvent(userName, apiToken, overallErrorClass, elementInErrorClassArray, createdAt)
        #     numberOfEventsSent += 1
        #
        #     sm.sendMeasurements(userName, apiToken, eventDict, avgNumberOfErrorsPerMinute, createdAt)

    _thread.exit()