# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8


# def degree_number(c,d):
#     if d == 0:
#         return 1
#     return c * degree_number(c , d-1)

# a = int(input("input number A ="))
# b = int(input("input number B ="))
# print(f"A = {a}; B = {b} -> {degree_number(a , b)} {{a}} в степени {b}")

# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4

# def sum(c,d):
#     if d == 0:
#      return c
#     return 1 + sum (c , d-1)

# a = int(input("input number a ="))
# b = int(input("input number b ="))
# print(f"{a} +{b} = {sum(a ,b)}")


# Задача No41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится число N — количество элементов в массиве Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.
# Ввод:        Ввод:
# 5             5
# 1 2 3 4 5    1 5  1 5 1
# Вывод:        Вывод:
# 0              2

# number = int(input('input number '))
# list = []
# for _ in range(number):
#     list.append(int(input()))
#     count = 0
#     for i in range(1 , len(list) -1):
#         if list[i+1] < list[i] > list[i-1]:
#             count += 1
# print( list ,count)


# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод:        Вывод:
# 300          220 284



# n = 300
# list_1 = list()
# for i in range(n):
#     summa = 0
#     for j in range(1, i // 2 + 1):
#         if i % j == 0:
#            summa += j
# list_1.append(tuple([i, summa]))
# print(list_1)


# k = 300

# list =[]

# for i in range (k):
#     summa = 0
#     for j in range(1, i // 2 + 1):
#         if i % j == 0 and i != j:
#             summa += j
#     list.append(summa)
# print(list)

