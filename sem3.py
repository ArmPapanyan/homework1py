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



# Задача 1. Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# n = int(input('input count digit'))
# some_list = []
# for _ in range(n):
#     some_list.append(int(input()))
# print(some_list)
# count = 0
# i = 0
# for i in range(len(some_list)):
#     if some_list[i] != some_list[i-1]:
#       count += 1
# print(count)

#2 primer
# n = int(input('КВведите кол-во элементов: '))
# some_list = []
# for _ in range(n):
#   some_list.append(int(input()))
# print(some_list)
# new_list = []
# for elem in some_list:
#     if elem not in new_list:
#         new_list.append(elem)
# print(len(new_list))







# Задача 2. Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]


# n = int(input('input digit'))
# some_list = []
# for _ in range(n):
#     some_list.append(int(input()))
# print(some_list)

# k = int(input('input k: '))

# for i in range(k-1):
#     some_list.insert(0,some_list[-1])
#     some_list.pop(-1)
# print(some_list)



# Задача 3. Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

# n = int(input('input digit'))
# list = []
# for _ in range(n):
#     list.append(input(''))
# print(list)

# count =0
# i = 0
# for i in range(len(list)):
#      if list[i] > list[i-1]:
#        count += 1
# print(count)

# Задача №4. 
# 


# n = int(input('input digit'))
# list = []
# for _ in range(n):
#     list.append(input(''))
# print(list)

# indexMax =0 
# for i in range(1 ,len(list)):
#     if list[i -1] < list[i] > list[i + 1]:
#       indexMax += 1
# print(indexMax)