import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from PDMLSub.PDMLManager import pdmlmanager


class EditorWidget:
    
        def __init__(self):
            self.packetLabel = Gtk.Label()
            self.packetnum = ""
            self.packetproto = ""
        
        def create_widget(self):

            

            
            vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            self.packetLabel = Gtk.Label()
            self.packetLabel.set_markup("<b>NO PACKET SELECTED</b>")
            self.packetLabel.set_alignment(xalign=0, yalign=0) 
            vbox.pack_start(self.packetLabel,False,False,0)
            contentBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
            vbox.pack_start(contentBox,True,True,0)
            self.fieldscrolledview = Gtk.ScrolledWindow()
            self.valuescrolledview = Gtk.ScrolledWindow()
            #contentBox.pack_start(self.valuescrolledview, True, True, 0)
            contentBox.pack_start(self.fieldscrolledview, True, True, 0)
            
            
            self.fieldtreestore = Gtk.TreeStore(str, str)
            fieldtreeview = Gtk.TreeView(self.fieldtreestore)
            self.fieldscrolledview.add(fieldtreeview)
            
            
            
            fieldcheckCell = Gtk.CellRendererToggle();
            fieldcheckCell.connect("toggled", self.on_cell_toggled)
            fieldcell = Gtk.CellRendererText()
            fieldcell.set_property("editable", False)
            fieldcell.connect("edited", self.text_edited)
            
            #fieldcheckCell2 = Gtk.CellRendererToggle();
            #fieldcheckCell2.connect("toggled", self.on_cell_toggled)
            fieldcell2 = Gtk.CellRendererText()
            fieldcell2.set_property("editable", True)
            fieldcell2.connect("edited", self.text_edited)
            
            fieldtvcolumn = Gtk.TreeViewColumn('Field')
            fieldtreeview.append_column(fieldtvcolumn)
            fieldtvcolumn2 = Gtk.TreeViewColumn('Value')
            fieldtreeview.append_column(fieldtvcolumn2)
            
            fieldtvcolumn.pack_start(fieldcheckCell, True)
            fieldtvcolumn.pack_start(fieldcell, True)
            fieldtvcolumn.add_attribute(fieldcell, 'text', 0)
            
            fieldtvcolumn2.pack_start(fieldcell2, True)
            #fieldtvcolumn2.pack_start(fieldcheckCell2, True)
            fieldtvcolumn2.add_attribute(fieldcell2, 'text', 1)
            
            fieldtreeview.set_search_column(0)
            fieldtreeview.set_reorderable(True)
            fieldtreeview.connect('size-allocate', self.treeview_changed)

            
            
            
            legendBox = Gtk.Box(spacing=6)
            legendTitle = Gtk.Label()
            legendTitle.set_markup("<b>Legend</b>")
            legendTitle.set_alignment(xalign=0, yalign=1)
            vbox.pack_start(legendTitle,False,False,0)
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

            

        def treeview_changed(self, widget, event, data = None):
            adj = self.fieldscrolledview.get_vadjustment()
            
            
            
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
#             print("Added "+text+" at path:", path)
            
            num = self.packetnum
            proto = self.packetproto
            fieldname = self.fieldtreestore[path[0]][1]
            fieldname = fieldname.split(' ', 1)[-1]
            
            attribname = self.fieldtreestore[path][0]
            attribname = attribname.split(' ', 1)[-1]

            fieldelement = self.pdmlman.get_field_element(int(num), proto, fieldname)
            
            print("packetnum",num)
            print("proto", proto)
            print("fieldname",fieldname)
            print("attribname", attribname)
            print(fieldelement)
            
            attribsnames  = fieldelement.field_attributes_names
            attribvalues = fieldelement.field_attributes_values
            print(attribsnames)
            print(attribvalues)
            x = 0
            while(x < len(attribsnames)):
#                 print(attribsnames[x])
                if(attribsnames[x] == attribname):
                    attribvalues[x] = text
                    print("set ", attribsnames[x], " to ", text)
                x+=1
            
            self.fieldtreestore[path][1] = text

            
        
        def clear_list(self):
            self.fieldtreestore.clear()
            
        
        def update_field_info(self, packetnum, proto):
            self.clear_list()
            packet = self.pdmlman.get_packet_of_id(int(packetnum))
            protos = packet.get_proto_element()
            x = 0
            while(x < len(protos)):
                if(protos[x].proto_attributes_values[0] == proto):
                    protocol = protos[x]
                x+=1
            fields = protocol.get_field_element()
            x = 0
            while(x < len(fields)):
                fieldnames = fields[x].get_all_field_attributes_name()
                fieldvalues = fields[x].get_all_field_attributes_value()

                fielditer = self.fieldtreestore.append(None, ["("+str(x)+") "+fieldnames[0], fieldvalues[0]])
                y = 1
                while(y < len(fieldnames)):
                    self.fieldtreestore.append(fielditer, ["["+str(y-1)+"] "+fieldnames[y],fieldvalues[y]])
                    y+=1
                
                x+=1
                
            
            
            
        def set_pdml_man(self, p):
            self.pdmlman = p
            
            
            

        