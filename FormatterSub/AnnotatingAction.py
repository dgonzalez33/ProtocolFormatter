#!/usr/bin/python3

from FormatterSub.Action import Action
from PDMLSub.FieldElement import fieldelement

class AnnotatingAction(Action):

    def getActionResult(self, target, attribute, value):
        renameObject = RenamingAction();

        return renamingObject.getActionResult(target, attribute, value)
