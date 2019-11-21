class State:
    def __init__(self, state_name = 'unknown', inputs = 'unknown', outputs = 'unknown'):
        self.state_name = state_name
        self.inputs = inputs
        self.outputs = outputs

    def printState(self):
        print("Name: " + self.state_name)
        print("Inputs: " + self.inputs)
        print("Ouputs: " + self.outputs)
