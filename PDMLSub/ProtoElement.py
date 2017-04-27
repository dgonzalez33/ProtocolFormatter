
class protoelement:
    
#     proto_attributes = {}
    index = 0
    proto_attributes_names = []
    proto_attributes_values = []
    field_elements = []
    
    
    
    def __init__(self):
        self.create_self()
        self.field_elements = []
        self.proto_attributes = {}
     
    def create_self(self):
        #print("protoelement class")
        return 0
        
    def set_proto_attrib(self, key, value):
        self.proto_attributes_names.append(key)
        self.proto_attributes_values.append(value)
        self.index+=1
        return 0

            
    def set_field_element(self, field2):
        self.field_elements.append(field2)
    
    def get_proto_attrib(self):
        return self.proto_attributes
    
    def get_proto_attrib_value(self, i):
        return self.proto_attributes_values[i]
    
    def get_proto_attrib_name(self, i):
        return self.proto_attributes_names[i]
    
    def get_all_proto_attrib_names(self):
        return self.proto_attributes_names
    
    def get_all_proto_attrib_vales(self):
        return self.proto_attributes_values
    
    def get_field_element(self):
        return self.field_elements
    
    def get_field_element_at_index(self, index):
        return self.field_elements[index]


if(__name__ == "__main__"):
    y = protoelement()
    
