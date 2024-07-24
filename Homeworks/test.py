a = "Акжол2hgv00jh0 ahs"
# print(a[5])
# print(type(a[5]))
# b = int(a[5])
# print(b,type(b))

number = ''
for sim in a:
    # print (sim)
    if sim.isdigit():
        print(sim)
        number = number + sim


print(number, type(number))
number = int(number)
print(number, type(number))

a = "Акжол2hgv00jh0 ahs"
number = ''.join([sim for sim in a if sim.isdigit()])
print(number)
text = 'asadsadas frf gtgrg fg3rg'
print(text.split())
print('_'.join(['hello', 'world', 'my', 'name', 'is', 'Ako'])) 


def my_num(numbers_amount):
    numbers = set()
    for i in range(numbers_amount):
        number = int(input('Введите число: '))
        numbers.add(number)
    print(numbers)
    num_list = list(numbers)
    min_num = num_list[0]
    for num in num_list:
        if num < min_num:
            min_num = number
    print(min_num)
    # min_num = min(numbers)
    # print(min_num)
    
sayi = int(input('Сколько чисел хотите ввести?:'))

my_num(sayi)


# numbers = [10,2,3,8,5,56,34]
# min_num = numbers[0]
# for number in numbers:
#     if number < min_num:
#         min_num = number
# print(min_num)