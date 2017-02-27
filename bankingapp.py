import sendmeasurements as sm
import sendevents as se
import abnormalerrorsetutilities
import definemetrics as dm
import time
import random
import argparse
import _thread
import GetTime

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
# dm.defineAllMetrics(userName, apiToken)

NON_CONSISTENT_ERROR_TYPE = 0

# timeOfLastStandardError = time.time()
# standardErrorInterval = 0
#
# abnormalErrorSetInterval = random.randint(1, 3)
# timeOfLastAbnormalErrorSet = time.time()

numberOfErrors = random.randint(1, 5)
counter = 0

# Live action - push random errors in an ongoing basis
# at random intervals, also start sending consistent error messages (still with the random errors at the same speed)

while True:
    # Measurement data for the login issues

    createdAt = GetTime.getTime()
    eventDict = se.postEvent(userName, apiToken, NON_CONSISTENT_ERROR_TYPE, 0, createdAt)
    sm.sendMeasurements(userName, apiToken, eventDict, numberOfErrors, createdAt)

    if counter == random.randint(600, 1000):
        _thread.start_new_thread(abnormalerrorsetutilities.CreateAbnormalErrorSet, (userName, apiToken))
        counter = 0

    counter += 1


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



