"============ 1 =============="
# file = open('myfile.txt', 'r')
# # print(file.read())
# file.close()
"============ 2 =============="
# login = input('Введите логин:')
# password = input('Введите пароль:')
# with open ('users.txt', 'a') as file:
#     file.write(f'\nLogin: {login} \nParol: {password}')

"============ 3 =============="
# with open('myfile.txt', 'r') as file:
#     content = file.read()
# if 'w' in content:
#     print('DA est "w"')
# else:
#     print('Net "w"')

"============ 4 =============="
# text = """Next, install the Python 3 interpreter on your computer. This is the program that reads Python programs and carries out their instructions;
# you need it before you can do any Python programming. Mac and Linux distributions may include an outdated version of Python (Python 2),
# but you should install an updated one (Python 3). See BeginnersGuide/Download for instructions to download the correct version of Python."""

# with open('python.txt', 'w') as file:
#     file.write(text)
# with open('python.txt', 'r') as file:
#     content = file.read()
# o_words = [word for word in content.split() if 'o' in word]
# print(o_words)

"============ 5 =============="

# text = """
# .detacilpmoc naht retteb si xelpmoC
# .xelpmoc naht retteb si elpmiS
# .ticilpmi naht retteb si ticilpxE
# .ylgu naht retteb si lufituaeB"""

# with open('task5.txt','w') as file:
#     file.write(text)
# with open('task5.txt','r') as file:
#     content = file.read()
#     reversed_content = content[::-1]
#     print(reversed_content)

"============ 6 =============="
text = """123
aaa456
fxdya 5 0 0"""

with open('task6.txt', 'w') as file:
    file.write(text)
total_sum = 0
with open('task6.txt', 'r') as file:
    for line in file:
        for word in line.split():
            number = ''.join(filter(str.isdigit,word))
            if number:
                total_sum += int(number)
print(f'Сумма чисел: {total_sum}')

import csv
