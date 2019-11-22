class Entrepot:
    def __init__(self, items_list):
        self._items_list   = items_list          # Constant. DO NOT CHANGE IT. IT'S PRIVATE ATTIBUTE.
        self._dynamic_list = self.items_list
    
    def getItems(self):
        return self.items_list
    
    def checkItem(self, item):
        if item in self._dynamic_list:
            return True
        return False
        
    def find_item_by_name(self, name):
        for item in self._dynamic_list:
            if(item.name == name):
                return item
        return False

    def find_item_by_id(self, id_code):
        for item in self._dynamic_list:
            if(item.id_code == id_code):
                return item
        return False

    def find_items_by_Type(self, type_item):
        list_type = []
        for item in self._dynamic_list:
            if(item.type == type_item):
                list_type.append(item)
        return list_type


    def search_item_name(self, name):
        list_search_hits = []
        prelimenary_search = self.find_item_by_name(name)
        if prelimenary_search != False:
            return prelimenary_search
        
        for item in self._dynamic_list:
            if item.name == name:
                list_search_hits = [item]
                return list_search_hits
            elif name.find(item.name) == 0:
                list_search_hits.append(item.name)   

        return list_search_hits