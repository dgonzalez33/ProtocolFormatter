import subprocess
class Script:
    def applyScript(self): 
    	scriptCall = list()
    	scriptCall.append("python")
    	scriptCall.append(self.scriptPath)
    	scriptCall.extend(self.arguments)
    	field = subprocess.check_output(scriptCall).decode("utf-8").rstrip()
    	print(repr(field))

    def __init__(self, scriptPath, arguments):
    	self.scriptPath = scriptPath
    	self.arguments = arguments

script = Script('testScript.py',[])
script.applyScript()