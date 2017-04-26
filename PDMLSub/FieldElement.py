
class fieldelement:
    
    field_attributes = {}
    
    def __init__(self):
        self.create_self()
        self.field_attributes = {}
     
    def create_self(self):
        #print("fieldelement class")
        return 0
        
        
    
    def set_field_attrib(self, key, val):
        self.field_attributes[key] = val
        
    def get_field_attributes(self):
        return self.field_attributes
    
    def get_field_attributes_value(self, key):
        return self.field_attributes[key]


if(__name__ == "__main__"):
    r = fieldelement()
    
