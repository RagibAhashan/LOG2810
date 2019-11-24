import os
import platform

acceptable_chars = [ chr(i+97) for i in range(26)]
for i in range(10):
    acceptable_chars.append(str(i))


class SearchEngine:
    def __init__(self, entrepot_data, state_machine_mealy):
        self.entrepot_data          = entrepot_data
        self.search_items_hits      = entrepot_data.get_items_dynamic()
        self.state_machine_mealy    = state_machine_mealy

        self.filter_name_activated  = False
        self.filter_type_activated  = False
        self.filter_idCode_activated= False

        self.search_name   = ''
        self.search_type   = ''
        self.search_IDCODE = ''
        
    
    def update_search_filters(self):
        temp_array = self.search_items_hits[:]
        self.search_items_hits.clear()
        for item in self.state_machine_mealy.search_hits:
            if item in temp_array:
                self.search_items_hits.append(item)



    def reset_filters(self):
        self.search_items_hits = self.entrepot_data.get_items_dynamic()



    def search_by_type(self, reset_filter = False):
        print("Search id type")

        for item in self.search_items_hits:
            item.printItem()

        # Pas essentiel a l'implementation de notre automate. C'est pour formatter l'affichage.#######
        if platform.system() == "Windows":                                                          ##
            correction_spaces = 3                                                                   ##
        else:                                                                                       ##
            correction_spaces = 2                                                                   ##
                                                                                                    ##
        for space in range(os.get_terminal_size().lines - len(self.search_items_hits) - correction_spaces): ##
            print('')                                                                               ##
                                                                                                    ##
        # Pas essentiel a l'implementation de notre automate. C'est pour formatter l'affichage.#######

        # if reset_filter == True:
        #     self.filter_type_activated  = False
        # else:
        #     self.filter_type_activated  = True
        


        ans_type = str(input("Search Type: "))
        self.search_type = ans_type
        list_hits_type = self.entrepot_data.find_items_by_Type(ans_type)



        temp_array = self.search_items_hits[:]
        self.search_items_hits.clear()

        # Deep search
        for item in list_hits_type:
            for i in range(len(temp_array)):
                if item.type == temp_array[i].type:
                    self.search_items_hits.append(item)








    def search_by_name(self, reset_filter = False):
        print("Search id name")
        self.state_machine_mealy.run(True)

        if reset_filter == True:
            self.filter_name_activated = False
        else:
            self.filter_name_activated = True


    def search_by_idCode(self, reset_filter = False):
        print("Search id code")
        self.state_machine_mealy.run(False)
        #self.filter_idCode_activated= True
        if reset_filter == True:
            self.filter_idCode_activated = False
        else:
            self.filter_idCode_activated = True
    

    def get_search_filter_selection(self):
        temp_array = self.search_items_hits[:]
        self.search_items_hits.clear()
        for item in self.state_machine_mealy.search_hits:
            if item in temp_array:
                self.search_items_hits.append(item)

        print("List of items found on research...")
        for item in self.search_items_hits:
            item.printItem()
        
        
        # Pas essentiel a l'implementation de notre automate. C'est pour formatter l'affichage.#######
        if platform.system() == "Windows":                                                          ##
            correction_spaces = 13                                                                   ##
        else:                                                                                       ##
            correction_spaces = 12                                                                   ##
                                                                                                    ##
        for space in range(os.get_terminal_size().lines - len(self.search_items_hits) - correction_spaces): ##
            print('')                                                                               ##
                                                                                                    ##
        # Pas essentiel a l'implementation de notre automate. C'est pour formatter l'affichage.#######

        print("Searching: ")
        print("          Type    : " + self.search_type  )
        print("          IDCODE  : " + self.search_IDCODE)
        print("          Name    : " + self.search_name  )

        
        

        print("\nSelect a search filter")
        if self.filter_type_activated == True:
            print(" Search by type [1]     [X]")
        else:
            print(" Search by type [1]     [ ]")
        
        if self.filter_idCode_activated == True:
            print(" Search by ID   [2]     [X]")
        else:
            print(" Search by ID   [2]     [ ]")

        if self.filter_name_activated == True:
            print(" Search by name [3]     [X]")
        else:
            print(" Search by name [3]     [ ]")

        print(" Reset filters  [4]")

        while True : 
            search_type = str(input("Filter of choice: "))
            if search_type == '1' or search_type == '2' or search_type == '3' or search_type == '4':
                break
            print("Choix possibles: [1, 2, 3, 4]")
        
        return search_type



    def run_search_engine(self):

        print("===== ITEMS IN STOCK =====")
        for item in self.entrepot_data.get_items_dynamic():
            item.printItem()
        
        
        # Pas essentiel a l'implementation de notre automate. C'est pour formatter l'affichage.#######
        if platform.system() == "Windows":                                                          
            correction_spaces = 8                                                                   
        else:                                                                                       
            correction_spaces = 7                                                                   
                                                                                                    
        for space in range(os.get_terminal_size().lines - len(self.entrepot_data.get_items_dynamic()) - correction_spaces): 
            print('')                                                                                       
        # Pas essentiel a l'implementation de notre automate. C'est pour formatter l'affichage.#######

        print("Select a search filter")
        print("Search by type [1]     [ ]")
        print("Search by ID   [2]     [ ]")
        print("Search by name [3]     [ ]\n")

        while True : 
            search_type = str(input("Filter of choice: "))
            if search_type == '1' or search_type == '2' or search_type == '3':
                break
            print("Choix possibles: [1, 2, 3]")


        type_search   = '1'
        id_search     = '2'
        name_search   = '3'
        reset_filters = '4'

        while True:

            if search_type == type_search:
                self.update_search_filters()
                self.search_by_type()
                ans = input("Would you like to change search filters? Enter 1 for YES: ")
                if ans != '1':
                    break
                elif ans in acceptable_chars:
                    search_type = self.get_search_filter_selection()

            if search_type == id_search:
                self.update_search_filters()
                self.search_by_idCode()
                self.search_IDCODE = self.state_machine_mealy.currently_searching_item_name
                ans = input("Would you like to change search filters? Enter 1 for YES: ")
                if ans != '1':
                    break
                else:
                    search_type = self.get_search_filter_selection()

            if search_type == name_search:
                self.update_search_filters()
                self.search_by_name()
                self.search_name = self.state_machine_mealy.currently_searching_item_name
                ans = input("Would you like to change search filters? Enter 1 for YES: ")
                if ans != '1':
                    break
                else:
                    search_type = self.get_search_filter_selection()

            if search_type == reset_filters:
                self.reset_filters()
                search_type = self.get_search_filter_selection()
                
                    



        
        
    



