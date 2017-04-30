import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from PDMLSub.PDMLManager import pdmlmanager


class EditorWidget:
    
        def __init__(self):
            self.packetLabel = Gtk.Label()
        
        def create_widget(self):

            

            
            vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            self.packetLabel = Gtk.Label()
            self.packetLabel.set_markup("<b>NO PACKET SELECTED</b>")
            self.packetLabel.set_alignment(xalign=0, yalign=1) 
            vbox.pack_start(self.packetLabel,True,True,0)
            contentBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
            vbox.pack_start(contentBox,True,True,0)
            self.fieldscrolledview = Gtk.ScrolledWindow()
            self.valuescrolledview = Gtk.ScrolledWindow()
            contentBox.pack_start(self.fieldscrolledview, True, True, 0)
            contentBox.pack_start(self.valuescrolledview, True, True, 0)
            
            self.fieldtreestore = Gtk.TreeStore(str)
            fieldtreeview = Gtk.TreeView(self.fieldtreestore)
            self.fieldscrolledview.add(fieldtreeview)
            fieldtvcolumn = Gtk.TreeViewColumn('Field Name')
            fieldtreeview.append_column(fieldtvcolumn)
            fieldcheckCell = Gtk.CellRendererToggle();
            fieldcheckCell.connect("toggled", self.on_cell_toggled)
            fieldcell = Gtk.CellRendererText()
            fieldcell.set_property("editable", True)
            fieldcell.connect("edited", self.text_edited)
            fieldtvcolumn.pack_start(fieldcell, True)
            fieldtvcolumn.pack_start(fieldcheckCell, True)
            fieldtvcolumn.add_attribute(fieldcell, 'text', 0)
            fieldtreeview.set_search_column(0)
            fieldtreeview.set_reorderable(True)

            self.valuetreestore = Gtk.TreeStore(str)
            valuetreeview = Gtk.TreeView(self.valuetreestore)
            self.valuescrolledview.add(valuetreeview)
            valuetvcolumn = Gtk.TreeViewColumn('Value')
            valuetreeview.append_column(valuetvcolumn)
            valuecell = Gtk.CellRendererText()
            valuecheckCell = Gtk.CellRendererToggle();
            valuecheckCell.connect("toggled", self.on_cell_toggled)
            valuecell.set_property("editable", True)
            valuecell.connect("edited", self.text_edited)
            valuetvcolumn.pack_start(valuecell, True)
            valuetvcolumn.pack_start(valuecheckCell, True)
            valuetvcolumn.add_attribute(valuecell, 'text', 0)
            valuetreeview.set_search_column(0)
            valuetreeview.set_reorderable(True)
            
            
            legendBox = Gtk.Box(spacing=6)
            legendTitle = Gtk.Label()
            legendTitle.set_markup("<b>Legend</b>")
            legendTitle.set_alignment(xalign=0, yalign=1)
            vbox.pack_start(legendTitle,True,True,0)
            hideField = Gtk.CheckButton("Hide Field ")
            legendBox.pack_start(hideField,False,False,0)
            hideField.connect("toggled", self.on_hide_toggled, "hideField")
            vbox.pack_start(legendBox,False,False,0)
            annotate = Gtk.Button.new_with_label("<>")
            annotate.connect("clicked", self.on_annotate_clicked)
            legendBox.pack_start(annotate,False,False,0)
            annotateEntry = Gtk.Entry()
            annotateEntry.set_text("Annotate")
            legendBox.pack_start(annotateEntry,True,True,0)
            
            return vbox

            

        
        def on_hide_toggled(self, button, name):
            if button.get_active():
                state = "on"
            else:
                state = "off"
            print("Button", name, "was turned", state)
            
        def on_annotate_clicked(self, button):
            print("\"Annotate\" button was clicked")
            self.fieldtreestore.append(None, ['test'])
            self.valuetreestore.append(None, ['test'])
#             for parent in range(4):
#                 piter = self.fieldtreestore.append(None, ['Line %i' % parent])
#                 for child in range(3):
#                     self.fieldtreestore.append(piter, ['Field Name %i' %
#                                                   (child)])
#                 self.fieldtreestore.append(piter, ['<Enter Text>'])            
            
        def on_cell_toggled(self, widget, path):
            print(path)
            
        def text_edited(self, widget, path, text):
            print("Added "+text+"!")
            
        def set_pdml_man(self, p):
            self.pdmlman = p
            
            
            

        