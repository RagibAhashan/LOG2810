import os
import platform
from FiniteStateMachine import StateMachine
from random import randrange


class SearchEngine:
    def __init__(self, automates_liste = []):

        self.search_results       = 0
        self.number_results_found = 0

        self.search_type          = ''
        self.search_IDCODE        = ''
        self.search_name          = ''

        self.liste_automates      = automates_liste
        self.list_hits            = []

        self.search_hits_name     = automates_liste
        self.search_hits_TYPE     = automates_liste
        self.search_hits_IDCODE   = automates_liste


    def search_item_by_type(self, langage):
        list_hits = []
        for item in self.liste_automates:
            if item.verify_langage(langage, 'TYPE') == True:
                list_hits.append(item)
        self.search_hits_TYPE = list_hits


    def search_item_by_IDCODE(self, langage):
        list_hits = []
        for item in self.liste_automates:
            if item.verify_langage(langage, 'IDCODE') == True:
                list_hits.append(item)
        self.search_hits_IDCODE = list_hits


    def search_item_by_name(self, langage):
        list_hits = []
        for item in self.liste_automates:
            if item.verify_langage(langage, 'NAME') == True:
                list_hits.append(item)
        self.search_hits_name = list_hits


    def update_search_results(self):
        search_results = []
        recent_results = []

        for recent_hit in self.search_hits_TYPE:
            for hit_IDCODE in self.search_hits_IDCODE:
                if recent_hit.ID_CODE == hit_IDCODE.ID_CODE:
                    recent_results.append(recent_hit)

            

        for recent_hit in recent_results:
            for hit_NAME in self.search_hits_name:
                if recent_hit.ID_CODE == hit_NAME.ID_CODE:
                    search_results.append(recent_hit)
            
        self.number_results_found = len(search_results)
        self.list_hits            = search_results
        
        return search_results



    def reset_search(self):
        pass

    

    def get_search_filter_selection(self, header_msg = '==== ITEMS SUGGESTED ====', sub_head_msg = '', main_menu = False, print_permission = True):
        
        print(header_msg)
        print(sub_head_msg)

        if len(self.list_hits) <= 10:
            for item in self.list_hits:
                item.printAutomate()
        else:
            for item in self.list_hits[0:10]:
                item.printAutomate()
        

        

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
        

        acceptable_inputs = ['1','2','3','4','5','6','7','8','9', '0']

        while True:
            if filter_selection == TYPE:
                self.get_search_filter_selection('==== ITEMS SUGGESTED ====', '', False, False)
                langage = str(input("Search by type: "))
                self.search_item_by_type(langage)

                
                
                
                
            
            if (filter_selection) == IDCODE:
                langage = str(input("Search by type: "))
                self.search_item_by_IDCODE(langage)
                
                
                


            if (filter_selection) == NAME:
                langage = str(input("Search by type: "))
                self.search_item_by_name(langage)
                self.get_search_filter_selection('==== ITEMS SUGGESTED ====', '', False, False)
                

            self.get_search_filter_selection('==== ITEMS SUGGESTED ====')


            
            filter_selection = str(input("\nSelect option: "))
            

            
            
