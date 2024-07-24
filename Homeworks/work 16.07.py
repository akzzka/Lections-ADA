# ================ 1 ===============
# list = [False, True, False, True, False, True, False, True, False, True] 
# m_list = [1 if i == True else 0 for i in list]
# print(m_list)

# ================ 2 ===============
# list_name = ["paul", "john", "george", "ringo", "eric", "patty", "yoko", "cynthia", "linda", "jude"]
# list1 = [len(i) for i in list_name]
# print(list1)

# ================ 3 ===============
# list2 = [i for i in range(1, 1001, 125) if i % 2 == 0]
# print(list2)

# ================ 4 ===============
# list1 = [44, 54, 64, 74, 104]
# MyList = [i+6 for i in list1]
# print(MyList)

# ================ 5 ===============
# list1 = [2, 4, 6, 8, 10, 12, 14]
# mlist = [ i ** 2 for i in list1 if i ** 2 > 50]
# print(mlist)

# ================ 6 ===============
# dict = {"a": {"d": 3, "e": 45}, "b": {"f": 23, "j": 9}, "c": {"h": 12, "i": 89}}
# list_ = [[ i for i in j.values() ] for j in dict.values()]
# print(list_)

# ================ 7 ===============
# dict_ = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# list2 = [ i for i in int(dict_.values()) < 5000 ]
# print(list2)

# ================ 8 ===============
list1 = [1, 2, 3, 0, None, "a", "abc", [], 23, [1, 2, 3, 4], "", {"a": 1, "b": 2}, "drf", []]
list3 = [i for i in list1 if i != None ]
print(list3)
