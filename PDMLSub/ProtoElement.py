
class protoelement:
    
    proto_attributes = {}
    field_elements = []
    
    def __init__(self):
        self.create_self()
     
    def create_self(self):
        print("protoelement class")
        
    def set_proto_attrib(self, key, val):
        self.proto_attributes[key] = val
            
    def set_field_element(self, index, field):
        self.field_elements[index] = field
    
    def get_proto_attrib(self):
        return self.proto_attributes
    
    def get_field_element(self):
        return self.field_elements


if(__name__ == "__main__"):
    d = protoelement()
    
