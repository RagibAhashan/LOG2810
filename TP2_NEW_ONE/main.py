########################################################################################################
############# 	LOG2810 - STRUCTURES DISCRETES								        		############
#############	Travail réalisé par Ragib Ahashan, Pritam Patel, Nawras Mohammmed Amin		############
#############	Travail Pratique 2															############
#############																				############
#############	Version de Python utilisé: 3.7.3								        	############
########################################################################################################

from Object import Object
from OrderManager import OrderManager
from Entrepot import Entrepot
from State import State
from FiniteStateMachine import StateMachine
from SearchEngine import SearchEngine
from ShoppingCart import ShoppingCart
from Automate     import Automate

import csv
import os
import platform


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
		print("Error reading this file! Le fichier '" + file_name + "' ne peut pas être lu.")

	return automate_list

def test():
	from OrderManager import OrderManager

	automate_list = read_file('inventaire.txt')
	search_engine = SearchEngine(automate_list)
	shopping_cart = ShoppingCart()
	order = OrderManager(automate_list, shopping_cart, search_engine)
	order.excute_order()



def menu_principal():
	# Initialiser le lexique: 
	# Shopping/Ajouter au panier:
	# Remove an object:
	# Clear Cart:
	# Checkout:
	# Quitter

	# Si les valeurs à l'interieur de cet liste n'est pas un input de l'usager, on refuse la reponse.
	reponses_possibles = ['1','2','3','4','5','6', '7']
	
	space_col = int(os.get_terminal_size().columns/2) - 28
	msg_initialiser_lexique = ''
	msg_shopping = ''
	msg_view_cart = ''
	msg_remove_item = ''
	msg_clear_cart = ''
	msg_checkout = ''
	msg_quit = ''

	for col_space in range(int(space_col)):
		msg_initialiser_lexique += ' '
		msg_shopping += ' '
		msg_view_cart += ' '
		msg_remove_item += ' '
		msg_clear_cart += ' '
		msg_checkout += ' '
		msg_quit += ' '


	msg_initialiser_lexique += "Initialisez le programme avec un lexique      Tappez [1]"
	msg_shopping 			+= "Chercher un objet et magasiner                Tappez [2]"
	msg_view_cart			+= "Voir votre panier                             Tappez [3]"
	msg_remove_item			+= "Enlever un item du panier                     Tappez [4]"
	msg_clear_cart 			+= "Vider votre panier                            Tappez [5]"
	msg_checkout			+= "Commander les objets dans votre panier        Tappez [6]"
	msg_quit				+= "Quitter le programme                          Tappez [7]"


	while True:
		print()
		print()
		print(msg_initialiser_lexique)
		print(msg_shopping)
		print(msg_view_cart)
		print(msg_remove_item)
		print(msg_clear_cart)
		print(msg_checkout)
		print(msg_quit)


		correction_spaces = 11
		for space in range(os.get_terminal_size().lines - correction_spaces):
			print('')

		msg_input = ''
		for i in range(space_col):
			msg_input += ' '
		msg_input += "Votre choix: "
		ans = str(input(msg_input))
		if ans in reponses_possibles:
			return ans
		

def format_spaces(correction_spaces):
	for space in range(os.get_terminal_size().lines - correction_spaces):
			print('')



def main():
	

	INITIALISE_LEXIQUE    = '1'
	ORDER_ITEM            = '2'
	VIEW_CART             = '3'
	REMOVE_ITEM_FROM_CART = '4'
	CLEAR_CART            = '5'
	CONFIRM_ORDER         = '6'
	QUIT_PROGRAM          = '7'

	current_state = '0'


	automate_list = False
	search_engine = False
	shopping_cart = False
	order 		  = False
	
	

	while True:
		current_state = menu_principal() 

		if current_state == INITIALISE_LEXIQUE:
			file_name = str(input("Rentrez le nom du fichier a lire: "))
			if file_name != 'inventaire.txt' and file_name != 'Inventaire_grosFichier.txt':
				alternatif = str(input("Vouliez vous lire 'inventaire.txt' au lieu? Tappez 1 pour oui" ))
				if alternatif == '1':
					automate_list = read_file('inventaire.txt')
					search_engine = SearchEngine(automate_list)
					shopping_cart = ShoppingCart()
					order = OrderManager(automate_list, shopping_cart, search_engine)
			else:
				automate_list = read_file(file_name)
				search_engine = SearchEngine(automate_list)
				shopping_cart = ShoppingCart()
				order = OrderManager(automate_list, shopping_cart, search_engine)


		if current_state == ORDER_ITEM:
			if automate_list != False:
				order.search_item_to_order()


		if current_state == VIEW_CART:
			if automate_list != False:
				order.print_order()
				input("       Appuyez sur 'Enter' pour retourner au Menu...     ")
			


		if current_state == REMOVE_ITEM_FROM_CART:
			if automate_list != False:
				order.remove_item_from_cart()
				input("       Appuyez sur 'Enter' pour retourner au Menu...     ")
				



		if current_state == CLEAR_CART:
			if automate_list != False:
				order.clear_cart_items()
				input("LE PANIER EST VIDÉE!\n       Appuyez sur 'Enter' pour retourner au Menu...     ")
				


		if current_state == CONFIRM_ORDER:
			if automate_list != False:
				if order.verify_order() == True:
					order.print_order(True)
					order.clear_cart_items()
				input("       Appuyez sur 'Enter' pour retourner au Menu...     ")
				


		if current_state == QUIT_PROGRAM:
			break

		if automate_list == False:
				print("               INITIALISEZ LE PROGRAMME AVEC UN LEXIQUE")
		else:
			print()


if __name__ == '__main__':
	main()