
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
    
    def get_packet_with_id(self, id):
        len_of_packets = len(self.packets)
        x = 0
        while(x < len_of_packets):
            if(self.packets[x].packetid == id):
                return self.packets[x]
        return 0
    
    def get_all_packets(self):
        return self.packets
    
    


if(__name__ == "__main__"):
    d = pdml()
    
