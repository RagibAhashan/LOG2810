class State:
    def __init__(self, state_name = 'unknown', inputs = 'unknown', output = 'unknown', terminal = False, all_items = []):
        self.state_name = state_name
        self.output     = output
        self.inputs     = inputs
        self.terminal   = terminal
        self.all_items  = all_items

    def printState(self):
        print("Name: "   + self.state_name)
        print("Inputs: " +     self.inputs)
        print("Ouput: "  +     self.output)

    def get_items_state(self):
        return self.all_items