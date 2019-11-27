from Object import Object
from ShoppingCart import ShoppingCart

class OrderManager:
    def __init__(self, all_items, search_engine, shopping_cart):
        self.all_items      = all_items
        self.search_engine  = search_engine
        self.shopping_cart  = shopping_cart

    def add_item(self, item):
        self.shopping_cart.add_to_cart(item)

    def remove_item(self, item):
        self.shopping_cart.remove_item(item)
        
    def get_items_in_cart(self):
        pass

    def verify_order(self):
        pass