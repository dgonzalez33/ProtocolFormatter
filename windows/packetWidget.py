import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class PacketWidget:
        packetBuffer = Gtk.TextBuffer()
        packetView = Gtk.TextView()
             
        def create_widget(self):
            
            #vbox is the top_level parent
            vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        
            #fullContainer is a container for the whole  widget
            fullContainer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            
            #buttonContainer contains the buttons
            buttonContainer = Gtk.Box(spacing=6)
            
            #pack_start says fullContainer is now a child of vbox
            vbox.pack_start(fullContainer,True,True,0)
            
            #create a scrollable container (ScrolledWindow is not really a 'window')
            scrollContainer = Gtk.ScrolledWindow()
            adj = Gtk.Adjustment()
            adj.set_page_size(500)
            scrollContainer.set_hadjustment(adj)
            #create a container for the packet 
            
            self.listbox = Gtk.ListBox()
            self.row = Gtk.ListBoxRow()
            packetContainer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
            
            
            filetext = "\n\n\n\n			<Packet Contents Shown Here>\n\n\n\n"

            self.set_packet_window_text(filetext)
            
            #packetviewer is now a child of packet container 
            packetContainer.pack_start(self.packetView, False, False, 0)
            
            #add the packetview to the scroll window 
            scrollContainer.add(packetContainer)
            
            #scroll window is now a child of the full container
            fullContainer.pack_start(scrollContainer,True,True,0)
            
            return vbox
        
        def set_packet_window_text(self, filetext):
            self.packetBuffer = Gtk.TextBuffer()
            self.packetBuffer.set_text(filetext)
            self.packetView.set_buffer(self.packetBuffer)
            return 0
      
        def read_file(self, filename):
            with open(filename, 'r') as myfile:
                data = myfile.read()
            self.packetBuffer.set_text(data)
            self.packetView.set_buffer(self.packetBuffer)
            return data


