# TODO решить с помощью list comprehension и распечатать его

from pprint import pprint

def get_count_char(list_):

    return[{
           "bin": bin(i),
           "dec": list1[i],
           "hex": hex(i),
           "oct": oct(i)} for i in list1]

list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

pprint(get_count_char(list1))



