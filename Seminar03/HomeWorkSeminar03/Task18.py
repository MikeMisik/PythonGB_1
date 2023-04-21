# Задача 18: 
# Требуется найти в массиве A[1..N] 
# самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит 
# натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random   
c = int(input("Введите длину массива: "))
d = [] 
for i in range(c): 
    temp = random.randint(0, 9)
    d.append(temp)
print(d)
e = int(input("Введите число: "))
g_1 = abs(d[0] - e) 
temp_1 = d[0]
dif = 0
for i in range(len(d)):
    if d[i] == e:
        temp_1 = d[i] 
        break           
    if d[i] < e:
        dif = e - d[i]
    if d[i] > e:
        dif = d[i] - e
    if dif < g_1:
        g_1 = dif
        temp_1 = d[i]
print(temp_1)
