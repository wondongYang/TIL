from abc import abstractmethod


# Instance Method

# print(dir(str))
str_a = 'abcde'
print(str_a.upper()) #=> ABCDE

# print(dir(list))
list_a = [1, 2, 3, 4, 5, 2, 2, 2]
print(list_a.count(2)) #=> 4

# print(dir(dict))
dict_a = {'1':2, '2':3, '3':4}
print(dict_a.get('1')) #=> 2