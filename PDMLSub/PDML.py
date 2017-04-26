
class pdml:
    
    packets = []
    pdml_attributes = {}
    protos = []
    
    def __init__(self):
        self.create_self()
        self.packets = []
        self.protos = []
        self.pdml_attributes = {}
     
    def create_self(self):
        #print("pdml class instantiated")
        return 0
        
        
    def set_pdml_attrib(self, key, val):
        self.pdml_attributes[key] = val        
    
    def set_packet(self, pac):
        self.packets.append(pac)
    
    def set_protos(self, pro):
        self.protos.append(pro)
    
    def get_all_protocols(self):
        return self.protos
    
    def get_pdml_attributes(self):
        return self.pdml_attributes
    
    def get_packet_with_id(self, num):
        if(num < 0 or num > len(self.packets)):
            return "invalid id"
        else:
            return self.packets[num]
        return "Packet not found"
    
    def get_all_packets(self):
        return self.packets
    
    


if(__name__ == "__main__"):
    d = pdml()
    
