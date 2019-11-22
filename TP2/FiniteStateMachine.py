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

        # msg = ''
        # current_state = self.initial_state
        
        # while(True):
		
        #     x = get_input("Search: " + msg)
        #     if x == False:
        #         break
        #     if x == '':
        #         msg = msg[0 : len(msg)-1]
                
        #     for item in self.all_states:
		#         item.printItem()
            
            
        #     for i in range(os.get_terminal_size().lines - len(self.all_states) - 3):
        #         print('')
        #     print("Press Enter to exit...")
        #     msg += x



        
        pass

    def stop(self):
        pass
    
    