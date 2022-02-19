lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lst_1 = [[1, 2, 3], [2, 1, 3], [4, 0, 1]]


def get_second_half(obj: list):
    return obj[len(obj) // 2:]


def move_last_three_elements_in_beginning(obj: list):
    return obj[-3:] + obj[:-3]


def sort_by_second_inner_element(obj: list):
    obj.sort(key=lambda x: x[1])
    return obj


def safe_remove_element(obj: list, elem):
    if elem in obj:
        obj.remove(elem)


# print(get_second_half(lst))
# print(move_last_three_elements_in_beginning(lst))
# print(sort_by_second_inner_element(lst_1))
# safe_remove_element(lst, 5)
# print(lst)