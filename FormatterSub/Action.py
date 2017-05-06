#!/usr/bin/python3
from PDMLSub.FieldElement import fieldelement

class Action:
    def __init__ (self, attribute, value, key):
        self.attribute = attribute
        self.value = value
        self.key = key

    def setAttrib(self, attribute):
        self.attribute = attribute

    def getAttrib(self):
        return self.attribute

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value
    def getKey(self):
    	return self.key
    def copyfieldelement(self, target):
        newtarget = fieldelement()
        for i in list(range(target.get_field_attributes_length())):
            newtarget.set_field_attrib(target.get_field_attributes_name(i), target.get_field_attributes_value(i))
        return newtarget

    def getActionResult(self, target):
        newtarget = self.copyfieldelement(target)
        if newtarget.set_field_attrib(self.attribute, self.value) == -1:
            newtarget.set_field_attrib(self.attribute, self.value)
        return newtarget
