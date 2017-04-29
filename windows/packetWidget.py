import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from windows.editorWidget import EditorWidget


class PacketWidget:

        def __init__(self):
            self.liststore = Gtk.ListStore(str, str, str, str, str)
            self.packetclicked = ""
            self.e_widget = EditorWidget()
        
             
        def create_widget(self):

            vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
            
            appliedFormattersContainer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            vbox.pack_start(appliedFormattersContainer,True,True,0)
            filterContainer = Gtk.Box(spacing=0)
            scrollContainer = Gtk.ScrolledWindow()
            
            appliedFormattersContainer.pack_start(scrollContainer,True,True,0)
            
            self.treeview = Gtk.TreeView(model=self.liststore)
            
            tree_selection = self.treeview.get_selection()
            tree_selection.set_mode(Gtk.SelectionMode.MULTIPLE)
            tree_selection.connect("changed", self.packet_tree_clicked)
            
            self.add_columns_to_list("Packet id", 0, 0)  
            self.add_columns_to_list("Proto Name", 1, 1)
            self.add_columns_to_list("Showname", 2, 2)
            self.add_columns_to_list("Size", 3, 3)
            self.add_columns_to_list("Pos", 4, 4)
 
            
            
            filterContainer.pack_start(self.treeview,True,True,0)
            
            scrollContainer.add(filterContainer)

            
            return vbox
        
        def packet_tree_clicked(self, tree_selection):
            (model, pathlist) = tree_selection.get_selected_rows()
            for path in pathlist :
                tree_iter = model.get_iter(path)
                value = model.get_value(tree_iter,0)
                self.packetclicked = "<b>Packet: "+value+" Selected</b>"
                self.e_widget.packetLabel.set_markup(self.packetclicked)

            
        def set_editor_widget(self, widget):
            self.e_widget = widget
        
        def text_edited(self, widget, path, text):
            self.liststore[path][1] = text
            
                
            
        def add_columns_to_list(self, name, num, s_id):
            renderer_text = Gtk.CellRendererText()
            column_text = Gtk.TreeViewColumn(name, renderer_text, text=num)
            column_text.set_clickable(True)
            column_text.set_sort_column_id(s_id)
            self.treeview.append_column(column_text)
            
        def clear_list(self):
            self.liststore.clear()
            
        def add_to_list(self, value):
            self.liststore.append(value)

            
        