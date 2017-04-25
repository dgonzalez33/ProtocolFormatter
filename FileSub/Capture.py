from Tshark_Handler import Tshark_Handler
class Capture:
    def isPDML(filePath):
        filePath.lower().endswith('.pdml')
    def __init__(self, filePath):
        self.filePath = filePath
        if(isPDML(filePath) is False):
            self.filePath = createPDML(filePath)
    