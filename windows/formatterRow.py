import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class FormatterRow():
    def __init__(self, listBox, fieldVal, rowList, index):
        self.row = Gtk.ListBoxRow()
        self.listBox = listBox
        self.rowList = rowList
        self.index = index
        expression = Gtk.Box(spacing=6)
        self.field = Gtk.Label()
        self.field.set_text(fieldVal)
        delete = Gtk.Button("X")
        delete.connect("clicked",self.on_delete_clicked)
        expression.pack_start(self.field,True,True,0)
        expression.pack_start(delete,False,False,0)
        self.row.add(expression)
    def getRow(self):
        return self.row
    def getVals(self):
        return self.field.get_text()
    def on_delete_clicked(self, widget):
        if(type(self.rowList).__name__ != "Formatter"):
            if(self.index == len(self.rowList)-1):
               self.listBox.remove(self.row)
               self.listBox.show_all()
               self.rowList.pop()        
