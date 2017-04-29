
from PDMLSub.PDMLManager import pdmlmanager

from gi.repository import GObject

class controller:

    #p_manager = pdmlmanager("../Scripts/dns_query_response2.pdml")
   # w = WindowController()

    
    def __init__(self):
        GObject.threads_init()
        self.create_self()
        GObject.idle_add(self.update_after)
       # self.w.main()

     
    def create_self(self):
        #print("hello")
        #print(self.p_manager.get_pdml_as_text())
        return 0
    
    def update_after(self):
        print("after")
        #self.w.packet_widget.set_packet_window_text(self.p_manager.get_pdml_as_text())
        return 0;
    
    def set_pdml_file(self, filename):
        self.pdmlman = pdmlmanager(filename)
        return 0
    
    def get_pdml_text(self):
        return self.pdmlman.get_pdml_as_text()
    
    def get_pdml_protocols(self):
        return self.pdmlman.get_all_protocol_names()
    
    def get_packets_of_protocol(self, val):
        return self.pdmlman.get_packets_with_protocol(val)
    
    def get_all_packets(self):
        return self.pdmlman.get_all_packets()
        
    


    
