from PDMLSub.PDML import pdml
from PDMLSub.Packet import packet
from PDMLSub.ProtoElement import protoelement
from PDMLSub.FieldElement import fieldelement

class pdmlparser:
    
    

    
    
    def __init__(self, pdmlfilepath):
        self.pdml = pdml()
        self.debug_print = 0
    
        self.len_of_pdml = 0
        
        self.lastfileread = ""
            
        self.num_of_pdml = 0
        self.num_of_packet = 0
        self.num_of_proto = 0
        self.num_of_field = 0
        
        self.total_num_of_pdml = 0
        self.total_num_of_packet = 0
        self.total_num_of_proto = 0
        self.total_num_of_field = 0
        self.parse_pdml(pdmlfilepath)
        self.read_file_as_text(pdmlfilepath)
     
    def parse_pdml(self, pdmlfilepath):
        #self.clean_pdml()
        self.num_of_lines(pdmlfilepath)
        self.pdml = self.read_file(pdmlfilepath)
        print("total num of pdmls: ",self.total_num_of_pdml)
        print("total num of packets: ",self.total_num_of_packet)
        print("total num of protos: ",self.total_num_of_proto)
        print("total num of fields: ",self.total_num_of_field)
        
        if(self.debug_print == 1):
            self.test_structure_depth()

    def get_total_num_of_pdml(self):
        return self.total_num_of_pdml
    
    def get_total_num_of_packet(self):
        return self.total_num_of_packet
    
    def get_total_num_of_proto(self):
        return self.total_num_of_proto
    
    def get_total_num_of_field(self):
        return self.total_num_of_field
    
    def get_packet_of_id_from_pdml(self, num):
        return self.pdml.get_packet_with_id(num)
    
    def get_packets_of_protocols(self, name):
        result = []
        pdmlpackets = self.pdml.get_all_packets()
        count = 0
        
        while(count < len(pdmlpackets)):
            protocols = pdmlpackets[count].get_proto_element()
            count2 = 0
            
            while(count2 < len(protocols)):
                p_names = protocols[count2].get_all_proto_attrib_names()
                p_values = protocols[count2].get_all_proto_attrib_values()
                count3 = 0
                while(count3 < len(p_names)):
                    if(p_names[count3] == "proto name"):
                        if(p_values[count3] == name):
                            result.append(pdmlpackets[count].get_packet_id())
                
                    count3+=1
                count2 += 1
            count+=1
        return result
    
    def get_field_of_proto_from_packet(self,packetid, protocol, key):
        packets = self.pdml.get_all_packets()
        if(packetid< 0 or packetid > self.total_num_of_packet):
            return "error, packetid out of index"
        protos = packets[packetid].get_proto_element()
        count = 0
        while(count < len(protos)):
            p_names = protos[count].get_all_proto_attrib_names()
            p_values = protos[count].get_all_proto_attrib_values()
            count2 = 0
            while(count2 < len(p_names)):
                if(p_names[count2] == "proto name"):
                    if(p_values[count2] == protocol):
                        fields = protos[count].get_field_element()
                        count3 = 0
                        while(count3 < len(fields)):
                            f_names = fields[count3].get_all_field_attributes_name()
                            f_values = fields[count3].get_all_field_attributes_value()
                            count4 = 0
                            while(count4 < len(f_names)):
                                if(f_names[count4] == "field name"):
                                    #print(f_values[count4])
                                    if(f_values[count4] == key):
                                        return fields[count3]
                                count4 +=1
                            count3 +=1
                count2 += 1
            count+=1   
        return "error (not found)"
    
    
        
    def get_all_packets_of_pdml(self):
        return self.pdml.get_all_packets()
    
    
    def get_all_protocol_names(self):
        protonames = {}
        Dup = {}
        pdmlpackets = self.pdml.get_all_packets()
        len_of_packets = len(pdmlpackets)
        count = 0
         
        while(count < len_of_packets):
            protocols = pdmlpackets[count].get_proto_element()
            len_of_protocols = len(protocols)
            count2 = 0
             
            while(count2 < len_of_protocols):
                p_names = protocols[count2].get_all_proto_attrib_names()
                p_values = protocols[count2].get_all_proto_attrib_values()
                count3 = 0
                while(count3< len(p_names)):
                    if(p_names[count3] == "proto name"):
                        protonames[protocols[count2].get_proto_attrib_value(count3)] = "found"
                    count3+=1
                count2 += 1
            count+=1
        protonames = list(protonames.keys())
        return protonames
    
    def test_structure_depth(self):
        pdmlpackets = self.pdml.get_all_packets()
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
    
    def clean_pdml(self):
        pdmlpackets = self.pdml.get_all_packets()
        len_of_packets = len(pdmlpackets)
        count = 0
        
        while(count < len_of_packets):
            protocols = pdmlpackets[count].get_proto_element()
            len_of_protocols = len(protocols)
            count2 = 0
            
            while(count2 < len_of_protocols):
                fieldlist = protocols[count2].get_field_element()
                len_of_fields = len(fieldlist)
                count3 = 0
                
                while(count3< len_of_fields):
                    
                    fieldlist[count3].field_attributes_names = []
                    fieldlist[count3].field_attributes_values = []
                    count3+=1
                    
                protocols[count2].proto_attributes_names = []
                protocols[count2].proto_attributes_values = []
                protocols[count2].field_elements = []
                count2 += 1
                
            pdmlpackets[count].proto_elements = []
            pdmlpackets[count].packetid = 0
            count+=1
        return 0
    
    
    def num_of_lines(self, filename):
        with open(filename, 'r') as myfile:
            data = myfile.readlines()
            self.len_of_pdml = len(data)

    def read_file_as_text(self, filename):
        with open(filename, 'r') as myfile:
            data = myfile.read()
            self.lastfileread = data
        return 0      
    
    def read_file(self, filename):
        with open(filename, 'r') as myfile:
            x = 0
            self.pdml = pdml()
            self.field_depth = 0
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
                    self.pdml.set_packet(p)
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
                        if(w[xx+1].find('/>')!= -1):
                            pro.set_proto_attrib(w[xx].strip(), w[xx+1].strip())
                            
                            w[xx+1] = w[xx+1].strip('>.-')
                        if(w[xx+1].find('=') != -1):
                            w[xx+1] = w[xx+1].strip('=.-')
                        pro.set_proto_attrib(w[xx].strip(), w[xx+1].strip())
                        xx+=2 
                    
                    p.set_protoelement(pro)
                    self.num_of_field = 0
                    self.num_of_proto+=1
                    self.total_num_of_proto+=1
                if(data.find("</field>") != -1):
                    self.field_depth -= 1
                    
                if(data.find("<field ") != -1):
                    if(self.debug_print == 1):
                        print("        field found", self.num_of_field)
                        print(data)
                
                    field_e = fieldelement()
                    w = data.strip().split("\"")
                   
                    xx = 0
                    while(xx < len(w)-1):

                        if(w[xx].find('<') != -1):
                            w[xx] = w[xx].strip('<') 
                        if(w[xx].find('>')!= -1):
                            w[xx] = w[xx].strip('>')
                        if(w[xx].find('=') != -1):
                            w[xx] = w[xx].strip('=')
                            
                        if(w[xx+1].find('<') != -1):
                            w[xx+1] = w[xx+1].strip('<')
                        if(w[xx+1].find('>')!= -1):
                            w[xx+1] = w[xx+1].strip('>')
                        if(w[xx+1].find('=') != -1):
                            w[xx+1] = w[xx+1].strip('=')
                        
                        field_e.set_field_attrib(w[xx].strip(), w[xx+1].strip())
                        xx+=2 
                        
                    xx = 0

                    pro.set_field_element(field_e)
                    field_e.set_depth_of_indent(self.field_depth)  
                    self.num_of_field+=1
                    self.total_num_of_field+=1
                       
                    if(w[len(w)-1] != "/>"):
                        field_e.endcap = ">"
                        self.field_depth+=1
                    else:
                        field_e.endcap = "/>"
              
                
                if(data.find("</proto>") != -1):
                    self.num_of_field = 0
                    
                
                if(data.find("</packet>") != -1):
                    self.num_of_proto = 0
                    self.num_of_field = 0
                    
                
                    
                x+=1
                
                if(data.find("</packet>") == -1 and data.find("</packet>") == -1 and data.find("<field ") == -1 and data.find("</field>") == -1 and data.find("<proto ") == -1 and data.find("</proto>") == -1 and data.find("<packet>") == -1 and data.find("<packet ") == -1):
                    self.pdml.set_misc_info(data, x)
                    #print(x, data)
                    
        return self.pdml
                
    
    
