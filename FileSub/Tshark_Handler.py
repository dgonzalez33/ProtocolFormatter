from subprocess import call
import os

class Tshark_Handler:
    def createPDML(self, filePath):
        basename = (os.path.splitext(filePath)[0])
        with open(basename+".pdml", 'w') as f:
            call(["tshark","-r",filePath,"-T","pdml"], stdout=f)
        return basename+".pdml"
    def __init__(self):
        return
