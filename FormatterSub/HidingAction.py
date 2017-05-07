#!/usr/bin/python3

from FormatterSub.Action import Action
# from PDMLSub.FieldElement import fieldelement
# from FormatterSub.RenamingAction import RenamingAction

class HidingAction(Action):
    def __init__(self, value, key):
    	super().__init__("hide",value,key)