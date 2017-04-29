import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from windows.editorWidget import EditorWidget


class PacketWidget:

        def __init__(self):
            self.liststore = Gtk.ListStore(str, str)
            self.packetclicked = ""
            self.e_widget = EditorWidget()
        
             
        def create_widget(self):

            vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
            
            appliedFormattersContainer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            vbox.pack_start(appliedFormattersContainer,True,True,0)
            filterContainer = Gtk.Box(spacing=0)
            scrollContainer = Gtk.ScrolledWindow()
            
            appliedFormattersContainer.pack_start(scrollContainer,True,True,0)
            
            
            self.liststore = Gtk.ListStore(str, str)
            self.add_to_list("packet 1", "tcp")
    
            treeview = Gtk.TreeView(model=self.liststore)
            treeview.connect("row-activated", self.packet_tree_clicked)
            
            
            renderer_text = Gtk.CellRendererText()
            column_text = Gtk.TreeViewColumn("Packetid", renderer_text, text=0)
            treeview.append_column(column_text)
    
            renderer_editabletext = Gtk.CellRendererText()
            #renderer_editabletext.set_property("editable", True)
    
            column_editabletext = Gtk.TreeViewColumn("Protocol",renderer_editabletext, text=1)
            treeview.append_column(column_editabletext)
    
            #renderer_editabletext.connect("edited", self.text_edited)
            
            filterContainer.pack_start(treeview,True,True,0)
            
            scrollContainer.add(filterContainer)

            
            return vbox
        
        def packet_tree_clicked(self, widget, x, y):
            #packet_editor_title = "<Packet:"+str(x)+"> Selected"
            self.packetclicked = "<b>Packet: "+x.to_string()+" Selected</b>"
            print(self.packetclicked)
            self.e_widget.packetLabel.set_markup(self.packetclicked)
            
        def set_editor_widget(self, widget):
            self.e_widget = widget
        
        def text_edited(self, widget, path, text):
            self.liststore[path][1] = text
            
        def clear_list(self):
            self.liststore.clear()
            
        def add_to_list(self, p_name, proto):
            self.liststore.append([p_name, proto])

            
        