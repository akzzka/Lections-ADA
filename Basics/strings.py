"===========Строки========="
# Строки это неизменяемый тип данных который предназначен для хранения текста,
# заключенного в одинарные или двойные ковычки
str_ = 'строка с одинарнымы ковычками'
str2 = "строка с двойными ковычками"
str3 = """
Многострочный текст в двойных кавычках, можно использовать 'любые' " кавычки"
"""
str4 = 'Don\'t'
str5 = "don't"

"==============Конкатенция==================="

name = "Акжол"
last_name = "Эргешов"
full_name = name + ' ' + last_name
print(full_name)
print ('Акжол' + ' ' + 'Эргешов')
print ("hello " * 10)

"===========Экранизация строк=============="

# \n = переносит на новую строку
print('hello\nworld')

# \t = табуляция
print('hello\tworld')

# \v = перенос на новую строку со смещением вправо на длину предыдущей строки
print('hello\vworld\vmy\vname\v')

# \r = перенос каретки на начало строки
print('hello\rHi')

# '\'' = отоброжение кавычки '
# "\"" = отоброжение кавычки "

"=============Форматирования строк==============="

title = 'Iphone 15'
price = 1000
print(f'Название: {title}\nЦена: {price}')

format2 = 'Название: {}\nцена:{}'
print(format2.format('Iphone 15', '1000'))

"==============Методы строк============="
# Методы - это функции, которые относятся к определенному классу(типу данных), к ним мы обращаемся чререз .

# print(dir(str)) # dir() = показывает все методы определенного типа данных(класса)

# .extend() # Rashirenie

string = 'hello'
print(string.upper()) # переводит все символы строки в верхний регистр

string1 = 'HeLLO'
print(string1.lower()) # переводит все символы в нижний регистр
 
print('heLLO'.swapcase()) # переводит все символы строки в противоположный регистр

print('hello world! i love'.title()) # переводит первую букву каждого слова в верхний регистр

print('hello world! i love'.capitalize()) # переводит только первую букву первого слова в верхний регистр,
# остальные слова остаются неизменным

print('hello'.center(11, '~')) # центрует нашу строку, по указаному ограничителю (1 значение - ограничение, 2 значение - разделение)

print('world'.count('w')) # возвращают количество вхождение заданного символа

print('hello'.startswith('h')) # проверяет начинается ли строка с заданного символа, возвращают True/False
print('Hello'.startswith('h')) # False

# .endswith() - проверяет заканчивается ли строка заданным символом/символами, возвращают True/False
print('hello'.endswith('lo')) # True
print('hello'.endswith('O')) # False
print('hello'.endswith('hello')) # True

# .islower() - проверяет находится ли строка полностью в нижнем регистре
print('hello world'.islower()) # True
print('hello woRld'.islower()) # False

# .isupper() - проверяет находится ли строка полностью в верхнем регистре
print('HELLO WORLD'.isupper()) # True
print('HeLLO WORLD'.isupper()) # False

# .isdigit() - проверяет состоит ли строка полностью из чисел
print('123423134'.isdigit()) # True
print('12342ывы3134'.isdigit()) # False

# .isalpha() - проверяет состоит ли строка полностью из букв
print('hello'.isalpha()) # True
print('hello312'.isalpha()) # False

# .isalnum() - проверяет состоит ли строка полностью из букв и чисел
print('hello312'.isalnum()) # True
print('hello'.isalnum()) # True
print('312'.isalnum()) # True

# .split() - возвращает список который разделил по заданному разделителю на отдельные строки
print('hello world my name is Ako'.split()) # ['hello', 'world', 'my', 'name', 'is', 'Ako']

# .join() - соединяет список по указанному разделителю
print('-'.join(['hello', 'world', 'my', 'name', 'is', 'Ako'])) #hello-world-my-name-is-Ako

# .strip() - убирает пробелы слева и справа
nadpis = '                         hello                  '
print(nadpis)
print(nadpis.strip())

nadpis1 = '    hello      '

# .lstrip() - убирает пробелы слева
print(nadpis1.lstrip())

# .rstrip() - убирает пробелы справа
print(nadpis1.rstrip())

"=============== Индексы ================="
# Индекс - порядковый номер в последовательности (символа в строке), (индексация начинается с нуля)
'h e l l o w o r l d' 
#0 1 2 3 4 5 6 7 8 9 
#             -3-2-1

slova1 = 'hello world'
print(slova1[10]) # d
print(slova1[0]) # h
print(slova1[-1]) # d

# срез - подстрока нашей строки
print(slova1[0:5]) # hello
print(slova1[0:4]) # hell
print(slova1[6:11]) # world
print(slova1[6:]) # world
print(slova1[6:-1]) # worl
# print(slova1[start:end:step])
print(slova1[::-1]) # dlrow olleh
print(slova1[::2]) # hlowrd
print(slova1[1:5:2]) # el

marka = input('Введите марку машин: ')
model = input('Введите модель машину: ')
god = input('Введите год выпуска машин: ')
# god = int(input('Введите год выпуска машин: '))
print(god.isdigit())
print ('Ваш выбор: '+marka.upper()+'|'+model.upper()+'|F90|'+god+'|черный|'.upper())
# if god <= int('2024'):
#     print(marka.upper(),model.center(15).upper(),god)
# else : 
#     print ('пожалуйста введите год выпуска машин правильно!'.title().center(70, '~'))
 
