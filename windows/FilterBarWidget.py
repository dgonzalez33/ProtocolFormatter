
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from windows.packetWidget import PacketWidget

class FilterBarWidget:
    
    
    def __init__(self):
        self.currenttext = "<Enter Filter>"
        self.p_widget = PacketWidget()

    def create_widget(self):
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)

        filterbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        
        
        filterlabelframe = Gtk.Frame()
        filterlabelframe.set_label("Filter Bar")
        filterlabelframe.set_label_align( 0.5, 0)
        filterlabelframe.show()

        
        protolabel = Gtk.Label()
        protolabel.set_text("Proto name:")
        protolabel.show()
        
        
        
        self.protoEntry = Gtk.Entry()
    
       
        
        submitbutton = Gtk.Button("Submit")
        submitbutton.connect("clicked", self.update_filter)
        submitbutton.show()
        
        
        filterbox.add(protolabel)
        filterbox.add(self.protoEntry)

        filterbox.add(submitbutton)
        
        filterlabelframe.add(filterbox)
        
        vbox.pack_start(filterlabelframe,False,False,5)
        #vbox.pack_start(filterbox,False,False,0)

        
        
        return vbox
    
    def update_filter(self, val):
        #print("protoentry: ",self.protoEntry.get_text())
        if(self.protoEntry.get_text() == ""):
            self.p_widget.current_filter_language = None 
        else:
            templist = []
            templist.append(self.protoEntry.get_text())
            self.p_widget.set_filter_list_all_packets(templist)
        #self.p_widget.refilter_list()

        
    def set_packet_widget(self, widget):
        self.p_widget = widget
        
        
