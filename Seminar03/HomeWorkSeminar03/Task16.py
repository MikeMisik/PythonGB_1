# Задача 16: 
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – 
# # количество элементов в массиве. 
# # В последующих  строках записаны N целых чисел Ai. 
# # Последняя строка содержит число X
# # *Пример:*
# # 5
# #     1 2 3 4 5
# #     3
# #     -> 1

import random   
a = int(input("Введите длину массива: "))
l = [] 
for i in range(a): 
    temp1 = random.randint(0, 9)
    l.append(temp1)
print(l)
b = int(input("Введите число: "))
count = 0
for i in range(len(l)): 
    if l[i] == b:
        count += 1
print(count)