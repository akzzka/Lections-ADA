"============== Модули и пакеты ==============="
# любой файл с расширением .ру - модуль 
# пакеты - набор модулей(обезятельно должен быть файл _int_.py)

"=============== Работа с файлами ============="
#  open() - функция, котороя открывает файл в определенном режиме
'Режимы'
# r - read (только для чтения)
# w - write (только для записи, если такого файла нет, то он его создаст. Каждый раз файл очищается)
# a - append (только для записи, данные добавляется в конец)
# x - создает файл, но если файл есть выйдет ошибка
# b - binary (в бинарном виде)

"=================== Read ====================="
# file = open('test.txt', 'r')
# print(dir(file))
# print(file.writable()) # False (проверяет можно ли записать в файл)
# print(file.readable()) # True (можно ли читать файл)
# print(file.read())

# print(file.read())
# file.seek(0)
# print(file.read(50))
# print(file.read(3))

# file.seek(0)
# print(file.readline()) # hello (читает одну строку)
# print(file.readline())

# file.seek(0)
# print(file.readlines()) #['hello\n', 'world\n', 'komstkombvkerm\n', 'cwe;c,vwvw12\n', '2000']

# file.close()

"===================== Write =================="
# file = open('test2.txt', 'w')
# Если такого файла нет, то он его создаст
# print(file.readable()) # False
# print(file.writable()) # True

# file2 = open('test.txt', 'w')
# стирает данные существующего если они там есть
# file.write('hello\n') # zpis v fail
# file.writelines('hello, world\n ') # zapis v strok

# file.close()

"=================== Append ====================="
# file = open('test3.txt', 'a')
# print(file.readable()) # False
# file.write('hello')
# file.writelines(['hello', 'hello', 'world'])
# file.close()

"================== контекстный менеджер =============="
# with ... as...  # Автоматически закрывает файл

# try:
#     file = open('sdacaasa', 'w')
#     file.read()
# finally:
#     file.close

# with open('test3.txt', 'r') as file:
#     print(file.read()) # hellohellohellohellohellohelloworld
