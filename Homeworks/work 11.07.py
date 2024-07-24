"========================= 1 ============================"
# d1 = {"a": 100, "b": 200, "c":300}
# d2 = {"a": 300, "b": 200, "d":400}
# print(d1["b"] == d2["b"])
"========================= 2 ============================"
# person = {"name": "Kelly" , "age": 25, "city": "New york"}
# print(person["age"])

"========================= 3 ============================"
# sample_set = {"Yellow", "Orange", "Black"}
# sample_list = ["Blue", "Green", "Red"]
# result = sample_set.union(sample_list)
# print(result)

"========================= 4 ============================"
# set1 = {6, 4, 2, 5, 7, 8, 10, 9}
# set1.discard(7)
# print(set1)

"========================= 5 ============================"
# set2 = {'Python', 'it', 'c++', 'java', 'programming'}
# set3 = {'html', 'css', 'c++', 'java', 'dart', 'programming'}
# print(set3 & set2)
# print(set2.intersection(set3))

"========================= 6 ============================"
# set2 = {'Python', 'it', 'c++', 'java', 'programming'}
# set3 = {'html', 'css', 'c++', 'java', 'dart', 'programming'}
# print(set3.difference(set2))

"========================= 7 ============================"
# set_ = {6, 2, 3, 4, 5}
# set_.add(6)
# pops = set_.pop()
# print(set_, pops)

"========================= 8 ============================"
# menu = {'manty': 200, 'plov': 150, 'lagman': 130, 'borsh': 100}
# menu ['besh_barmak'] = 130
# menu ["lagman"] = 135
# print(menu)

"========================= 9 ============================"
# menu = {'manty': 200, 'plov': 150, 'lagman': 130, 'borsh': 100}
# menu ['drinks'] = 'Coco-Cola', 'Sprite', 'Fanta'
# print(menu)

"========================= 10 ============================"
# print(dir(set))
# print(dir(dict))
# set1 = {'__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', 
#         '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', 
#         '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', 
#         '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', 
#         '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', 
#         '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 
#         'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 
#         'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'}

# set2 = {'__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', 
#         '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', 
#         '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__',
#         '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', 
#         '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 
#         'pop', 'popitem', 'setdefault', 'update', 'values'}
# print(set1.intersection(set2))

"========================= 12 ============================"
suitcase = []
suitcase.append('бейсболка')
suitcase.append('шорты')
suitcase.append('футболка')
suitcase.append('очки')
suitcase.append('пaнама')
print(suitcase)

suitcase.pop(4)

print(suitcase)

