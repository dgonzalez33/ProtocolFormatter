import subprocess
class Script:
    def applyScript(self):
        # One way
        scriptCall = list()
        scriptCall.append("python")
        scriptCall.append(self.scriptPath)
        scriptCall.extend(self.arguments)
        fieldValue = subprocess.check_output(scriptCall).decode("utf-8").rstrip()
#         print(fieldValue)
        return fieldValue

    def __init__(self, scriptPath, arguments):
        self.scriptPath = scriptPath
        self.arguments = arguments

# script = Script('test.py',[])
# script.applyScript()