from FormatterSub.Rule import Rule
from PDMLSub.PDMLManager import pdmlmanager
from FormatterSub.Action import Action
from FormatterSub.RenamingAction import RenamingAction
from FormatterSub.HidingAction import HidingAction
from FormatterSub.Tracker import Tracker
from FileSub.Capture import Capture
import pickle
class Formatter:
    def __init__(self, pdml, formatterName):
        self.pdml = pdml
        self.formatterName = formatterName
        self.ruleList = []
        self.tracker = Tracker()
        return
    def applyFormatter(self):

        for rule in self.ruleList:
            self.tracker.recordsChanges(rule.applyRule(self.pdml))
            # print(rule.applyRule(self.pdml))
    def addRule(self, rule):
        self.ruleList.append(rule)
        return
    def removeRule(self):
        self.tracker.undoLastChange()
        self.ruleList.pop()
    def getChangeForm():
        return changeForm
    def saveFormatter(self):
        with open("FormatterSub/Formatters/"+self.formatterName+'.donttouch', 'wb') as fp:
            pickle.dump(self.ruleList, fp)
    def loadFormatter(self):
        with open("FormatterSub/Formatters/"+self.formatterName+'.donttouch', 'rb') as fp:
            self.ruleList = pickle.load(fp)

pdml = pdmlmanager("Scripts/cubic2.pdml")
form = Formatter(pdml,"ip")
# form.loadFormatter()
# form.applyFormatter()
# print(pdml.get_pdml_as_text())
# form.removeRule()
rule = Rule()
act = HidingAction("True","ip.len")
rule.setFilter("ip","","")
rule.addAction(act)
nxtRule = Rule()
nxtact = HidingAction("True", "ip.id")
nxtRule.setFilter("ip src net 192 or tcp","","")
nxtRule.addAction(nxtact)
form.addRule(rule)
form.addRule(nxtRule)
form.applyFormatter()
form.removeRule()
# form.saveFormatter()
# print(form.changeForm)
cap = Capture()
cap.set_man(pdml)
# print(cap.pdml_object_to_string(pdml))

