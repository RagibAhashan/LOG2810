class State:
    def __init__(self, state_name = 'unknown', inputs = 'unknown', outputs = 'unknown', terminal = False):
        self.state_name = state_name
        self.outputs    = outputs
        self.inputs     = inputs
        self.terminal   = terminal

    def printState(self):
        print("Name: "   + self.state_name)
        print("Inputs: " +     self.inputs)
        print("Ouput: "  +     self.output)

