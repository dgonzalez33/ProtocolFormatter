#!/usr/bin/python3

from FormatterSub.Action import Action
# from PDMLSub.FieldElement import fieldelement
# from FormatterSub.RenamingAction import RenamingAction

class HidingAction(Action):

    def __init__(self,value):
        super().__init__("Hiding", value)

    def getActionResult(self, target):
        return super().getActionResult(target)
