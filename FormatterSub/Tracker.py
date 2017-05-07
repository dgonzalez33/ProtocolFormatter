from PDMLSub.FieldElement import fieldelement
class Tracker:
	def __init__(self):
		self.changeList = []
	def recordsChanges(self, change):
		self.changeList.append(change)
	def undoLastChange(self):
		lastChange = self.changeList.pop()
		for field in lastChange.keys():
			field.set_field_to_field(lastChange[field])