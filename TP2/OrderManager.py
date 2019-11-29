from Object import Object
from ShoppingCart import ShoppingCart
import time

class OrderManager:
    def __init__(self, entrepot, search_engine, shopping_cart):
        self.entrepot      = entrepot
        self.search_engine  = search_engine
        self.shopping_cart  = shopping_cart
        self._n_orders = 0

    def add_item(self, item):
        self.shopping_cart.add_to_cart(item)

    def remove_item(self, item):
        self.shopping_cart.remove_from_cart(item)

    def remove_item_with_index(self, index):
        item_to_delete = self.shopping_cart.cart_items[index]
        del self.shopping_cart.cart_items[index]
        return item_to_delete
        
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

    def remove_from_order(self):
        remove = '1'
        while remove == '1' :
            print("\n" + "Which item would you like to remove? ")
            self.print_order()
            if(len(self.shopping_cart.cart_items) == 0):
                print("\n"+"THERE ARE NO ITEMS TO REMOVE!")
                time.sleep(2.5)
                break
            index = int(input("Type the number corresponding to the item you would like to remove : ")) + - 1
            if isinstance(index, int) and index >= 0 and index < len(self.shopping_cart.cart_items):
                item_to_add = self.remove_item_with_index(index)
                self.entrepot.add_item(item_to_add)
                print("Item sucessfully removed from cart!")
            else:
                print("Not a valid number... Try again")
                self.remove_from_order()   
            remove = input("Would you like to remove another item? Type '1' for YES or '2' for NO: ") 

    #### ADD DETAILS
    def confirm_order(self):
        checkout = input("Would you like to order these items? Type '1' for YES or '2' for NO : ")
        if checkout == '1':
            print('\n'+ '\n' + '\n' +'\n')
            print("Thank you for your order(s)!")
            print("Here's a summary of your orders: ")
            self.print_order()
            print('\n'+ '\n' + '\n' +'\n')
            exit()
        elif checkout == '2':
            print("Alright! You may add other items to your order : ")
            time.sleep(2.5)
            return True

        else:
            print("Not a valid answer...")
            self.confirm_order()

    def clear_cart(self):
        self.shopping_cart.empty_cart()

    def order_items(self):
        pass

    def run_order_manager(self):
        while True:
            ans = self.search_engine.run_search_engine()

            # If user wants to exit search
            if ans == "EXIT_SEARCH":
                print("Search was abandonned!")
                exit()
    
            # If user wants to view shopping cart
            elif ans == "VIEW_CART": 
                print("\n" + "\n" + "\n") 
                print("VIEWING SHOPPING CART")
                self.print_order()
                self.confirm_order()
            
            # If user wants to clear cart
            elif ans == "CLEAR_CART":
                self.clear_cart()

            # If user wants to remove item(s)
            elif ans == False:
                self.remove_from_order()

            
            # If user wants to add item(s)
            else:
                self.add_item(ans)
                self.entrepot.remove_item(ans)