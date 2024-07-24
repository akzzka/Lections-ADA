"================ 1 ================="
# hello = 'Hello'
# print(tuple(enumerate(hello)))

"================ 2 ================="
# list1 =  [-7, -2, 12, 32, 432, 23, 37, 11, 76, 0, -23, 45, -32, -56]
# list2 = list(filter(lambda a: a > 0, list1))
# print(list2)

"================ 3 ================="
# list1 = ["hello", 123]
# list2 = list(map(type,list1))
# print(list2)

"================ 4 ================="
# name_list = ["rauchel", "john", "peter", "jessica", "steven123", "dandy34", "kamest", "potter"]
# def func(name):
#     if len(name) > 5:
#         return f'Python {name}'
#     else:
#         return f'JavaScript {name}' 
# mylist = list(map(func, name_list))
# print(mylist)

# "================ 5 ================="
# email_list = ["123hello@gmail.com", "123", "hello"]
# def gmail_com(mail):
#     if mail.endswith('@gmail.com'):
#         return mail
#     else: return 'Not valid email'

# mylist = list(map(gmail_com,email_list))
# print(mylist)

"================ 6 ================="
from functools import reduce
list1 = ['a', 'n', 'n', 'a']
prav = list1[::-1]
otvet = reduce(lambda x, y: 'yes' if list1[:] == prav else 'no' , list1)
print(otvet)
