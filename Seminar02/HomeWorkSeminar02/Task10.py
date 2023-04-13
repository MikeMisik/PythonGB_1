# Задача 10: На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть



import random

n = int(input("Введите кол-во монеток: "))
coins = [] 
for i in range(n): 
    coin_type = random.randint(0, 1)
    coins.append(coin_type)
print(coins)

heads = tails = 0
for j in coins:
    if j > 0:
        heads += 1
    else:
        tails += 1
if heads < tails:
    print(heads)
else:
    print(tails)        
