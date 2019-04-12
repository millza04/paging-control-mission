class menu():
    def __init__(self, output):
        self.output = output

    def gatherInfo(self):
        inputFile = input("Enter the input file you wish to use? ")
        redAlerts = int(input("Number of red alerts? "))
        redTime = float(input("Time for those read alerts to occur(minutes)? "))
        yellowAlerts = int(input("Number of yellow alerts? "))
        yellowTime = float(input("Time for those yellow alerts to occur(minutes)? "))
        return [inputFile, redAlerts, redTime, yellowAlerts, yellowTime]
