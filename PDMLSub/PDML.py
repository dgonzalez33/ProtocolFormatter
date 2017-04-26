
class pdml:
    
    packets = []
    pdml_attributes = {}
    protos = []
    
    def __init__(self):
        self.create_self()
     
    def create_self(self):
        print("pdml class")
        
        
    def set_pdml_attrib(self, key, val):
        self.pdml_attributes[key] = val        
    
    def set_packet(self, index, pac):
        self.packets[index] = pac
    
    def set_protos(self, index, pro):
        self.protos[index] = pro
    
    def get_all_protocols(self):
        return self.protos
    
    def get_pdml_attributes(self):
        return self.pdml_attributes
    
    def get_packet_with_id(self, id):
        len_of_packets = len(self.packets)
        x = 0
        while(x < len_of_packets):
            if(self.packets[x].packetid == id):
                return self.packets[x]
        return 0
    
    


if(__name__ == "__main__"):
    d = pdml()
    
