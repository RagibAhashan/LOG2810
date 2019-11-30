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




def main():
	items_store = read_file('inventaire.txt')

	entrepot = Entrepot(items_store)
	
	search_engine = SearchEngine(entrepot)

	shopping_cart = ShoppingCart()

	orders = OrderManager(entrepot, search_engine, shopping_cart)

	orders.run_order_manager()

	

		





if __name__ == '__main__':
	main()