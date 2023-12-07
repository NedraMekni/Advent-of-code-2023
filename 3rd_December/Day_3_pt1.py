


def get_symbols_coordinates(matrix):
	symbols_coordinates=[]

	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] != "." and not matrix[i][j] in [str(x) for x in range(0,10)]:
				symbols_coordinates.append((i,j))
	return symbols_coordinates




def get_neighbors(i, j, len_row, len_col):

	list_coord_neighbors = []

	for i1 in range(i-1, i+2):
		for j1 in range(j-1, j+2):
			if not (i1==i and j1==j) and j1>=0 and i1>=0 and i1 <len_row and j1<len_col:
				list_coord_neighbors.append((i1,j1))
	return list_coord_neighbors


def get_numbers_coordinates(matrix):
	number_dict={}

	for i in range(len(matrix)):

		l=matrix[i]

		index_l= 0
		number_acc = ''
		index_acc = []
		
		for c in l:
			if c.isdigit():
				number_acc+=c
				index_acc.append((i,index_l))

			else:
				if len(number_acc)!=0:
					number_dict[number_acc+" "+ str(i)+" "+ str(index_l)]=index_acc.copy()
					number_acc=''
					index_acc=[]
			index_l+=1

		if len(number_acc)!=0:
			number_dict[number_acc+" "+ str(i)+" "+ str(index_l)]=index_acc.copy()
		
	return number_dict
 









if __name__ == '__main__':

	input_file='./input.txt'

	with open(input_file,"r") as f:
		matrix= [ l.strip() for l in f.readlines()]

	symbols_coordinates= get_symbols_coordinates(matrix)
	#print(symbols_coordinates)

	'''
	prendendo matrix estarre i numeri e le coordinate di ogni cifra
	'''
	numbers = get_numbers_coordinates(matrix)
	result = []

	len_row = len(matrix)
	len_col = len(matrix[0])

	for symbols_coordinate in symbols_coordinates:
		i_symb =symbols_coordinate[0]
		j_symb =symbols_coordinate[1]
		neighbors_symb_coordinates=get_neighbors(i_symb,j_symb,len_row,len_col)



		for k_num in numbers.keys():
			number_coordinates=numbers[k_num]

			touch_coordinates= [x for x in neighbors_symb_coordinates if x in number_coordinates]
			if len(touch_coordinates)>0:

				result.append(int(k_num.split(" ")[0]))

	solution = sum(result)
	print(solution)






	



