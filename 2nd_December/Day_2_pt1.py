


def play_one_round(inp):

	resuls_from_game = inp.strip().split(":")
	print(resuls_from_game)

	title = resuls_from_game[0].strip()
	
	title_number = int(title.split()[-1])
	print(title_number)
	game = resuls_from_game[1].strip()
	
	set_valid_result = []
	for set_game in game.split(';'):
		set_valid_result.append(valid_set(set_game))

	result = 0
	if all(set_valid_result):
		result=title_number
	return result



def valid_set(set_game):
	print(set_game)


	set_game = set_game.replace(",", "")

	print(set_game)

	set_game = set_game.split()
	print(set_game)

	
	color_number_dict = {}

	for i in range(0, len(set_game), 2):
		number = int(set_game[i])
		color = set_game[i + 1]

		if color in color_number_dict:
			color_number_dict[color].append(number)
		else:
			color_number_dict[color] = [number]
	
	print(color_number_dict)



	green_count = 0
	blue_count = 0
	red_count = 0
	is_valid = False

	for k,value in color_number_dict.items():
		if k == 'green':
			green_count += sum(value)
		if k == 'blue':
			blue_count += sum(value)
		if k == 'red':
			red_count += sum(value)

	print("total green box: ",green_count)
	print("total blue box: ",blue_count)
	print("total red box: ",red_count)
	
	if green_count <= 13:
		if blue_count <= 14:
			if red_count <=12:
				is_valid=True

	return is_valid



if __name__ == '__main__':
	

	solve = []

	fname = 'input.txt'
	with open(fname, 'r') as f:

		lines =f.readlines()
		for line in lines:
			print(line)

			result = play_one_round(line)

			print(result)

			solve.append(result)
			
	print(solve)
	print(len(solve))

	print("THE SOLUTION IS: ",sum(solve))



