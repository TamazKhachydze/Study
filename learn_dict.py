table = {}


def get_value(row, col):
	return table.get((row, col), 'Cell not found')


def add_or_update_value(row, col, value):
	table.update({(row, col): value})


# add_or_update_value(0, 1, 'first')
# add_or_update_value(1, 1, 'second')
# add_or_update_value(0, 3, 'third')
# add_or_update_value(2, 1, 'fourth')
# print(table)
# add_or_update_value(1, 1, 'new_second')
# print(table)
# print(get_value(1, 1))
# print(get_value(1, 8))


def get_count_words():

	result = {}

	with open('ModificateMobyDick.txt', 'r') as file:
		for row in file:
			word = row.strip()
			result[word] = result.get(word, 0) + 1

	for key in result.keys():
		print(key, ' = ', result[key])


get_count_words()