#!/usr/bin/python3

from Action import Action

class HidingAction(Action):

    def getActionResult(self, target, attribute, value):
        index = target.find(attribute)
        if index == -1:
            index = target.find(">")
            newString = target[:index] + " Hidden=\""+value+"\""+target[index:]
        else:
            index = target.find("\"",index,len(target))
            index2 = target.find("\"",index+1,len(target))
            newString = target[:index+1] + value + target[index2:]
        return newString
