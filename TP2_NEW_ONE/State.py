
#############################################################################################
#	Classe State: Cette classe défini un état
#############################################################################################
class State:
    def __init__(self, state_name = '', inputs_required = [], possible_inputs = [], terminal = False):
        self.state_name = state_name

        # inputs that are accepted in this state. Otherwise, it will violate langage of state machine.
        self.possible_inputs   = possible_inputs    
        
        # Inputs that are required to acces this state.
        self.inputs_required   = inputs_required

        # If it's a terminal state.
        self.terminal = terminal

        self.next_state = ''

    #############################################################################################
    #   methode isTerminalState: retourne un si c'est un état terminal
    #	params [self]
    #############################################################################################
    def isTerminalState(self):
        return self.terminal


    def setNextState(self, next_state):
        self.next_state = next_state

    def print_state(self):
        print('state_name: ' + self.state_name)
        print('User input required to acces this state: ', self.inputs_required)
        print('User input(s) that will be accepted (Else, its empty space and langage rejected): ', self.possible_inputs)
        print('Terminal: ', self.terminal)
        

