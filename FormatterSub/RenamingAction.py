#!/usr/bin/python3
from Action import Action
class RenamingAction(Action):

        def getActionResult(self, target, attribute, value):
            print(target)
            index = target.find(attribute)
            index = target.find("\"",index,len(target))
            index2 = target.find("\"",index+1,len(target))
            newString = target[:index+1] + value + target[index2:]
            return newString
