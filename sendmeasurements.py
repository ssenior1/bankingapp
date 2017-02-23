# python 3 sample to create metric definitions
# importing the requests library, run "pip3 install requests" to install
import requests
import json
import time
import randomdata
import _thread

# api endpoint
MEASURES_ADD_URL = "https://api.truesight.bmc.com/v1/measurements"
HEADERS = {'Content-Type': 'application/json'}


def sendMeasurements(userName, apiToken, eventDict):
    currentTime = round(time.time())

    location_dict = getMeasureDict("Total numberof login issues", "Login issue", currentTime)
    _thread.start_new_thread(multiThreadedPostMeasures, (location_dict, userName, apiToken))

    location_dict = getMeasureDict(eventDict["properties"]["customer_location"], "Login issue", currentTime)
    _thread.start_new_thread(multiThreadedPostMeasures, (location_dict, userName, apiToken))

    web_portal_dict = getMeasureDict(eventDict["properties"]["web_portal_name"], "Login issue", currentTime)
    _thread.start_new_thread(multiThreadedPostMeasures, (web_portal_dict, userName, apiToken))

    operating_system_dict = getMeasureDict(eventDict["properties"]["operating_system"], "Login issue", currentTime)
    _thread.start_new_thread(multiThreadedPostMeasures, (operating_system_dict, userName, apiToken))

    browser_dict = getMeasureDict(eventDict["properties"]["browser"], "Login issue", currentTime)
    _thread.start_new_thread(multiThreadedPostMeasures, (browser_dict, userName, apiToken))


def getMeasureDict(metricName, sourceName, timeStamp):
    measurement_dict = {
        "source" : sourceName,
        "metric" : metricName,
        "measure" : 1,
        "timestamp" : timeStamp,
        "metadata" : {
            "app_id" : "BANKING PORTAL"
        }
    }
    return measurement_dict

def multiThreadedPostMeasures(measureDict, userName, apiToken):
    response = requests.post(MEASURES_ADD_URL,
        auth=(userName, apiToken), data=json.dumps(measureDict), headers=HEADERS)
    if response.status_code == requests.codes.ok:
        print("Successfully sent measurement " + measureDict["metric"] +
            " for source " + measureDict["source"] + " @ time:" +
            str(measureDict["timestamp"]))
    else:
        print("Unable to send measurement " + measureDict["metric"] +
            " for source " + measureDict["source"] + " @ time:" +
            str(measureDict["timestamp"]) + " Error code:" + str(response.status_code))
