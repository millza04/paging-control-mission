def writer(file, satData, color):
    file.write("{satelliteId: "+satData.satId+",severity: \""+color+"\",component: \""+satData.comp.replace("\n", "")+"\",timestamp: \""+satData.time+"\"}")
    file.close()

def startFile(file):
    file.write("[")
    file.close()

def endFile(file):
    file.write("]")
    file.close()
