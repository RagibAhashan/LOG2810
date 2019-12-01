import os
import platform
from FiniteStateMachine import StateMachine
from random import randrange


class SearchEngine:
    def __init__(self, automates_liste = []):

        self.search_results  = 0
        self.number_results_found = 0
        self.search_type     = ''
        self.search_IDCODE   = ''
        self.search_name     = ''
        self.liste_automates = automates_liste
        self.list_hits       = []

    def search_item_by_type(self, langage):
        list_hits = []
        for item in self.liste_automates:
            if item.verify_langage(langage, 'TYPE') == True:
                list_hits.append(item)
        return list_hits


    def search_item_by_IDCODE(self, langage):
        list_hits = []
        for item in self.liste_automates:
            if item.verify_langage(langage, 'IDCODE') == True:
                list_hits.append(item)
        return list_hits


    def search_item_by_name(self, langage):
        list_hits = []
        for item in self.liste_automates:
            if item.verify_langage(langage, 'NAME') == True:
                list_hits.append(item)
        return list_hits


    def update_search_results(self):
        pass



    def reset_search(self):
        pass

    

    def get_search_filter_selection(self, header_msg = '==== ITEMS SUGGESTED ====', sub_head_msg = '', main_menu = False, print_permission = True):
        
        print(header_msg)
        print(sub_head_msg)

        
        # Pas essentiel a l'implementation de notre automate. C'est pour formatter l'affichage.                                                                                      ##
        correction_spaces = 27
        for space in range(os.get_terminal_size().lines - correction_spaces): 
            print('')
            

        
        



        
        print("Searching: ")
        print("            TYPE : " + self.search_type  )
        print("          IDCODE : " + self.search_IDCODE)
        print("            NAME : " + self.search_name + "\n")
        
        print("Options: ")
        print("--- Filter Search ---")
        print("     Search by type            [1]")
        print("     Search by ID              [2]")
        print("     Search by name            [3]")
        print("     Reset filters             [4]" + "\n")


        # Does not go in search engine!
        # print("--- Manage Order ---")
        # print("     Add item to cart          [5]")
        # print("     Remove item(s) from cart  [6]")
        # print("     Clear cart                [7]")
        # print("     View cart                 [8]" + "\n")

        # print("--- Finalize Order ---")
        # print("     Confirm order             [9]")     
        # print("     Exit                      [0]")                                                                 
                                                                                                    
        



    def run_search_engine(self):
        
        # States
        TYPE   = '1'
        IDCODE = '2'
        NAME   = '3'
        RESET_FILTERS = '4'
        ADD_ITEM = '5'
        REMOVE_ITEM = '6'
        CLEAR_CART = '7'
        VIEW_CART = '8'
        CONFIRM_ORDER = '9'
        EXIT_SEARCH = '0'
        
        filter_selection = '1'
        print('\n' + '\n' + "\n")
        self.get_search_filter_selection('==== SEARCH MENU ====', '', True)
        
        filter_selection = input("\nSelect option: ")

        first_searched_activation = False
        print_permission = False

        acceptable_inputs = ['1','2','3','4','5','6','7','8','9', '0']

        while True:
            if filter_selection == TYPE:
                self.get_search_filter_selection('==== ITEMS SUGGESTED ====', '', False, print_permission)

                
                print_permission = True
                
                
            
            if (filter_selection) == IDCODE:
                
                
                print_permission = True


            if (filter_selection) == NAME:
                
                self.get_search_filter_selection('==== ITEMS SUGGESTED ====', '', False, print_permission)
                
                print_permission = True


            
            if (filter_selection) == RESET_FILTERS:

                print_permission = False
                self.get_search_filter_selection('==== ITEMS IN STOCK ====', '', print_permission)
                return self.run_search_engine()

            
            if (filter_selection) == ADD_ITEM:
                pass

            if (filter_selection) == EXIT_SEARCH:
                return "EXIT_SEARCH"

            self.get_search_filter_selection('==== ITEMS SUGGESTED ====')


            
            filter_selection = str(input("\nSelect option: "))
            if  self.search_type == '' and self.search_IDCODE == '' and self.search_name == '':
                print_permission = False

            if filter_selection == '':
                break
            
