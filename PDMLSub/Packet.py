
class packet:
    
    packetid = 0;
    proto_elements = []
    packet_attributes = {}
    
    def __init__(self):
        self.create_self()
        self.proto_elements = []
        self.packet_attributes = {}
     
    def create_self(self):
        #print("packet class")
        return 0
        
    def set_packet_id(self, ident):
        self.packetid = ident
        
    def set_protoelement(self, proto):
        self.proto_elements.append(proto)
        
    def set_packet_attrib(self, key, val):
        self.packet_attributes[key] = val
                
    def get_proto_element(self):
        return self.proto_elements
    
    def get_proto_element_at_index(self, index):
        return self.proto_elements[index]
    
    def get_field_attributes(self):
        return self.packet_attributes
    
    def get_packet_id(self):
        return self.packetid
    



if(__name__ == "__main__"):
    b = packet()
    
