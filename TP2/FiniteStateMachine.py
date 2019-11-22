from State import State
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
    
    def __init__(self, all_states, input_state, initial_state, terminal_states):
        self.all_states          = all_states
        self.input_state         = input_state
        
        self.initial_state       = initial_state
        self.terminal_states     = terminal_states


    def run(self):
        pass


    def transition_state(self):
        pass
        

    def stop(self):
        pass
    
    