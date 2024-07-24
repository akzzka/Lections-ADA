"================ Стройные функции ================"
# map, filter, reduce, zip, enumerate

# zip - соединает несколько последовательностей (получаем генератор, в котором элементы - tuple)

# list1 = [1,2,3,4,5]
# list2 = ['a', 'b ', 'c']
# list3 = [10.5, 20.6, 100.54]

# zipped = zip(list1, list2, list3)
# for el in zipped:
#     print(el)
#     # (1, 'a', 10.5)
#     # (2, 'b ', 20.6)
#     # (3, 'c', 100.54)

# list1 = [1, 2, 3, 4, 5]
# list2 = ['a','b','c','d','e']
# dict_ = dict(zip(list1,list2))
# print(dict_) # {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

"==================== Enumerate ==============="
#  enumerate - нумерует последовательность (ро дефолту с 0) (так же получаем генератор)

# enumerated = enumerate('hello')
# # print(enumerated) # <enumerate object at 0x104fb67c0>
# for el in enumerated:
#     print(el) 
#     #(0, 'h')
#     # (1, 'e')
#     # (2, 'l')
#     # (3, 'l')
#     # (4, 'o')

# string = 'hello world'
# print(list(enumerate(string[5:]))) #[(0, ' '), (1, 'w'), (2, 'o'), (3, 'r'), (4, 'l'), (5, 'd')]

"==================== Map ====================="
# map - принимает функцию и последовательность 
# (записывает в новую последовательность результат функции, в которую передаются элементы последовательности)

# list_ = ['1','2','3','4','5']
# mapped_list = list(map(int, list_))
# print(mapped_list) # [1, 2, 3, 4, 5]

# string = 'hello world'
# res = ''.join(map(lambda x: x.upper(), string))
# print(res) # HELLO WORLD

# list_ = [1, 2, 3, 4, 5]
# list2 = list(map(lambda x: x**2, list_))
# print(list2) # [1, 4, 9, 16, 25]

# list_ = [1, 2, 3, 4, 5]
# def to_2_degree(x):
#     return x ** 2
# print(list(map(to_2_degree, list_))) # [1, 4, 9, 16, 25]

"======================= Filter ====================="
#  filter - возвращает генератор, с элементами, с прошедшими филтр(какое-то условия), 
# принимает в себя функции. и последовательность

# list1 = [1, 0, -2, -3, -4, 5, 10]
# filtered =list(filter(lambda x: x > 0, list1))
# print(filtered) # [1, 5, 10]

# users = [ 
#     {'name': 'nikita', 'age': 12},
#     {'name': 'nastya', 'age': 20},
#     {'name': 'artem', 'age': 19}
# ]

# result = list(filter(lambda user: user['age'] > 18, users))
# print(result)

"Вывести только имена пользователей которые младше 15"

# filtired = list(filter(lambda user: user['age'] < 15, users))
# result = list(map(lambda x: x['name'], filtired))
# print(result)

'======================= Reduce ===================='
from functools import reduce
#  reduce - принимает функцию и последовательностью возвоащает 1 результат( передаваемая функция должна принимать 2 аргуменита)

# list_ = [1, 2, 3, 4, 5]
# res = reduce(lambda x, y: x*y,list_)
# print(res) # 120

# string = 'hello'
# res = reduce(lambda x, y: x + '@' + y, string)
# print(res)

# string = 'hello'
# print(reduce(lambda x, y: string.replace(x, y), string))

" выведите самое маленкое счтсло"
# list1 = [ 3, 4, 78, 345, 21, 4 ,54, 23]
# res = reduce(lambda x, y: x if x < y else y, list1)
# print(res)

"Выведите самого  младшего пользователя с помощю reduce"
# users = [ 
#     {'name': 'nikita', 'age': 12},
#     {'name': 'nastya', 'age': 20},
#     {'name': 'artem', 'age': 19}
# ]

# def min_dict(dict1, dict2):
#     if dict1['age'] < dict2['age']:
#         return dict1
#     return dict2
# res = reduce(min_dict, users)
# print(res)

# result = reduce(lambda x, y: x if x['age'] < y['age'] else y, users)
# print(result)

# 1) напишите программу, которая суммирует все элементы в списке используя какую то встроенную функция
from functools import reduce

# list1 = [1, 12000, 134, 12431, 43542]
# new_list = reduce(lambda x, y: x + y, list1)
# print(new_list)

# 2
# list1 = [1, 12000, 134, 12431, 43542]
# res = list(map(lambda x: x**2, list1))
# print(res)

# 3
# list1 = [1, 12000, 134, 12431, 43542]
# result = list(filter(lambda x: x%2 ==0,list1))
# print(result)

# 4
# list_ = ["inheritance", "solid", "polymorphism", "dry", "yagni"]
# res = list(filter(lambda word: len(word) > 7, list_))
# print(res)

# 5
# list1 = [1,2,3,4,5,6,7,8,9,10]
# list2 = len(list(filter(lambda x: x%2 != 0, list1)))
# list3 = len(list(filter(lambda x: x%2 == 0, list1)))
# result = f'четные: {list3}, нечетные: {list2}'
# print(result)

# 6
# list1 = ["Paul", "George", "Ringo", "John"]
# res = reduce(lambda x,y: x if len(x) > len(y) else y, list1)
# print(res)

# 7
# res = list(map(lambda x: 'Fizz' if x % 3 == 0 else 'Buzz', range(1,51)))
# print(res)

# 8
# list1 = [1, 2, 3, 4, 234, 534, 123, -123, 342, 654]
# res = reduce(lambda x ,y: x if x < y else y, list1)
# print(res)
