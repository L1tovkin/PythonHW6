# list comprehension

# Задайте список из n чисел последовательности (1 + 1/n)^n. Вывести в консоль сам список и сумму его элементов.

# n = int(input('Введите список из n чисел: '))
# my_list = [round((1+1/i)**i, 2) for i in range(1, n+1)]
# print(f'Список -> {my_list}\nСумма его элементов -> {round(sum(my_list), 2)}')

# map

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов. (подробности в конце записи семинара).
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# my_list = list(map(float, input("Введите числа через пробел:\n").split()))
# new_list = [round(i % 1, 2) for i in my_list if i % 1 != 0]
# print(max(new_list) - min(new_list))

# lambda

# Написать программу, которая будет ввыводит в консоль заданный текст (Python - один из самых популярных языков программирования в мире), затем принимать из консоли шаблон подстроки и удалять в задданом тексте все слова в которых присутствует введенный шаблон

# text = input("Введите текст: ")
# text_sub = input("Введите подстроку для удаления: ")

# words_text = text.split()
# result = ' '.join((filter(lambda s: text_sub not in s, words_text)))
# print("Отфильтрованная строка:", result)