"============= 1 ==============="
# numbers = [i for i in range(1,101)]
# print(numbers)

"============= 2 ==============="
# list1 = [i for i in range(2, 51, 2) ]
# print(list1)

"============= 3 ==============="
# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list = [num for num in list_ if num > 0 ]
# print(int_list)

"============= 4 ==============="
# list2 = [i ** 2 for i in range(1, 26)]
# print(list2)

"============= 5 ==============="
# str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'] 
# list_ = [int(num) for num in str_list ]
# print(list_)

"============= 6 ==============="
# list3 =[i ** 2 if i % 2 == 0 else i for i in range(1 ,11)  ]
# print(list3)

"============= 7 ==============="
# list4 = [True if i % 2 == 0 else False for i in range(1, 11)]
# print(list4)

"============= 8 ==============="
# list_name = ["paul", "john", "george", "ringo", "eric", "patty", "yoko", "cynthia", "linda", "jude" ]
# list5 = ['shorter' if len(name) < 5 else 'longer' for name in list_name]
# print(list5)
"============= 9 ==============="
# dict1 = {key: key ** 2 for key in range(1, 11)}
# print(dict1)

"============= 10 ==============="
n = int(input("Введите число: "))
dict2 = {i: i * i for i in range(1 ,501) if i % n == 0}
print(dict2)
