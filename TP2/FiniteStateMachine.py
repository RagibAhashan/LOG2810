from State import State
from Object import Object
import msvcrt
import os
import platform


def get_input(message = ''):
	
	if(platform.system() == 'Windows'):
		print(str(message))
		ans = str(msvcrt.getch())
		if ans[0] == 'b' and ans[1] == "'" and ans[3] == 'r':
			return False
		if ans.find('x08') == 3 and ans[1] == "'":
			return ''
		return ans[2]
	else:
		return input(message + '\n')



class StateMachine:
    
    def __init__(self, all_states, initial_state, terminal_states, entrepot_data):
        self.all_states          = all_states
        self.initial_state       = initial_state
        self.terminal_states     = terminal_states
        self.entrepot_data       = entrepot_data


    def run(self):
        S0_initial_state         = self.all_states[0]
        S1_partial_success_state = self.all_states[1]
        S2_fail_search_state     = self.all_states[2]
        S3_sucess_state          = self.all_states[3]
        S4_exit_state            = self.all_states[4]

        current_state         = S0_initial_state
        ans = [False, ""]

        while(True):

            if current_state == S0_initial_state:
                print("S0_initial_state")
                ans = self.transition_state()
                if ans[0] == True:
                    current_state = S1_partial_success_state
                

            if current_state == S1_partial_success_state:
                print("S1_partial_success_state")
                ans = self.transition_state(ans[1])
                if ans[0] == True:
                    current_state = S1_partial_success_state
                    item = self.entrepot_data.find_item_by_name(ans[1])
                    if item != False:
                        current_state = S3_sucess_state

                else:
                    current_state = S2_fail_search_state
                

            if current_state == S2_fail_search_state:
                print("S2_fail_search_state")
                ans = self.transition_state(ans[1])
                if ans[0] == True:
                    current_state = S1_partial_success_state
                else:
                    current_state = S2_fail_search_state

            if current_state == S3_sucess_state:
                print("S3_sucess_state")
                length_ans_search = len(ans[1])
                ans = self.transition_state(ans[1])

                if length_ans_search < len(ans[1]):
                    current_state = S2_fail_search_state

                elif length_ans_search > len(ans[1]):
                    current_state = S1_partial_success_state

                elif length_ans_search == len(ans[1]):
                    break

            if current_state == S4_exit_state:
                print("S4_exit_state")
                break
            




    def transition_state(self, name = ''):
        updated_list = self.entrepot_data.get_items_dynamic()
        list_names_found = self.entrepot_data.search_item_by_name(name)
        updated_list     = self.entrepot_data.update_dynamic_list(list_names_found)
        
    
        for item in updated_list:
            item.printItem()
        

        for i in range(os.get_terminal_size().lines - len(updated_list) - 3):
            print("")
        
        print("Press ENTER to exit...")

        inp = get_input("Search item by name: " + name)

        # if inp == False and len(updated_list) != 0:
        #     return [True, name]
        

        if inp == False:
            print("ENTER")
            return [True, name]

        if platform.system() == "Windows":
            if inp == '':
                name = name[0:len(name)-1]
            
            name += inp
        else:
            name = inp
        
        list_names_found = self.entrepot_data.search_item_by_name(name)
        updated_list     = self.entrepot_data.update_dynamic_list(list_names_found)
		
        if len(updated_list) != 0:
            return [True, name]
        else:
            return [False, name]

    def stop(self):
        pass
    
    