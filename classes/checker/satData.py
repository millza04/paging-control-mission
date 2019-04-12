# Written by: Zachary Miller
# Date: 4/11/2019

class satData:
    def __init__(self, time, satId, redHigh, yellowHigh, redLow, yellowLow, redBreach, yellowBreach, data, comp):
        self.time = str(time)
        self.satId = satId
        self.redHigh = float(redHigh)
        self.yellowHigh = float(yellowHigh)
        self.redLow = float(redLow)
        self.yellowLow = float(yellowLow)
        self.redBreach = redBreach
        self.yellowBreach = yellowBreach
        self.data = float(data)
        self.comp = comp

    def toString(self):
        string = ""
        string += "Time: " + self.time
        string += "\nSat Id: " + self.satId
        string += "\nRed High: " + str(self.redHigh)
        string += "\nYellow High: " + str(self.yellowHigh)
        string += "\nRed Low: " + str(self.redLow)
        string += "\nYellow Low: " + str(self.yellowLow)
        string += "\nRed Breched: " + str(self.redBreach)
        string += "\nYellow Breched: " + str(self.yellowBreach)
        string += "\nData: " + str(self.data)
        string += "\nComp: " + self.comp
        string += "\n\n"
        return string


