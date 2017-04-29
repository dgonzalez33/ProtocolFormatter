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
            self.treeview.connect("row-activated", self.packet_tree_clicked)
            
            self.add_columns_to_list("Packet id", 0)  
            self.add_columns_to_list("Proto Name", 1)
            self.add_columns_to_list("Showname", 2)
            self.add_columns_to_list("Size", 3)
            self.add_columns_to_list("Pos", 4)
 
  
            
#             renderer_text = Gtk.CellRendererText()
#             column_text = Gtk.TreeViewColumn("Packetid", renderer_text, text=0)
#             self.treeview.append_column(column_text)
#     
#             renderer_editabletext = Gtk.CellRendererText()
#             #renderer_editabletext.set_property("editable", True)
#     
#             column_editabletext = Gtk.TreeViewColumn("Protocol",renderer_editabletext, text=1)
#             self.treeview.append_column(column_editabletext)
    
            #renderer_editabletext.connect("edited", self.text_edited)
            
            
            filterContainer.pack_start(self.treeview,True,True,0)
            
            scrollContainer.add(filterContainer)

            
            return vbox
        
        def packet_tree_clicked(self, widget, x, y):
            self.packetclicked = "<b>Packet: "+x.to_string()+" Selected</b>"
            print(self.packetclicked)
            self.e_widget.packetLabel.set_markup(self.packetclicked)
            
        def set_editor_widget(self, widget):
            self.e_widget = widget
        
        def text_edited(self, widget, path, text):
            self.liststore[path][1] = text
            
#         def clear_columns(self):
#             x = 0
#             while(x < 5):
#                 if(self.treeview.get_column(x) != None):
#                     self.treeview.remove_column(self.treeview.get_column(x))
#                 print(self.treeview.get_column(x), x)
#                 x+=1
                
            
        def add_columns_to_list(self, name, num):
            renderer_text = Gtk.CellRendererText()
            column_text = Gtk.TreeViewColumn(name, renderer_text, text=num)
            self.treeview.append_column(column_text)
            
        def clear_list(self):
            self.liststore.clear()
            
        def add_to_list(self, value):
            self.liststore.append(value)

            
        