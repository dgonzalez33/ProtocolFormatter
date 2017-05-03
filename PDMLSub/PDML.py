
class pdml:
    
    
    def __init__(self):
        self.packets = []
        self.protos = []
        self.misc_string = []
        self.misc_linenum = []


        
    def set_pdml_attrib(self, key, val):
        self.pdml_attributes[key] = val        
    
    def set_packet(self, pac):
        self.packets.append(pac)
    
    def set_protos(self, pro):
        self.protos.append(pro)
        
    def set_misc_info(self, value, line):
        self.misc_string.append(value)
        self.misc_linenum.append(line)
    
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
    
    def get_misc_strings(self):
        return self.misc_string
    
    def get_misc_linenums(self):
        return self.misc_linenum
    
    
    
    


if(__name__ == "__main__"):
    d = pdml()
    
