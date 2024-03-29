import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from PDMLSub.PDMLManager import pdmlmanager
from FormatterSub.AnnotatingAction import AnnotatingAction
from FormatterSub.HidingAction import HidingAction
from FormatterSub.RenamingAction import RenamingAction
from FormatterSub.HookAction import HookAction
from windows.hookWidget import HookWidget
import os.path as os

class EditorWidget:
    
        def __init__(self):
            self.packetLabel = Gtk.Label()
            self.packetnum = ""
            self.packetproto = ""
            self.annotate_actions = {}
            self.hiding_actions = {}
            self.renaming_actions = {}
            self.hook_actions = {}
            self.actions = {}
            
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
            
            
            self.fieldtreestore = Gtk.TreeStore(str, str, bool)
            self.fieldtreeview = Gtk.TreeView(self.fieldtreestore)
            self.fieldscrolledview.add(self.fieldtreeview)
            
            
            
            fieldcheckCell = Gtk.CellRendererToggle();
            fieldcheckCell.set_property('activatable', True)
            fieldcheckCell.connect("toggled", self.toggled_cb, (self.fieldtreestore, 2))
            
            fieldcell = Gtk.CellRendererText()
            fieldcell.set_property("editable", False)
            fieldcell.connect("edited", self.text_edited)
            

            fieldcell2 = Gtk.CellRendererText()
            fieldcell2.set_property("editable", True)
            fieldcell2.connect("edited", self.text_edited)
            #fieldcell2.connect("clicked", self.on_cell_clicked)
            
            fieldtvcolumn = Gtk.TreeViewColumn('Field')
            self.fieldtreeview.append_column(fieldtvcolumn)
            fieldtvcolumn2 = Gtk.TreeViewColumn('Value')
            self.fieldtreeview.append_column(fieldtvcolumn2)
            fieldtvcolumn3 = Gtk.TreeViewColumn('Hide')
            self.fieldtreeview.append_column(fieldtvcolumn3)
            
            #fieldtvcolumn.pack_start(fieldcheckCell, True)
            fieldtvcolumn.pack_start(fieldcell, True)
            fieldtvcolumn.add_attribute(fieldcell, 'text', 0)
            
            fieldtvcolumn2.pack_start(fieldcell2, True)
            #fieldtvcolumn2.pack_start(fieldcheckCell2, True)
            fieldtvcolumn2.add_attribute(fieldcell2, 'text', 1)
            
            fieldtvcolumn3.pack_start(fieldcheckCell, True)
            fieldtvcolumn3.add_attribute(fieldcheckCell, "active", 2)
            
            
            self.fieldtreeview.set_search_column(0)
            self.fieldtreeview.set_reorderable(True)
            self.fieldtreeview.connect('size-allocate', self.treeview_changed)
            self.fieldtreeview.connect('button-press-event', self.on_cell_clicked)
            

            
            
            
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
        def get_actions(self):
            return self.actions
        def create_hook_window(self, fieldelement, proto):
            hook_widget = HookWidget(self.actions, proto)
            hookbox = hook_widget.create_widget(fieldelement)
            hook_window = Gtk.Window()
            hook_window.set_size_request(500, 300)
            hook_window.add(hookbox)
            hook_window.show_all()
        def on_cell_clicked(self, treeview, event):
            if(event.button == 3):
                path = treeview.get_path_at_pos(event.x, event.y)
                print(path[0])
                val = path[0]
                print(val)
                num = self.packetnum
                proto = self.packetproto
                fieldname = self.fieldtreestore[val[0]][1]
                fieldname = fieldname.split(' ', 1)[-1]
                
                attribname = self.fieldtreestore[val][0]
                attribname = attribname.split(' ', 1)[-1]
    
                fieldelement = self.pdmlman.get_field_element(int(num), proto, fieldname)
                
                print("packetnum",num)
                print("proto", proto)
                print("fieldname",fieldname)
                print("attribname", attribname)
                
                self.create_hook_window([(fieldname,attribname)], proto)
                # w = Gtk.Window(Gtk.WindowType.POPUP)
                # self.opendialog = Gtk.FileChooserDialog("Please choose a Hook", w,
                #     Gtk.FileChooserAction.OPEN,
                #     (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                #      Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
                # # print("./"+os.getcwd()+"/Scripts")
                # # self.opendialog.set_current_folder("./"+os.getcwd()+"/Scripts")
                # self.opendialog.set_current_folder(os.abspath('../Scripts'))
                # self.opendialog.set_transient_for(w)
                # w.add(self.opendialog)
                # response = self.opendialog.run()
                # if response == Gtk.ResponseType.OK:
                #     print("Open clicked")
                #     self.chosenfile = self.opendialog.get_filename()
                #     print("filename chosen",self.chosenfile)
                #     #self.scriptBuffer.set_text(self.read_file(self.chosenfile))
                #     #self.hook_actions[proto].append(HookAction(self.chosenfile, self.fieldtreestore[val[0]][1]))
                #     try:
                #         self.actions[proto].append(HookAction(self.chosenfile, self.fieldtreestore[val[0]][1]))
                #     except KeyError:
                #         self.actions[proto] = list()
                #         self.actions[proto].append(HookAction(self.chosenfile, self.fieldtreestore[val[0]][1]))
    
                # elif response == Gtk.ResponseType.CANCEL:
                #     print("Cancel clicked")
                # self.opendialog.destroy()
                # w.destroy()
                
                print(self.annotate_actions)
                print(self.renaming_actions)
                print(self.hiding_actions)
                print(self.hook_actions)
#                 print(self.fieldtreestore[path[0]][1])
                #print(self.fieldtreestore[path][0])
                print("right click detected")
                

        def treeview_changed(self, widget, event, data = None):
            adj = self.fieldscrolledview.get_vadjustment()
            
            
            
        def on_hide_toggled(self, button, name):
            if button.get_active():
                state = "on"
            else:
                state = "off"
            print("Button", name, "was turned", state)
            

            
        def toggled_cb(self,cell, path, user_data):
            model, column = user_data
            print(path)
            model[path][column] = not model[path][column]
            
            if(model[path][column]):
                text = "True"
            else:
                text = "False"
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
            
            self.hiding_actions[proto] = (HidingAction(text, fieldname))
            try:
                self.actions[proto].append(HidingAction(text, fieldname))
            except KeyError:
                self.actions[proto] = list()
                self.actions[proto].append(HidingAction(text, fieldname))
            print(self.annotate_actions)
            print(self.renaming_actions)
            print(self.hiding_actions)
            print(self.hook_actions)
            return   
                
        def on_annotate_clicked(self, button):
            print("\"Annotate\" button was clicked")     
            
        
            
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
            
            if(attribname == "Annotate"):
                self.annotate_actions[proto] = (AnnotatingAction(attribname, text, fieldname))
                try:
                    self.actions[proto].append(AnnotatingAction(attribname, text, fieldname))
                except KeyError:
                    self.actions[proto] = list()
                    self.actions[proto].append(AnnotatingAction(attribname, text, fieldname))
            else:
                while(x < len(attribsnames)):
    #                 print(attribsnames[x])
                    if(attribsnames[x] == attribname):
                        if(attribvalues[x] != text):
                            attribvalues[x] = text
                            print("set ", attribsnames[x], " to ", text)
                            self.renaming_actions[proto] = (RenamingAction(attribname, text, fieldname))
                            try:
                                self.actions[proto].append(RenamingAction(attribname, text, fieldname))
                            except KeyError:
                                self.actions[proto] = list()
                                self.actions[proto].append(RenamingAction(attribname, text, fieldname))
                    x+=1
            
            self.fieldtreestore[path][1] = text
            
            print(self.annotate_actions)
            print(self.renaming_actions)
            print(self.hiding_actions)
            
        
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

                fielditer = self.fieldtreestore.append(None, ["("+str(x)+") "+fieldnames[0], fieldvalues[0], False])
                y = 1
                while(y < len(fieldnames)):
                    self.fieldtreestore.append(fielditer, ["["+str(y-1)+"] "+fieldnames[y],fieldvalues[y], False])
                    y+=1
                self.fieldtreestore.append(fielditer, ["<> Annotate","", False])
                x+=1
                
            
            
            
        def set_pdml_man(self, p):
            self.pdmlman = p
            
            
            

        