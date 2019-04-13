# Written by: Zachery Miller
# Date: 4/11/2019
# Purpose: See ReadMe.md

from classes.menu.mainMenu import menu
from classes.checker.alertChecker import checkAlert
from classes.checker.satData import satData
from classes.helpers.lineBreaker import *
from classes.writer.fileWrite import *

# call menu
mainMenu = menu("output/output.txt")

# get return from menu and get file object
inputFile, redAlerts, redTime, yellowAlerts, yellowTime = mainMenu.gatherInfo()
#inputFile, redAlerts, redTime, yellowAlerts, yellowTime = ["input.txt", 3, 5, 0, 0]


# Instantiate our checkAlert class
checkAlert = checkAlert(redAlerts, redTime, yellowAlerts, yellowTime)
startFile(open("output/output.txt", "a"))

# For each line of file
with open(("input/" + inputFile)) as f:
    for line in f:
        time, satId, rMax, yMax, rMin, yMin, value, comp = breakString(line)
        comp.replace("\n", "")
        # Load data in and check the alert
        # Returns the string to be output as alert, if no alert return empty string
        result = checkAlert.addAndCheckSatData(satData(time, satId, rMax, yMax, rMin, yMin, False, False, value, comp))
        if (result != ""):
            # Call output class to print out data
            writer(open("output/output.txt", "a"), result[0], result[1])

    


# Close files and terminate
endFile(open("output/output.txt", "a"))
