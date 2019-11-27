import os
import platform
from FiniteStateMachine import StateMachine



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
        if self.search_type == '':
            self.states_machine.search_hits_TYPE    = self.entrepot.get_items_dynamic()
        self.states_machine.search_hits_TYPE = self.entrepot.find_items_by_Type(answer)
        return answer
            
    

    def update_search_results(self, updated_IDCODE = False, updated_NAME = False):
        
        search_results = []
        recent_results = []

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
                correction_spaces = 17
                for space in range(os.get_terminal_size().lines - correction_spaces): 
                    print('')
            else:
                for item in self.search_results:
                    item.printItem()
            
                # Pas essentiel a l'implementation de notre automate. C'est pour formatter l'affichage.                                                                                      ##
                correction_spaces = 18
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
        print("            NAME : " + self.search_name  )
        
        print("Select a search filter")
        print("     Search by type [1]")
        print("     Search by ID   [2]")
        print("     Search by name [3]")
        print("     Reset filters  [4]")
        print("     Confirm Search [5]")
        print("     Exit Search    [6]")                                                                 
                                                                                                    
        



    def run_search_engine(self):
        
        # States
        TYPE   = 1
        IDCODE = 2
        NAME   = 3
        RESET_FILTERS = 4
        CONFIRM_SEARCH = 5
        EXIT_SEARCH = 6
        
        filter_selection = 1
        self.get_search_filter_selection('==== SEARCH MENU ====', '', True)
        print('')
        filter_selection = int(input("Select Search Parameter: "))

        first_searched_activation = False
        print_permission = False

        while True:
            if filter_selection == TYPE:
                

                self.get_search_filter_selection('==== ITEMS SUGGESTED ====', '', False, print_permission)
                self.search_type = self.sort_with_type()
                self.search_results = self.update_search_results()
                print_permission = True
                
                
            
            if filter_selection == IDCODE:
                if first_searched_activation == False:
                    first_searched_activation = True


                self.states_machine.settings_machine('IDCODE')
                self.get_search_filter_selection('==== ITEMS SUGGESTED ====', '', False, print_permission)
                self.states_machine.run()
                self.search_results = self.update_search_results()
                self.search_IDCODE  = self.states_machine.name_item_search
                print_permission = True

            if filter_selection == NAME:
                if first_searched_activation == False:
                    first_searched_activation = True


                self.states_machine.settings_machine('NAME')
                self.get_search_filter_selection('==== ITEMS SUGGESTED ====', '', False, print_permission)
                self.states_machine.run()
                self.search_results = self.update_search_results()
                self.search_name    = self.states_machine.name_item_search
                print_permission = True
            
            if filter_selection == RESET_FILTERS:
                self.reset_search()
                self.get_search_filter_selection('==== ITEMS IN STOCK ====')
                print_permission = False
            
            if filter_selection == CONFIRM_SEARCH:
                if len(self.search_results) == 1:
                    item = self.search_results[0]
                    self.reset_search()
                    return item
                else:
                    self.get_search_filter_selection('==== ITEMS SUGGESTED ====', 'CANNOT SELECT MORE THAN TWO ITEMS!')
            
            if filter_selection == EXIT_SEARCH:
                return False

            self.get_search_filter_selection('==== ITEMS SUGGESTED ====')
            
            filter_selection = int(input("\nSelect Search Parameter: "))
            
                


