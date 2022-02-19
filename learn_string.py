import re
import string


punctuation = '.,!?:;"`-()[]/\'\\'
some_str = "this is a test"
str_with_puctuation = "this() is a test?"
x = ['"abc"', 'def', '"ghi"', '"klm"', 'nop']


def replace_hyphens_with_spaces(obj: str) -> str:
    return '-'.join(obj.split())


def replace_punctuation_marks_with_spaces(obj: str) -> str:
    table = obj.maketrans(punctuation, ' '*len(punctuation))
    return obj.translate(table)


def remove_all_double_quotes(obj: list) -> list:
    lst = []
    for i in range(len(obj)):
        last_elem = obj.pop()
        if '"' in last_elem:
            new_str = last_elem.replace('"', '')
            lst.insert(0, new_str)
        else:
            lst.insert(0, last_elem)
    return lst


def modificate_moby_dick() -> None:

    pattern = r'[-.,:;?!—]'

    with open('MobyDick.txt', 'r') as infile, open('ModificateMobyDick.txt', 'w') as outfile:
        for row in infile:
            cleaned_row = re.sub(pattern, '', row).strip().lower()
            all_words = cleaned_row.split()
            for word in all_words:
                outfile.write(word + '\n')


# print(replace_hyphens_with_spaces(some_str)
# print(replace_punctuation_marks_with_spaces(str_with_puctuation))
# print(remove_all_double_quotes(x))

modificate_moby_dick()