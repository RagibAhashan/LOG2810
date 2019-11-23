class Object:
    def __init__(self, name, id_code, type_item):
        self.type = type_item
        self.id_code = id_code
        self.name = name
    
    def printItem(self):
        print(self.type + "   "+ self.id_code + "   " + self.name)
        #print("Name: " + self.name + "   " + self.id_code + "   " +  self.type )
