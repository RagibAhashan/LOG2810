import csv

def read_file(file_name = 'inventaire.txt'):
	

	try:
		with open(file_name) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=' ')
			for line in csv_reader:
				print(line)
		print("Le ficher est lu!")
	except Exception as e:
		print("Erreur de lecture du fichier! Le fichier '" + file_name + "' ne peut pas être lu.")
		return False, False


	return list_vertices, list_arcs




def main():
    read_file()




main()