
from PDMLSub.PDMLManager import pdmlmanager
from windows.WindowController import WindowController
from gi.repository import GObject

class controller:

    p_manager = pdmlmanager("../Scripts/dns_query_response2.pdml")
    w = WindowController()

    
    def __init__(self):
        self.create_self()
        GObject.idle_add(self.update_after)
        self.w.main()

     
    def create_self(self):
        #print("hello")
        #print(self.p_manager.get_pdml_as_text())
        return 0
    
    def update_after(self):
        print("after")
        #self.w.packet_widget.set_packet_window_text(self.p_manager.get_pdml_as_text())
        return 0;
        
    


if(__name__ == "__main__"):
    GObject.threads_init()
    d = controller()
    

    
