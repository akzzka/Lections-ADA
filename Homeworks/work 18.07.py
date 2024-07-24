"================ 1 ================"
# def found_num():
#     numbers = set()
#     for i in range(5):
#         number = int(input('Введите число: '))
#         numbers.add(number)
#     print(numbers)
#     my_num = list(numbers)
#     min_num = my_num[0]
#     for num in my_num:
#         if num < min_num:
#             min_num = num
#     print('Маленькое число:',min_num)

# found_num()

"================ 2 ================"
# def credit():
#     while True:
#         amount = float(input('Желаемое сумма займа: '))
#         if amount >= 100000:
#             total1 = amount * (7.89/100)
#             total = total1 + amount
#             print('Наша ставка: 7,89%')
#             print(f'Вы вернете нам: {total:.2f}')
#             break
#         else: 
#             print('Пожалуйста введите сумму от 100 000!')

# credit()

"================ 3 ================"
# def number():
#     name = input('Введите имя и возраст: ')
#     num = ''.join(num for num in name if num.isdigit())      
#     print(num)
# number()

"================ 4 ================"
# def days(month,year):
#     month *= year
#     day = month * 30
#     print(day)
# days(month = int(input('Введите количество месяцев: ')), year=int(input('Введите количество лет: ')))

"================ 5 ================"
# def slovar():
#     dict1 = {i:i ** 3 for i in range(1,11)}
#     print(dict1)
# slovar()

"================ 6 ================"
# def res():
#     summa = 0
#     for i in range(1,51):
#         summa += i
#     print(summa)
# res()

"================ 7 ================"
# def add(num1=int, num2=int):
#     result = num1 + num2
#     print(result)
# add(int(input('Введите 1 число: ')),int(input('Введите 2 число: ')))

"================ 8 ================"
# def get_string_length(str1):
#     len1 = len(str1)
#     print('Длина вашего строка:',len1)
# get_string_length(input('Введите: '))

"================ 9 ================"
# def get_type(a,b):
#     print('Тип данных первого:',type(a))
#     print('Тип данных второго:',type(b))

# a = 123
# b = 'qwwerty'
# get_type(a,b)

"================ 10 ================"
# def check(num):
#     if num % 2 == 0:
#         print('It is even number')
#     else: print('It is odd number')

# check(int(input('Введите число: ')))


"================ 11 ================"
# def is_palindrome(string):
#     string = string.lower()
#     str1 = string[0:len(string)] 
#     str2 = string[::-1]
#     if str1 == str2:
#         print(True)
#     else:
#         print(False)

# is_palindrome(input('Введите лобое слово:'))

"================ 12 ================"
# def max_num(num1,num2):
#     if num1>num2: print(num1)
#     elif num1<num2: print(num2)
#     else: print('Оба числа равны')

# max_num(int(input('Введите 1 число:')),int(input('Введите 2 число:')))

"================ 13 ================"
# def multiply_list(rep):
#     mylist = []
#     for i in range(rep):  
#         a = i + 1
#         n = int(input(f'Введите {a} число: '))
#         mylist.append(n)
#     print(mylist)
#     mylist = [i for i in mylist]
#     number = 1 
#     for num in mylist:
#         number = number * num
#     print(number)

# multiply_list(int(input('Cколько чисел хотите ввести?:')))
"================ 14 ================"
# def sum_digits(num):
#     list1 = [int(i) for i in num]
#     print(list1)
#     number = 0
#     for i in list1:
#         number = number + i
#     print(number)
# sum_digits(input('Введите одно целое число:'))

"================ 15 ================"
def func15(stroka):
    mydict = {i:stroka.count(i) for i in stroka}
    print(mydict)

func15(input('введите: '))

"============ Enumerate =============="
# names = ['asas', 'wad', 'efa', 'kok']
# for i, el in enumerate(names):
#     print(i, el)


