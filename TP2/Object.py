class Object:
    def __init__(self, name, id_code, type_item):
        self.type = type_item
        self.id_code = id_code
        self.name = name
        self.weight = self.set_weight()
    
    def printItem(self):
        print(self.type + "   " + self.id_code + "   " + self.name)
        

    def return_string_item(self):
        item_info = self.type + "   " + self.id_code + "   " + self.name
        return item_info
        
    def set_weight(self): 
        if self.type == 'A':
            self.weight = 1
        elif self.type == 'B':
            self.weight = 3
        elif self.type == 'C':
            self.weight = 6
        return self.weight

    def get_weight(self):
        return self.weight