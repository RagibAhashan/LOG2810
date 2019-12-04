from Object import Object
from ShoppingCart import ShoppingCart
from SearchEngine import SearchEngine

class OrderManager:
    def __init__(self, entrepot, shopping_cart, search_engine = ''):
        self.entrepot       = entrepot
        self.search_engine  = search_engine        # Agregation
        self.shopping_cart  = shopping_cart
        self._n_orders      = 0

    def remove_item_with_index(self, index):
        item_to_delete = self.shopping_cart.cart_items[index]
        del self.shopping_cart.cart_items[index]
        return item_to_delete
        
    def print_order(self):
        print("\n\n\n Viewing cart : \n")
        self.shopping_cart.print_cart_items()

    def get_cart_weight(self):
        return self.shopping_cart.weight_of_items

    def verify_order(self):
        if(self.shopping_cart.weight_of_items <= 25) : 
            print("Thank you for your order!")
            return True
        else:
            print("Your cart is too heavy!"+  str(self.shopping_cart.weight_of_items) +" is too much! Order rejected.")
            return False

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
            return True

        else:
            print("Not a valid answer...")
            self.confirm_order()

    def clear_cart(self):
        self.shopping_cart.empty_cart()

    def order_items(self):
        pass
    
    def put_back_items_from_cart(self, list_items):
        for item in list_items:
            self.entrepot.append(item)
            #self.search_engine.liste_automates.append(item)



    def excute_order(self):

        ORDER_ITEM            = '1'
        VIEW_CART             = '2'
        REMOVE_ITEM_FROM_CART = '3'
        CLEAR_CART            = '4'
        CONFIRM_ORDER         = '5'

        current_state         = '0'

        while True:
            print("Options : ")
            print("     Order item                     [1]")
            print("     View cart                      [2]")
            print("     Remove item(s) from cart       [3]")
            print("     Clear cart                     [4]\n")
            print("     Confirm order                  [5]")

            current_state = str(input("\n   Select option : "))

            if current_state == ORDER_ITEM:
                item_ordered = self.search_engine.execute_search()
                if item_ordered != False:
                    self.shopping_cart.add_to_cart(item_ordered)


            if current_state == VIEW_CART:
                self.print_order()
                
            if current_state == REMOVE_ITEM_FROM_CART:
                removed_items_list = self.shopping_cart.remove_an_item()
                print('\n\n\n ITEM REMOVED: \n')
                self.put_back_items_from_cart(removed_items_list)
                
                for item in removed_items_list:
                    item.printAutomate()


            if current_state == CLEAR_CART:
                removed_items = self.shopping_cart.empty_cart()
                self.put_back_items_from_cart(removed_items)

            if current_state == CONFIRM_ORDER:
                if self.verify_order() == True:
                    break









            