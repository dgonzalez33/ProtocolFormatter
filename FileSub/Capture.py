from FileSub.Tshark_Handler import Tshark_Handler
from PDMLSub.PDMLManager import pdmlmanager
from subprocess import call

class Capture:
    def createCapture(self, filePath):
        if(self.isCapture(filePath)):
            self.filePath = filePath
            if(self.isPDML(filePath) is False):
                self.filePath = Tshark_Handler().createPDML(filePath)
        else:
            self.filePath = None
        return self.filePath
    def __init__(self, filePath):
        
        self.pdmlman = pdmlmanager(filePath)
        self.pdml = self.pdmlman.get_pdml()
        self.save_pdml(self.pdml, filePath)
        

        return
    def isPDML(self,filePath):
        return filePath.lower().endswith('.pdml')
    
    def save_pdml(self,pdml,filePath):
        pdmlString = self.pdml_object_to_string(self.pdml)
        #print(pdmlString)
        miscstrings = self.pdml.get_misc_strings()
        misclinenumbers = self.pdml.get_misc_linenums()
        with open(filePath, "w") as f:
            #print(pdmlString)
            f.write(pdmlString)    
            x = 0
#         print(miscstrings)
        while(x < len(miscstrings)):
            cmd = str(misclinenumbers[x])+"i "+ miscstrings[x]
            call(["sed", "-i", cmd, filePath])
            x+=1
            
      
        
        cmd = str(self.file_len(filePath))+"d"
        
        call(["sed", "-i", cmd, filePath])

            
       
    def file_len(self,fname):
        with open(fname) as f:
            for i, l in enumerate(f):
                pass
        return i + 1
          
    def pdml_object_to_string(self,pdml):
        current_indent = 0
        indent = "  "
        pdmlString = ''
        packets = self.pdml.get_all_packets()
        numofmiscline = self.pdml.get_misc_strings()
        y = 0
        extralinecounter = 0
        while(y < len(numofmiscline)):
            if(numofmiscline[y] == "\n"):
                extralinecounter+=1
            y+=1
        numofmiscline = extralinecounter
        print(numofmiscline)
        count = 0
        while(count < len(packets)):
            pdmlString += "<packet>\n"
            protos = packets[count].get_proto_element()
            count2 = 0
            while(count2 < len(protos)):
                protoNames = protos[count2].get_all_proto_attrib_names()
                protoVals = protos[count2].get_all_proto_attrib_values()
                pdmlString += (indent)+("<")
                count3 = 0
                while(count3 < len(protoNames)):
                    pdmlString += (protoNames[count3]+"=\""+protoVals[count3]+"\" ")
                    count3 +=1
                pdmlString = pdmlString[:-1]  
                pdmlString += (">\n")
                fields = protos[count2].get_field_element()
                count4 = 0
                prevIndent = 0
                while(count4 < len(fields)):
                    fieldNames = fields[count4].get_all_field_attributes_name()
                    fieldValues = fields[count4].get_all_field_attributes_value()
                    fieldIndent = fields[count4].get_depth_of_indent()
                    current_indent = fieldIndent
                    if(prevIndent > fieldIndent):
                        while(prevIndent > 0 and prevIndent > fieldIndent):
                            pdmlString += ((indent*(1+prevIndent)+"</field>\n"))
                            prevIndent-= 1
                    pdmlString += ((indent*(2+fieldIndent))+"<")
                    count5 = 0
                    while(count5 < len(fieldNames)):
                        pdmlString += (fieldNames[count5]+"=\""+fieldValues[count5]+"\" ")
                        count5 +=1
                    pdmlString = pdmlString[:-1]  
                    pdmlString += fields[count4].endcap+"\n"
                    if(count4 > 0):
                        prevIndent = fieldIndent
                    count4+=1
                count2 +=1
                while(current_indent > 0):
                    pdmlString += ((indent*(1+current_indent)+"</field>\n"))
                    current_indent-= 1
                pdmlString += ((indent)+"</proto>\n")
            count+=1
            pdmlString += "</packet>\n"
            
#         x = 0
#         while( x < numofmiscline):
#             pdmlString += "\n"
#             x+=1
        pdmlString+='\n'
        #print(pdmlString)
        return pdmlString

    def isCapture(self, filePath):
        return filePath.lower().endswith(('.pdml','.pcap','pcapng'))
    def getFilePath(self):
        return self.filePath
    
if(__name__ == "__main__"):
    d = Capture("../Scripts/dns_query_response2.pdml")

    
    
    
    
    
    
    
    
    