from FormatterSub.Rule import Rule
from PDMLSub.PDMLManager import pdmlmanager
from FormatterSub.Action import Action
from FormatterSub.RenamingAction import RenamingAction
from FormatterSub.HidingAction import HidingAction
import json
import pickle
class Formatter:
    def __init__(self, pdml, formatterName):
        self.pdml = pdml
        self.formatterName = formatterName
        self.ruleList = []
        self.changeForm = []
        return
    def applyFormatter(self):
        for rule in self.ruleList:
            self.changeForm.append(rule.applyRule(self.pdml))
    def addRule(self, rule):
        self.ruleList.append(rule)
        return
    def removeRule(self):
        self.ruleList.pop()
    def getChangeForm():
        return changeForm
    def saveFormatter(self):
        with open("FormatterSub/Formatters/"+self.formatterName+'.obj', 'wb') as fp:
            pickle.dump(self.ruleList, fp)
    def loadFormatter(self):
        with open("FormatterSub/Formatters/"+self.formatterName+'.obj', 'rb') as fp:
            self.ruleList = pickle.load(fp)

pdml = pdmlmanager("Scripts/cubic.pdml")
form = Formatter(pdml,"ip")
form.loadFormatter()
form.applyFormatter()
# rule = Rule()
# act = HidingAction("True","ip.len")
# rule.setFilter("ip src net 192","","")
# rule.addAction(act)
# nxtRule = Rule()
# nxtact = HidingAction("True", "ip.id")
# nxtRule.setFilter("ip src net 192","","")
# nxtRule.addAction(nxtact)
# form.addRule(rule)
# form.addRule(nxtRule)
# form.applyFormatter()
# form.saveFormatter()
# print(form.changeForm)
# print(pdml.get_pdml_as_text())

