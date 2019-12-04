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

        self.first_run = False

        
        


    def search_item_by_type(self, langage):
        list_hits = []
        for item in self.liste_automates:
            if item.verify_langage(langage, 'TYPE') == True:
                list_hits.append(item)
        
        if len(list_hits) == 0:
            self.search_hits_TYPE = []
        else:
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

        # if self.first_run == False:
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
        self.first_run = True
        
        
        # elif self.search_hits_IDCODE == '' and self.search_hits_name != '':
        #     for recent_hit in self.search_hits_TYPE:
        #         for hit_name in self.search_hits_name:
        #             if recent_hit.ID_CODE == hit_name.ID_CODE:
        #                 recent_results.append(recent_hit)
        #     self.number_results_found = len(search_results)
        #     self.list_hits            = search_results


        return search_results



    def reset_search(self):
        self.search_results       = 0
        self.number_results_found = 0
        self.search_type          = ''
        self.search_IDCODE        = ''
        self.search_name          = ''
        self.list_hits            = []
        self.search_hits_name     = self.liste_automates
        self.search_hits_TYPE     = self.liste_automates
        self.search_hits_IDCODE   = self.liste_automates
        

    

    def get_search_filter_selection(self, header_msg = '==== ITEMS SUGGESTED ====', sub_head_msg = '', main_menu = False, print_permission = True):
        
        #print(header_msg)

        if len(self.list_hits) > 10:
           print('==== ITEMS SUGGESTED ====' + "(First 10 results of the search are shown)")
        else:
           print('==== ITEMS SUGGESTED ====')


        # print('==== ITEMS SUGGESTED ====' + "(First 10 results of the search are shown)")

        if print_permission == True:
            #print(self.number_results_found, 'items found with your search.\n'+ header_msg)
            if len(self.list_hits) <= 10:
                print(self.number_results_found, 'items found with your search.\n'+ header_msg)#+ "(First 10 results of the search are shown)")
                for item in self.list_hits:
                    item.printAutomate()
            else:
                print(self.number_results_found, 'items found with your search.\n'+ header_msg+ "(First 10 results of the search are shown)")
                for item in self.list_hits[0:10]:
                    item.printAutomate()
        
        

        if len(self.list_hits) > 10:
            list_correction_spaces = 10 
        else:
            list_correction_spaces = len(self.list_hits)
        correction_spaces = 17 + list_correction_spaces
        for space in range(os.get_terminal_size().lines - correction_spaces): 
            print('')
            
        
        item_suggested = '[ITEM SELECTED: NONE (Must select ONE item)]'

        if len(self.list_hits) == 1:
            item_suggested = '[ITEM SELECTED: '
            item_suggested += self.list_hits[0].ID_CODE
            item_suggested += '  ' + self.list_hits[0].item_name
            item_suggested += '  ' + self.list_hits[0].type_item + ']'

        print("Searching: ")
        print("            TYPE : " + self.search_type  )
        print("          IDCODE : " + self.search_IDCODE)
        print("            NAME : " + self.search_name + "\n")
        
        print("Options: ")
        print("--- Filter Search ---")
        print("     Search by type            [1]")
        print("     Search by ID              [2]")
        print("     Search by name            [3]")
        print("     Reset filters             [4]")
        print("     Add Object to Cart        [5]   " + item_suggested )
        print("     Exit Search               [6]")

                                                                                                    
        



    def execute_search(self):
        
        # States
        TYPE           = '1'
        IDCODE         = '2'
        NAME           = '3'
        RESET_FILTERS  = '4'
        COMFIRM_OBJECT = '5'
        EXIT_SEARCH    = '6'
        
        
        filter_selection = '1'

        self.get_search_filter_selection('==== SEARCH MENU ====', '', True)
        
        filter_selection = input("\nSelect option: ")

        print_items_permission = False

       
        while True:
            if filter_selection == TYPE:
                self.get_search_filter_selection('==== ITEMS SUGGESTED ====', '', False, print_items_permission)
                langage = str(input("Search by type: "))
                print('     \n     Loading results...')
                
                self.search_item_by_type(langage)
                self.update_search_results()
                self.search_type = langage
                
                if self.search_type != '' and langage == '':
                    pass
                else:
                    pass

                

            if filter_selection == IDCODE:
                langage = str(input("Search by IDCODE: "))
                print('     \n     Loading results...')
                
                
                self.search_item_by_IDCODE(langage)
                self.update_search_results()
                self.search_IDCODE = langage

                if self.search_IDCODE != '' and langage == '':
                    pass
                else:
                    pass

                

            if filter_selection == NAME:
                self.get_search_filter_selection('==== ITEMS SUGGESTED ====', '', False, print_items_permission)
                langage = str(input("Search by NAME: "))
                print('     \n     Loading results...')
                
                if self.search_name != '' and langage == '':
                    pass
                else:
                    pass

                self.search_item_by_name(langage)
                self.update_search_results()
                self.search_name = langage

                

            if filter_selection == RESET_FILTERS:
                self.reset_search()
        
            if filter_selection == COMFIRM_OBJECT:
                if len(self.list_hits) == 1:
                    item = self.list_hits[0]
                    self.liste_automates.remove(item)
                    self.reset_search()
                    return item
                else:
                    input("You must select one item! Press 'Enter' to continue.")

            if filter_selection == EXIT_SEARCH:
                self.reset_search()
                return False
                


            print_items_permission = True
            if self.search_name == '' and self.search_type == '' and self.search_IDCODE == '':
                print_items_permission = False
            self.get_search_filter_selection('==== ITEMS SUGGESTED ====', '', False, print_items_permission)
            filter_selection = str(input("\nSelect option: "))
            

        return False
            
