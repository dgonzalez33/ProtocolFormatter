from FormatterSub.Rule import Rule
from PDMLSub.PDMLManager import pdmlmanager
from FormatterSub.Action import Action
from FormatterSub.RenamingAction import RenamingAction
from FormatterSub.HidingAction import HidingAction
from FormatterSub.Tracker import Tracker
from pathlib import Path
from FileSub.Capture import Capture
import pickle
import os.path as osp
class Formatter:
    def __init__(self, pdml, formatterName):
        self.pdml = pdml
        self.formatterName = formatterName
        self.ruleList = []
        if Path(osp.abspath('../FormatterSub/Formatters/')+"/"+self.formatterName+'.obj').is_file():
            self.loadFormatter()
        self.tracker = Tracker()
        return
    def applyFormatter(self):

        for rule in self.ruleList:
            self.tracker.recordsChanges(rule.applyRule(self.pdml))
        self.saveFormatter()
    def addRule(self, rule):
        self.ruleList.append(rule)
        return
    def undoRule(self):
        self.tracker.undoLastChange()
        self.ruleList.pop()
    def removeRule(self):
        self.ruleList.pop()
    def get_rules_in_string(self):
        stringList = []
        ruleNum = 1
        for rule in self.ruleList:
            rowString = "Rule "+str(ruleNum)
            rowString += " <"+ rule.getFilterName()+">"
            for action in rule.getActions():
                rowString += " <"+ type(action).__name__+">"
            stringList.append(rowString)
            ruleNum+=1
        return stringList
    def get_rules(self):
        return self.ruleList
    def getChangeForm():
        return changeForm
    def saveFormatter(self):
        with open(osp.abspath('../FormatterSub/Formatters/')+"/"+self.formatterName+'.obj', 'wb') as fp:
                pickle.dump(self.ruleList, fp)
    def loadFormatter(self):
        with open(osp.abspath('../FormatterSub/Formatters/')+"/"+self.formatterName+'.obj', 'rb') as fp:
                self.ruleList = pickle.load(fp)

# pdml = pdmlmanager("Scripts/cubic2.pdml")
# form = Formatter(pdml,"ip")
# # form.loadFormatter()
# form.applyFormatter()
# # print(pdml.get_pdml_as_text())
# # form.removeRule()
# rule = Rule()
# act = HidingAction("True","ip.len")
# rule.setFilter("ip","","")
# rule.addAction(act)
# nxtRule = Rule()
# nxtact = HidingAction("True", "ip.id")
# nxtRule.setFilter("ip src net 192 or tcp","","")
# nxtRule.addAction(nxtact)
# form.addRule(rule)
# form.addRule(nxtRule)
# form.applyFormatter()
# # form.removeRule()
# # form.saveFormatter()
# # print(form.changeForm)
# cap = Capture()
# cap.set_man(pdml)
# print(form.get_rules_in_string())
# # print(cap.pdml_object_to_string(pdml))

