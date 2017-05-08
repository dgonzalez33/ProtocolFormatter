from FormatterSub.Filter import Filter
import copy
class Rule:
    def __init__(self):
        self.actionList = []
        return
    def setFilter(self, filter, icontent, econtent):
        self.filter = Filter()
        self.filter.set_bpf_filter(filter, icontent, econtent)
        self.filter.setFilter()
    def getFilter(self):
        return self.filter
    def getFilterName(self):
        return self.filter.getName()
    def addAction(self, action):
        self.actionList.append(action)
    def getActions(self):
        return self.actionList
    def applyRule(self, pdml):
        changes = {}
        # print(type(self.filter))
        self.filter.set_pdmlman(pdml)
        self.filter.applyFilter()
        protoList = self.filter.getFormatterProtos()
        for proto in protoList:
            fields = proto.get_field_element()
            for field in fields:
                for act in self.actionList:
                    fieldNames = field.get_all_field_attributes_name()
                    fieldValues = field.get_all_field_attributes_value()
                    try:
                        nameInd = fieldNames.index("field name")
                    except ValueError:
                        continue
                    if act.getKey() == fieldValues[nameInd]:
                        temp = copy.deepcopy(field)
                        print(field.get_all_field_attributes_value())
                        newField = act.getActionResult(field)
                        field.set_field_to_field(newField)
                        # booboo = "boooboo"
                        # field.get_all_field_attributes_value()[0] = booboo
                        print(field.get_all_field_attributes_value())
                        changes[field] = temp
        return changes

