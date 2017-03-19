import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from filterRow import FilterRow


class EditorWindow(Gtk.Window):

        def __init__(self):

            def makeFieldBox(self,fieldName):
                fieldBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
                title = Gtk.Label()
                title.set_markup("<b>Field Name</b>")
                title.set_alignment(xalign=0, yalign=1)
                fieldBox.pack_start(title,False,False,0) 
                # fieldLabel = Gtk.Label("Line 1")
                # fieldLabel.set_alignment(xalign=0, yalign=1)
                # fieldBox.pack_start(fieldLabel,False,False,0)
                # fieldButton = Gtk.CheckButton("Field Name " + fieldName)
                # fieldBox.pack_start(fieldButton,False,False,0)
                # entry = Gtk.Entry()
                # entry.set_text("Enter Text")
                # fieldBox.pack_start(entry,False,False,0)
                treestore = Gtk.TreeStore(str)
                for parent in range(4):
                    piter = treestore.append(None, ['Line %i' % parent])
                    for child in range(3):
                        treestore.append(piter, ['Field Name %i' %
                                                      (child)])
                    treestore.append(piter, ['<Enter Text>'])
                
                treeview = Gtk.TreeView(treestore)
                tvcolumn = Gtk.TreeViewColumn('Field Name')
                treeview.append_column(tvcolumn)
                checkCell = Gtk.CellRendererToggle();
                checkCell.connect("toggled", self.on_cell_toggled)
                cell = Gtk.CellRendererText()
                cell.set_property("editable", True)
                cell.connect("edited", self.text_edited)
                tvcolumn.pack_start(cell, True)
                tvcolumn.pack_start(checkCell, True)
                tvcolumn.add_attribute(cell, 'text', 0)
                treeview.set_search_column(0)
                treeview.set_reorderable(True)
                fieldBox.pack_start(treeview,False,False,0)
                return fieldBox
            def makeValueBox(self,valueName):
                valueBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
                title = Gtk.Label()
                title.set_markup("<b>Value</b>")
                title.set_alignment(xalign=0, yalign=1)
                valueBox.pack_start(title,False,False,0) 
                # valueLabel = Gtk.Label("Line 1")
                # valueLabel.set_alignment(xalign=0, yalign=1)
                # valueBox.pack_start(valueLabel,False,False,0)
                # valueButton = Gtk.CheckButton("Value = " + valueName)
                # valueBox.pack_start(valueButton,False,False,0)
                # entry = Gtk.Entry()
                # entry.set_text("Enter Value")
                # valueBox.pack_start(entry,False,False,0)
                treestore = Gtk.TreeStore(str)
                for parent in range(4):
                    piter = treestore.append(None, ['Line %i' % parent])
                    for child in range(3):
                        treestore.append(piter, ['Value %i' %
                                                      (child)])
                    treestore.append(piter, ['<Enter Text>'])
                treeview = Gtk.TreeView(treestore)
                tvcolumn = Gtk.TreeViewColumn('Value')
                treeview.append_column(tvcolumn)
                cell = Gtk.CellRendererText()
                checkCell = Gtk.CellRendererToggle();
                checkCell.connect("toggled", self.on_cell_toggled)
                cell.set_property("editable", True)
                cell.connect("edited", self.text_edited)
                tvcolumn.pack_start(cell, True)
                tvcolumn.pack_start(checkCell, True)
                tvcolumn.add_attribute(cell, 'text', 0)
                treeview.set_search_column(0)
                treeview.set_reorderable(True)
                valueBox.pack_start(treeview,False,False,0)
                return valueBox

            Gtk.Window.__init__(self, title="Editor Window")
            vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            self.set_border_width(10)
            self.add(vbox)
            packetLabel = Gtk.Label()
            packetLabel.set_markup("<b>Packet #1</b>")
            packetLabel.set_alignment(xalign=0, yalign=1) 
            vbox.pack_start(packetLabel,True,True,0)
            contentBox = Gtk.Box(spacing=6)
            vbox.pack_start(contentBox,True,True,0)
            fieldBox = makeFieldBox(self, "name")
            contentBox.pack_start(fieldBox,True,True,0)
            valueBox = makeValueBox(self,"tcp")
            contentBox.pack_start(valueBox,True,True,0)
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
        def on_hide_toggled(self, button, name):
            if button.get_active():
                state = "on"
            else:
                state = "off"
            print("Button", name, "was turned", state)
        def on_annotate_clicked(self, button):
            print("\"Annotate\" button was clicked")
        def on_cell_toggled(self, widget, path):
            print(path)
        def text_edited(self, widget, path, text):
            print("Added "+text+"!")

        
win = EditorWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()