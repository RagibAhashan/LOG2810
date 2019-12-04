from Automate import Automate

class ShoppingCart:
    def __init__(self):
        self.cart_items = []
        self.weight_of_items = 0

    def add_to_cart(self, item):
        self.cart_items.append(item)
        self.weight_of_items += item.weight

    def remove_from_cart(self, item):
        if item in self.cart_items:
            self.weight_of_items -= item.weight
            self.cart_items.remove(item)
        else:
            print("This item is not in your cart")


    def remove_an_item(self):
        
        acceptable_inputs = [str(i) for i in range(len(self.cart_items) + 1)]
        list_remove_items = []
        ans = ''

        if len(self.cart_items) == 0:
            print('The shopping cart is empty!')
            return list_remove_items
        
        while True:
            acceptable_inputs = [str(i) for i in range(len(self.cart_items) + 1)]

            self.print_cart_items()
            index = str(input("Which Item Would you like to remove? [SELECT ITEM #] "))
            
            if index in acceptable_inputs:
                remove_item = self.cart_items.pop(int(index)-1)
                self.weight_of_items -= remove_item.weight
                list_remove_items.append(remove_item)
                
                ans = str(input("Would you like to remove another item? Enter [N] for NO or [Y] for YES: "))
            

            else:
                print(index, 'item does not exist in your shopping cart!')

            if ans == 'n' or ans == 'N' or len(self.cart_items) == 0:
                break
            
        return list_remove_items



    def print_cart_items(self):
        index = 1
        for item in self.cart_items:
            print("[#" + str(index) + "]      " + item.info())
            index += 1
        print("\n" + "Total items in the cart: " + str(len(self.cart_items)))
        print("And the total weight is:" , self.weight_of_items, 'kg. ')

    def empty_cart(self):
        remove_items         = self.cart_items
        self.cart_items      = []
        self.weight_of_items = 0
        return remove_items
    
