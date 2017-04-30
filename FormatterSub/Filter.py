#!/usr/bin/python3
import re
from ..PDMLSub.PDMLManager import pdmlmanager
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
        return andList

    def applyFilter(self, pdmlMan):
        protosKept = list()
        packets = pdmlMan.get_all_packets()
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
                                # if(isOrKeptBool):
                            else:
                                # print(fieldValues[nameInd]+"------"+ors[0])
                                # print(bool(re.match(ors[0],fieldValues[nameInd])))
                                # print(fieldValues[showInd]+"------"+ors[1])
                                # print(bool(re.match(ors[1],fieldValues[showInd])))
                                # print(isOrKeptBool or bool(re.match(ors[0],fieldValues[nameInd])) and bool(re.match(ors[1],fieldValues[showInd])))
                                isOrKeptBool = isOrKeptBool or bool(re.match(ors[0],fieldValues[nameInd])) and bool(re.match(ors[1],fieldValues[showInd]))
                                # if(isOrKeptBool):
                                    # print(fieldValues[showInd]+","+ ors[1])
                                    # print(bool(re.match(ors[1],fieldValues[showInd])))
                            if(isOrKeptBool):
                                break
                        if(isOrKeptBool):
                            break
                    isKeptBool = isOrKeptBool and isKeptBool                            
                if(isKeptBool is True):
                    protosKept.append(proto)
                    break
                
                    
        return protosKept





    def __init__(self, bpfFilter):
        self.protocols = ['ether', 'fddi','tr','wlan','ip','ip6','arp','rarp',
        'decnet', 'tcp', 'udp','eth']
        self.ipProtos = ['icmp', 'icmp6', 'igmp', 'igrp', 'pim', 'ah', 'esp', 'vrrp', 'udp','tcp']
        self.etherProtos = ['ip', 'ip6', 'arp', 'rarp', 'atalk', 'aarp', 'decnet', 'sca', 'lat', 'mopdl', 'moprc', 'iso', 'stp', 'ipx', 'netbeui']
        self.isoProtos = ['clnp', 'esis','isis']
        self.types = ['host','net','port','portrange','len']
        self.conditionals = ['==','!=','>','<','>=','<=']
        self.conjuctions = ['and', 'or','&&', '||']
        self.dirs = ['src','dst']
        self.bpfFilter = bpfFilter+" "
        self.parseList = list()

    

# sfilter = Filter("eth")
# result = sfilter.setFilter()
# print(result)
# protos = sfilter.applyFilter( pdmlmanager("ProtocolFormatter/Scripts/cubic.pdml") )
# pdmlString = ""
# for proto in protos:
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
# print(pdmlString)