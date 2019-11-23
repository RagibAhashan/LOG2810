from Object import Object
from OrderManager import OrderManager
from Entrepot import Entrepot
from State import State
#from FiniteStateMachine import StateMachine
from FiniteStateMachine import StateMachine


import csv
import numpy as np
import msvcrt
import os
import platform


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

	
	name = ''

	entrepot = Entrepot(items_store)
	# ans = entrepot.search_item_by_name("")
	

	# updated_list = entrepot.update_dynamic_list(ans)
	

	state_machine = StateMachine([0,1,2,3,4] , 0, [3,4], entrepot)


	#print(state_machine.transition_state())
	ans = state_machine.run()
	print(ans)


	print("\n")

	


	# while(True):

	# 	for item in updated_list:
	# 		item.printItem()
		
	# 	for i in range(os.get_terminal_size().lines - len(updated_list) - 3):
	# 		print('')
		
	# 	print("Press Enter to exit...")
	# 	inp = get_input("Search item by name: " + name)
		
	# 	if inp == False:
	# 		break
		
	# 	if platform.system() == "Windows":
	# 		if inp == '':
	# 			name = name[0:len(name)-1]
		
	# 		name += inp
	# 	else:
	# 		name = inp
		
	# 	list_names_found = entrepot.search_item_by_name(name)
	# 	updated_list 	 = entrepot.update_dynamic_list(list_names_found)
		







main()