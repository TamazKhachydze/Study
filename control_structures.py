import string


lst = [1, 4, 2, 67, -2, -1, 0, -6]


def remove_negative_numbers(obj: list) -> list:
    return list(i for i in obj if i > 0)


def get_unpaired_numbers():
    return (i for i in range(100) if i % 2 == 1)


def create_dictionary():
    return {i: i**3 for i in range(11, 16)}


def get_count_row_word_symbol():

    rows, words, symbols = 0, 0, 0
    with open('example.txt') as file:
        for line in file:
            print(line)
            rows += 1
            symbols += len(line)
            words += len(line.split())
    print(f"count row = {rows}, count word = {words}, count symbol = {symbols}")


# print(remove_negative_numbers(lst))
# for i in get_unpaired_numbers():
#     print(i)
# print(create_dictionary())
# get_count_row_word_symbol()