from PDMLSub.PDMLParser import pdmlparser

class pdmlmanager:
    

    parser = pdmlparser("../Scripts/dns_query_response2.pdml")
    
    def __init__(self, f):
        self.create_self()
        self.packets = []
        self.protos = []
        self.pdml_attributes = {}
        self.parser = pdmlparser(f)
     
    def create_self(self):

        print("packets with proto'udp'",self.get_packets_with_protocol("udp"))
        print("packet with id 1", self.get_packet_of_id(1))
        print("all packets:",self.get_all_packets())
        print("all proto names", self.get_all_protocol_names())
        print("field'sll.pkttype'of sll in packet1 :",self.get_field_element(1,"sll","sll.pkttype"))
        return 0
        
        
    def get_pdml_as_text(self):
        result = self.parser.read_file_as_text()
        return result 
    
    def get_packets_with_protocol(self, protocol):
        packets = self.parser.get_packets_of_protocols(protocol)
        return packets   
    
    def get_packet_of_id(self, num):
        return self.parser.get_packet_of_id_from_pdml(num)
    
    def get_all_packets(self):
        packets = self.parser.get_all_packets_of_pdml()
        return packets
    
    def get_all_protocol_names(self):
        protonames = self.parser.get_all_protocol_names()
        return protonames
        
    def get_field_element(self, packetid, protocol, key): 
        return self.parser.get_field_of_proto_from_packet(packetid, protocol, key)
        
    
    
    


if(__name__ == "__main__"):
    d = pdmlmanager()
    
