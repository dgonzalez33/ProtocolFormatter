#!/usr/bin/python3
from FormatterSub.Action import Action
from PDMLSub.FieldElement import fieldelement
class RenamingAction(Action):

        def getActionResult(self, target, attribute, value):
            #print(target)
            #index = target.find(attribute)
            #index = target.find("\"",index,len(target))
            #index2 = target.find("\"",index+1,len(target))
            #newString = target[:index+1] + value + target[index2:]
            #return newString
            newFieldElem = fieldelement()
            oldAttrib = target.get_field_attributes()
            for key in oldAttrib:
                newFieldElem.set_field_attrib(key, oldAttrib[key])
            newFieldElem.set_field_attrib(attribute, value)
            return newFieldElem
