
class fieldelement:
    
    #field_attributes = {}
    index = 0
    field_attributes_names = []
    field_attributes_values = []
    
    def __init__(self):
        self.create_self()
        self.field_attributes = {}
     
    def create_self(self):
        #print("fieldelement class")
        return 0
        
        
    
    def set_field_attrib(self, key, val):
        print(key, " and ", val)
        self.field_attributes_names.append(key)
        self.field_attributes_values.append(val)
        self.index=+1
        

    
    def get_field_attributes_value(self, i):
        return self.field_attributes_values[i] 
    
    def get_field_attributes_name(self, i):
        return self.field_attributes_names[i] 
    
    def get_all_field_attributes_value(self):
        return self.field_attributes_values 
    
    def get_all_field_attributes_name(self):
        return self.field_attributes_names 
    
    def get_field_attributes_length(self):
        return len(self.field_attributes_values)


if(__name__ == "__main__"):
    r = fieldelement()
    
