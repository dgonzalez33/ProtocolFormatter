import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from windows.editorWidget import EditorWidget


class PacketWidget:

        def __init__(self):
            self.liststore = Gtk.ListStore(str, str, str, str)
            self.packetclicked = ""
            self.e_widget = EditorWidget()
            self.listofiterators = []
            
        
             
        def create_widget(self):

            vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
            
            appliedFormattersContainer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            
            vbox.pack_start(appliedFormattersContainer,True,True,0)
            filterContainer = Gtk.Box(spacing=0)
            self.scrollContainer = Gtk.ScrolledWindow()
            
            appliedFormattersContainer.pack_start(self.scrollContainer,True,True,0)
            
            
            self.current_filter_language = None
            
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
            
            
            
            #filterContainer.pack_start(self.treeview,True,True,0)

            
            
            return vbox
        
        def language_filter_func(self, model, iter, data):
            if self.current_filter_language is None or self.current_filter_language == "None":
                return True
            else:
                return model[iter][1] == self.current_filter_language
  
        
        def packet_tree_clicked(self, tree_selection):
#             print(tree_selection)
            (model, pathlist) = tree_selection.get_selected_rows()
            for path in pathlist :
                tree_iter = model.get_iter(path)
                value = model.get_value(tree_iter,0)
                value2 = model.get_value(tree_iter, 1)
                self.packetclicked = "<b>"+value+" Protocol: "+value2+"</b>"
                self.e_widget.packetLabel.set_markup(self.packetclicked)
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

            
        