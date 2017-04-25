
class packet:
    
    packetid = 0;
    proto_elements = []
    packet_attributes = {}
    
    def __init__(self):
        self.create_self()
     
    def create_self(self):
        print("packet class")
        
    def set_packet_id(self, id):
        self.packetid = id
        
    def set_proto_element(self, index, proto):
        self.proto_elements[index] = proto
    
    def set_packet_attrib(self, key, val):
        self.packet_attributes[key] = val
                
    def get_proto_element(self, id, protoname, fieldname):
        return self.proto_elements
    
    def get_field_attributes(self):
        return self.packet_attributes
    
    def get_packet_id(self):
        return self.packetid
    



if(__name__ == "__main__"):
    d = packet()
    
