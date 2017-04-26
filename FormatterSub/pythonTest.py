#!/usr/bin/python3
from RenamingAction import RenamingAction
from HidingAction import HidingAction
# def replaceMethod(testString, field, newValue):

#
# testString = "<FirstName = 'ezequiel' LastName = 'Rios' Age = '21' BDay = '05/01/95'>"
# newString = replaceMethod(testString, "LastName", "hello!! :)")
#
# print(newString)

renamingObject = RenamingAction()
hidingObject = HidingAction()
testString = "<FirstName = \"ezequiel\" LastName = \"rios\" Age = \"21\" BDay = \"05/01/95\" Hidden=\"false\">"
print(testString)
attribute = "LastName"
value = "Lopez"
newString = renamingObject.getActionResult(testString, attribute, value)
print(newString)
newString = hidingObject.getActionResult(newString, "Hidden", "true")
print(newString)
