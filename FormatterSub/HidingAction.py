#!/usr/bin/python3

from FormatterSub.Action import Action
from PDMLSub.FieldElement import fieldelement
from FormatterSub.RenamingAction import RenamingAction

### This class is a bit useless since it does what renaimg does anyway
### For future note we may have to get rid of this class altogether if
### We cannont find another reason to have it
class HidingAction(Action):

    def getActionResult(self, target, attribute, value):
        renameObject = RenamingAction()
        return renameObject.getActionResult(target, attribute, value)
