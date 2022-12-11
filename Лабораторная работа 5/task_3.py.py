
     # TODO написать функцию для получения списка уникальных целых чисел

from random import randint


numbers1 = [20, 20, 30, 30, 40]
numbers = [randint(-10, 10) for i in range(15)]

def get_unique_numbers(numbers):
    unique = []

    while len(unique) < 15:
     a = randint(-10, 10)
     if a not in unique:
            unique.append(a)
    return unique

print(get_unique_numbers(numbers))






