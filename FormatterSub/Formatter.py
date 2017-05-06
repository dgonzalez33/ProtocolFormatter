from FormatterSub.Rule import Rule
from PDMLSub.PDMLManager import pdmlmanager
from FormatterSub.Action import Action
from FormatterSub.RenamingAction import RenamingAction
from FormatterSub.HidingAction import HidingAction
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

pdml = pdmlmanager("Scripts/cubic.pdml")
form = Formatter(pdml,"ip")
rule = Rule()
act = HidingAction("80085","ip.len")
rule.setFilter("ip src net 192","","")
rule.addAction(act)
form.addRule(rule)
form.applyFormatter()
print(form.changeForm)
# print(pdml.get_pdml_as_text())

