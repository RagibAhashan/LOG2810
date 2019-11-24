from Object import Object
from OrderManager import OrderManager
from Entrepot import Entrepot
from State import State
from FiniteStateMachine import StateMachine
import csv
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

	entrepot = Entrepot(items_store)
	
	state_machine_autocomplete = StateMachine([0,1,2,3,4] , 0, [3,4], entrepot)


	ans = state_machine_autocomplete.run()
	print(ans)


	print("\n")

	





if __name__ == '__main__':
	main()
