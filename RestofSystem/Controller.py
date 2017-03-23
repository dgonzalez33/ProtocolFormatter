
from PDMLSub.PDMLManager import pdmlmanager
from windows.WindowController import WindowController


class controller:
    
    packets = []
    pdml_attributes = {}
    protos = []
    
    p_manager = pdmlmanager()
    w_controller = WindowController()
    w_controller.main()
    
    def __init__(self):
        self.create_self()
        self.packets = []
        self.protos = []
        self.pdml_attributes = {}
     
    def create_self(self):
        #print("pdml class instantiated")
        return 0
        
        
    
    


if(__name__ == "__main__"):
    d = controller()
    
