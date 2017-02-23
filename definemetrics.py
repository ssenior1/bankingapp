# python 3 sample to create metric definitions
# importing the requests library, run "pip3 install requests" to install
import requests
import json
import randomdata

# api endpoint
METRICS_CREATE_URL = "https://api.truesight.bmc.com/v1/metrics"
HEADERS = {'Content-Type': 'application/json'}

''' Create a metric based on the dictionary passed '''
def createMetric(metricInfo, userName, apiToken):
    response = requests.post(METRICS_CREATE_URL,
        auth=(userName, apiToken), data=json.dumps(metricInfo), headers=HEADERS)
    if response.status_code == requests.codes.ok:
        print("Successfully created metric " + metricInfo["displayName"])
    else:
        print("Metric " + metricInfo["displayName"] +
            " not created, perhaps it already exists? " +
            "Error code:" + str(response.status_code))

def defineAllMetrics(userName, apiToken):

    createMetricDetails(userName, apiToken, "Location", randomdata.Customer.location)
    createMetricDetails(userName, apiToken, "Browser", randomdata.UsageDetails.browser)
    createMetricDetails(userName, apiToken, "Operating System", randomdata.UsageDetails.operatingSystem)
    createMetricDetails(userName, apiToken, "Portal", randomdata.UsageDetails.webPortalName)
    createMetricDetailsForTotal(userName, apiToken, "Total_login_issues")


def createMetricDetails (userName, apiToken, metricName, metricObject):

    for element in metricObject:
        metric = {
            "name": element,
            "type": "Login_Issue_Metrics",
            "description": "Issue has a " + metricName + " of " + element,
            "displayName": element,
            "displayNameShort": element,
            "unit": "number",
            "defaultAggregate": "AVG"
            }
        createMetric(metric, userName, apiToken)

def createMetricDetailsForTotal (userName, apiToken, metricName):

        metric = {
            "name": metricName,
            "type": "Login_Issue_Metrics",
            "description": "Total number of login issues",
            "displayName": "Total number of login issues",
            "displayNameShort": "Total number of login issues",
            "unit": "number",
            "defaultAggregate": "AVG"
            }
        createMetric(metric, userName, apiToken)