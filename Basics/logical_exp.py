"====Логические операторы======="
# Логические операторы - выражение, коиорые возвращают True, если выражение верное,
# False - если выражение не верное

"==Равенство==="
5 == 5 # сравнение, в данном выражении вернется True
# name = 5 - оператор присвания
2 == 5 # False

"====Не равенство======"
4 != 5 # True
5 != 5 # False

"====Больше===="
4 > 4 # False
10 > 5 # True

"=====Меньше====="
1 < 4 # True
10 < 5 # False

"=====Больше или равно====="
10 >= 4 # True
4 >= 4 # True
1 > 10 # False

"=======Меньше или равно======="
10 <= 20 # True
10 <= 10 # True
20 <= 10 # False

print('s' == 5)
print('hello' == 'hello')

"===== and, or, not ====="
# and - и, Возвращают True если оба условия верны, False если одно из них неверно
# or - или, Вернет True, если хоть одно условие верно, False если оба условия неверны
# not - не, 

a = 5
b = 3


print(a == b and a > b) # False
print(a == b or a > b) # True

print(not True) # False
print( not False) # True

print(not a == 5)

"====== Boolean Type ======="

print(bool(1)) # True
print(bool(0)) # False
print(bool(-12)) # True

print(bool('hello')) # True
print(bool(' ')) # True
print(bool('')) # False

"===== is ======"
a = 5
b = 5 
print(a == b) # True
print(a is b) # True

"=========== NoneType ========"
# None - неизменяемый тип данных с одним значением None, который используется для 
# обозначения отсуствия значения

print(bool(None)) # False
print(bool('None')) # True

