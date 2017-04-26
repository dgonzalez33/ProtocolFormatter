#Command line widget
#python 3.5
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class HistoricalCopyWidget:

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
        
        #create a container for the packet 
        packetContainer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        
        packetBuffer = Gtk.TextBuffer()
        filetext = "\n\n\n\n            <Historical Packet Contents>\n\n\n\n"

        packetBuffer.set_text(filetext)
        
        #create a Textviewer
        packetView = Gtk.TextView()
        packetView.set_buffer(packetBuffer)
        
        #packetviewer is now a child of packet container 
        packetContainer.pack_start(packetView, False, False, 0)

        restorebutton = Gtk.Button.new_with_label("Restore")
        packetContainer.pack_start(restorebutton, False, False, 0)


        
        #add the packetview to the scroll window 
        scrollContainer.add(packetContainer)
        
        #scroll window is now a child of the full container
        fullContainer.pack_start(scrollContainer,True,True,0)
        
        return vbox
