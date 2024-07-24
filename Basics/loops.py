"========== Циклы ============"
# Цикл - это блок когда, который отрабатывает несколько раз
# for - цикл, который работает с итерируемым объектом. Цикл заканчивает работу, 
# когда он доходит до последнего элемента итерируемого объекта
# while - цикл, который работает до тех пор, пока условие верное


list_ = ['hello world', 1,2,3,30, None, False, True, [1,2,3]]

# for elemnt in list_:
#     print (elemnt)

#     for letter in 'hello world':
#         print (letter)

# n = 1
# while n <= 10 :
#     print(n)
#     # n = n + 1
#     n += 1        

# n = 0
# while n :
#     print(n) # не запустится, потому что 0 - False

# while list_:
#     print('hello')
#     if list_:
#         print('1')

"===================== Операторы break/continue ================"        
#  break - полностью прерывает работу цикла (выйти из цикла)
# continue - пропускает 1 итерацию, и переходит к следющей

# for i in range(10):
#     if i == 3:
#         continue
#     print(i)
#     # 0 1 2 4 5 6 7 8 9


# for i in range(10): 
#     print(i)
#     if i == 3:
#         continue
#     # 0 1 2 3 4 5 6 7 8 9

# for i in range(10):
#     print(i)
#     break
#     #  0

# for i in range(10):
#     print(i)
#     if i == 3:
#         break
#     # 0 1 2 3 
   
# for i in range(10):
#     if i == 3:
#         break
#     print(i)   
#     # 0 1 2

# for i in range(10):
#     if i < 3:
#         continue
#     print(i)
#     # 3 4 5 6  7 8 9

list1 = [1,1,1,1,2,3,4,5,1,59,1,1]
new_list = []
for num in list1:
    # if num == 1:
    #     continue
    # new_list.append(num)
    if num != 1:
        new_list.append(num)
print(new_list)
# # 2 3 4 5 59

# list1 = [1,1,1,1,2,3,4,5,1,59,1,1]
# while 1 in list1:
#     list1.remove(1)
# print(list1)

# for i in range(10):
#     for j in range(10):
#         print(i ,j)
#         # два цикла


