import csv
from Object import Object
from FiniteStateMachine import StateMachine
from OrderManager import OrderManager
import numpy as np
import msvcrt
import os
import platform

print(platform.system())


# WORKS
def read_file(file_name = 'inventaire.txt'):
	items_list = []
	try:
		with open(file_name) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=' ')
			for line in csv_reader:
				name = str(line[0])
				id_code = str(line[1])
				type_object = str(line[2])
				item = Object(name, id_code, type_object)
				items_list.append(item)
                
		print("Le ficher est lu!")
	except Exception as e:
		print("Erreur de lecture du fichier! Le fichier '" + file_name + "' ne peut pas être lu.")

	return items_list

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


def print_items(items):
	for item in items:
		item.printItem()



def main():
	items_store = read_file()
	all_states  = []
	input_state = []
	transition_function = []
	initial_state = []
	terminal_states = []


	automate = StateMachine(all_states, input_state, transition_function, initial_state, terminal_states)
	ts = os.get_terminal_size().lines
	print(os.get_terminal_size().lines)
	msg = ''
	
	while(True):
		
		x = get_input("Message: " + msg)
		if x == False:
			break
		if x == '':
			msg = msg[0 : len(msg)-1]
			
	
		print_items(items_store)
		for i in range(os.get_terminal_size().lines - len(items_store) - 3):
			print('')
		print("Press Enter to exit...")
		msg += x



main()