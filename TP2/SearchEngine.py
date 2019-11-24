import os
import platform

acceptable_chars = [ chr(i+97) for i in range(26)]
for i in range(10):
    acceptable_chars.append(str(i))


class SearchEngine:
    def __init__(self, entrepot_data, state_machine_mealy):
        self.entrepot_data          = entrepot_data
        self.search_items_hits      = entrepot_data.getItems()
        self.state_machine_mealy    = state_machine_mealy

        self.filter_name_activated  = False
        self.filter_type_activated  = False
        self.filter_idCode_activated= False
        
    
    def search_by_type(self):
        print("Search id type")
        self.filter_type_activated  = True

    def search_by_name(self):
        print("Search id name")
        self.state_machine_mealy.run(True)
        self.filter_name_activated = True


    def search_by_idCode(self):
        print("Search id code")
        self.state_machine_mealy.run(False)
        self.filter_idCode_activated= True
    

    def get_search_filter_selection(self):
        self.search_items_hits = self.state_machine_mealy.search_hits

        print("List of items found on research...")
        for item in self.search_items_hits:
            item.printItem()
        
        
        # Pas essentiel a l'implementation de notre automate. C'est pour formatter l'affichage.#######
        if platform.system() == "Windows":                                                          ##
            correction_spaces = 8                                                                   ##
        else:                                                                                       ##
            correction_spaces = 7                                                                   ##
                                                                                                    ##
        for space in range(os.get_terminal_size().lines - len(self.search_items_hits) - correction_spaces): ##
            print('')                                                                               ##
                                                                                                    ##
        # Pas essentiel a l'implementation de notre automate. C'est pour formatter l'affichage.#######
        
        

        print("Select a search filter")
        if self.filter_type_activated == True:
            print("Search by type [1]     [X]")
        else:
            print("Search by type [1]     [ ]")
        
        if self.filter_idCode_activated == True:
            print("Search by ID   [2]     [X]")
        else:
            print("Search by ID   [2]     [ ]")

        if self.filter_name_activated == True:
            print("Search by name [3]     [X]\n")
        else:
            print("Search by name [3]     [ ]\n")

        while True : 
            search_type = str(input("Filter of choice: "))
            if search_type == '1' or search_type == '2' or search_type == '3':
                break
            print("Choix possibles: [1, 2, 3]")
        
        return search_type

    def search_item(self):

        print("===== ITEMS IN STOCK =====")
        for item in self.search_items_hits:
            item.printItem()
        
        
        # Pas essentiel a l'implementation de notre automate. C'est pour formatter l'affichage.#######
        if platform.system() == "Windows":                                                          ##
            correction_spaces = 8                                                                   ##
        else:                                                                                       ##
            correction_spaces = 7                                                                   ##
                                                                                                    ##
        for space in range(os.get_terminal_size().lines - len(self.search_items_hits) - correction_spaces): ##
            print('')                                                                               ##
                                                                                                    ##
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


        type_search = '1'
        id_search   = '2'
        name_search = '3'

        while True:

            if search_type == type_search:
                self.search_by_type()
                ans = input("Would you like to change search filters? Enter 1 for YES: ")
                if ans != '1':
                    break
                elif ans in acceptable_chars:
                    search_type = self.get_search_filter_selection()

            if search_type == id_search:
                self.search_by_idCode()
                ans = input("Would you like to change search filters? Enter 1 for YES: ")
                if ans != '1':
                    break
                else:
                    search_type = self.get_search_filter_selection()

            if search_type == name_search:
                self.search_by_name()
                ans = input("Would you like to change search filters? Enter 1 for YES: ")
                if ans != '1':
                    break
                else:
                    search_type = self.get_search_filter_selection()


        
        
    



