import re
class Filter:

    def setFilter(self):
        expressions = re.split(' ',self.bpfFilter)
        parseList = {}
        parseList['proto'] = list()
        parseList['type'] = list()
        parseList['dir'] = list()
        lastConditional = "=="
        last = ""
        lastType = ""
        lastConj = ""
        for exp in expressions:
            if(exp.lower() in self.conjuctions):
                lastConj = exp
            elif(exp.lower() in self.types):
                lastType = exp
            elif(exp.lower() in self.conditionals):
                lastConditional = exp
            elif(exp in self.protocols):
                primitive = lastConj + " "+ exp
                primitive = primitive.lstrip(' ')
                parseList['proto'].append(primitive)
                lastConj = ""
            elif(exp.lower() in self.dirs):
                primitive = lastConj + " "+ exp
                primitive = primitive.lstrip(' ')
                parseList['dir'].append(primitive)
                lastConj = ""
            elif(last.lower() == "proto"):
                parseList['proto'].append(exp)
            elif(lastType in self.types):
                primitive = lastConj + " " +lastType
                primitive = primitive.lstrip(' ')
                primitive += " " + lastConditional
                primitive = primitive.lstrip(' ')
                primitive += " " + exp
                parseList['type'].append(primitive)
                lastConditional = ""
                lastConj = ""
                lastType = ""
            # if(exp.lower() == 'not'):

            # if(exp.lower() == 'and'):

            # if(exp.lower() == 'or'):
            last = exp
        return parseList    
    def applyFilter(self, pdml):
        packets = pdml.get_all_packets()
        protos = packet.get_proto_element()
        fields = get_field_element()
        # for field in fields:


    def __init__(self, bpfFilter):
        self.protocols = ['ether', 'fddi','tr','wlan','ip','ip6','arp','rarp',
        'decnet', 'tcp', 'udp']
        self.types = ['host','net','port','portrange']
        self.conditionals = ['==','!=','>','<','>=','<=']
        self.conjuctions = ['and', 'or','&&', '||']
        self.dirs = ['src','dst']
        self.bpfFilter = bpfFilter
        self.applicableProtos = list()
    

sfilter = Filter("ip host 200 and net 101 and src or dst")
result = sfilter.setFilter()
print(result)




