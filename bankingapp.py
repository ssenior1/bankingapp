import sendmeasurements as sm
import sendevents as se
import abnormalerrorsetutilities
import definemetrics as dm
import random
import argparse
import _thread
import GetTime
import getandsetabornmalissueintervals

# Help for the CLI
parser = argparse.ArgumentParser(description='Sample integration with TrueSight Intelligence')
parser.add_argument('--email', help='Your TrueSight Intelligence account email', required=True)
parser.add_argument('--api', help='Your TrueSight Intelligence API token', required=True)
parser.add_argument('--freq', help='Polling frequency, defaults to 10 secs', default=10)

# get the values passed via CLI
args = parser.parse_args()
userName = args.email
apiToken = args.api
pollingFrequency = args.freq

# Metadata definition for the metrics, this will create the metric definitions
# if they do not exist
dm.defineAllMetrics(userName, apiToken)

NON_CONSISTENT_ERROR_TYPE = 0

# Live action - push random errors in an ongoing basis
# at random intervals, also start sending consistent error messages (still with the random errors at the same speed)
counter = 0

while True:
    createdAt = GetTime.getTime()
    numberOfErrors = random.randint(1, 7)
    for i in range(numberOfErrors):
        eventDict = se.postEvent(userName, apiToken, NON_CONSISTENT_ERROR_TYPE, NON_CONSISTENT_ERROR_TYPE, createdAt)
        sm.sendMeasurements(userName, apiToken, eventDict, numberOfErrors, createdAt)
        print(str(counter))
        counter += 1


# Commented out the abnormal issues section of the code during testing to make sure normal events hit the API
#
#
#
#
#
#

    # counter += 1

# if the abnormality interval is the same as the number of errors sent so far, start sending abnormal errors
#     if (getandsetabornmalissueintervals.getIntervalForAbnormalIssues()) / counter == 1:
        # abnormalerrorsetutilities.CreateAbnormalErrorSet(userName, apiToken)
        # # _thread.start_new_thread(abnormalerrorsetutilities.CreateAbnormalErrorSet, (userName, apiToken))
        # getandsetabornmalissueintervals.setNewIntervalForAbnormalIssues()
        # counter = 0


# Previous way of setting timing for errors - moved to counter for further simplicity.

# if time.time() >= (timeOfLastStandardError + standardErrorInterval):
    #     createdAt = GetTime.getTime()
    #     eventDict = se.postEvent(userName, apiToken, NON_CONSISTENT_ERROR_TYPE, 0, createdAt)
    #     timeOfLastStandardError = time.time()
    #     standardErrorInterval = random.uniform(10, 30)
    #     numberOfErrors = random.randint(1, 5)
    #     sm.sendMeasurements(userName, apiToken, eventDict, numberOfErrors, createdAt)
    #
    # if time.time() >= (timeOfLastAbnormalErrorSet + abnormalErrorSetInterval):
    #     timeOfLastAbnormalErrorSet = time.time()
    #     abnormalErrorSetInterval = random.randint(3600, 172800)
    #     _thread.start_new_thread(abnormalerrorsetutilities.CreateAbnormalErrorSet, (userName, apiToken))



