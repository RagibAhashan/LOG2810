class Object:
    def __init__(self, name, id_code, type_item):
        self.type = type_item
        self.id_code = id_code
        self.name = name
    
    def printItem(self):
        print("Object type: " + self.type + ". Object id code: "+ self.id_code + " Object name: " + self.name)
