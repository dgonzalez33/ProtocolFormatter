#!/usr/bin/python3
from PDMLSub.FieldElement import fieldelement

class Action:
    def __init__ (self, attribute, value):
        self.attribute = attribute
        self.value = value

    def setAttrib(self, attribute):
        self.attribute = attribute

    def getAttrib(self):
        return self.attribute

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def getActionResult(self, target):
        newFieldElem = fieldelement()
        oldAttrib = target.get_field_attributes()
        for key in oldAttrib:
            newFieldElem.set_field_attrib(key, oldAttrib[key])
        newFieldElem.set_field_attrib(self.attribute, self.value)
        return newFieldElem
