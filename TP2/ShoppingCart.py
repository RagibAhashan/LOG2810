class ShoppingCart:
    def __init__(self, items):
        self.cart_items = items     #cart_items: list[]
    

    def add_to_cart(self, item):
        self.cart_items.append(item)

    def remove_from_cart(self, item):
        if item in self.cart_items:
            self.cart_items.remove(item)
        else:
            print("This item is not in your cart")

    def print_cart_items(self):
        for item in self.cart_items:
            item.printItem()
        print("Total items in the cart: " + len(self.cart_items))

    def empty_cart(self):
        self.cart_items.clear()
    