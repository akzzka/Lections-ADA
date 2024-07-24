"=============== JSON =================="
# JavaScript object notation - Универсальный формвт, в которои мы можем хранить данные в типах данных, 
# понятных почти для всех языков программирование
import json
json_list = '[1,2,3,4,5]'
print(type(json_list))  # <class 'str'>

python_list = json.loads(json_list)
print(type(python_list))

# Десериализация - перевод с JSON строки в PYTHON объекты
#  .loads() - метод для десериализации с json строки
# .load() - метод для десериализации с json файла

# сериализация - перевод python объектов в json строки
# .dumps() - медот для сериализация в json строку 
# .dump() - медот для сериализация в json файла

with open('test.json') as file:
    list_ = json.load(file)
print(list_)
list_.append((1,2,3))
print(list_)
# list_.append((1,2,3))
# list_.append((1,2,3))
# print(list_)

with open('test.json','w') as file:
    list_ = json.dump(list_,file)
