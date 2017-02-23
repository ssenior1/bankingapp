import random
import datetime
import time

class Customer:
    location = ['San_Francisco', 'San_Jose', 'Las_Vegas', 'Houston', 'Santa_Clara']

class UsageDetails:
    webPortalName = ['Bank_West', 'BankToGo', 'National_Bank', 'Point_Bank']
    operatingSystem = ['Windows', 'Linux', 'MacOSX', 'iOS', 'Android', 'Other_OS']
    browser = ['Internet_Explorer', 'Google_Chrome', 'Safari', 'Mozilla_Firefox', 'Other_browser']

def setCustomerAttributes(errorType):

    customer = Customer()

    if errorType == 1:
        customer.location = Customer.location[1]
    else:
        customer.location =  Customer.location[random.randint(0, len(Customer.location)-1)]

    return customer


def setUsageAttributes(errorType):

    usageDetails = UsageDetails()

    if errorType == 2:
        usageDetails.webPortalName = UsageDetails.webPortalName [3]
    else:
        usageDetails.webPortalName = UsageDetails.webPortalName[random.randint(0, len(UsageDetails.webPortalName) - 1)]
    if errorType == 3:
        usageDetails.browser = UsageDetails.browser[4]
    else:
        usageDetails.browser = UsageDetails.browser[random.randint(0, len(UsageDetails.browser) - 1)]

    usageDetails.operatingSystem = UsageDetails.operatingSystem[random.randint(0, len(UsageDetails.operatingSystem)-1)]

    return usageDetails


def getEventInfo(errorType):
    usageDetails = setUsageAttributes(errorType)
    customer = setCustomerAttributes(errorType)

    eventvalues = {
        "fingerprintFields": [
            "@title", "@createdAt"
        ],
        "source": {
            "ref": "Login issue",
            "type": "LOGIN_ISSUE_METRICS"
        },
        "title": "Login issue for " + usageDetails.webPortalName + " by customer using " +
                 usageDetails.operatingSystem + " running " + usageDetails.browser + " located in "
            + customer.location,
        "createdAt":  time.time(),
        "eventClass": "Login_Issue_Metrics",
        "properties" : {
            "app_id": "BANKING PORTAL",
            "web_portal_name" : usageDetails.webPortalName,
            "operating_system" : usageDetails.operatingSystem,
            "browser" : usageDetails.browser,
            "customer_location" : customer.location,
        }
    }

    return eventvalues
