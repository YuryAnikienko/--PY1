def delete(list_, index=None):
      # TODO реализовать функцию удаления элемента из списка по индексу

     if index == 0:
        new_list_2 = list_[list_[0] + 1:]
        new_list_3 = new_list_2
     elif index == len(list_):
        new_list_3 = list_[:len(list_)]

     elif index == None:
           new_list_1 = list_[:len(list_)-1]
           new_list_3 = new_list_1

     else:
         new_list_1 = list_[:index]
         new_list_2 = list_[index + 1:]
         new_list_3 = new_list_1 + new_list_2

     return new_list_3

print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]

