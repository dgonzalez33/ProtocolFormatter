from PDML import pdml
from Packet import packet
from ProtoElement import protoelement
from FieldElement import fieldelement

class pdmlparser:
    
    pdml = pdml()
    
    debug_print = 0
    
    len_of_pdml = 0
    
    num_of_pdml = 0
    num_of_packet = 0
    num_of_proto = 0
    num_of_field = 0
    
    total_num_of_pdml = 0
    total_num_of_packet = 0
    total_num_of_proto = 0
    total_num_of_field = 0
    
    
    def __init__(self, pdmlfilepath):
        self.parse_pdml(pdmlfilepath)
     
    def parse_pdml(self, pdmlfilepath):
        self.num_of_lines(pdmlfilepath)
        self.read_file(pdmlfilepath)
        if(self.debug_print == 1):
            print("total num of pdmls: ",self.total_num_of_pdml)
            print("total num of packets: ",self.total_num_of_packet)
            print("total num of protos: ",self.total_num_of_proto)
            print("total num of fields: ",self.total_num_of_field)
            self.test_structure_depth()

        
    def test_structure_depth(self):
        pdmlpackets = pdml.get_all_packets(pdml)
        len_of_packets = len(pdmlpackets)
        count = 0
        
        while(count < len_of_packets):
            print("packet: ",pdmlpackets[count].packetid)
            protocols = pdmlpackets[count].get_proto_element()
            len_of_protocols = len(protocols)
            count2 = 0
            
            while(count2 < len_of_protocols):
                print("protocol: ", count2)
                fieldlist = protocols[count2].get_field_element()
                len_of_fields = len(fieldlist)
                count3 = 0
                
                while(count3< len_of_fields):
                    print("field: ", count3)

                    count3+=1
                count2 += 1
            count+=1
    
    def get_root_pdml(self):
        return self.pdml
    
    
    def num_of_lines(self, filename):
        with open(filename, 'r') as myfile:
            data = myfile.readlines()
            self.len_of_pdml = len(data)

          
    def read_file(self, filename):
        with open(filename, 'r') as myfile:
            x = 0
            while(x < self.len_of_pdml):
                data = myfile.readline()
                
                if(data.find("<pdml>") != -1 or data.find("<pdml ") != -1):
                    if(self.debug_print == 1):
                        print("pdml number", self.num_of_pdml)
                        print(data)
                    self.num_of_pdml+=1
                    self.total_num_of_pdml+=1
                    
                if(data.find("<packet>") != -1 or data.find("<packet ") != -1):
                    if(self.debug_print == 1):
                        print("packet found", self.num_of_packet)
                        print(data)
                    p = packet()
                    p.set_packet_id(self.num_of_packet)
                    pdml.set_packet(pdml, p)
                    self.num_of_packet+=1
                    self.total_num_of_packet+=1
                    
                if(data.find("<proto ") != -1):
                    if(self.debug_print == 1):
                        print("    proto found", self.num_of_proto)
                        print(data)
                    pro = protoelement()
                    w = data.strip().split("\"")
                    xx = 0
                    while(xx < len(w)-1):
                        if(w[xx].find('<') != -1):
                            w[xx] = w[xx].strip('<.-')
                        if(w[xx].find('>')!= -1):
                            w[xx] = w[xx].strip('>.-')
                        if(w[xx].find('=') != -1):
                            w[xx] = w[xx].strip('=.-')
                            
                        if(w[xx+1].find('<') != -1):
                            w[xx+1] = w[xx+1].strip('<.-')
                        if(w[xx+1].find('>')!= -1):
                            w[xx+1] = w[xx+1].strip('>.-')
                        if(w[xx+1].find('=') != -1):
                            w[xx+1] = w[xx+1].strip('=.-')

                        pro.set_proto_attrib(w[xx].strip(), w[xx+1].strip())
                        xx+=2 
                        
                    p.set_protoelement(pro)
                    self.num_of_field = 0
                    self.num_of_proto+=1
                    self.total_num_of_proto+=1
                    
                if(data.find("<field ") != -1):
                    if(self.debug_print == 1):
                        print("        field found", self.num_of_field)
                        print(data)
                
                    field_e = fieldelement()
                    w = data.strip().split("\"")
                    xx = 0
                    while(xx < len(w)-1):
                        if(w[xx].find('<') != -1):
                            w[xx] = w[xx].strip('<.-')
                        if(w[xx].find('>')!= -1):
                            w[xx] = w[xx].strip('>.-')
                        if(w[xx].find('=') != -1):
                            w[xx] = w[xx].strip('=.-')
                            
                        if(w[xx+1].find('<') != -1):
                            w[xx+1] = w[xx+1].strip('<.-')
                        if(w[xx+1].find('>')!= -1):
                            w[xx+1] = w[xx+1].strip('>.-')
                        if(w[xx+1].find('=') != -1):
                            w[xx+1] = w[xx+1].strip('=.-')

                        field_e.set_field_attrib(w[xx].strip(), w[xx+1].strip())
                        xx+=2 
   
                    pro.set_field_element(field_e)
                    self.num_of_field+=1
                    self.total_num_of_field+=1
              
                
                if(data.find("</proto>") != -1):
                    self.num_of_field = 0
                
                if(data.find("</packet>") != -1):
                    self.num_of_proto = 0
                    self.num_of_field = 0
                    
                x+=1
                
    

if(__name__ == "__main__"):
    d = pdmlparser('dns_query_response2.pdml')
    
