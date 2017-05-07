import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from windows.editorWidget import EditorWidget


class PacketWidget:

        def __init__(self):
            self.liststore = Gtk.ListStore(str, str, str, str, str)
            self.packetclicked = ""
            self.e_widget = EditorWidget()
            self.listofiterators = []
            self.editorisopen = 0
            self.filterlist = []
            
        
             
        def create_widget(self):

            vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
            
            appliedFormattersContainer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            
            vbox.pack_start(appliedFormattersContainer,True,True,0)
            filterContainer = Gtk.Box(spacing=0)
            self.scrollContainer = Gtk.ScrolledWindow()
            
            appliedFormattersContainer.pack_start(self.scrollContainer,True,True,0)
            
            
            self.current_filter_language = "True"
            
            self.language_filter = self.liststore.filter_new()
            self.language_filter.set_visible_func(self.language_filter_func)
            
            self.treeview = Gtk.TreeView()
            self.sorted = Gtk.TreeModelSort(self.language_filter)
            self.treeview.set_model(self.sorted)
            
            tree_selection = self.treeview.get_selection()
            tree_selection.set_mode(Gtk.SelectionMode.MULTIPLE)
            tree_selection.connect("changed", self.packet_tree_clicked)
            
            self.add_columns_to_list("Packet id", 0, 0)  
            self.add_columns_to_list("Proto Name", 1, 1)
            self.add_columns_to_list("Proto Showname", 2, 2)
            self.add_columns_to_list("Captured Time", 3, 3)

            frame = Gtk.Frame()
            frame.add(filterContainer)
            
            self.scrollContainer.add(self.treeview)
            self.currentpackets = []
            
            
            
            #filterContainer.pack_start(self.treeview,True,True,0)

            
            
            return vbox
        
        def language_filter_func(self, model, iter, data):
            if self.current_filter_language is None or self.current_filter_language == "None":
                return True
            else:
                return model[iter][4] == self.current_filter_language
  
        def set_filter_list(self, flist):
            self.daList = flist
           
            if(len(self.daList) < 1):
                x = 0
                self.filterlist.clear()
                print("i was empty")
                while(x < len(self.currentpackets)):
                    proto = self.currentpackets[x].get_proto_element()
                    y = 0 
                    while(y < len(proto)):
                    
                        self.filterlist.append("False")
                        y+=1
                    x+=1
            else:
                print(self.daList[0][0], self.daList[0][1])
                filterindex = 0
                x = 0
                while(x < len(self.currentpackets)):
                    protos = self.currentpackets[x].get_proto_element()
                    y = 0
                    while(y < len(protos)):
                        print(protos[y].proto_attributes_values[0], "+", self.daList[0][1], self.currentpackets[x].packetid, self.daList[x][0])
                        if(self.currentpackets[x].packetid == self.daList[x][0] and protos[y].proto_attributes_values[0] == self.daList[0][1]):
                            print("packet",x," and proto",y)
                            self.filterlist[filterindex] = "True"
                            print("true")
                            filterindex+=1
                        else:
                            print("packet",x," and proto",y)
                            self.filterlist[filterindex] = "False"
                            print("false")
                            filterindex+=1
                            
                        print(filterindex)
                        y+=1
                    x+=1
                
            self.clear_list()
            self.update_packet_window(self.currentpackets)   
            self.refilter_list()
            print("yay ", self.filterlist)
        
        def clear_filter_list(self):
            x = 0
            self.filterlist = []
            self.clear_list()
           #self.update_packet_window(self.currentpackets) 
            self.refilter_list()
        
        def packet_tree_clicked(self, tree_selection):
#             print(tree_selection)
            (model, pathlist) = tree_selection.get_selected_rows()
            for path in pathlist :
                tree_iter = model.get_iter(path)
                value = model.get_value(tree_iter,0)
                value2 = model.get_value(tree_iter, 1)
                self.packetclicked = "<b>Packet: "+value+" Protocol: "+value2+"</b>"
                if(self.editorisopen == 1):
                    self.e_widget.packetnum = value
                    self.e_widget.packetproto = value2
                    self.e_widget.packetLabel.set_markup(self.packetclicked)
                    self.e_widget.update_field_info(value, value2)
#             adj = self.scrollContainer.get_vadjustment()
#             print(adj.get_value())
#             self.scrollContainer.set_vadjustment(adj)
            

    
        def set_editor_widget(self, widget):
            self.e_widget = widget
        
        def text_edited(self, widget, path, text):
            print("tried to edit",path," with:", text)
            
       
            
        def print_all_protos(self):
            x = 0
            while(x < len(self.listofiterators)):
                print(self.liststore[self.listofiterators[x]][1])
                x+=1
                
        def refilter_list(self):
            print("%s language selected!" % self.current_filter_language)
            #we update the filter, which updates in turn the view
            self.language_filter.refilter()

        def update_packet_window(self, packets):
            self.currentpackets = packets
            
            if(len(self.filterlist) < 1):
                x = 0
                print("i was empty :)")
                while(x < len(packets)):
                    proto = packets[x].get_proto_element()
                    y = 0 
                    while(y < len(proto)):
                    
                        self.filterlist.append("True")
                        y+=1
                    x+=1
            
            filterindex = 0
            x = 0
            print("packetwidget", len(packets))
            while(x < len(packets)):
                self.rowvalue = []
                self.p_name = ""
                if(x < 10):
                    self.p_name = "0"+str(packets[x].get_packet_id())
                else:
                    self.p_name =""+str(packets[x].get_packet_id())
                    
                self.rowvalue.append(self.p_name)
                    
                proto = packets[x].get_proto_element()
                y = 0
                while(y < len(proto)):
                    self.rowvalue.append(proto[y].proto_attributes_values[0])
                    
                    if(proto[y].proto_attributes_values[0] == "geninfo"):
                        self.rowvalue.append(proto[y].proto_attributes_values[2])
                    elif(len(proto[y].proto_attributes_values) > 1):
                        self.rowvalue.append(proto[y].proto_attributes_values[1])
                    else:
                        self.rowvalue.append("")
    
                    if(proto[y].proto_attributes_values[0] == "geninfo"):
                        self.field = proto[y].get_field_element_at_index(3)
                        self.date = self.field.field_attributes_values[2]
                        self.rowvalue.append(self.date)
                        self.rowvalue.append(self.filterlist[filterindex])
                        filterindex+=1
                        
                    else:
                        self.rowvalue.append(self.date)
                        self.rowvalue.append(self.filterlist[filterindex])
                        filterindex+=1
                        
                    if(len(self.rowvalue) != 5):
                        print("packetwidget mistake", self.rowvalue)
                        self.rowvalue.clear()
                        self.rowvalue.append(self.p_name)
                        
                    else:  
                        #print("here",self.rowvalue)
                        self.add_to_list(self.rowvalue)
                        self.rowvalue.clear()
                        self.rowvalue.append(self.p_name)
                    y+=1
                self.rowvalue.clear()
                    
                x+=1  
                
            
        def add_columns_to_list(self, name, num, s_id):
            renderer_text = Gtk.CellRendererText()
            if(name != "Packet id"):
                renderer_text.set_property("editable", True)
                #renderer_text.set_property("foreground", 'red')
                column_text = Gtk.TreeViewColumn(name, renderer_text, text=num)
                renderer_text.connect("edited", self.text_edited)
            else:
                column_text = Gtk.TreeViewColumn(name, renderer_text, text=num)
                 
                
            column_text.set_clickable(True)
            column_text.set_sort_column_id(s_id)
            self.treeview.append_column(column_text)
            
        def clear_list(self):
            self.liststore.clear()
            
        def add_to_list(self, value):
            itere = Gtk.TreeIter()
            self.listofiterators.append(self.liststore.append(value))
#             print(self.liststore.get_value(itere, 0))
#             itere = self.liststore.get_iter(0)

            
        