from Object import Object
from ShoppingCart import ShoppingCart
import time

class OrderManager:
    def __init__(self, entrepot, search_engine, shopping_cart):
        self.entrepot      = entrepot
        self.search_engine  = search_engine
        self.shopping_cart  = shopping_cart

    def add_item(self, item):
        self.shopping_cart.add_to_cart(item)

    def remove_item(self, item):
        self.shopping_cart.remove_from_cart(item)
        
    def print_orders(self):
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

    #### ADD DETAILS
    def confirm_order(self):
        checkout = input("Would you like to checkout? Type '1' for YES and '2' for NO : ")
        if checkout == '1':
           # print('\n'+ '\n' + '\n' +'\n')
            print("Thank you for your order(s)!")
            print("Here's a summary of your orders: ")
            self.print_orders()
            exit()
        elif checkout == '2':
            print("Alright thank you! You may make another order: ")
            time.sleep(2.5)
            return True

        else:
            print("Not a valid answer...")
            self.confirm_order()

    def hide_order(self):
        pass

    def run_order_manager(self):
        while True:
            ans = self.search_engine.run_search_engine()
            # If user wants to exit search
            if ans == False:
                print("Search was abandonned!")
                exit()
    
            # If user wants to view shopping cart
            elif ans == True:  
                print("VIEWING SHOPPING CART")
                self.print_orders()
                self.confirm_order()
            
            # If user wants to place orders
            else:
                self.add_item(ans)
                self.entrepot.remove_item(ans)