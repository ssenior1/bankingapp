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
    minutesOfConsistentErrors = random.randint(15, 90)

    overallErrorClass = random.randint(1, 4)
    elementInErrorClassArray = random.randint(0, 4)

    for i in range(minutesOfConsistentErrors):

        createdAt = GetTime.getTime()
        avgNumberOfErrorsPerMinute = random.randint(10, 25)

        for j in range(avgNumberOfErrorsPerMinute):
            eventDict = se.postEvent(userName, apiToken, overallErrorClass, elementInErrorClassArray, createdAt)
            sm.sendMeasurements(userName, apiToken, eventDict, avgNumberOfErrorsPerMinute, createdAt)

# Commented out all the multi-threading during inital stages to make sure everything is working
#
#
#
#
#

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

    # _thread.exit()