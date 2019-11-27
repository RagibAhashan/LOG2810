from Object import Object
from OrderManager import OrderManager
from Entrepot import Entrepot
from State import State
from FiniteStateMachine import StateMachine
from SearchEngine import SearchEngine
import csv
import os
import platform

if(platform.system() == 'Windows'):
		import msvcrt


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
	items_store = read_file('Inventaire_grosFichier.txt')

	entrepot = Entrepot(items_store)
	
	search_engine = SearchEngine(entrepot)
	while True:
		ans = search_engine.run_search_engine()
		if ans == False:
			print("Search was abandonned!")
		else:
			entrepot.remove_item(ans)
		
	
	





if __name__ == '__main__':
	platform_using = platform.system()
	if platform_using == 'Windows':
		main()
	else:
		print("******CE PROGRAMME NE FONCTIONNE QUE SUR WINDOWS******")
		print("VOUS UTILISEZ UNE VERSION DE ***"+ platform_using + "***")
		
