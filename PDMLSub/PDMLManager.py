import sys
sys.path.insert(0, '../')

from PDMLSub.PDMLParser import pdmlparser

class pdmlmanager:
    


    def __init__(self, f):
        self.parser = pdmlparser(f)
        self.packets = []
        self.result = ""
        self.protonames = []
        self.create_self()
     
    def create_self(self):
        
#         print("packets with proto'udp'",self.get_packets_with_protocol("udp"))
#         print("packet with id 1", self.get_packet_of_id(1))
#         print("all packets:",self.get_all_packets())
#         print("all proto names", self.get_all_protocol_names())
#         print("field: udp.port in proto: udp or packet 1",self.get_field_element(1,"udp","udp.port"))
        return 0
        
        
    def get_pdml_as_text(self):
        return self.parser.lastfileread
    
    def get_packets_with_protocol(self, protocol):
        self.packets = []
        self.packets = self.parser.get_packets_of_protocols(protocol)
        return self.packets   
    
    def get_packet_of_id(self, num):
        return self.parser.get_packet_of_id_from_pdml(num)
    
    def get_all_packets(self):
        self.packets = self.parser.get_all_packets_of_pdml()
        return self.packets
    
    def get_all_protocol_names(self):
        self.protonames = self.parser.get_all_protocol_names()
        return self.protonames
        
    def get_field_element(self, packetid, protocol, key): 
        return self.parser.get_field_of_proto_from_packet(packetid, protocol, key)
    
    def get_pdml(self):
        return self.parser.get_root_pdml();
        
    
    
    


if(__name__ == "__main__"):
    d = pdmlmanager("../Scripts/dns_query_response2.pdml")
    
