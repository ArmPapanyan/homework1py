
# Вводятся числа, пока не введут 0. Найти произведение чисел, оканчивающихся на 4.


# mult = 1
# number = int(input())
# while number != 0:
#     if number % 10 == 4:
#         mult *= number
#     number = int(input())
# if mult == 1:
#     mult = 0
# print(mult)


# Вводятся строки, пока не будет введена пустая строка. Если длина очередного введеного слова равна 5, то
# нужно вывести сообщение "YES" и прекратить возможность ввода для пользователя, если таких слов нет, то
# вывести 'NO' один раз в конце.

#1 tarberak
# flag = True
# while True:
#     some_str = input()
#     # if some_str == '':
#     #     break
#     if not some_str:
#         break
#     if len(some_str) == 5:
#         print('YES')
#         flag = False
#         break
# if flag:
#     print('NO')

#2,tarberak

# some_str = input()
# while some_str:
#     if len(some_str) == 5:
#         print('YES')
#         break
#     some_str = input()
# else:
#     print('NO')




# Переменная итератор используется внутри цикла.

# for i in 'hello':
#     print(i)

# for j in 1, 2, 3, 4, 5, 6, 7, 8, 9, 10:
#     print(j ** 2)

# range()
# for number in range(1, 11):  # 1, 2, 3, 4...
#     print(number)
#
# for number in range(5):
#     print(number)
#
# for number in range(2, 101, 2):
#     print(number)

# for number in range(10, 1, -2):
#     print(number)



# Переменная итератор используется внутри цикла.

# for i in 'hello':
#     print(i)

# for j in 1, 2, 3, 4, 5, 6, 7, 8, 9, 10:
#     print(j ** 2)

# range()
# for number in range(1, 11):  # 1, 2, 3, 4...
#     print(number)
#
# for number in range(5):
#     print(number)
#
# for number in range(2, 101, 2):
#     print(number, end=' ')

# for number in range(10, 1, -2):
#     print(number)


# Переменная итератор не используется внутри цикла.
# 100 раз вывести слово hello в консоль

# i = 1
# while i <= 100:
#     print('Hello')
#     i += 1

# for _ in range(100):  # 0, 1, 2, 3, 4, 5, 6, 7, 8...99
#     print('Hello')



# Вводится количество чисел, затем сами числа, если число = 10, вывести YES и закончить ввод,
# в конце вывести NO если никакое из чисел не было равно 10.
# n = int(input('Введите кол-во чисел: '))
# for _ in range(n):
#     number = int(input())
#     if number == 10:
#         print('YES')
#         break
# else:
#     print('NO')


# Строки
# some_str = 'hello world'
# print(len(some_str))
# print(some_str[-1])
# print(some_str[::-1])
# print(some_str)
# #
# for letter in some_str:
# print(letter)
#
# for ind in range(0, len(some_str)):
# print(ind)
#
# print(some_str.index('h'))

# some_str[1] = 'l'
# print(some_str)

# spiski
# some_list = [1, 'g', True, 1213.2121, [1, 2, 3], True]
# print(some_list[0:])
# some_list[0] = 2
# print(some_list)
# some_list.append(10)
# print(some_list)
# some_list.insert(2, False)
# print(some_list)
# some_list.pop(-1)
# print(some_list)
# # some_list.remove(True)
# # print(some_list)
# for element in some_list:
# if element == True:
# some_list.remove(True)
# print(some_list)

# n = int(input('КВведите кол-во элементов: '))
# some_list = []
# for _ in range(n):
# some_list.append(int(input()))
# print(some_list)

# some_list = [1, 2, 3, 4, 5, 6]
#
# for element in some_list:
# print(element)
#
# count = 0
# for ind in range(1, len(some_list)):
# if some_list[ind] > some_list[ind



# import random
# import time
# 
# some_set = set()
# for _ in range(10 ** 6):
#     some_set.add(random.randint(100, 1100))
# some_list = list(some_set)
# 
# start = time.perf_counter()
# print(99 in some_list)
# end = time.perf_counter()
# first_duration = end - start
# 
# start = time.perf_counter()
# print(99 in some_set)
# end = time.perf_counter()
# second_duration = end - start
# print(first_duration / second_duration)