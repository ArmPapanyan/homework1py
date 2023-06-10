

# zadacha ;18

# count = int(input('Кол-во: '))
# some_list = []
# for _ in range(count):
# number = int(input())
# some_list.append(number)

# # some_list = [int(input('Введите число: ')) for _ in range(int(input('Кол-во: ')))]

# x = int(input('Заданное число: '))
# find_number = some_list[0]
# for number in some_list:
# if abs(x - number) < abs(x - find_number):
# find_number = number
# print(find_number)

# 2.variant
# count = int(input('Кол-во: '))
# some_set = set([int(input('Введите число: ')) for _ in range(count)])
# x = int(input('Заданное число: '))
# diff = 1
# while True:
# if x + diff in some_set:
# print(x + diff)
# break
# if x - diff in some_set:
# print(x - diff)
# break
# diff += 1



# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1




# n = int(input('Введите кол-во оценок: '))
# some_list = []
# for _ in range(n):
#    some_list.append(int(input()))
# print(some_list)
# max = some_list[0]
# min = some_list[0]

# for i in range(len(some_list)):
#     if some_list[i] > max:
#         max = some_list[i]
#     if some_list[i] < min :
#         min = some_list[i]    
# print(max , min)
 

# for i in range(len(some_list)):
#     if some_list[i]== max :
#        some_list[i]= min
#        print(some_list)
    
    





