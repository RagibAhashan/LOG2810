from State import State
from Object import Object
import os
import platform
import SearchEngine

acceptable_chars = [ chr(i+97) for i in range(26)]
for i in range(10):
    acceptable_chars.append(str(i))

if platform.system() == 'Windows':
    import msvcrt


def get_input(message = ''):
    if platform.system() == 'Windows':
        print(str(message))
        ans = str(msvcrt.getch())

        if ans[0] == 'b' and ans[1] == "'" and ans[3] == 'r':
            return False
        if ans.find('x08') == 3 and ans[1] == "'":
            return ''
        return ans[2]
    else:
        ans = str(input(message))
        return ans




class StateMachine:
    
    def __init__(self, all_states, initial_state, terminal_states, entrepot_data):
        self.all_states          = all_states
        self.initial_state       = initial_state
        self.terminal_states     = terminal_states
        self.entrepot_data       = entrepot_data
        self.search_hits         = entrepot_data.getItems()

        self.currently_searching_item_name = ''


    def run(self, search_name = True):
        S0_initial_state         = self.all_states[0]
        S1_partial_success_state = self.all_states[1]
        S2_fail_search_state     = self.all_states[2]
        S3_sucess_state          = self.all_states[3]
        S4_exit_state            = self.all_states[4]

        current_state            = S0_initial_state
        ans = [False, "", False]

        go_to_next_state_index     = 0
        search_name_index          = 1
        exit_states_machine_index  = 2


        if search_name == True:
            while(True):

                if current_state == S0_initial_state:
                    print("S0_initial_state")
                    print("Items available: \n")
                    ans = self.transition_state()

                    if self.entrepot_data.find_item_by_name(ans[search_name_index]) != False:
                        current_state = S3_sucess_state
                    else:
                        if ans[go_to_next_state_index] == True:
                            current_state = S1_partial_success_state
                        if ans[go_to_next_state_index] == False:
                            current_state = S2_fail_search_state

                if current_state == S1_partial_success_state:
                    print("S1_partial_success_state")
                    print("'" + ans[search_name_index] + "' is not an item in the list.\nItems suggested:")
                    

                    
                    if platform.system() == 'Windows':    
                        ans = self.transition_state(ans[search_name_index])            
                        if ans[exit_states_machine_index] == True:
                            return ans[search_name_index]
                        
                        if ans[go_to_next_state_index] == True:
                            
                            current_state = S1_partial_success_state
                            item = self.entrepot_data.find_item_by_name(ans[search_name_index])
                            if item != False:
                                current_state = S3_sucess_state
                        else:
                            current_state = S2_fail_search_state
                    else:
                        self.displat_search_hits()
                        print("")
                        return ans[search_name_index]

                if current_state == S2_fail_search_state:
                    print("S2_fail_search_state")
                    print("No items found: \n")
                    if platform.system() != 'Windows':
                        response = str(input("'" + ans[search_name_index] + "' does not exist. Would you like to keep searching? Enter [1] for yes: "))
                        if response != '1' or response != "1":
                            return ans[search_name_index]
                        else:
                            ans[search_name_index] = ''
                    ans = self.transition_state(ans[1])
                    
                    if ans[exit_states_machine_index] == True:
                        return ans[search_name_index]
                    
                    if ans[go_to_next_state_index] == True:
                        current_state = S1_partial_success_state
                    elif ans[go_to_next_state_index] == False:
                        current_state = S2_fail_search_state
                    
                    

                if current_state == S3_sucess_state:
                    print("S3_sucess_state")
                    print("Search for '" + ans[search_name_index] + "' was found: \n")
                    print("Search result for item '" + ans[search_name_index] + "'. " + str(len(self.search_hits)) + " results are found.") 
                    length_ans_search = len(ans[search_name_index])

                    for item in self.search_hits:
                        item.printItem()
                    
                    # Pas essentiel a l'implementation de notre automate. C'est pour formatter l'affichage.#######
                    if platform.system() == "Windows":                                                          ##
                        correction_spaces = 5                                                                   ##
                    else:                                                                                       ##
                        correction_spaces = 4                                                                   ##
                                                                                                                ##
                    for space in range(os.get_terminal_size().lines - len(self.search_hits) - correction_spaces): ##
                        print('')

                    return ans[search_name_index]

                    # ans = self.transition_state(ans[search_name_index])

                    # object_name_search = self.entrepot_data.check_if_item_exist(ans[search_name_index])
                    # if ans[exit_states_machine_index] == True:
                    #     return ans[search_name_index]
                    # if length_ans_search != len(ans[search_name_index]) and object_name_search:
                    #     current_state = S3_sucess_state
                    # else:
                    #     current_state = S2_fail_search_state

                    # if length_ans_search == len(ans[search_name_index]):
                    #     return ans[search_name_index]



                if current_state == S4_exit_state:
                    print("S4_exit_state")
                    break
        
        if search_name == False:
            while(True):

                if current_state == S0_initial_state:
                    print("S0_initial_state")
                    print("Items available: \n")
                    ans = self.transition_state('','', search_name)

                    if self.entrepot_data.find_item_by_id(ans[search_name_index]) != False:
                        current_state = S3_sucess_state
                    else:
                        if ans[go_to_next_state_index] == True:
                            current_state = S1_partial_success_state
                        if ans[go_to_next_state_index] == False:
                            current_state = S2_fail_search_state

                if current_state == S1_partial_success_state:
                    print("S1_partial_success_state")
                    print("'" + ans[search_name_index] + "' is not an item in the list.\nItems suggested:")
                    

                    
                    if platform.system() == 'Windows':    
                        ans = self.transition_state('',ans[search_name_index],False)            
                        if ans[exit_states_machine_index] == True:
                            return ans[search_name_index]
                        
                        if ans[go_to_next_state_index] == True:
                            
                            current_state = S1_partial_success_state
                            item = self.entrepot_data.find_item_by_id(ans[search_name_index])
                            if item != False:
                                current_state = S3_sucess_state
                        else:
                            current_state = S2_fail_search_state
                    else:
                        self.displat_search_hits()
                        print("")
                        return ans[search_name_index]

                if current_state == S2_fail_search_state:
                    print("S2_fail_search_state")
                    print("No items found: \n")
                    if platform.system() != 'Windows':
                        response = str(input("'" + ans[search_name_index] + "' does not exist. Would you like to keep searching? Enter [1] for yes: "))
                        if response != '1' or response != "1":
                            return ans[search_name_index]
                        else:
                            ans[search_name_index] = ''
                    ans = self.transition_state('',ans[1],False)
                    
                    if ans[exit_states_machine_index] == True:
                        return ans[search_name_index]
                    
                    if ans[go_to_next_state_index] == True:
                        current_state = S1_partial_success_state
                    elif ans[go_to_next_state_index] == False:
                        current_state = S2_fail_search_state
                    
                    

                if current_state == S3_sucess_state:
                    print("S3_sucess_state")
                    print("Search for '" + ans[search_name_index] + "' was found: \n")
                    print("Search result for item '" + ans[search_name_index] + "'. " + str(len(self.search_hits)) + " results are found.") 
                    length_ans_search = len(ans[search_name_index])

                    for item in self.search_hits:
                        item.printItem()
                    
                    # Pas essentiel a l'implementation de notre automate. C'est pour formatter l'affichage.#######
                    if platform.system() == "Windows":                                                          ##
                        correction_spaces = 5                                                                   ##
                    else:                                                                                       ##
                        correction_spaces = 4                                                                   ##
                                                                                                                ##
                    for space in range(os.get_terminal_size().lines - len(self.search_hits) - correction_spaces): ##
                        print('')

                    return ans[search_name_index]

                    # ans = self.transition_state(ans[search_name_index])

                    # object_name_search = self.entrepot_data.check_if_item_exist(ans[search_name_index])
                    # if ans[exit_states_machine_index] == True:
                    #     return ans[search_name_index]
                    # if length_ans_search != len(ans[search_name_index]) and object_name_search:
                    #     current_state = S3_sucess_state
                    # else:
                    #     current_state = S2_fail_search_state

                    # if length_ans_search == len(ans[search_name_index]):
                    #     return ans[search_name_index]



                if current_state == S4_exit_state:
                    print("S4_exit_state")
                    break
            
























    def displat_search_hits(self):
        for item in self.search_hits:
            item.printItem()
        
        # Pas essentiel a l'implementation de notre automate. C'est pour formatter l'affichage.#######
        if platform.system() == "Windows":                                                          ##
            correction_spaces = 5                                                                   ##
        else:                                                                                       ##
            correction_spaces = 4                                                                   ##
                                                                                                    ##
        for space in range(os.get_terminal_size().lines - len(self.search_hits) - correction_spaces): ##
            print('')                                                                               ##
                                                                                                    ##
        # Pas essentiel a l'implementation de notre automate. C'est pour formatter l'affichage.#######



    # Return [state_direction, string, Is ENTER pressed? true: Yes]
    def transition_state(self, name = '', id_code = '', search_name = True):
        
        if search_name == True:
            # list_names_found     = self.entrepot_data.search_item_by_name(name)
            # suggested_list       = self.entrepot_data.get_suggested_items(list_names_found)
            
        
            for item in self.search_hits:
                item.printItem()
            
            # Pas essentiel a l'implementation de notre automate. C'est pour formatter l'affichage.#######
            if platform.system() == "Windows":                                                          
                correction_spaces = 5                                                                   
            else:                                                                                       
                correction_spaces = 4                                                                   
                                                                                                        
            for space in range(os.get_terminal_size().lines - len(self.search_hits) - correction_spaces): 
                print('')                                                                               
            # Pas essentiel a l'implementation de notre automate. C'est pour formatter l'affichage.#######

            print("Searching with name: " + name)

            inp = get_input("Search item by name: ")
            print("Press 'ENTER' to confirm your search...")
            


            if platform.system() == "Windows":
                ENTER_BOUTON = False
                if inp == ENTER_BOUTON:
                    return [True, name, True]

                if inp == '':
                    name = name[0:len(name)-1]
                name += inp

            else:
                name = inp
            
            list_names_found   = self.entrepot_data.search_item_by_name(name)
            suggested_list     = self.entrepot_data.get_suggested_items(list_names_found)

            self.search_hits = suggested_list
            print(len(self.search_hits))
            self.currently_searching_item_name = name

            # Si la liste 
            if len(suggested_list) != 0:
                # Aller au prochain etat. Sans sortir de la machine a etat.
                return [True,  name, False]
            else:
                return [False, name, False]
        
        
        
        else:
            

            for item in self.search_hits:
                item.printItem()
            
            # Pas essentiel a l'implementation de notre automate. C'est pour formatter l'affichage.#######
            if platform.system() == "Windows":                                                          ##
                correction_spaces = 5                                                                   ##
            else:                                                                                       ##
                correction_spaces = 4                                                                   ##
                                                                                                        ##
            for space in range(os.get_terminal_size().lines - len(self.search_hits) - correction_spaces): ##
                print('')                                                                                 ##
                                                                                                          ##
            # Pas essentiel a l'implementation de notre automate. C'est pour formatter l'affichage.#######

            print("Searching with name: " + id_code)

            inp = get_input("Search item by ID CODE: ")
            print("Press 'ENTER' to confirm your search...")
            


            if platform.system() == "Windows":
                ENTER_BOUTON = False
                if inp == ENTER_BOUTON:
                    return [True, id_code, True]

                if inp == '':
                    id_code = id_code[0:len(id_code)-1]
                id_code += inp

            else:
                id_code = inp
            
            list_names_found   = self.entrepot_data.search_item_by_idCode(id_code)
            suggested_list     = self.entrepot_data.get_suggested_items_with_list_idcodes(list_names_found)

            self.search_hits = suggested_list
            print(len(self.search_hits))
            self.currently_searching_item_name = id_code

            # Si la liste 
            if len(suggested_list) != 0:
                # Aller au prochain etat. Sans sortir de la machine a etat.
                return [True,  id_code, False]
            else:
                return [False, id_code, False]

    
    