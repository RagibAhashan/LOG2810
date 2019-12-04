from ShoppingCart import ShoppingCart
from SearchEngine import SearchEngine

#############################################################################################
#	Classe OrderManager: Cette classe défini les commandes
#############################################################################################
class OrderManager:
    def __init__(self, entrepot, shopping_cart, search_engine = ''):
        self.entrepot       = entrepot
        self.search_engine  = search_engine        # Agregation
        self.shopping_cart  = shopping_cart
        self._n_orders      = 0


    #############################################################################################
    #	methode remove_index_with_index: affiche les charactéristique d'un automate
    #	params [self, index(int)]
    #   return item_to_delete(automate)
    #############################################################################################
    def remove_item_with_index(self, index):
        item_to_delete = self.shopping_cart.cart_items[index]
        del self.shopping_cart.cart_items[index]
        return item_to_delete


    #############################################################################################
    #	methode print_order: affiche les charactéristique du panier
    #	params [self]
    #############################################################################################
    def print_order(self, commande_print = False):
        if commande_print == True:
            print("\n\n\n THANK YOU FOR YOUR ORDER!  \n ORDER RECEIPT:")
        else:
            print("\n\n\n Viewing cart : \n")
        self.shopping_cart.print_cart_items(commande_print)


    #############################################################################################
    #	methode verify_order: verifie si le poids est respecté
    #	params [self]
    #   return True or False
    #############################################################################################
    def verify_order(self):
        if(self.shopping_cart.weight_of_items <= 25 and self.shopping_cart.weight_of_items > 0) : 
            print("Thank you for your order!")
            return True
        else:
            print("Your cart is too heavy!\n  "+  str(self.shopping_cart.weight_of_items) +"kg is too much! PLEASE REMOVE ITEMS FROM CART.\n ORDER REJECTED!.")
            return False


    #############################################################################################
    #	methode put_back_Items_from_cart: remet l'item enlever du panier dans l'entrepot
    #	params [self, list_items]
    #############################################################################################
    def put_back_items_from_cart(self, list_items):
        for item in list_items:
            self.entrepot.append(item)


    #############################################################################################
    #	methode search_item_to_order: cherche l'item à placer dans le panier
    #	params [self]
    #############################################################################################
    def search_item_to_order(self):
        item_ordered = self.search_engine.execute_search()
        if item_ordered != False:
            self.shopping_cart.add_to_cart(item_ordered)

    #############################################################################################
    #	methode remove_item_from_cart: enleve l'item du panier
    #                                  rajoute l'item dans l'entrepot
    #	params [self]
    #############################################################################################
    def remove_item_from_cart(self):
        removed_items_list = self.shopping_cart.remove_an_item()
        print('\n\n\n ITEM REMOVED: \n')
        self.put_back_items_from_cart(removed_items_list)


    #############################################################################################
    #	methode clear_cart_items: réinitialise le panier et ses composantes
    #                             rajoute les items dans l'entrepot
    #	params [self]
    #############################################################################################
    def clear_cart_items(self):
        removed_items = self.shopping_cart.empty_cart()
        self.put_back_items_from_cart(removed_items)


    #############################################################################################
    #	methode execute_order: cette methode forme l'interface de gestion
    #                          de commandes. L'utilisateur peut chercher
    #                          un item, voir le panier, enlever des items du
    #                          panier, ou de confimer sa transaction.
    #	params [self]
    #############################################################################################
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









            