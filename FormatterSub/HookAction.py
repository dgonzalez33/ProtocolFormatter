from FormatterSub.Action import Action
from PDMLSub.FieldElement import fieldelement
from FileSub.Script import Script


class HookAction(Action):
    arguments = []

    def __init__(self, scriptPath, arguments):
        self.scriptPath = scriptPath
        self.arguments = arguments
    def addArgument(self, attribute, value):
        self.arguments.append(attribute)
        self.arguments.append(value)
    def getArguments(self):
        return self.arguments

    def getActionResult(self, target):
        #Still need to parse through what script returns
        #format is: "attribute\r\nvalue..."
        hook = Script(self.scriptPath, self.arguments)
        resultString = hook.applyScript()
        #parse result string here, change attribute and value found and return
        #new target
        newtarget = self.copyfieldelement(target)
        if newtarget.set_field_attrib(arguments[0], arguments[1]) == -1:
            newtarget.set_field_attrib(arguments[0], arguments[1])
        return newtarget
