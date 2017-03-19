import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class FilterRow():
    def __init__(self, listBox, fieldVal, valueVal):
        self.row = Gtk.ListBoxRow()
        self.listBox = listBox
        expression = Gtk.Box(spacing=6)
        field = Gtk.Label()
        field.set_text(fieldVal)
        value = Gtk.Label()
        value.set_text(valueVal)
        delete = Gtk.Button("X")
        delete.connect("clicked",self.on_delete_clicked)
        expression.pack_start(field,True,True,0)
        expression.pack_start(value,True,True,0)
        expression.pack_start(delete,False,False,0)
        self.row.add(expression)
    def getRow(self):
        return self.row
    def on_delete_clicked(self, widget):
        self.listBox.remove(self.row)
        self.listBox.show_all()        
