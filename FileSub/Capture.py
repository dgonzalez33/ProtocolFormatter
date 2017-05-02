from FileSub.Tshark_Handler import Tshark_Handler
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
        return
    def isPDML(self,filePath):
        return filePath.lower().endswith('.pdml')
    def save_pdml(self,pdml,filePath):
        pdmlString = pdml_object_to_string(pdml)
        with open(filePath, "w") as f:
            f.write(pdmlString)    
    def pdml_object_to_string(self,pdml):
        indent = "  "
        pdmlString = '<?xml version="1.1"?>\n'
        pdmlString += '<?xml-stylesheet type="text/xsl" href="pdml2html.xsl"?>\n'
        pdmlString += '<!-- You can find pdml2html.xsl in /usr/share/wireshark or at https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob_plain;f=pdml2html.xsl. -->\n'
        pdmlString += "<pdml>\n"
        ##Missing PDML attributes non existent in other places :SSSS
        packets = pdml.get_all_packets()
        for packet in packets:
            pdmlString += "<packet>\n"
            protos = packet.get_proto_element()
            for proto in protos:
                protoNames = proto.get_all_proto_attrib_names()
                protoVals = proto.get_all_proto_attrib_values()
                pdmlString += (indent)+("<")
                for name, val in zip(protoNames,protoVals):
                    pdmlString += (name+"=\""+val+"\"")
                pdmlString += (">\n")
                fields = proto.get_field_element()
                ##SubFields are not represented properly :ssssss
                for field in fields:
                    fieldNames = field.get_all_field_attributes_name()
                    fieldValues = field.get_all_field_attributes_value()
                    pdmlString += ((indent*2)+"<")
                    for name, val in zip(fieldNames, fieldValues):
                        pdmlString += (name+"=\""+val+"\"")
                    pdmlString += ("/>\n")
                pdmlString += ((indent)+"</proto>\n")
            pdmlString += "</packet>\n\n"
        #extra line is on purpose for pdmls
        pdmlString += "\n</pdml>"
        print(pdmlString)

    def isCapture(self, filePath):
        return filePath.lower().endswith(('.pdml','.pcap','pcapng'))
    def getFilePath(self):
        return self.filePath