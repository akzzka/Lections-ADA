'===================== Области видимости ===================='
# LEGB - Local Enclosed Global Built - in

"=============== Built - in =================="
#  Встроенное пространство имен (list, sum, dict, print input)

"================== Global ===================="
# Все переменные которые мы создали внутри одного файла
# чтобы посмотреть все глобальные переменные, можно использовать globals()

a = 5
b = ' hello'
# print(globals())

"================== Local ======================"

# Локальное пространство имен - переменные. созданные внутри функции locals()

# a = 10
# def func(a, b):
#     print('GLOBALS', globals())
#     print('LOCALS', locals())
#     print(a ,b)

# func(5, 7)

'================== Enclosed ================='
# Замкнутая пространство имен - локальные пространство, у которго есть внутреннее локальное пространство

# var = 'global'

# def func():
#     # Локальное пространство для глобального пространства
#     # замкнутое пространство(потому что есть более локальное пространство)
#     var = 'enclosed'
#     def innner_func():
#         # локальное пространство для пространства func
#         var = 'local'
#         print(var) # 3) local
#     print(var) # 2) enclosed
#     innner_func()
# print(var) # 1) global
# func()

# a = 'hello'

# def abc():
#     a = 123
# print(abc)
# print(a)

# count = 1
# def increasr_count():
#     global count
#     print(count)
#     count += 1

# increasr_count()
# increasr_count()
# increasr_count()
# increasr_count()
# increasr_count()

# def count(i):
#     counter = 0

#     def increase_counter():
#         nonlocal counter
#         # доступ на изменение переменной закнутого пространства
#         print(counter)
#         counter += 1
#     for _ in range(i):
#         increase_counter()
# count(10)


def res():
    for i in range(1,51):
        result = i * (i + 1) // 2
    print(result)

res()