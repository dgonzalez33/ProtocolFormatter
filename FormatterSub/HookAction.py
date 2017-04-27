from FormatterSub.Action import Action
from PDMLSub.FieldElement import fieldelement
from FileSub.Script import Script
from FormatterSub.RenamingAction import RenamingAction

class HookAction(Action):
    scriptPath = ""

    def __init__(self, scriptPath):
        self.scriptPath = scriptPath

    def getActionResult(self, target, attribute, value):
        #waiting on script implementation to be finished
        #but basically this is what is going to happen
        hook = Script(scriptPath, argument = [attribute, target.get_field_attributes()[attribute]])
        renamingObject = RenamingAction()

        return renamingObject.getActionResult(target, attribute, hook.applyScript())
