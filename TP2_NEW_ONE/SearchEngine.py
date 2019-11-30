import os
import platform
from FiniteStateMachine import StateMachine
from random import randrange


class SearchEngine:
    def __init__(self, entrepot_data):
        self.states_machine = StateMachine([0,1,2,3,4] , 0, [3,4], entrepot_data)   # Composition.
        self.entrepot       = entrepot_data                                         # Agregation.

        self.search_results = entrepot_data.get_items_dynamic()
        self.number_results_found = 0
        self.search_type    = ''
        self.search_IDCODE  = ''
        self.search_name    = ''
        
        
        
    def sort_with_type(self):
        
        answer = str(input("\nSelect a type: "))
        if answer == '':
            self.states_machine.search_hits_TYPE    = self.entrepot.get_items_dynamic()
            return answer
        print('\n     SUCCESS!\n     Loading Results...   \n')
        self.states_machine.search_hits_TYPE = self.entrepot.find_items_by_Type(answer)
        return answer
            
    

    def update_search_results(self):
        
        search_results = []
        recent_results = []

        if  self.search_type == '' and self.search_IDCODE == '' and self.search_name == '':
            self.number_results_found = 0
            return search_results

        for recent_hit in self.states_machine.search_hits_TYPE:
            for hit_IDCODE in self.states_machine.search_hits_IDCODE:
                if recent_hit.id_code == hit_IDCODE.id_code:
                    recent_results.append(recent_hit)

            

        for recent_hit in recent_results:
            for hit_NAME in self.states_machine.search_hits:
                if recent_hit.id_code == hit_NAME.id_code:
                    search_results.append(recent_hit)
            
        self.number_results_found = len(search_results)
        return search_results



    def reset_search(self):
        self.states_machine.search_hits         = self.entrepot.get_items_dynamic()
        self.states_machine.search_hits_IDCODE  = self.entrepot.get_items_dynamic()
        self.states_machine.search_hits_TYPE    = self.entrepot.get_items_dynamic()

        self.states_machine.name_item_search = ''
        self.search_type    = ''
        self.search_IDCODE  = ''
        self.search_name    = ''
        self.search_results = self.entrepot.get_items_dynamic()
        self.number_results_found = 0

    

    def get_search_filter_selection(self, header_msg = '==== ITEMS SUGGESTED ====', sub_head_msg = '', main_menu = False, print_permission = True):
        
        print(header_msg)
        print(sub_head_msg)

        if print_permission ==  True:
            if main_menu == True:
                # Pas essentiel a l'implementation de notre automate. C'est pour formatter l'affichage.                                                                                      ##
                correction_spaces = 27
                for space in range(os.get_terminal_size().lines - correction_spaces): 
                    print('')
            else:
                for item in self.search_results:
                    item.printItem()
                    
            
                # Pas essentiel a l'implementation de notre automate. C'est pour formatter l'affichage.                                                                                      ##
                correction_spaces = 28
                for space in range(os.get_terminal_size().lines - len(self.search_results) - correction_spaces): 
                    print('')

            if main_menu == False:
                print("\n" + str(self.number_results_found) + " Suggestion(s) found based on your Recent Search...\n")
            else:
                print('\n')
        else:
            correction_spaces = 15
            for space in range(os.get_terminal_size().lines  - correction_spaces): 
                    print('')

        
        if self.search_type == '':
            self.states_machine.search_hits_TYPE    = self.entrepot.get_items_dynamic()
        if self.search_IDCODE == '':
            self.states_machine.search_hits_IDCODE  = self.entrepot.get_items_dynamic()
        if self.search_name == '':
            self.states_machine.search_hits         = self.entrepot.get_items_dynamic()



        
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

        print("--- Manage Order ---")
        print("     Add item to cart          [5]")
        print("     Remove item(s) from cart  [6]")
        print("     Clear cart                [7]")
        print("     View cart                 [8]" + "\n")

        print("--- Finalize Order ---")
        print("     Confirm order             [9]")     
        print("     Exit                      [0]")                                                                 
                                                                                                    
        



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
                self.search_type = self.sort_with_type()
                self.search_results = self.update_search_results()
                print_permission = True
                
                
            
            if (filter_selection) == IDCODE:
                self.states_machine.settings_machine('IDCODE')
                self.get_search_filter_selection('==== ITEMS SUGGESTED ====', '', False, print_permission)
                self.states_machine.run()
                self.search_IDCODE  = self.states_machine.name_item_search
                self.search_results = self.update_search_results()
                
                print_permission = True


            if (filter_selection) == NAME:
                self.states_machine.settings_machine('NAME')
                self.get_search_filter_selection('==== ITEMS SUGGESTED ====', '', False, print_permission)
                self.states_machine.run()
                self.search_name    = self.states_machine.name_item_search
                self.search_results = self.update_search_results()
                print_permission = True


            
            if (filter_selection) == RESET_FILTERS:
                self.reset_search()
                print_permission = False
                self.get_search_filter_selection('==== ITEMS IN STOCK ====', '', print_permission)
                return self.run_search_engine()

            
            if (filter_selection) == ADD_ITEM:
                should_add = True
                if len(self.search_results) == 1:
                    print_permission = False
                    item = self.search_results[0]
                    self.reset_search()
                    return item
                else:
                    self.get_search_filter_selection('==== ITEMS SUGGESTED ====', 'CANNOT SELECT MORE THAN TWO ITEMS!')
            
            if (filter_selection) == VIEW_CART:
                return "VIEW_CART"
            
            if (filter_selection) == REMOVE_ITEM:
                return False

            if (filter_selection) == CLEAR_CART:
                return "CLEAR_CART"

            if (filter_selection) == EXIT_SEARCH:
                return "EXIT_SEARCH"

            self.get_search_filter_selection('==== ITEMS SUGGESTED ====')


            
            filter_selection = str(input("\nSelect option: "))
            if  self.search_type == '' and self.search_IDCODE == '' and self.search_name == '':
                print_permission = False

            if filter_selection == '':
                break
            

            

            
                


