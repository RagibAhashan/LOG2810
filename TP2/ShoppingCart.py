from Object import Object

class ShoppingCart:
    def __init__(self):
        self.cart_items = []
        self.weight_of_items = 0

    def add_to_cart(self, item):
        self.cart_items.append(item)
        self.weight_of_items += item.get_weight()

    def remove_from_cart(self, item):
        if item in self.cart_items:
            self.weight_of_items -= item.get_weight()
            self.cart_items.remove(item)
        else:
            print("This item is not in your cart")

    def print_cart_items(self):
        for item in self.cart_items:
            item.printItem()
        print("Total items in the cart: " + str(len(self.cart_items)))

    def empty_cart(self):
        self.cart_items.clear()
        self.weight_of_items = 0
    
