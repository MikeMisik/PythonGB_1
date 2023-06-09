# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, 
# насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в 
# каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, 
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если 
# с ритмом все не в порядке
# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам





poem = input("Введите стихотворение: ")


def count_vowels(word):
    vowels = "уеыаоэяию"
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count


phrases = poem.split()


vowels_count = []

for phrase in phrases:
    words = phrase.split("-")
    phrase_vowels_count = 0
    for word in words:
        phrase_vowels_count += count_vowels(word)
    vowels_count.append(phrase_vowels_count)


if vowels_count.count(vowels_count[0]) == len(vowels_count):
    print("Парам пам-пам")
else:
    print("Пам парам") 