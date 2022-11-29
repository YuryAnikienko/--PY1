list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]


max_index = 0
max_value = list_numbers[0]

for i in range (1, len(list_numbers)):
     if list_numbers[i] >= max_value:
         max_value = list_numbers[i]
         max_index = i

list_numbers[max_index], list_numbers[len(list_numbers)-1] = list_numbers[len(list_numbers)-1], list_numbers[max_index]

print(list_numbers)

# TODO Оформить решение

 # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
