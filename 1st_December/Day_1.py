
if __name__ == '__main__':
	
	fname = 'puzzle_input.txt'
	final_plus_2 = []
	final_minor_1= []



	with open(fname, 'r') as f:

		line =f.readlines()
		for l in line:
			lines = l.strip()
			find_digit = [str(x) for x in lines if x.isdigit()] 
			digit = "".join(find_digit) 

			merge_plus_2 = ["{}{}".format(digit[0],digit[-1])]
			final_plus_2.append(merge_plus_2)
			

	flat_plus_2_list = [int(inner[0]) for inner in final_plus_2]


	sum_digit = sum(flat_plus_2_list)
	print(sum_digit)

