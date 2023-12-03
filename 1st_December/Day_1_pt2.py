
import re



def resolve_line(inp):
	translate_to_digit = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
	numbers = [k for k in translate_to_digit.keys()]

	matched_number = [s for s in numbers if s in inp]
	matched_digit = [str(s) for s in range(10) if str(s) in inp] 
	number_dict={}
	for n in matched_number:
		all_index=re.finditer(n,inp)

		for index_span in all_index:

			start_index = index_span.start()
			number_dict[start_index] = str(translate_to_digit[n])

	for n in matched_digit:
		all_index=re.finditer(n,inp)
		for index_span in all_index:
			start_index = index_span.start()
			number_dict[start_index] = n
	list_position = list(number_dict.keys())
	list_position.sort()

	first_number = number_dict[list_position[0]]
	last_number = number_dict[list_position[-1]]

	result = int(first_number + last_number)
	return result

if __name__ == '__main__':

	solve = []

	fname = 'puzzle_input.txt'
	with open(fname, 'r') as f:

		lines =f.readlines()
		for line in lines:
			print(line)

			result = resolve_line(line)

			print(result)
			solve.append(result)

	print(sum(solve))




			

















	