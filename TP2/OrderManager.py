from Object import Object
from ShoppingCart import ShoppingCart

class OrderManager:
    def __init__(self, entrepot, search_engine, shopping_cart):
        self.entrepot      = entrepot
        self.search_engine  = search_engine
        self.shopping_cart  = shopping_cart

    def add_item(self, item):
        self.shopping_cart.add_to_cart(item)
        self.remove_item(item)

    def remove_item(self, item):
        self.shopping_cart.remove_item(item)
        
    def print_order(self):
        self.shopping_cart.print_cart_items()


    def get_cart_weight(self):
        return self.shopping_cart._weight_of_items()

    def verify_order(self):
        if(self.get_cart_weight <= 25) : 
            print("Thank you for your order!")
            return True
        else:
            print("Your cart is too heavy! Please restart.")
            return False

    def confirm_order(self):
        pass


    def run_order_manager(self):
        while True:
            ans = self.search_engine.run_search_engine()

            self.add_item(ans)

            if ans == False:
                print("Search was abandonned!")
            else:
                entrepot.remove_item(ans)