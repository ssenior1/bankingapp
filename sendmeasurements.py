# python 3 sample to create metric definitions
# importing the requests library, run "pip3 install requests" to install
import requests
import json
import time
import _thread
import GetTime

# api endpoint
MEASURES_ADD_URL = "https://api.truesight.bmc.com/v1/measurements"
HEADERS = {'Content-Type': 'application/json'}

START_TIME = time.time()
counter = 0


def sendMeasurements(userName, apiToken, eventDict, numberOfErrors, createdAt):
    global counter

    location_dict = getMeasureDict("Total_login_issues", "Login issue", numberOfErrors, createdAt)
    _thread.start_new_thread(multiThreadedPostMeasures, (location_dict, userName, apiToken))

    location_dict = getMeasureDict(eventDict["properties"]["customer_location"], "Login issue",numberOfErrors, createdAt)
    _thread.start_new_thread(multiThreadedPostMeasures, (location_dict, userName, apiToken))

    web_portal_dict = getMeasureDict(eventDict["properties"]["web_portal_name"], "Login issue", numberOfErrors, createdAt)
    _thread.start_new_thread(multiThreadedPostMeasures, (web_portal_dict, userName, apiToken))

    operating_system_dict = getMeasureDict(eventDict["properties"]["operating_system"], "Login issue", numberOfErrors, createdAt)
    _thread.start_new_thread(multiThreadedPostMeasures, (operating_system_dict, userName, apiToken))

    browser_dict = getMeasureDict(eventDict["properties"]["browser"], "Login issue", numberOfErrors, createdAt)
    _thread.start_new_thread(multiThreadedPostMeasures, (browser_dict, userName, apiToken))

    counter += 1
    return counter


def getMeasureDict(metricName, sourceName, numberOfErrors, createdAt):
    measurement_dict = {
        "source" : sourceName,
        "metric" : metricName,
        "measure" : numberOfErrors,
        "timestamp" : createdAt,
        "metadata" : {
            "app_id" : "BANK PORTALS"
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
