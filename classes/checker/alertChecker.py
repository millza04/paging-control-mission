# Written by: Zachary Miller
# Date: 4/11/2019
# Purpose: This class takes in a single sattelite reading and determines
# if an alert should be generated. This is accomplished by loading it
# into a dictionary with previous reading, checking if an alert should
# be created. Then push out the older reading

from classes.checker import satData
from classes.helpers.helper import *

class checkAlert:
    def __init__(self, redAlerts, redTime, yellowAlerts, yellowTime):
        # Number of red values out of range before alert
        self.redAlerts = redAlerts
        # Time range for red alerts to occur
        self.redTime = redTime
        # Number of yellow values out of range before alert
        self.yellowAlerts = yellowAlerts
        # Time range for yellow alerts to occur
        self.yellowTime = yellowTime
        # This is the list which will be auto updated as we go through
        # The list will contain satData objects in it
        self.masterList = {}

    def getMasterList(self):
        return self.masterList

    def addAndCheckSatData(self, satData):
        # Check if this current satData throws an alert
        if (satData.redHigh < satData.data or satData.redLow > satData.data):
            satData.redBreach = True

        if (satData.yellowHigh < satData.data or satData.yellowLow > satData.data):
            satData.yellowBreach = True
        # Check if current satData was already added to masterList
        # If yes, append satData to the current satData
        if (satData.satId in self.masterList):
            self.masterList[satData.satId].append(satData)
        # If no, add satData to list
        else:
            self.masterList[satData.satId] = [satData]
        
        # Not that the value is added to our list we have to take that list and
        # of previous sat data and check to see if we need to throw an alert
        return self.checkSatDataList(satData.satId)


    # This function takes the list of satData, checks how many have thrown an
    # alert and in what time frame and returns satId that triggered the
    # alert. Otherwise it returns null
    def checkSatDataList(self, satId):
        satDataList = self.masterList[satId]
        rCount = 0
        yCount = 0
        redAlert = False
        yellowAlert = False
        for satData in satDataList:
            if (satData.redBreach == True):
                rCount += 1
            if (satData.yellowBreach == True):
                yCount += 1
        
        # If we are over our allowed time frame, remove the oldest value from the list
        if (findTimeDifference(self.masterList[satId]) > (self.redTime * 60) and len(self.masterList[satId]) != 1):
            del self.masterList[satId][0]
            
        # If our number of alerts is above our threshold
        if (rCount > self.redAlerts):
            # check to make sure time difference between alerts is under our limit
            if (findTimeDifference(self.masterList[satId]) < (self.redTime * 60)):
                redAlert = True
            
            
        if (yCount > self.yellowAlerts):
            # check to make sure time difference between alerts is under our limit
            if (findTimeDifference(self.masterList[satId]) < (self.yellowTime * 60)):
                yellowAlert = True

        
        if (redAlert == True):
            return (self.masterList[satId][len(self.masterList[satId]) - 1], "red")
        if (yellowAlert == True):
            return (satId, "yellow")
        else:
            return ""

    
