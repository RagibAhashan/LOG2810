from State import State
from Object import Object
import os
import platform

###########################################################################################
#   Classe StateMachine: cette classe fait le lien entre les états du système
###########################################################################################
class StateMachine:
    
    def __init__(self, all_states, initial_state, terminal_states, entrepot_data):
        self.all_states       = all_states
        self.initial_state    = initial_state
        self.terminal_states  = terminal_states
        self.entrepot_data    = entrepot_data
        
        self.search_hits        = entrepot_data.get_items_dynamic().copy()
        self.search_hits_IDCODE = entrepot_data.get_items_dynamic().copy()
        self.search_hits_TYPE   = entrepot_data.get_items_dynamic().copy()
        self.name_item_search   = ''
        self._run_name_search   = True
        self._run_IDCODE_search = False

    #############################################################################################
    #	methode settings_machine: 
    #	params [self, search_parameter]
    #############################################################################################
    def settings_machine(self, search_parameter):
        if search_parameter == 'NAME':
            self._run_name_search   = True
            self._run_IDCODE_search = False
        
        elif search_parameter == 'IDCODE':
            self._run_IDCODE_search = True
            self._run_name_search   = False
        
        else:
            print("'NAME' or 'IDCODE' are accepted.")

    #############################################################################################
    #	methode run: methode 
    #	params [self]
    #############################################################################################
    def run(self):
        S0_initial_state         = self.all_states[0]
        S1_sucess_state          = self.all_states[1]
        S2_fail_search_state     = self.all_states[2]
        S3_sucess_state          = self.all_states[3]
        
        current_state            = S0_initial_state

        if self._run_name_search:
            input_message = "\nSearch name: "
        else:
            input_message = "\nSearch IDCODE: "

        
        while True:
            if current_state == S0_initial_state:
                #print("INITIAL")
                self.name_item_search = str(input(input_message))
                current_state = self.transition_state(self.name_item_search)

            if current_state == S1_sucess_state:
                print("SUCESS")
                print('\n     Loading results...   \n')
                break


            if current_state == S2_fail_search_state:
                print("\nFAIL! NO ITMES NAMED '"+ self.name_item_search +"' WAS FOUND!\n")

                # This is not a terminal state. Permission to exit is denied.
                self.name_item_search = str(input(input_message))
                current_state = self.transition_state(self.name_item_search)
                


    #############################################################################################
    #	methode transition_state: methode permettant de changer d'etat
    #	params [self, name_item_search = '']
    #   return Sucess_STATE (state) or Fail_State (state)
    #############################################################################################
    def transition_state(self, name_item_search = ''):

        Sucess_STATE = self.all_states[1]
        Fail_State   = self.all_states[2]
        
        if self._run_name_search == True:
            names_suggested_list = self.entrepot_data.search_item_by_name(name_item_search)
            self.search_hits     = self.entrepot_data.get_suggested_items(names_suggested_list)
            

        if self._run_IDCODE_search == True:
            names_suggested_list = self.entrepot_data.search_item_by_idCode(name_item_search)
            self.search_hits_IDCODE = self.entrepot_data.get_suggested_items_with_list_idcodes(names_suggested_list)

        
        # Si la liste est plus grande que 0, il existe des suggestions.
        if len(self.search_hits) > 0:
            return Sucess_STATE   # Return Success state.
        return Fail_State         # Return Fail state.

    
    