class Object:
    def __init__(self, name, id_code, type_item, weight = 0):
        self.type = type_item
        self.id_code = id_code
        self.name = name
        self.weight = weight
    
    def printItem(self):
        print(self.type + "   " + self.id_code + "   " + self.name)
        
    def get_weight(self): 
        if self.type == 'A':
            self.weight = 1
        elif self.type == 'B':
            self.weight = 3
        elif self.type == 'C':
            self.weight = 6
        return self.weight