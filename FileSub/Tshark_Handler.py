from subprocess import call
import os

class Tshark_Handler:
    def createPDML(filePath):
        basename = (os.path.splitext(filePath)[0])
        with open(basename+".pdml", 'w') as f:
            call(["tshark","-r","rand.pcapng","-T","pdml"], stdout=f)
    def __init__(self):
        return
# filePath = 'rand.pcapng'
# basename = (os.path.splitext(filePath)[0])
# with open(basename+".pdml", 'w') as f:
#   call(["tshark","-r","rand.pcapng","-T","pdml"], stdout=f)