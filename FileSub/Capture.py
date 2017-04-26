from Tshark_Handler import Tshark_Handler
class Capture:
    def createCapture(self, filePath):
        if(self.isCapture(filePath)):
            self.filePath = filePath
            if(self.isPDML(filePath) is False):
                self.filePath = Tshark_Handler().createPDML(filePath)
        else:
            self.filePath = None
        return self.filePath
    def __init__(self, filePath):
        return
    def isPDML(self,filePath):
        return filePath.lower().endswith('.pdml')
    def isCapture(self, filePath):
        return filePath.lower().endswith(('.pdml','.pcap','pcapng'))
    def getFilePath(self):
        return self.filePath