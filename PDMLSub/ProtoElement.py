
class protoelement:
    
    proto_attributes = {}
    field_elements = []
    
    
    
    def __init__(self):
        self.create_self()
        self.field_elements = []
        self.proto_attributes = {}
     
    def create_self(self):
        #print("protoelement class")
        return 0
        
    def set_proto_attrib(self, key, val):
        self.proto_attributes[key] = val
            
    def set_field_element(self, field2):
        self.field_elements.append(field2)
    
    def get_proto_attrib(self):
        return self.proto_attributes
    
    def get_field_element(self):
        return self.field_elements
    
    def get_field_element_at_index(self, index):
        return self.field_elements[index]


if(__name__ == "__main__"):
    y = protoelement()
    
