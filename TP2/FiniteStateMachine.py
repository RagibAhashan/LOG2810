from State import State
from Object import Object
import os
import platform


# def get_input(message = ''):
#     if platform.system() == 'Windows':
#         print(str(message))
#         ans = str(msvcrt.getch())

#         if ans[0] == 'b' and ans[1] == "'" and ans[3] == 'r':
#             return False
#         if ans.find('x08') == 3 and ans[1] == "'":
#             return ''
#         return ans[2]
#     else:
#         ans = str(input(message))
#         return ans

class StateMachine:
    
    def __init__(self, all_states, initial_state, terminal_states, entrepot_data):
        self.all_states       = all_states
        self.initial_state    = initial_state
        self.terminal_states  = terminal_states
        self.entrepot_data    = entrepot_data
        
        self.search_hits       = entrepot_data.get_items_dynamic().copy()
        self.name_item_search  = ''
        self._run_name_search   = True
        self._run_IDCODE_search = False


    def settings_machine(self, search_parameter):
        if search_parameter == 'NAME':
            self._run_name_search   = True
            self._run_IDCODE_search = False
        
        elif search_parameter == 'IDCODE':
            self._run_IDCODE_search = True
            self._run_name_search   = False
        
        else:
            print("'NAME' or 'IDCODE' are accepted.")


    def run(self):
        S0_initial_state         = self.all_states[0]
        S1_partial_success_state = self.all_states[1]
        S2_fail_search_state     = self.all_states[2]
        S3_sucess_state          = self.all_states[3]
        S4_exit_state            = self.all_states[4]
        current_state            = S0_initial_state

        if self._run_name_search:
            input_message = "Search name: "
        else:
            input_message = "Search IDCODE: "

        
        while True:
            if current_state == S0_initial_state:
                print("INITIAL")
                self.name_item_search = str(input(input_message))
                current_state = self.transition_state(self.name_item_search)

            if current_state == S1_partial_success_state:
                print("SUCESS")
                break

                # This is a terminal state. Permission to exit granted.
                # self.name_item_search = str(input(input_message))
                # current_state = self.transition_state(self.name_item_search)
                # break 

            if current_state == S2_fail_search_state:
                print("FAIL")

                # This is not a terminal state. Permission to exit is denied.
                self.name_item_search = str(input(input_message))
                current_state = self.transition_state(self.name_item_search)
                



            if current_state == S3_sucess_state:
                pass
            if current_state == S4_exit_state:
                return "EXIT"

            

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
        pass



    def transition_state(self, name_item_search = ''):

        # List all items available.
        # for item in self.entrepot_data.get_items_dynamic():
        #     item.printItem() 

        # print("\n")

        Sucess_STATE = self.all_states[1]
        Fail_State   = self.all_states[2]
        
        if self._run_name_search == True:
            names_suggested_list = self.entrepot_data.search_item_by_name(name_item_search)
            self.search_hits     = self.entrepot_data.get_suggested_items(names_suggested_list)
            # for item in self.search_hits:
            #     item.printItem()

        
        if self._run_IDCODE_search == True:
            names_suggested_list = self.entrepot_data.search_item_by_idCode(name_item_search)
            self.search_hits     = self.entrepot_data.get_suggested_items_with_list_idcodes(names_suggested_list)
            # for item in self.search_hits:
            #     item.printItem()

        
        
        # Si la liste est plus grande que 0, il existe des suggestions.
        if len(self.search_hits) > 0:
            return Sucess_STATE   # Return Success state.
        return Fail_State         # Return Fail state.

    
    