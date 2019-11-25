import os
import platform
from FiniteStateMachine import StateMachine

acceptable_chars = [ chr(i+97) for i in range(26)]
for i in range(10):
    acceptable_chars.append(str(i))


class SearchEngine:
    def __init__(self, entrepot_data):
        self.states_machine = StateMachine([0,1,2,3,4] , 0, [3,4], entrepot_data)   # Composition.
        self.entrepot       = entrepot_data                                         # Agregation.
        
        self.search_results = entrepot_data.get_items_dynamic().copy()
        self.search_type    = ''
        self.search_IDCODE  = ''
        self.search_name    = ''
        
        
    def sort_with_type(self):
        answer = str(input("Select a type: "))
        if answer == 'A' or answer == 'B' or answer == 'C':
            self.states_machine.search_hits = self.entrepot.find_items_by_Type(answer)
            return answer
        else:
            self.sort_with_type()
    

    def update_search_results(self):
        updated_list = []

        for item in self.search_results:
            for i in range(len(self.states_machine.search_hits)):
                if item.id_code == self.states_machine.search_hits[i].id_code:
                    print("item.id_code: " + item.id_code + "    "+ self.states_machine.search_hits[i].id_code)
                    updated_list.append(item)
        
        print("====LIST====\n")
        for item in updated_list:
            item.printItem()
        print("====LIST====\n")
        return updated_list



    def reset_search(self):
        self.states_machine.search_hits      = self.entrepot.get_items_dynamic().copy()
        self.states_machine.name_item_search = ''
        self.search_type    = ''
        self.search_IDCODE  = ''
        self.search_name    = ''
        self.search_results = self.entrepot.get_items_dynamic().copy()

    

    def get_search_filter_selection(self, header_msg = '==== ITEMS SUGGESTED ====', sub_head_msg = ''):
        # if suggested == True:
        #     print("==== ITEMS SUGGESTED ====\n")
        # else:
        #     print("==== ITEMS IN STOCK ====\n")
        

        print(header_msg)
        print(sub_head_msg)



        for item in self.search_results:
            item.printItem()
        
        # Pas essentiel a l'implementation de notre automate. C'est pour formatter l'affichage.                                                                                      ##
        correction_spaces = 16
        for space in range(os.get_terminal_size().lines - len(self.search_results) - correction_spaces): 
            print('')

        print("Searching: ")
        print("            TYPE : " + self.search_type  )
        print("          IDCODE : " + self.search_IDCODE)
        print("            NAME : " + self.search_name  )
        print("\nSelect a search filter")
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
        self.get_search_filter_selection('==== ITEMS IN STOCK ====')
        print('')
        filter_selection = int(input("Select Search Parameter: "))

        while True:
            if filter_selection == TYPE:
                self.get_search_filter_selection('==== ITEMS SUGGESTED ====')
                self.search_type = self.sort_with_type()
                self.search_results = self.update_search_results()
                
                
            
            if filter_selection == IDCODE:
                self.states_machine.settings_machine('IDCODE')
                self.get_search_filter_selection('==== ITEMS SUGGESTED ====')
                self.states_machine.run()
                self.search_results = self.update_search_results()
                self.search_IDCODE  = self.states_machine.name_item_search

            if filter_selection == NAME:
                self.states_machine.settings_machine('NAME')
                self.get_search_filter_selection('==== ITEMS SUGGESTED ====')
                self.states_machine.run()
                self.search_results = self.update_search_results()
                self.search_name    = self.states_machine.name_item_search
            
            if filter_selection == RESET_FILTERS:
                self.reset_search()
                self.get_search_filter_selection('==== ITEMS IN STOCK ====')
            
            if filter_selection == CONFIRM_SEARCH:
                if len(self.search_results) == 1:
                    return self.search_results[0]
                else:
                    self.get_search_filter_selection('==== ITEMS SUGGESTED ====', 'CANNOT SELECT MORE THAN TWO ITEMS!')
            
            if filter_selection == EXIT_SEARCH:
                pass

            self.get_search_filter_selection('==== ITEMS SUGGESTED ====')
            
            filter_selection = int(input("\nSelect Search Parameter: "))
            
                


