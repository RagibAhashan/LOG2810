from Object import Object
from OrderManager import OrderManager
from Entrepot import Entrepot
from State import State
from FiniteStateMachine import StateMachine
from SearchEngine import SearchEngine
from ShoppingCart import ShoppingCart
from OrderManager import OrderManager
from Automate     import Automate

import csv
import os
import platform


# WORKS
def read_file(file_name = 'inventaire.txt'):
	items_list = []
	automate_list = []
	try:
		with open(file_name) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=' ')
			line_counter = 0
			for line in csv_reader:
				name = str(line[0])
				id_code = str(line[1])
				type_object = str(line[2])

				automate = Automate(name, id_code, type_object, str(line_counter))
				line_counter += 1
				automate_list.append(automate)
				item = Object(name, id_code, type_object)
				items_list.append(item)
	except Exception as e:
		print("Erreur de lecture du fichier! Le fichier '" + file_name + "' ne peut pas être lu.")

	return items_list, automate_list



def main():
	#items_store, automate_list = read_file('Inventaire_grosFichier.txt')
	items_store, automate_list = read_file('inventaire.txt')

	#a = Automate('ami', '111111', 'B', '0')



	# for item in automate_list:
	# 	item.printAutomate()

	# print('\n\n\n\n\n')
	# # entrepot = Entrepot(items_store)


	
	search_engine = SearchEngine(automate_list)
	

	item = search_engine.execute_search()

	print('\n\n\n\n\n')
	
	item.printAutomate()
	print('\n\n\n\n\n')

	for item in search_engine.liste_automates:
		item.printAutomate()


	

	# automate_list.remove(automate_list[2])
	

	# for item in automate_list:
	# 	item.printAutomate()
	
	
	
	
	# while True:
	# 	print("Results: ")
		
		
	# 	search_engine.search_IDCODE = str(input("Search code: "))
	# 	search_engine.search_item_by_IDCODE(search_engine.search_IDCODE)
		
		
	# 	search_engine.search_name = str(input("Search name: "))
	# 	search_engine.search_item_by_name(search_engine.search_name)
		
		
	# 	search_engine.search_type = str(input("Search type: "))
	# 	search_engine.search_item_by_type(search_engine.search_type)
		
		
	# 	search_engine.update_search_results()
	# 	print()
	# 	print('IDCODE:')
	# 	for item in search_engine.search_hits_IDCODE:
	# 		item.printAutomate()

	# 	print()
	# 	print('NAME:')
	# 	for item in search_engine.search_hits_name:
	# 		item.printAutomate()

	# 	print()
	# 	print('TYPE:')
	# 	for item in search_engine.search_hits_TYPE:
	# 		item.printAutomate()
	# 	print()
	# 	print()

	
		# search_engine.update_search_results()
		
		# print(search_engine.number_results_found)
		# search_engine.get_search_filter_selection()
		# for item in search_engine.list_hits:
		# 	item.printAutomate()
	





if __name__ == '__main__':
	main()