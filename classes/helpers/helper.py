# Given a satDataList, this finds the largest time difference between the
# data elements

import time
import datetime

def findTimeDifference(satDataList):
    # Get the first and last element of the list
    firstSatData = satDataList[0]
    endSatData = satDataList[len(satDataList) - 1]
    # Find the difference between the two values
    startDate = datetime.datetime.strptime(firstSatData.time, "%Y%m%d %H:%M:%S.%f").timetuple()
    endDate = datetime.datetime.strptime(endSatData.time, "%Y%m%d %H:%M:%S.%f").timetuple()

    elapsedTime = time.mktime(endDate) - time.mktime(startDate)
    return elapsedTime    




     
