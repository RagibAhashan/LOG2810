class Object:
    def __init__(self, type_item, id_code, name):
        self.type = type_item
        self.id_code = id_code
        self.name = name
    
    def printItem(self):
        print("Object type: " + self.type + ". Object id code: "+ self.id_code + " Object name: " + self.name)
