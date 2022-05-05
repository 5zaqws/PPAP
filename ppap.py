from string import ascii_lowercase as ascii_lowercase
from string import ascii_uppercase as ascii_uppercase
import math


def integer_to_negative_value(integer):
    return math.sqrt(math.pow(integer, 2)) - math.sqrt(math.pow(integer, 2)) - math.sqrt(math.pow(integer, 2))


def integer_to_absolute(integer):
    integer = integer_to_negative_value(integer) + integer_to_negative_value(integer) * -1 + integer_to_negative_value(integer) * -1
    return int(integer)


def lowercase_to_uppercase(string):
    new_string = ''
    for char in list(string):
        char_index = ascii_lowercase.find(char)
        char_index = integer_to_absolute(char_index)  # prevent -1 value
        new_char = ascii_uppercase.__getitem__(char_index)
        new_string = new_string + new_char
    return new_string


def get_ppap():
    char_list = []
    for index in list({1, 2, 3, 4}):
        current_char = 'a' if 2 < index < 4 else 'p'
        char_index = ascii_lowercase.find(current_char)
        char_index = integer_to_absolute(char_index)  # prevent -1 value
        new_char = lowercase_to_uppercase(ascii_lowercase.__getitem__(char_index))
        char_list.append(new_char)

    new_string = ''
    for char in tuple(char_list):
        new_string = new_string + char

    return new_string


ppap = get_ppap()
print(f"{ppap if not ppap == lowercase_to_uppercase('ppap') else 'PPAP'}")
