# Задача 1. По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while


















# Задача 2. Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.


# Задача 3. Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50

# num_day = int(input('Введите колличество дней: '))

# max_count = 0
# temp_count = 0

# for _ in range(num_day):
#     temperature = int(input('Введите температуру: '))
#     if temperature >= 0:
#         temp_count += 1
#     else:
#         temp_count = 0
#     if temp_count > max_count:
#         max_count = temp_count
# print(max_count)




# Задача 4. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза


# watermelons = int(input('Введите кол-во арбузов: '))

# max_kg = int(input('Введите массу арбуза: '))
# min_kg = max_kg
# for _ in range(watermelons - 1):
#     weight = int(input('Введите массу арбуза: '))
#     if weight > max_kg:
#         max_kg = weight
#     else:
#         if weight < min_kg:
#             min_kg = weight
# print(f'Для себя любимого - {max_kg}, для любимой тещи - {min_kg}')