import csv

def read_file(file_name = 'inventaire.txt'):
	
	list_vertices 	= []
	list_arcs 		= []
	n_Attributes_Vertex = 4
	n_Attributes_Arc 	= 3

	try:
		with open(file_name) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			#line_count = 0
			for line in csv_reader:
				if(len(line) == n_Attributes_Vertex):
					vertex_id 		 = line[0]
					vertex_objects_A = line[1]
					vertex_objects_B = line[2]
					vertex_objects_C = line[3]
					v = Vertex(vertex_id,vertex_objects_A,vertex_objects_B,vertex_objects_C)
					list_vertices.append(v)
					
				elif (len(line) == n_Attributes_Arc):
					first_vertex_id  	= int(line[0])
					second_vertex_id 	= int(line[1])
					distance_arc  		= int(line[2])

					first_vertex 	= list_vertices[first_vertex_id]
					second_vertex 	= list_vertices[second_vertex_id]
					
					arc = Arc(first_vertex, second_vertex, distance_arc)
					list_arcs.append(arc)
		print("Le ficher est lu!")
	except Exception as e:
		print("Erreur de lecture du fichier! Le fichier '" + file_name + "' ne peut pas être lu.")
		return False, False


	return list_vertices, list_arcs




def main():





main()