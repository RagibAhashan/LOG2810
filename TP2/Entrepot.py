class Entrepot:
    def __init__(self, items_list):
        self._items_list   = items_list          # Constant. DO NOT CHANGE IT. IT'S PRIVATE ATTIBUTE.
        self._dynamic_list = items_list[:]
        
    
    def getItems(self):
        return self._items_list

    def get_items_dynamic(self):
        return self._dynamic_list
    
    def checkItem(self, search_item):
        for item in self._dynamic_list:
            if item.id_code == search_item.id_code:
                return True
        return False

    def check_if_item_exist(self, name = False, id_code = False, type_item = False):
        if id_code != False:
            code = self.find_item_by_id(id_code)
            if code == False:
                return False
            else:
                return True

        if name != False:
            for item in self._dynamic_list:
                if item.name ==  name:
                    return True
        
        pass
        
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


    def search_item_by_name(self, name):
        list_search_hits = []
        for item in self._dynamic_list:
            if item.name.find(name) == 0:
                list_search_hits.append(item.name)   
        return list_search_hits
    
    def get_suggested_items(self, list_hits_names):
        updated_list = []
        for i in range(len(self._items_list)):
            if self._items_list[i].name in list_hits_names:
                updated_list.append(self._items_list[i])



        return updated_list
        
