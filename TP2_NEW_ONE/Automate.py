from State import State
class Automate:
    def __init__(self, item_name = '', ID_CODE = '', type_item = '', item_number = '0'):
        self.main_state = State('S' + item_number, [], [item_name[0], ID_CODE[0], type_item[0]], True)
        self.item_name  = item_name
        self.ID_CODE    = ID_CODE
        self.type_item  = type_item

        self.name_chemin = [State('S' + item_number, [], [item_name[0], ID_CODE[0], type_item[0]], True)]
        self.id_chemin   = [State('S' + item_number, [], [item_name[0], ID_CODE[0], type_item[0]], True)]
        self.type_chemin = State('T1', type_item, ['1'], True)
        self.assemble_states()

        # Toute est relier. [S0, [N1], [C1], [T1]]
        self.chemins     = [self.main_state, self.name_chemin, self.id_chemin, self.type_chemin]



    def assemble_states(self):

        for i in range(len(self.item_name)):
            input_letter = self.item_name[i]

            if i + 1 < len(self.item_name):
                next_letter = self.item_name[i + 1]
                name_state = State('N' + str(i+1), input_letter, [next_letter, 0], False)
            else:
                name_state = State('N' + str(i+1), input_letter, ['1'], True)

            self.name_chemin.append(name_state)



        for i in range(len(self.ID_CODE)):
            input_letter = self.ID_CODE[i]

            if i + 1 < len(self.ID_CODE):
                next_letter = self.ID_CODE[i + 1]
                name_state = State('C' + str(i+1), input_letter, [next_letter, 0], False)
            else:
                name_state = State('C' + str(i+1), input_letter, [], True)

            self.id_chemin.append(name_state)

        for s in self.name_chemin:
            s.print_state()
            print()

        for s in self.id_chemin:
            s.print_state()
            print()

        self.type_chemin.print_state()

    

    def transition_state_function(self, user_input, current_state, mode = 'NAME'):
        first_state_terminal = 0
        if mode == 'NAME':
            if self.name_chemin[current_state].possible_inputs[0] == user_input:
                return current_state + 1
            else:
                return first_state_terminal
        
        
        if mode == 'IDCODE':
            if current_state == 0:
                if self.id_chemin[current_state].possible_inputs[1] == user_input:
                    return current_state + 1
                else:
                    return first_state_terminal

            else:
                if self.id_chemin[current_state].possible_inputs[0] == user_input:
                    return current_state + 1
                else:
                    return first_state_terminal







    # Return true if the langage is found in the States Machine!
    def verify_langage(self, langage = '', mode = 'NAME'):
        is_a_langage_in_automate = False
    
        first_state = 0
        current_state = first_state
        if mode == 'NAME':
            if len(langage) == 1:
                if self.name_chemin[current_state].possible_inputs[0] == langage:
                    return True
                else:
                    return False

            
            for I in langage:
                current_state = self.transition_state_function(I, current_state, mode)
            
            if self.name_chemin[current_state].isTerminalState() == True and current_state != 0:
                is_a_langage_in_automate = True


            return is_a_langage_in_automate
        




        elif mode == 'IDCODE':
            if len(langage) == 1 or len(self.ID_CODE) == 1:
                if self.id_chemin[current_state].possible_inputs[1] == langage:
                    return True
                else:
                    return False

            
            for I in langage:
                current_state = self.transition_state_function(I, current_state, mode)
            
            if self.id_chemin[current_state].isTerminalState() == True and current_state != 0:
                is_a_langage_in_automate = True


            return is_a_langage_in_automate
            
        elif mode == 'TYPE':
            if self.id_chemin[current_state].possible_inputs[2] == langage:
                return True
            else:
                return False
            
        else:
            print("The mode '" + mode + "' is NOT ACCEPTED!")
            return is_a_langage_in_automate


# a = Automate('ami', '111111', 'B', '1')

# print()



# print(a.verify_langage('ami','NAME'))

# print(a.verify_langage('B','TYPE'))
# print(a.verify_langage('111111','IDCODE'))




