import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class FilterRow():
    def __init__(self, listBox, fieldVal, valueVal, rowList):
        self.row = Gtk.ListBoxRow()
        self.listBox = listBox
        self.rowList = rowList
        if(valueVal == "Proto" or valueVal == "Dir" or valueVal == "Conjuction" or valueVal == "Negation"):
            self.rowList.append((fieldVal, ""))
        else:
            self.rowList.append((fieldVal, valueVal))
        expression = Gtk.Box(spacing=6)
        self.field = Gtk.Label()
        self.field.set_text(fieldVal)
        self.value = Gtk.Label()
        self.value.set_text(valueVal)
        delete = Gtk.Button("X")
        delete.connect("clicked",self.on_delete_clicked)
        expression.pack_start(self.field,True,True,0)
        expression.pack_start(self.value,True,True,0)
        expression.pack_start(delete,False,False,0)
        self.row.add(expression)
    def getRow(self):
        return self.row
    def getVals(self):
        return [self.field.get_text(),self.value.get_text()]
    def on_delete_clicked(self, widget):
        self.listBox.remove(self.row)
        self.listBox.show_all()
        self.rowList.pop()        
