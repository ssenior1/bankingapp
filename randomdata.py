import random
import datetime
import time
import GetTime
import uuid

class Customer:
    location = ['San_Francisco', 'San_Jose', 'Las_Vegas', 'Houston', 'Santa_Clara']

class UsageDetails:
    webPortalName = ['Bank_West', 'BankToGo', 'National_Bank', 'Point_Bank', 'Lighthouse_Bank']
    operatingSystem = ['Windows', 'Linux', 'MacOSX', 'iOS', 'Android', 'Other_OS']
    browser = ['Internet_Explorer', 'Google_Chrome', 'Safari', 'Mozilla_Firefox', 'Other_browser']

counter = 0
START_TIME = time.time()


def setCustomerAttributes(overallErrorClass, elementInErrorClassArray):

    customer = Customer()

    if overallErrorClass == 1:
        customer.location = Customer.location[elementInErrorClassArray]
    else:
        customer.location = Customer.location[random.randint(0, len(Customer.location)-1)]

    return customer


def setUsageAttributes(overallErrorClass, elementInErrorClassArray):

    usageDetails = UsageDetails()

    if overallErrorClass == 2:
        usageDetails.webPortalName = UsageDetails.webPortalName[elementInErrorClassArray]
    else:
        usageDetails.webPortalName = UsageDetails.webPortalName[random.randint(0, len(UsageDetails.webPortalName) - 1)]

    if overallErrorClass == 3:
        usageDetails.browser = UsageDetails.browser[elementInErrorClassArray]
    else:
        usageDetails.browser = UsageDetails.browser[random.randint(0, len(UsageDetails.browser) - 1)]

    if overallErrorClass == 4:
        usageDetails.operatingSystem = UsageDetails.operatingSystem[elementInErrorClassArray]
    else:
        usageDetails.operatingSystem = UsageDetails.operatingSystem[random.randint(0, len(UsageDetails.operatingSystem)-1)]

    return usageDetails


def getEventInfo(overallErrorClass, elementInErrorClassArray, createdAt):

    usageDetails = setUsageAttributes(overallErrorClass, elementInErrorClassArray)
    customer = setCustomerAttributes(overallErrorClass, elementInErrorClassArray)

    eventvalues = {
        "fingerprintFields": [
            "@title", "uid"
        ],
        "source": {
            "ref": "Login issue",
            "type": "LOGIN_ISSUE_METRICS"
        },
        "title": "Login issue for " + usageDetails.webPortalName + " by customer using " +
                 usageDetails.operatingSystem + " running " + usageDetails.browser + " located in "
            + customer.location,
        "createdAt":  createdAt,
        "eventClass": "Login_Issue_Metrics",
        "properties" : {
            "app_id": "BANK PORTALS",
            "web_portal_name" : usageDetails.webPortalName,
            "operating_system" : usageDetails.operatingSystem,
            "browser" : usageDetails.browser,
            "customer_location" : customer.location,
            "uid" : str(uuid.uuid1()),
        }
    }

    return eventvalues
