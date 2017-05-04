#!/usr/bin/python3
import re
import os 
import json
from PDMLSub.PDMLManager import pdmlmanager
class Filter:
    def setFilter(self):
        self.bpfFilter = self.bpfFilter.replace("&&", "and")
        self.bpfFilter = self.bpfFilter.replace("||", "or")
        self.bpfFilter = self.bpfFilter.replace("!", "not")
        self.bpfFilter = self.bpfFilter.lower()
        try:
            portRange = self.bpfFilter.split("portrange",1)[1].split(" ")[1]
            ports = portRange.split("-")
            newRange = ""
            for i,j in zip(ports[0],ports[0]):
                newRange += "["+str(i)+"-"+str(j)+"]"
            for i in range(len(ports[0]),len(ports[1])):
                newRange += "[0-"+ports[1][i]+"]"
            self.bpfFilter = self.bpfFilter.replace(portRange,newRange)
        except IndexError:
            pass
        self.bpfFilter = self.bpfFilter.replace("portrange","port")
        self.bpfFilter = self.bpfFilter.replace("src or dst host","host")
        self.bpfFilter = self.bpfFilter.replace("src and dst host","&host")
        self.bpfFilter = self.bpfFilter.replace("src host","src_host")
        self.bpfFilter = self.bpfFilter.replace("dst host","dst_host")
        self.bpfFilter = self.bpfFilter.replace("src or dst net","net")
        self.bpfFilter = self.bpfFilter.replace("src and dst net","&net")
        self.bpfFilter = self.bpfFilter.replace("src net","src_net")
        self.bpfFilter = self.bpfFilter.replace("dst host","dst_net")
        self.bpfFilter = self.bpfFilter.replace("src port","src_port")
        self.bpfFilter = self.bpfFilter.replace("dst port","dst_port")
        self.bpfFilter = self.bpfFilter.replace("src or dst port","port")
        self.bpfFilter = self.bpfFilter.replace("src and dst port","&port")
        self.bpfFilter = self.bpfFilter.replace("ether","ip")
        for proto in self.etherProtos:
            self.bpfFilter = self.bpfFilter.replace("ether proto "+proto,proto)
        for proto in self.ipProtos:
            self.bpfFilter = self.bpfFilter.replace("ip proto "+proto,proto)
        for proto in self.isoProtos:
            self.bpfFilter = self.bpfFilter.replace("iso proto "+proto,proto)
        for proto in self.protocols:
            self.bpfFilter = self.bpfFilter.replace(proto+" ",proto+".")
        # self.bpfFilter = self.bpfFilter.replace("ip ","ip.")
        parseList = self.bpfFilter.split("and")
        andList = list()
        for primAnd in parseList:
            parseOr = primAnd.split(" or ")
            orList = list()
            for primOr in parseOr:
                primOr = primOr.rstrip().lstrip()
                if("net" in primOr):
                    primOr = primOr.replace("net", "host")
                    primOr += ".*"
                else:
                    primOr += "$"
                if("not" in primOr):
                    primOr = primOr.replace("not ","")
                    if ' ' in primOr:
                        ind = primOr.index(' ')
                        primOr = primOr[:ind+1] + "(?!"+primOr[ind+1:] + ")"
                    else:
                        primOr = primOr[:0] + "(?!"+primOr[0:] + ")"
                ors = primOr.split(" ")
                if("." not in ors[0]):
                    ors[0] = '.*[.]'+ors[0]+"$"
                if(ors[0][-2:] == ".$"):
                    ors[0] = ors[0][:-2]
                if(ors[0][-3:] == ".$)"):
                    ors[0] = ors[0][:-3]+")"

                if("&" in ors[0]):
                    andInd = ors[0].index('&')
                    if("host" in ors[0]):
                        ors[0] = ors[0].replace("&host","src_host")
                        andList.append([[ors[0].replace("src_host","dst_host"),ors[1]]])
                    elif("port" in ors[0]):
                        ors[0] = ors[0].replace("&port","src port")
                        andList.append([[ors[0].replace("src_port","dst_port"),ors[1]]])
                orList.append(ors)
            andList.append(orList)
        self.parseList = andList
        #print(andList)
        return andList

    def set_pdmlman(self, pman):
        self.pdmlman = pman

    def applyFilter(self):
        self.setFilter()
        self.protosKept = list()
        self.viewProtos = list()
        packets = self.pdmlman.get_all_packets()
        for pack in packets:
            protos = pack.get_proto_element()
            for proto in protos:
                protoNames = proto.get_all_proto_attrib_names()
                protoVals = proto.get_all_proto_attrib_values()
                protoNameInd = protoNames.index("proto name")
                fields = proto.get_field_element()
                isKeptBool = True
                for ands in self.parseList:
                    isOrKeptBool = False
                    for ors in ands:
                        for field in fields:
                            fieldNames = field.get_all_field_attributes_name()
                            fieldValues = field.get_all_field_attributes_value()
                            try:
                                nameInd = fieldNames.index("field name")
                                showInd = fieldNames.index("show")
                            except ValueError:
                                continue
                            if(len(ors)==1):
                                isOrKeptBool = isOrKeptBool or bool(re.match(ors[0],protoVals[protoNameInd]))
                            else:
                                isOrKeptBool = isOrKeptBool or bool(re.match(ors[0],fieldValues[nameInd])) and bool(re.match(ors[1],fieldValues[showInd]))
                            if(isOrKeptBool):
                                break
                        if(isOrKeptBool):
                            break
                    isKeptBool = isOrKeptBool and isKeptBool                            
                if(isKeptBool is True):
                    self.protosKept.append(proto)
                    self.viewProtos.append( (pack.get_packet_id(), protoVals[protoNameInd]) )
                    #break
        # return self.protosKept

    # def applyContent(self, pdmlMan):
    #     protosKept = list()
    #     packets = pdmlMan.get_all_packets()
    #     for pack in packets:
    #         protos = pack.get_proto_element()
    #         for proto in protos:
    #             protoNames = proto.get_all_proto_attrib_names()
    #             protoVals = proto.get_all_proto_attrib_values()
                
    #             for names,vals in zip(protoNames,protoVals):

    #             fields = proto.get_field_element()
    def getFormatterProtos(self):
        return self.protosKept   
                 
    def getViewProtos(self):
        return self.viewProtos

    def setContentFilter(self, iContentFilter, eContentFilter):
        self.iContentFilter = iContentFilter
        self.eContentFilter = eContentFilter

    def saveFilter(self,name):
        filterJson = {}
        filterJson["bpf"] = self.bpfFilter
        filterJson["include"] = self.iContentFilter
        filterJson["exclude"] = self.eContentFilter
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(dir_path+"/Filters/"+name+".json", "w") as f:
            json.dump(filterJson,f)

    def __init__(self):
        self.protocols = ['ether', 'fddi','tr','wlan','ip','ip6','arp','rarp',
        'decnet', 'tcp', 'udp','eth']
        self.ipProtos = ['icmp', 'icmp6', 'igmp', 'igrp', 'pim', 'ah', 'esp', 'vrrp', 'udp','tcp']
        self.etherProtos = ['ip', 'ip6', 'arp', 'rarp', 'atalk', 'aarp', 'decnet', 'sca', 'lat', 'mopdl', 'moprc', 'iso', 'stp', 'ipx', 'netbeui']
        self.isoProtos = ['clnp', 'esis','isis']
        self.types = ['host','net','port','portrange','len']
        self.conditionals = ['==','!=','>','<','>=','<=']
        self.conjuctions = ['and', 'or','&&', '||']
        self.dirs = ['src','dst']
        self.bpfFilter = ""
        self.iContentFilter = ""
        self.eContentFilter = ""
        self.parseList = list()
        
    def set_bpf_filter(self, bpf, icontent, econtent):
        self.iContentFilter = icontent
        self.eContentFilter = econtent
        self.bpfFilter = bpf+" "

    


# sfilter = Filter("ip net 192","","")
# result = sfilter.setFilter()
# print(result)
# sfilter.applyFilter( pdmlmanager("Scripts/cubic.pdml") )
# pdmlString = ""
# for proto in sfilter.protosKept:
#     protoNames = proto.get_all_proto_attrib_names()
#     protoVals = proto.get_all_proto_attrib_values()
#     pdmlString += ("<")
#     for name, val in zip(protoNames,protoVals):
#         pdmlString += (name+"=\""+val+"\"")
#     pdmlString += (">\n")
#     fields = proto.get_field_element()
#     for field in fields:
#         fieldNames = field.get_all_field_attributes_name()
#         fieldValues = field.get_all_field_attributes_value()
#         pdmlString += ("\t<")
#         for name, val in zip(fieldNames, fieldValues):
#             pdmlString += (name+"=\""+val+"\"")
#         pdmlString += ("/>\n")
#     pdmlString += ("</proto>\n")
# # print(pdmlString)
# protView = sfilter.getViewProtos()
# print(protView)