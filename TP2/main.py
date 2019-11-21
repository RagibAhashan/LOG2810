import csv
from Object import Object
from FiniteStateMachine import Automate
from OrderManager import OrderManager



def read_file(file_name = 'inventaire.txt'):
	items_list = []

	try:
		with open(file_name) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=' ')
			for line in csv_reader:
				print(len(line))
                #name = line[0]
		print("Le ficher est lu!")
	except Exception as e:
		print("Erreur de lecture du fichier! Le fichier '" + file_name + "' ne peut pas être lu.")





def main():
    read_file()




main()